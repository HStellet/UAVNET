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
    registered[1]=IOT(0xdFA2236927A85497BE55934FFC4A846697116EB9,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDYnoGR9akTl9fkcQp9KDuzHHGX\n4X6juW9+lZAL1OyTVpuCDxuxS1pCUM3wERt4zUgFidVm6JRiFOBmtmVMZft+A/c+\n+pkeDoGg0wUG8Rkcz4fBktF6OQLg7Y3xOLEUxQkEm2fCyWPh2K8R45GOkopNc4GI\nixT23IwOJs+VAKzxkwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,0,0,1,0,1);
    registered[2]=IOT(0x845068b561FE8EbB14912D3865F1Cc3Af316b483,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDgdeWGyxiFpHpochyYFMMywSPT\nAgrX3T1bY4SwWbZsgSWi5AeosXkvRnBGCxHb7UCJctYTEv1Oq8GkBJK6cFx7Sj/O\ndtF+McsB3QfgOsspcsEbJVYnvTWlfg2pdEWMZC9g2M0z3LudqSdQYKZjggnTbzf8\newB5bC4XKIUZMYA/wwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,1,0,1,0,1);
    registered[3]=IOT(0xb884D6Fa6f3d0C98482Ad3a3d9D3E9dbf7eFdbfB,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCQZglkt9OPJRaGg+EzEEAptx45\nIp04S8FpWQDPmWjyg4LxUoyYbUWI2YWJYekbwoijlbJWEzZM+Zd4buRnHP86280V\nCNVRNZCURQwP62YgPvSrPfi0rzUVfCPGozuCip3VWWEEwe/jMnfBYaNovyOEXKbV\nljjpoLdqfZ+MwhSEewIDAQAB\n-----END PUBLIC KEY-----",0,0,0,2,0,1,0,1);
    registered[4]=IOT(0x8BB948E837d7e651939a992eC06fEd0b5af33356,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCe3b0CxPaPZ5yUXFMUZEyB2Pol\nKGUSgHSeVA0vKBcJmL8S8xvnJF7VkiBdEt8j4tP0GLrw00HE4ALUc0Zd+7vT+Mn1\nwfctt9MEwLeOgUUqFKtjQxPxIKicr2t90J+xytXC8idUX52WBBSNlXSZqwms1bey\ncTWQUAgufncmHJkuxwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,0,0,0,0,0);
    registered[5]=IOT(0x4402cEC8692c79C3640B6299A9C4B6107F70836A,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCDpQL/h+9nYI60P2FTcUtA4gZv\n0rOknWU3ozEt0NyW8YTjKZTClYy8vbdGHSYVbqhxcqcigVQaDFqZhJJeVQ/JK7bM\nJG7v/AuFEjGu3UKfvIiDdSqA7GQnQHN4aT217A0MtaR9VTos4ytb5n1h+srIR8dr\nA1Sbq0rTJCONEzN2wwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,1,0,0,0,0);
    registered[6]=IOT(0x42d9103A4EE6Bdf5E6d58073B68Ff13684c7c6d7,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC87aj11vwV/ji58cLigpHvcSTJ\nteAdajJ3PwnUvHHCTjh5Rjh07sZOb1MV2vcOB6PmxlHqocqIEvmT1PBqIoLN9jpB\nC/tbTWtDLafNEirdtszeUgP2s8vFzhK3F7YqNGHzz7HiOCV7FYVsDe4jyjV10vEf\nB5tSXt0pH27LJipuZwIDAQAB\n-----END PUBLIC KEY-----",0,0,0,2,0,0,0,0);
    registered[7]=IOT(0x9BFEa330cA63e5E6503b8eDD4b7433f1c2f33350,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDMJlsg3FieJsbC9xLGyFC8MdkE\n9V0Yc33WjuZqU6ca7y7K3AUu+TsMYsKGAhQJvcNu5PxwZwfkudY+wIm//NroSt3s\nGhrMkaNoFTAW1Uc8Q5Y77K1L/kp9M0be0UXXG5Qb3QZ/dczEDDpnm0iLHusTYz7R\nnwOiJTtf9eGt5ClZ4wIDAQAB\n-----END PUBLIC KEY-----",0,0,0,3,0,0,0,0);
    registered[8]=IOT(0xa81FBBb24A70623Ac07cc4069cdDeD943DA3Bb60,"-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQD1UmkFyvP4PR6ceMCU9xiTBvA5\nRHi7Q4W/XdrlRoqXH4tBgwtXPObLcppjtGcgsFt6gu7U82Wk1OZ8iREOyY1uNTKD\n+aT3fXLtGbW6KDifeM5E69DOP2Vjfx61biCCNrjyMZj5qJvbinNvCo/Q37+0dGuU\npKZ992fW4FzFTBMKvQIDAQAB\n-----END PUBLIC KEY-----",0,0,0,4,0,0,0,0);


    pubToMac[registered[1].publicKey]=1;
    pubToMac[registered[2].publicKey]=2;
    pubToMac[registered[3].publicKey]=3;
    pubToMac[registered[4].publicKey]=4;
    pubToMac[registered[5].publicKey]=5;
    pubToMac[registered[6].publicKey]=5;
    pubToMac[registered[7].publicKey]=5;
    pubToMac[registered[8].publicKey]=5;


    list.push(1);
    list.push(2);
    list.push(3);
    list.push(4);
    list.push(5);
    list.push(6);
    list.push(7);
    list.push(8);

  }

}