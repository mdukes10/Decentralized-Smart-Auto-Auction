pragma solidity ^0.5.0;

import "http://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
import "http://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";


contract ucartx is ERC721Full {

    constructor() ERC721Full("ucartx", "UCR") public { }

    using Counters for Counters.Counter;
    Counters.Counter token_ids;

    struct Car {
      //Implement car struct.
        //address owner;
        string vin;
        string year;
        string make;
        string model;
        string state;
        uint miles;
        uint accidents;
        //uint owner;
        uint appraisal_value;

    }
    mapping(uint => Car) public car_data;
    mapping (address => uint256[]) internal ownedTokens;
    mapping (uint256 => address) internal tokenOwner;
    // Mapping from token ID to index of the owner tokens list 
    mapping(uint256 => uint256) internal ownedTokensIndex;
    //Mapping from token id to position in the allTokens array 
    mapping(uint256 => uint256) internal allTokensIndex;
    mapping (address => uint256) internal ownedTokensCount;
    //mapping for token URIs
    mapping(uint256 => string) internal tokenURIs;
    
    event Appraisal(uint token_id, uint appraisal_value, string report_uri);
    
    function registerVehicle(address owner, string memory vin, string memory year, string memory make, string memory model, string memory state, uint miles, uint accidents, uint initial_value, string memory token_uri) public returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();

        _mint(owner, token_id);
        _setTokenURI(token_id, token_uri);

        car_data[token_id] = Car(vin, year, make, model, state, miles, accidents, initial_value);

        return token_id;
    }
    
    function TransferFrom(address from, address to, uint256 tokenId) external;