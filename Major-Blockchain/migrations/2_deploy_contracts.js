const Registration = artifacts.require("Registration");
const DataSending = artifacts.require("DataSending");
const Queue = artifacts.require("Queue");

module.exports = function(deployer) {
  deployer.deploy(Registration);

  deployer.deploy(DataSending);
  deployer.deploy(Queue);

};
