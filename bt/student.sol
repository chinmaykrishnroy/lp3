//SPDX-License-Identifier: MIT 
pragma solidity ^0.8.0;

// Build the Contract
contract StudentData
{
	// Create a structure for
	// student details
	struct Student
	{
		int ID;
		string fName;
		string lName;
		int[2] marks;
	}
	// fallback () external payable {
		
	//  }

	address owner;
	int public stdCount = 0;
	mapping(int => Student) public stdRecords;

	modifier onlyOwner
	{
		require(owner == msg.sender);
		_;
	}
	constructor()
	{
		owner=msg.sender;
	}

	// Create a function to add
	// the new records
	function addNewRecords(int _ID,string memory _fName,string memory _lName,int[2] memory _marks) public onlyOwner
	{
		// Increase the count by 1
		stdCount = stdCount + 1;

		// Fetch the student details
		// with the help of stdCount
		stdRecords[stdCount] = Student(_ID, _fName,_lName, _marks);
	}

}


Ganache Output
Ganache CLI v6.12.2 (ganache-core: 2.13.2)

Available Accounts
==================
(0) 0xB1a2...e2E5 (100 ETH)
(1) 0x8B4c...aaB7 (100 ETH)
(2) 0x96d4...cF98 (100 ETH)
(3) 0x62c2...a2B4 (100 ETH)
(4) 0x10C2...5cF6 (100 ETH)

Private Keys
==================
(0) 0xe860...8f5b
(1) 0x2890...e9be
(2) 0xa74a...cc0a
(3) 0x7462...ed78
(4) 0xc8db...fdd0

Listening on 0.0.0.0:8545


Truffle Migration Output
Compiling your contracts...
==========================
> Compiling ./contracts/StudentData.sol
> Artifacts written to /path/to/your/project/build/contracts
> Compiled successfully using: solc: 0.8.0

Deploying 'StudentData'
==========================
> [email protected] (0x4C2d...EA87) has been deployed to:
0xF90B...Fe58

Hardhat Deployment Output
StudentData deployed to: 0xF90B...Fe58


Interaction Script Output
Student Data: {
  ID: 1,
  fName: 'John',
  lName: 'Doe',
  marks: [ 85, 90 ]
}
