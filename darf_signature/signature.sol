pragma solidity ^0.4.0;

contract SynchronizeStorage {
    string storedData;
    uint gaslimit;
    uint gasused;
    string documentHash;
    function setData(string x) {
        storedData = x;
    }
   
    function getGasLimit() constant returns (uint gas){
         gaslimit =  msg.gas;
         return gaslimit;
    }
    function HashOfDB() constant returns (string x) {
        return storedData;
    }
    function setDocumentHash(string timestamp, string md5) {
        documentHash = md5;
        storedData = timestamp;
    }
    function getDocumentHash() constant returns(string x){
        return storedData;
    }
    function getDocumentMD5() constant returns(string x){
        return documentHash;
    }
}