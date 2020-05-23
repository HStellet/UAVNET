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
    uint faulty;
    uint penaltytoken;
    int x;
    int y;
    int z;
    uint participating;
    uint timestamp;
    uint bcs;
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

  mapping (address=>uint) pubToMac;

  constructor() public{


    transaction=false;
    registered[1]=IOT(0x83385aCc745e5AF5f2408E5A9d3Ca41B8033F134,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYnoGR9akTl9fkcQp9KDuzHHGX\n4X6juW9+lZAL1OyTVpuCDxuxS1pCUM3wERt4zUgFidVm6JRiFOBmtmVMZft+A/c+\n+pkeDoGg0wUG8Rkcz4fBktF6OQLg7Y3xOLEUxQkEm2fCyWPh2K8R45GOkopNc4GI\nixT23IwOJs+VAKzxkwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,0,0,1,0,1);
    registered[2]=IOT(0x8EE94701c39929eb9722a09315F0e1695Abf555D,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDgdeWGyxiFpHpochyYFMMywSPT\nAgrX3T1bY4SwWbZsgSWi5AeosXkvRnBGCxHb7UCJctYTEv1Oq8GkBJK6cFx7Sj/O\ndtF+McsB3QfgOsspcsEbJVYnvTWlfg2pdEWMZC9g2M0z3LudqSdQYKZjggnTbzf8\newB5bC4XKIUZMYA/wwIDAQAB\n-----END PUBLIC KEY-----",0,0,6,0,0,1,0,1);
    registered[3]=IOT(0x7c0300b35b26924a92cBC9da5682279aD18A6E7b,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQZglkt9OPJRaGg+EzEEAptx45\nIp04S8FpWQDPmWjyg4LxUoyYbUWI2YWJYekbwoijlbJWEzZM+Zd4buRnHP86280V\nCNVRNZCURQwP62YgPvSrPfi0rzUVfCPGozuCip3VWWEEwe/jMnfBYaNovyOEXKbV\nljjpoLdqfZ+MwhSEewIDAQAB\n-----END PUBLIC KEY-----",0,0,4,0,0,1,0,1);
    registered[4]=IOT(0x23018548f67d4a0fF7027dB2870d61cA6D88b818,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCe3b0CxPaPZ5yUXFMUZEyB2Pol\nKGUSgHSeVA0vKBcJmL8S8xvnJF7VkiBdEt8j4tP0GLrw00HE4ALUc0Zd+7vT+Mn1\nwfctt9MEwLeOgUUqFKtjQxPxIKicr2t90J+xytXC8idUX52WBBSNlXSZqwms1bey\ncTWQUAgufncmHJkuxwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,2,0,0,0,0);
    registered[5]=IOT(0x107f93c9e5eE222A4281843D96A745c68387bD59,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDpQL/h+9nYI60P2FTcUtA4gZv\n0rOknWU3ozEt0NyW8YTjKZTClYy8vbdGHSYVbqhxcqcigVQaDFqZhJJeVQ/JK7bM\nJG7v/AuFEjGu3UKfvIiDdSqA7GQnQHN4aT217A0MtaR9VTos4ytb5n1h+srIR8dr\nA1Sbq0rTJCONEzN2wwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,4,0,0,0,0);
    registered[6]=IOT(0x7dEDCFB08c4E7C2856d44b35411893419d6E6Cf3,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC87aj11vwV/ji58cLigpHvcSTJ\nteAdajJ3PwnUvHHCTjh5Rjh07sZOb1MV2vcOB6PmxlHqocqIEvmT1PBqIoLN9jpB\nC/tbTWtDLafNEirdtszeUgP2s8vFzhK3F7YqNGHzz7HiOCV7FYVsDe4jyjV10vEf\nB5tSXt0pH27LJipuZwIDAQAB\n-----END PUBLIC KEY-----",0,0,2,4,0,0,0,0);
    registered[7]=IOT(0x34dCf4e9c4B0eD9F835c5B4173B2d90804b2a11f,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDMJlsg3FieJsbC9xLGyFC8MdkE\n9V0Yc33WjuZqU6ca7y7K3AUu+TsMYsKGAhQJvcNu5PxwZwfkudY+wIm//NroSt3s\nGhrMkaNoFTAW1Uc8Q5Y77K1L/kp9M0be0UXXG5Qb3QZ/dczEDDpnm0iLHusTYz7R\nnwOiJTtf9eGt5ClZ4wIDAQAB\n-----END PUBLIC KEY-----",0,0,4,4,0,0,0,0);
    registered[8]=IOT(0x5aF5E7EACd4552ED39E40aa82B2FA164b6A441a8,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD1UmkFyvP4PR6ceMCU9xiTBvA5\nRHi7Q4W/XdrlRoqXH4tBgwtXPObLcppjtGcgsFt6gu7U82Wk1OZ8iREOyY1uNTKD\n+aT3fXLtGbW6KDifeM5E69DOP2Vjfx61biCCNrjyMZj5qJvbinNvCo/Q37+0dGuU\npKZ992fW4FzFTBMKvQIDAQAB\n-----END PUBLIC KEY-----",0,0,4,2,0,0,0,0);

    blacklisted[0x23018548f67d4a0fF7027dB2870d61cA6D88b818]=10;
    pubToMac[registered[1].publicKey]=1;
    pubToMac[registered[2].publicKey]=2;
    pubToMac[registered[3].publicKey]=3;
    pubToMac[registered[4].publicKey]=4;
    pubToMac[registered[5].publicKey]=5;
    pubToMac[registered[6].publicKey]=6;
    pubToMac[registered[7].publicKey]=7;
    pubToMac[registered[8].publicKey]=8;


    list.push(1);
    list.push(2);
    list.push(3);
    list.push(4);
    list.push(5);
    list.push(6);
    list.push(7);
    list.push(8);

  }
  function registration(string memory pubkey) public payable{
    if(pubToMac[msg.sender]==0 && blacklisted[msg.sender]==0 && msg.value==5 ether)
    {
      list.push(list.length+1);
      pubToMac[msg.sender]=list.length;
      registered[pubToMac[msg.sender]].publicKey=msg.sender;
      registered[pubToMac[msg.sender]].encrypt=pubkey;
      registered[pubToMac[msg.sender]].faulty=0;
      registered[pubToMac[msg.sender]].penaltytoken=0;
      registered[pubToMac[msg.sender]].participating=0;
      registered[pubToMac[msg.sender]].bcs=0;
      registered[pubToMac[msg.sender]].x=0;
      registered[pubToMac[msg.sender]].y=0;
      registered[pubToMac[msg.sender]].z=0;

    }
    else
      return;
  }
  function removeFromFaulty() public payable{
    if(pubToMac[msg.sender]!=0 && registered[pubToMac[msg.sender]].faulty!=0)
    {
        if(registered[pubToMac[msg.sender]].penaltytoken == msg.value && (now-registered[pubToMac[msg.sender]].timestamp)<=registered[pubToMac[msg.sender]].faulty)
        {
          registered[pubToMac[msg.sender]].penaltytoken=0;
          registered[pubToMac[msg.sender]].faulty=0;
          registered[pubToMac[msg.sender]].timestamp=0;

        }
        else if( (now-registered[pubToMac[msg.sender]].timestamp)>registered[pubToMac[msg.sender]].faulty)
        {
            registered[pubToMac[msg.sender]].penaltytoken+=2 ether;
            registered[pubToMac[msg.sender]].faulty+=10;
            registered[pubToMac[msg.sender]].timestamp=now;

        }
        return;
    }
  }
  function checkBlacklisted() public view returns(uint)
  {
    return blacklisted[msg.sender];
  }
}
