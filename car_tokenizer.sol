pragma solidity ^0.5.0;

import "http://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/drafts/Counters.sol";
import "http://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC721/ERC721Full.sol";

contract car_tokenizer is ERC721Full {

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
        uint initial_value;

    }
    mapping(uint => Car) public car_data;
    mapping (address => uint256[]) internal ownedTokens;
    mapping (uint256 => address) internal tokenOwner;
    // Mapping from token ID to index of the owner tokens list 
    mapping(uint256 => uint256) internal ownedTokensIndex;
    //Mapping from token id to position in the allTokens array 
    mapping(uint256 => uint256) internal allTokensIndex;
    mapping (address => uint256) internal ownedTokensCount;
    mapping(uint256 => uint256) internal allTokens;
    //mapping for token URIs
    mapping(uint256 => string) internal tokenURIs;
    
    //event Appraisal(uint token_id, uint appraisal_value, string report_uri);
    event Transfer(address indexed _from, address indexed _to, uint256 token_id);
    
    event Approval(address indexed _owner, address indexed _approved, uint256 token_id);
    
    function registerVehicle(address owner, string memory vin, string memory year, string memory make, string memory model, string memory state, uint miles, uint accidents, uint initial_value, string memory token_uri) public returns(uint) {
        token_ids.increment();
        uint token_id = token_ids.current();

        _mint(owner, token_id);
        _setTokenURI(token_id, token_uri);

        car_data[token_id] = Car(vin, year, make, model, state, miles, accidents, initial_value);

        return token_id;
    }
    
<<<<<<< HEAD
    function TransferFrom(address from, address to, uint256 tokenId) external;
=======
    
    function totalSupply() public view returns (uint256) {
        return allTokens.length;
    }
    
    function balanceOf(address owner) public view returns (uint256) {
        require(owner != address(0), "ERC721: balance query for the zero address");

        return ownedTokensCount[owner].current();
    }
    
    function ownerOf(uint256 token_id) public view returns (address) {
        address owner = tokenOwner[token_id];
        require(owner != address(0), "ERC721: owner query for nonexistent token");

        return owner;
    }
    
    function _safeTransferFrom(address from, address to, uint256 token_id, bytes memory _data) internal {
        _transferFrom(from, to, token_id);
        require(_checkOnERC721Received(from, to, token_id, _data), "ERC721: transfer to non ERC721Receiver implementer");
    }
    
    function approve(address to, uint256 tokenId) public {
        address owner = ownerOf(tokenId);
        require(to != owner, "ERC721: approval to current owner");

        require(_msgSender() == owner || isApprovedForAll(owner, _msgSender()),
            "ERC721: approve caller is not owner nor approved for all"
        );

        car_data[tokenId] = to;
        emit Approval(owner, to, tokenId);
    }

    
    function takeOwnership(uint256 token_id)internal { 
        require(car_data[token_id]);
        address oldOwner = ownerOf(token_id);
        address newOwner = msg.sender;
        require(newOwner != oldOwner);
        require(approve[oldOwner][newOwner] == token_id);
        balanceOf[oldOwner] -= 1;
        tokenOwner[token_id] = newOwner;
        balanceOf[newOwner] += 1;
        Transfer(oldOwner, newOwner, token_id);

 }
 
}
>>>>>>> 9644ac06e09d86a05fca3920012e0f632a406e9e
