// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Bank {
    
    // Mapping to store the balances of each address
    mapping(address => uint) private balances;

    // Event emitted when ETH is deposited
    event Deposited(address indexed user, uint amount);
    
    // Event emitted when ETH is withdrawn
    event Withdrawn(address indexed user, uint amount);

    // Function to check the balance of the caller
    function getBalance() public view returns (uint) {
        return balances[msg.sender];
    }

    // Function to deposit ETH into the contract
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        
        // Update the balance of the sender
        balances[msg.sender] += msg.value;

        // Emit a Deposited event
        emit Deposited(msg.sender, msg.value);
    }

    // Function to withdraw ETH from the contract
    function withdraw(uint amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance");

        // Update the balance of the sender
        balances[msg.sender] -= amount;

        // Transfer the requested amount to the sender
        (bool sent, ) = msg.sender.call{value: amount}("");
        require(sent, "Failed to send ETH");

        // Emit a Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }
}

Output Expectations
During these commands, you should see logs in the console similar to the following:

After deposit:
Deposited 1 ETH

After checking balance:
Balance: 1.0

After withdrawal:
Withdrew 0.5 ETH

After checking new balance:
New Balance: 0.5

If you attempt to withdraw more than the balance:
Error: Insufficient balance