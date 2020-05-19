pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;
import "./DataSending.sol";
import "./UAV.sol";

contract PathFind is DataSending{

    event e(
        uint x
    );
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
          emit e(u);
          for (uint i = 0; i < routeTable[registered[u].publicKey].length; i++) {

              if (visited[pubToMac[routeTable[registered[u].publicKey][i]]] == false) {
                  visited[pubToMac[routeTable[registered[u].publicKey][i]]] = true;
                  pred[pubToMac[routeTable[registered[u].publicKey][i]]] = u;
                  q.enqueue(pubToMac[routeTable[registered[u].publicKey][i]]);

                  if (pubToMac[routeTable[registered[u].publicKey][i]] == pubToMac[destination])
                      return true;
              }
          }
      }
      return false;
  }

  function pathFind() public returns (route[] memory)
  {
      uint[] memory pred=new uint[](list.length+1);
      if (bfs(pred) == false) {
          Route.length=0;
          return Route;
      }

      uint crawl = pubToMac[destination];
      Route.push(route(crawl,"",0));
      while (pred[crawl] != 0) {
          Route.push(route(pred[crawl],"",0));
          crawl = pred[crawl];
      }
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
      return Route;
  }
}
