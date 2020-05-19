pragma solidity >=0.4.21 <0.6.0;
import "./DataSending.sol";

contract PathFind {
  mapping(uint => int) queue;
  uint first;
  uint last;
  constructor() public{
    first = 1;
    last = 0;
  }
  function enqueue(int data) public {
      last += 1;
      queue[last] = data;
  }

  function dequeue() public returns (bool) {
      if(first>=last)
      {
          delete queue[first];
          first += 1;
          return true;
      }
      else
          return false;

  }


}
