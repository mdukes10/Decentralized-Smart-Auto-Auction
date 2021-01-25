# Decentralized Smart Auto Auction

![bot header](Images/baheaderjpg.jpg)

# Goal:
Create a Smart Contract on the Blockchain that executes the following functions:

* Create Auction
* Register Assets / Register Auctioneers
* Add Bidders
* Transact Highest Bid 
* Execution via Python or Wallet Extension (MetaMask). 
# Problem Solved
Allow users to buy or sell vehicles (non-fungible assets) on a decentralized network and transact through SmartContracts avoiding traditional methods of payment (i.e. using Crypto). 

# Neccessary Equipment

* Solidity / Python languages:
  * OpenZepplin ERC721- Solidity
  * Web3 - Python
* Ganache Install 
* Remix IDE Install
* MetaMask Install Extension (Crypto Wallet)



# Install Instructions
* Solidify
* Ganache [Ganache Install](https://www.trufflesuite.com/docs/ganache/quickstart) 
* Remix IDE [Remix Install](https://remix.ethereum.org/#optimize=false&runs=200&evmVersion=null&version=soljson-v0.7.4+commit.3f05b770.js)
* MetaMask [MetaMask Download](https://metamask.io/download.html)
* AWS 
* Conversational User Interfaces (CUI's)

# Smart Contract Compiler 
* Uses OpenZepplin contracts to import ERC721 standard ,which tokenizes non-fungible assets into unique tokens to create secure transactions.
* Uses mapping and events
* Uses functions like createAuction, registerCar, addBidders, viewCars, endAuction, highestBid, highestBidder, bid
* SEE CODE (ServiceLayer.sol)

![sldeploy](Images/SLdeploy.gif)
# Python - Smart Contract
* Imports
* Connect to web3 
* Read in ABI file from Smart Contract
* Plug in smart contract address
* Establish functions and parse in information (i.e. bidder address, vehicle info., bid amount, etc.)
* Watch transaction in Ganache
## Beginning Balance
We will use the address ending in ...f4A1 to transact a bid with the Smart Contract

![ga1](Images/ga1.png)
## Run the Python Code
Run Python code using web3.middleware
* Register Car & Create Auction
* Add Bidder
* Place Bid
* End Auction

![pythongif](Images/pythongif.gif)

## After Running Python 
Notice how account ending ...f4a1 balance dropped to 98.24 ETH
![ga2](Images/ga2.png)