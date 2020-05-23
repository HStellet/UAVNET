pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;
import "./DataSending.sol";
import "./UAV.sol";

contract PathFind is DataSending{

    // event x(
    //     uint y, uint z);
    event x3(bool z);
  function bfs(uint[] memory pred) public returns(bool)
  {
      Queue q=new Queue();
      bool[] memory visited=new bool[](list.length+1);

      for (uint i = 0; i < visited.length; i++) {
          visited[i] = false;
          pred[i] = 0;
      }

      visited[pubToMac[source]] = true;
      q.enqueue(pubToMac[source]);
      while (q.isEmpty()==false) {

          uint u = q.dequeue();

          for (uint i = 0; i < routeTable[registered[u].publicKey].length; i++) {

              if (visited[pubToMac[routeTable[registered[u].publicKey][i]]] == false) {
                  visited[pubToMac[routeTable[registered[u].publicKey][i]]] = true;
                  pred[pubToMac[routeTable[registered[u].publicKey][i]]] = u;
                  q.enqueue(pubToMac[routeTable[registered[u].publicKey][i]]);
                //   emit x(u,pubToMac[routeTable[registered[u].publicKey][i]]);

                  if (pubToMac[routeTable[registered[u].publicKey][i]] == pubToMac[destination])
                      return true;
              }
          }
      }
      return false;
  }

  function pathFind() public payable
  {
    //   return bfs
    require(msg.sender==source && transaction==true);
      uint[] memory pred=new uint[](list.length+1);
      if(bfs(pred)==false){
          Route.length=0;
          sendBackToken();
          count=0;
          source=0x0000000000000000000000000000000000000000;
          destination=0x0000000000000000000000000000000000000000;
          transaction=false;
          emit x3(false);
          return;
      }
        // emit x1(Route);
      uint crawl = pubToMac[destination];
      Route.push(route(crawl,"",0));
      while (pred[crawl] != 0) {
          Route.push(route(pred[crawl],"",0));
          crawl = pred[crawl];
      }
    //   emit x1(Route);
      uint start=0;
      uint end=Route.length-1;
      while (start < end)
      {
          route memory temp = Route[start];
          Route[start] = Route[end];
          Route[end] = temp;
          start++;
          end--;
      }
      emit x3(true);
  }
  function returnRoute() public view returns(route[] memory)
    {return Route;}
}
