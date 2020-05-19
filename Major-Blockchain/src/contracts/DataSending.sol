pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;

contract Registration{

  address payable source;
  address payable destination;
  bool public transaction;

  struct IOT{
    address payable publicKey;
    string encrypt;
    uint blacklist;
    uint penaltytoken;
    int x;
    int y;
    int z;
    int participating;
    uint timestamp;
  }

  struct bcs{
    address payable publicKey;
    string encrypt;
    int x;
    int y;
    int z;
    uint participating;
  }
  struct route {
    uint id;
    string data;
    uint timestamp;
  }

  uint[] list;
  route[] Route;
  mapping(address=> uint) blacklisted;
  mapping (uint => IOT) registered;

  mapping (string => bcs) BCS;


  mapping (address=>uint) pubToMac;

  constructor() public{

    BCS["B1"]=bcs(0xCA35b7D915458ef540aDE6068DfE2F44e8fa733D,"",0,0,0,1);
    BCS["B2"]=bcs(0xcA35B7D915458Ef540aDE6068DFE2f44E8fA733e,"",0,1,0,1);
    BCS["B3"]=bcs(0xcA35b7d915458Ef540aDe6068Dfe2f44e8FA733f,"",0,2,0,1);

    transaction=false;

    registered[1]=IOT(0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c,"",0,1,0,0,0,0,0);
    registered[2]=IOT(0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C,"",0,1,0,1,0,0,0);
    registered[3]=IOT(0x4B0897b0513fdC7C541B6d9D7E929C4e5364D2dB,"",0,1,0,2,0,0,0);
    registered[4]=IOT(0x583031D1113aD414F02576BD6afaBfb302140225,"",0,1,0,3,0,0,0);
    registered[5]=IOT(0xdD870fA1b7C4700F2BD7f44238821C26f7392148,"",0,1,0,4,0,0,0);


    pubToMac[registered[1].publicKey]=1;
    pubToMac[registered[2].publicKey]=2;
    pubToMac[registered[3].publicKey]=3;
    pubToMac[registered[4].publicKey]=4;
    pubToMac[registered[5].publicKey]=5;

    list.push(1);
    list.push(2);
    list.push(3);
    list.push(4);
    list.push(5);
    Route.push(route(1,"",0));
    Route.push(route(2,"",0));
    Route.push(route(3,"",0));
    Route.push(route(4,"",0));
    Route.push(route(5,"",0));

  }

}
contract DataSending is Registration{
  uint timestamp;
  bool successful;
  uint count=0;
  mapping (address => address[]) routeTable;

  constructor() public{

    successful=false;

    routeTable[registered[1].publicKey].push(registered[2].publicKey);
    routeTable[registered[2].publicKey].push(registered[1].publicKey);
    routeTable[registered[2].publicKey].push(registered[3].publicKey);
    routeTable[registered[3].publicKey].push(registered[2].publicKey);
    routeTable[registered[3].publicKey].push(registered[4].publicKey);
    routeTable[registered[4].publicKey].push(registered[3].publicKey);
    routeTable[registered[4].publicKey].push(registered[5].publicKey);
    routeTable[registered[5].publicKey].push(registered[4].publicKey);

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
    if(pubToMac[msg.sender]!=0 && msg.value==1 ether && registered[pubToMac[msg.sender]].participating==0)
    {
      if(registered[pubToMac[msg.sender]].blacklist==0)
      {
        registered[pubToMac[msg.sender]].participating=1;
      }
      else
      {
        return;
      }
    }

    else if(pubToMac[msg.sender]==0 && msg.value==5 ether)
    {
      list.push(list.length+1);
      pubToMac[msg.sender]=list.length;
      registered[pubToMac[msg.sender]].publicKey=msg.sender;
      registered[pubToMac[msg.sender]].encrypt=string(msg.data);
      registered[pubToMac[msg.sender]].blacklist=0;
      registered[pubToMac[msg.sender]].penaltytoken=0;
      registered[pubToMac[msg.sender]].participating=0;
    }
    else if((pubToMac[msg.sender]==0 && msg.value!=5 ether)||(pubToMac[msg.sender]!=0 && msg.value!=1 ether))
      return;
    else if(blacklisted[msg.sender]!=0 && registered[pubToMac[msg.sender]].penaltytoken == msg.value && (now-registered[pubToMac[msg.sender]].timestamp>=registered[pubToMac[msg.sender]].blacklist))
    {
      registered[pubToMac[msg.sender]].penaltytoken=0;
      registered[pubToMac[msg.sender]].blacklist=0;

    }
    registered[pubToMac[msg.sender]].x=coordinates[0];
    registered[pubToMac[msg.sender]].y=coordinates[1];
    registered[pubToMac[msg.sender]].z=coordinates[2];

  }

  function getTable() public view returns(address[] memory)
  {

    return routeTable[msg.sender];

  }


  function updateGraph() public
  {

    require((msg.sender==source || msg.sender==BCS["B1"].publicKey || msg.sender==BCS["B2"].publicKey || msg.sender==BCS["B3"].publicKey) && transaction==true);
    for(uint i=0;i<list.length;i++)
    {
      routeTable[registered[list[i]].publicKey].length=0;
      for(uint j=0;j<list.length;j++)
      {
        if(i!=j)
        {
            int distance=(registered[list[i]].x-registered[list[j]].x)*(registered[list[i]].x-registered[list[j]].x) + (registered[list[i]].y-registered[list[j]].y)*(registered[list[i]].y-registered[list[j]].y) + (registered[list[i]].z-registered[list[j]].z)*(registered[list[i]].z-registered[list[j]].z);
            if(distance<=1)
            {
              routeTable[registered[list[i]].publicKey].push(registered[list[j]].publicKey);
            }
        }
      }
    }

  }

  function success() public payable {

      require(msg.sender==destination && now-timestamp<=60);
      Route[count].timestamp=now;
      successful=true;
      count=0;
      destination=0x0000000000000000000000000000000000000000;
      sendBackToken();

  }

  function sendBackToken() payable public
  {
    for(uint i=0;i<list.length;i++)
    {
      if(registered[list[i]].participating==1)
      {
        registered[list[i]].participating==0;
        registered[list[i]].publicKey.transfer(1 ether);
      }

    }
  }
  function unsuccessful(uint x) public payable{

      require(msg.sender==destination && now-timestamp>30);
      transaction=false;
      successful=false;
      if(x==0)
      {
        registered[Route[count].id].participating=0;
        blacklisted[registered[Route[count].id].publicKey]++;
        registered[Route[count].id].blacklist=blacklisted[registered[Route[count].id].publicKey]*10;
        registered[Route[count].id].penaltytoken=blacklisted[registered[Route[count].id].publicKey]*2 ether;
        registered[Route[count].id].timestamp=now;
      }
      else
      {
        for(uint i=1;i<Route.length;i++)
        {
          if(keccak256(bytes(Route[i].data))!=keccak256(bytes(Route[0].data)))
          {
            registered[Route[i].id].participating=0;
            blacklisted[registered[Route[i].id].publicKey]++;
            registered[Route[i].id].blacklist=blacklisted[registered[Route[i].id].publicKey]*10;
            registered[Route[i].id].penaltytoken=blacklisted[registered[Route[i].id].publicKey]*2 ether;
            registered[Route[i].id].timestamp=now;
            break;
          }
        }
      }
      sendBackToken();
      Route.length=0;
      count=0;
  }

  function transCompleted() public payable{

      require(msg.sender==source && transaction==true && successful==true);
      count=0;
      for(uint i=1;i<Route.length-1;i++)
      {
        registered[Route[i].id].publicKey.transfer(msg.value);
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
      if(count+1<Route.length-1)
        Route[count+1].data=string(x);
      count++;
  }
  function getData() public view returns (string memory) {
      require(msg.sender==registered[Route[count].id].publicKey);
      return Route[count].data;
  }
  function abort() public{

    require((msg.sender==BCS["B1"].publicKey || msg.sender==BCS["B2"].publicKey || msg.sender==BCS["B3"].publicKey));
    if(transaction==false)
    {
      uint count1=0;
      uint[] memory list1=new uint[](list.length);
      for(uint i=0;i<list.length;i++)
      {
        delete routeTable[registered[list[i]].publicKey];
        if(blacklisted[registered[list[i]].publicKey]<10)
        {
          list1[count1]=list[i];
          count1++;
        }
        else
        {
          delete pubToMac[registered[list[i]].publicKey];
          delete registered[list[i]];
        }
      }
      delete list;
      for(uint i=0;i<count1;i++)
      {
          list.push(list1[i]);
          pubToMac[registered[list1[i]].publicKey]=i+1;
          registered[i+1]=registered[list1[i]];
          delete registered[list1[i]];
      }
      delete list1;

    }

    Route.length=0;
    transaction=false;
    successful=false;
    count=0;
    source=0x0000000000000000000000000000000000000000;
    destination=0x0000000000000000000000000000000000000000;


  }

}
