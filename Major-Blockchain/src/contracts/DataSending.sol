pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;
import "./UAV.sol";

contract DataSending is Registration{
  uint timestamp;
  bool successful;
  address payable culprit;
  uint count=0;

  mapping (address => address[]) routeTable;

  constructor() public{

    successful=false;

  }

  function doTrans(address payable dest) public{

    require(transaction==false && msg.sender!=dest);
    transaction=true;
    source=msg.sender;
    destination=dest;
    timestamp=now;

  }


  function registerCoordinates(int[] memory coordinates) public payable
  {
    require(transaction==true && registered[pubToMac[msg.sender]].faulty==0);
    if(pubToMac[msg.sender]!=0)
    {
      if(registered[pubToMac[msg.sender]].bcs==0 && registered[pubToMac[msg.sender]].participating==0 && msg.value==1 ether)
      {
        registered[pubToMac[msg.sender]].participating=1;
      }
      else
        return;
    }
    else
      return;
    registered[pubToMac[msg.sender]].x=coordinates[0];
    registered[pubToMac[msg.sender]].y=coordinates[1];
    registered[pubToMac[msg.sender]].z=coordinates[2];

  }

  function getTable() public view returns(uint,uint,address[] memory)
  {

    return (registered[pubToMac[msg.sender]].faulty,blacklisted[msg.sender],routeTable[msg.sender]);

  }


  function updateGraph() public
  {

    require((msg.sender==source || msg.sender==registered[1].publicKey || msg.sender==registered[2].publicKey || msg.sender==registered[3].publicKey) && transaction==true);
    for(uint i=0;i<list.length;i++)
    {

      routeTable[registered[list[i]].publicKey].length=0;
      // emit x1(registered[list[i]].participating);
      //   emit x1(list[i]);
      if(registered[list[i]].participating==1){
      for(uint j=0;j<list.length;j++)
      {
        if(i!=j && registered[list[j]].participating==1)
        {
            int distance=(registered[list[i]].x-registered[list[j]].x)*(registered[list[i]].x-registered[list[j]].x) + (registered[list[i]].y-registered[list[j]].y)*(registered[list[i]].y-registered[list[j]].y) + (registered[list[i]].z-registered[list[j]].z)*(registered[list[i]].z-registered[list[j]].z);
            if(distance<=9)
            {
              routeTable[registered[list[i]].publicKey].push(registered[list[j]].publicKey);
            }
        }
      }}
    }

  }

  function success() public payable returns(bool){

      if(msg.sender==destination)
        {
            Route[count].timestamp=now;
            successful=true;
            count=0;
            destination=0x0000000000000000000000000000000000000000;
            sendBackToken();
        }
        else
          return false;
  }

  function sendBackToken() public payable
  {
    for(uint i=0;i<list.length;i++)
    {
        routeTable[registered[list[i]].publicKey].length=0;
      if(registered[list[i]].participating==1 && registered[list[i]].bcs==0)
      {

        registered[list[i]].participating=0;
        registered[list[i]].publicKey.transfer(1 ether);
      }

    }
  }
  function unsuccessful(uint x) public payable {

      require(msg.sender==destination);
      transaction=false;
      successful=false;
      if(x==0)
      {

        registered[Route[count].id].participating=0;
        blacklisted[registered[Route[count].id].publicKey]++;
        registered[Route[count].id].faulty=blacklisted[registered[Route[count].id].publicKey]*10;
        registered[Route[count].id].penaltytoken=blacklisted[registered[Route[count].id].publicKey]*2 ether;
        registered[Route[count].id].timestamp=now;
        culprit=registered[Route[count].id].publicKey;
      }
      else
      {
        for(uint i=1;i<Route.length;i++)
        {
          if(keccak256(bytes(Route[i].data))!=keccak256(bytes(Route[0].data)))
          {
            registered[Route[i-1].id].participating=0;
            blacklisted[registered[Route[i-1].id].publicKey]++;
            registered[Route[i-1].id].faulty=blacklisted[registered[Route[i-1].id].publicKey]*10;
            registered[Route[i-1].id].penaltytoken=blacklisted[registered[Route[i-1].id].publicKey]*2 ether;
            registered[Route[i-1].id].timestamp=now;
            culprit=registered[Route[i-1].id].publicKey;
            break;
          }
        }
      }
      sendBackToken();
  }
  function returnCulprit() public view returns(address payable)
  {
      return culprit;
  }

  function transCompleted() public payable{

      require(msg.sender==source && transaction==true && successful==true);
      count=0;
      uint divide=0;
      if(Route.length-2!=0)
        divide=msg.value/(Route.length-2);
      for(uint i=1;i<Route.length-1;i++)
      {
        registered[Route[i].id].publicKey.transfer(divide);
      }
      Route.length=0;
      transaction=false;
      successful=false;
      source=0x0000000000000000000000000000000000000000;


  }

  function send(string memory x) public{
      require(msg.sender==registered[Route[count].id].publicKey);
      if(count==0)
        Route[count].data=string(x);
      Route[count].timestamp=now;
      if(count+1<=Route.length-1)
        Route[count+1].data=string(x);
      count++;
  }
  function getData() public view returns (string memory) {
    if(msg.sender==registered[Route[count].id].publicKey)
      return Route[count].data;
    else
      return "";
  }
  function abort() public{
    uint count1=0;
      uint[] memory list1=new uint[](list.length);
      for(uint i=0;i<list.length;i++)
      {
        pubToMac[registered[list[i]].publicKey]=0;

        routeTable[registered[list[i]].publicKey].length=0;
        if(blacklisted[registered[list[i]].publicKey]<=10)
        {
          list1[count1]=list[i];
          count1++;
        }
        else
        {
            delete registered[list[i]];
        }
      }
      delete list;
      for(uint i=0;i<count1;i++)
      {
          list.push(list1[i]);
          registered[i+1]=registered[list[i]];
          if(i+1 != list[i])
            delete registered[list[i]];
          pubToMac[registered[i+1].publicKey]=i+1;
          list[i]=i+1;
      }
      delete list1;

      Route.length=0;
      transaction=false;
      successful=false;
      count=0;
      source=0x0000000000000000000000000000000000000000;
      destination=0x0000000000000000000000000000000000000000;


  }
  function getRegistered() public view returns(IOT memory,uint,uint)
  {
    return (registered[pubToMac[msg.sender]],blacklisted[msg.sender],pubToMac[msg.sender]);
  }

}
