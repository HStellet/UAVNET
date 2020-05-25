var Web3 = require('web3');
var web3=new Web3("http://127.0.0.1:7545")
var arr=web3.eth.getAccounts();
console.log(arr);
