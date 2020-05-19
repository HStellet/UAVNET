pragma solidity >=0.4.21 <0.6.0;

contract Queue{
  mapping(uint => uint) queue;
  uint first;
  uint last;
  constructor() public{
    first = 1;
    last = 0;
  }
  function enqueue(uint data) public {
      last += 1;
      queue[last] = data;
  }

  function dequeue() public returns (uint) {
    uint x=queue[first];
    delete queue[first];
    first += 1;
    return x;
  }
  function isEmpty() public view returns (bool){
    if(first>last)
        return true;
    else
        return false;
  }
}

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


  }

}
