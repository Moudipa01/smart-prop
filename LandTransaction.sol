// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Transfer {
    address public owner;
    string public message;

    constructor() {
        owner = msg.sender;
    }

    function transfer(address payable recipient, uint256 amount, string memory _message) public payable {
        require(msg.sender == owner, "Only the owner can transfer funds.");
        require(address(this).balance >= amount, "Insufficient balance in the contract.");

        recipient.transfer(amount);
        message = _message;
    }
}
