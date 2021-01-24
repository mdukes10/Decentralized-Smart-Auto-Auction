# Unit 20 Installation Guide

## Installing MetaMask

[MetaMask](https://metamask.io/) is a web browser extension that allows you to run Ethereum dApps right in your browser without running a full Ethereum node.

To install MetaMask, follow these steps:

* Open the [MetaMask website](https://metamask.io/) in your browser.

 ![MetaMask installation - 1](Images/metamask-1.png)

* Click on the "Download now" button. You will see a new page with the available MetaMask version. Choose "Chrome" to continue. Next, click on "Install MetaMask for Chrome."

  ![Downloading MeteMask for Chrome](Images/metamask-for-chrome.gif)

* A new window will be opened where you will install the MetaMask extension from the Chrome Web Store.

 ![MetaMask installation - 2](Images/metamask-2.png)

* Click on the "Add to Chrome" button to start the installation process. A pop-up window will open where you have to click on the "Add extension" button to continue.

 ![MetaMask installation - 3](Images/metamask-3.png)

* Next, the "Welcome to MetaMask" website will be opened.

 ![MetaMask installation - 4](Images/metamask-4.png)

* If MetaMask was successfully installed, you will see a small fox icon in the web browser's extensions list. If this does not show up, revisit the previous steps.

  ![MetaMask extension icon](Images/metamask-extension-icon.png)

* Optionally, in the latest version of Google Chrome, you can pin the MetaMask extension to your toolbar.

  ![Pinning MetaMask extension to the toolbar](Images/metamask-pinning-extension.gif)

* Click the "Get Started" button to start configuring your MetaMask account.

* You can now import the wallet that runs in your local blockchain. Click on the "Import wallet" button to continue.

 ![MetaMask installation - 5](Images/metamask-5.png)

* Next, you will see the data usage agreement where the MetaMask team asks you to collaborate on improving the tool. Click the choice of your preference to continue.

 ![MetaMask installation - 6](Images/metamask-6.png)

* In the next window, you should enter the twelve word mnemonic of your local wallet (your wallet password), and you should click on the `I have read and agree the Terms of Use` checkbox to continue.

* Be sure to read through the terms by clicking on the link.

 ![MetaMask installation - 7](Images/metamask-7.png)

* After filling out your wallet details, click on the "Import" button to continue, and you will see the following confirmation page.

 ![MetaMask installation - 8](Images/metamask-8.png)

* You may notice a message at the bottom of the page that says that `MetaMask cannot recover your seedphrase`, it means that once you import your keys, MetaMask won't export them again, so if you lose your mnemonic you can't extract it from MetaMask; keep your mnemonics in a safe place!

* Click on the "All Done" button to continue; you will see a page showing the balance of your wallet and the transaction history.

 ![MetaMask installation - 9](Images/metamask-9.png)

* You may note that you have `0 ETH` and no transactions. This is all right from now since you are not connected to your local blockchain.

Congratulations! You have installed MetaMask.

## Installing Ganache

[Ganache](https://www.trufflesuite.com/ganache) is a personal blockchain for Ethereum development you can use to deploy contracts, develop your applications, and run tests. It's available for Windows, OS X, and Linux.

To download Ganache, follow the next steps.

* Open the [Ganache website](https://www.trufflesuite.com/ganache) in your browser.

* Depending on your operating system, you will see the corresponding download button.

 | Ganache install button in Windows | Ganache install button in OS X |
 | ------------------------------------------------- | ------------------------------------------------- |
 | ![Ganache installation - 1](Images/ganache-1.png) | ![Ganache installation - 2](Images/ganache-2.png) |

* Click on the _Download_ button to save the installer to your computer.

### Running the Ganache Installer in OS X

* Open the installer file and drag the Ganache app to the "Applications" folder.

 ![Ganache installation - 3](Images/ganache-3.gif)

* Open the "Applications" folder and double-click on the "Ganache" icon. You will be asked for permission to run the application. You can safely click on the "Open" button to continue.

* Next, you will see a screen where the Ganache development team asks for your collaboration to share usage analytics with them. Choose the best option for you and click on the "Continue" button to finish the installation process.

 ![Ganache installation - 4](Images/ganache-4.gif)

### Running the Installer in Windows 10

* Open de installer file. A new window will pop-up asking to install Ganache.

* Make sure the "Launch when ready" checkbox is selected and click on the "Install" button to continue.

* Once the installation ends, the Ganache tool will be automatically launched after a few seconds.

* Next, you will see a screen where the Ganache development team asks for your collaboration to share usage analytics with them. Choose the best option for you and click on the "Continue" button to finish the installation process.

 ![Ganache installation - 5](Images/ganache-5.gif)

### Troubleshooting in Windows 10

If you see a warning message that says that Ganache is from an untrusted software publisher or source, you should enable the "Sideload apps" installation option as follows.

* Close the Ganache installer.

* Click on the "Windows" button and choose "Settings."

* In the "Windows Settings" search box type `developer` and choose `Developer settings."

* In the "Developer Settings" window, choose the "Sideload apps" options.

* You will see a warning message that states that you can expose your device to security risks. To install Ganache, you can safely click on the "Yes" button to continue.

* Close the "Windows Settings" window and open the Ganache installer again.

![Ganache installation - 6](Images/ganache-6.gif)

### Configuring a Workspace

* Launch the application to continue.

    ![Ganache releases](Images/ganache_create_workspace.png)

* Create a `New Workspace` and navigate through the various configuration pages. Apply the following settings on the following pages.

  * WORKSPACE
    * WORKSPACE NAME = `fintech`
    ![ganache_set_workspace_name.png](Images/ganache_set_workspace_name.png)

  * SERVER
    * HOSTNAME = `127.0.0.1`
    * PORT NUMBER = `8545`
    * AUTOMINE = `ON`
    ![ganache_set_server_info.png](Images/ganache_set_server_info.png)

  * ACCOUNTS & KEYS
    * ACCOUNT DEFAULT BALANCE = `100`
    * TOTAL ACCOUNTS TO GENERATE = `10`
    * AUTOGENERATE HD MNEMONIC = `YOUR MNEMONIC PHRASE`
    ![ganache_create_workspace.png](Images/ganache_import_mnemonic.png)

---
© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
