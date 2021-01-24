# Install Guide

## Installing MetaMask

[MetaMask](https://metamask.io/) is a web browser extension that allows you to run Ethereum dApps right in your browser without running a full Ethereum node.

To install MetaMask, follow these steps:

* Open the [MetaMask website](https://metamask.io/) in your browser.

* Click on the "Download now" button. You will see a new page with the available MetaMask version. Choose "Chrome" to continue. Next, click on "Install MetaMask for Chrome."

* A new window will be opened where you will install the MetaMask extension from the Chrome Web Store.

* Click on the "Add to Chrome" button to start the installation process. A pop-up window will open where you have to click on the "Add extension" button to continue.

* Next, the "Welcome to MetaMask" website will be opened.

* If MetaMask was successfully installed, you will see a small fox icon in the web browser's extensions list. If this does not show up, revisit the previous steps.

* Optionally, in the latest version of Google Chrome, you can pin the MetaMask extension to your toolbar.

* Click the "Get Started" button to start configuring your MetaMask account.

* You can now import the wallet that runs in your local blockchain. Click on the "Import wallet" button to continue.

* Next, you will see the data usage agreement where the MetaMask team asks you to collaborate on improving the tool. Click the choice of your preference to continue.

* In the next window, you should enter the twelve word mnemonic of your local wallet (your wallet password), and you should click on the `I have read and agree the Terms of Use` checkbox to continue.

* Be sure to read through the terms by clicking on the link.

* After filling out your wallet details, click on the "Import" button to continue, and you will see the following confirmation page.

* You may notice a message at the bottom of the page that says that `MetaMask cannot recover your seedphrase`, it means that once you import your keys, MetaMask won't export them again, so if you lose your mnemonic you can't extract it from MetaMask; keep your mnemonics in a safe place!

* Click on the "All Done" button to continue; you will see a page showing the balance of your wallet and the transaction history.

* You may note that you have `0 ETH` and no transactions. This is all right from now since you are not connected to your local blockchain.

Congratulations! You have installed MetaMask.

## Installing Ganache

[Ganache](https://www.trufflesuite.com/ganache) is a personal blockchain for Ethereum development you can use to deploy contracts, develop your applications, and run tests. It's available for Windows, OS X, and Linux.

To download Ganache, follow the next steps.

* Open the [Ganache website](https://www.trufflesuite.com/ganache) in your browser.

* Depending on your operating system, you will see the corresponding download button.

* Click on the _Download_ button to save the installer to your computer.

### Running the Ganache Installer in OS X

* Open the installer file and drag the Ganache app to the "Applications" folder.

* Open the "Applications" folder and double-click on the "Ganache" icon. You will be asked for permission to run the application. You can safely click on the "Open" button to continue.

* Next, you will see a screen where the Ganache development team asks for your collaboration to share usage analytics with them. Choose the best option for you and click on the "Continue" button to finish the installation process.

### Running the Installer in Windows 10

* Open de installer file. A new window will pop-up asking to install Ganache.

* Make sure the "Launch when ready" checkbox is selected and click on the "Install" button to continue.

* Once the installation ends, the Ganache tool will be automatically launched after a few seconds.

* Next, you will see a screen where the Ganache development team asks for your collaboration to share usage analytics with them. Choose the best option for you and click on the "Continue" button to finish the installation process.

### Troubleshooting in Windows 10

If you see a warning message that says that Ganache is from an untrusted software publisher or source, you should enable the "Sideload apps" installation option as follows.

* Close the Ganache installer.

* Click on the "Windows" button and choose "Settings."

* In the "Windows Settings" search box type `developer` and choose `Developer settings."

* In the "Developer Settings" window, choose the "Sideload apps" options.

* You will see a warning message that states that you can expose your device to security risks. To install Ganache, you can safely click on the "Yes" button to continue.

* Close the "Windows Settings" window and open the Ganache installer again.

### Configuring a Workspace

* Launch the application to continue.

* Create a `New Workspace` and navigate through the various configuration pages. Apply the following settings on the following pages.

  * WORKSPACE
    * WORKSPACE NAME = `fintech`

  * SERVER
    * HOSTNAME = `127.0.0.1`
    * PORT NUMBER = `8545`
    * AUTOMINE = `ON`

  * ACCOUNTS & KEYS
    * ACCOUNT DEFAULT BALANCE = `100`
    * TOTAL ACCOUNTS TO GENERATE = `10`
    * AUTOGENERATE HD MNEMONIC = `YOUR MNEMONIC PHRASE`