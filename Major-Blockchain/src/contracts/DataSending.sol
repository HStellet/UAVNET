pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;
contract Registration{

  struct IOT{
    address publicKey;
    uint blacklist;
    uint token;
    int x;
    int y;
    int z;
  }

  mapping (string => IOT) registered;
  mapping (address=>string) public pubToMac;
  constructor() public{
    registered["A"]=IOT(0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c,0,1,0,0,0);
    registered["B"]=IOT(0x14723A09ACff6D2A60DcdF7aA4AFf308FDDC160C,0,1,0,1,0);
    registered["C"]=IOT(0x4B0897b0513fdC7C541B6d9D7E929C4e5364D2dB,0,1,0,2,0);
    registered["D"]=IOT(0x583031D1113aD414F02576BD6afaBfb302140225,0,1,0,3,0);
    registered["E"]=IOT(0xdD870fA1b7C4700F2BD7f44238821C26f7392148,0,1,0,4,0);
    pubToMac[registered["A"].publicKey]="A";
    pubToMac[registered["B"].publicKey]="B";
    pubToMac[registered["C"].publicKey]="C";
    pubToMac[registered["D"].publicKey]="D";
    pubToMac[registered["E"].publicKey]="E";
  }
}
contract DataSending is Registration{

  mapping (address => address[]) routeTable;
  constructor() public{
    routeTable[registered["A"].publicKey].push(registered["B"].publicKey);
    routeTable[registered["B"].publicKey].push(registered["A"].publicKey);
    routeTable[registered["B"].publicKey].push(registered["C"].publicKey);
    routeTable[registered["C"].publicKey].push(registered["B"].publicKey);
    routeTable[registered["C"].publicKey].push(registered["D"].publicKey);
    routeTable[registered["D"].publicKey].push(registered["C"].publicKey);
    routeTable[registered["D"].publicKey].push(registered["E"].publicKey);
    routeTable[registered["E"].publicKey].push(registered["D"].publicKey);

  }
  function updateCoordinates(int[] memory coordinates) public
  {
    registered[pubToMac[msg.sender]].x=coordinates[0];
    registered[pubToMac[msg.sender]].y=coordinates[1];
    registered[pubToMac[msg.sender]].z=coordinates[2];
  }

  function getTable() public view returns(address[] memory)
  {
    return routeTable[msg.sender];
  }

}
