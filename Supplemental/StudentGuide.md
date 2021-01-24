# Unit 20: Solidity

## Variables and Parameters

* Local and State Solidity Variables and Use of Parameters: https://www.bitdegree.org/learn/solidity-variables

* Local variable and state variable, and the difference between them: https://ethereum.stackexchange.com/questions/25554/local-variable-and-state-variable-and-the-difference-between-them

* Why constant variables inside functions fail to compile in Solidity?: https://ethereum.stackexchange.com/questions/51366/why-constant-variables-inside-functions-fail-to-compile-in-solidity

## Control Structures

* Control Structures in Ethereum: https://medium.com/@k3no/control-structures-in-ethereum-3f2d4149b84a

* What is the difference between if and require in Solidity: https://ethereum.stackexchange.com/questions/60585/what-difference-between-if-and-require-in-solidity

## Compiling 

* Compiling a contract with Remix is as easy as selecting a compatible compiler version and clicking `Compile`. To avoid unexpected errors, its best to set your Remix compiler version to match your pragma. The pragma and and compiler version should match as seen in the below image:

    ![pragma_compiler_match](Images/pragma_compiler_match.png)

## Troubleshooting Gas Estimation Errors

* Perhaps the most common error you'll see as you navigate Solidity and Smart Contracts, is the _Gas estimatation failed_ error. This error is troublesome because it serves as a kind of "catch-all" error, delivering a vague message that offers little guidance on what actually caused it:

    <img alt=gas_estimation_failed src=Images/gas_estimation_failed.png width=350>

* Here is a non-exhaustive compilation of possible causes that will help you to troubleshoot the issue quickly:

    **1.** The value box must be empty on deployment.  After deployment, certain functions may then require a value in the box. If you are deploying, make sure the box is empty.  If you are running a function that requires a value, such as `deposit`, make sure the value in the box.  

    <img alt=value_box src=Images/value_box.png width=250>

    **2.** If the contract calls for a wallet address variable, you must replace any hardcoded address in the provided code, with your own address. Similarly, some contracts call for the `owner` of the contract to be the user.  Make sure you are connected to the contract `owner` address in MetaMask in those cases.
    
    <img alt=value_address  src=Images/value_address.png width=750>

    **3.** The contract must have sufficient funds to withdraw the designated amount.  Utilize a balance checker - like `balanceChecker` from the `JointSavings` contract activities - to check your balance. If you're writing your own contract, add your own balance checker to make sure you have enough funds.

    <img alt=value_balance src=Images/value_balance.png width=600>

    **4.** Some contracts are designed to error out if certain conditions are not met.  In those instances you may see the gas estimation error.  One such example of this can be found in the time lock activities from class. If you are getting an unexpected error with these activities, make sure you utilize the `fastforward` function to override the time lock, and thus allow the contract to operate.

</details>


## Books

* Building Ethereum Dapps, Roberto Infante, Manning Publications: https://www.manning.com/books/building-ethereum-dapps.

## Resources

* Ethereum for Developers: https://ethereum.org/developers/#getting-started

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
