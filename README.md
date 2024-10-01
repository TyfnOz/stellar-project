## PayChat
![Team Logo](https://github.com/TyfnOz/stellar-project/blob/master/logo.png)
## About Me
Tayfun Özdemir is a Computer Engineering student at Ankara Yıldırım Beyazıt University. 
He enjoys reading, playing video games, chess, and coding in his free time. 
Recently, Tayfun participated in the Risein Stellar Fullstack Bootcamp, where he deepened his knowledge of software development. 
His growing interest in blockchain and Web3 technologies has sparked new opportunities and ambitions in his career path.

## Description
This project is built on the Stellar Blockchain and aims to enhance Bitcoin transactions by allowing users to add messages to their payments. 
Users can send payments using Bitcoin tokens while attaching custom messages, improving transparency and communication during transactions.
Additionally, the application allows users to make payments to multiple recipients in a single transaction, streamlining the process for those who need to distribute funds to various people or entities at once.
By leveraging Stellar's fast and low-cost network, this project provides an efficient and user-friendly solution for Bitcoin payments, making it easier to manage multi-recipient transactions and include relevant information directly with each payment.

## Vision
Our vision is to transform payment transactions into the safest and most useful experience for users by harnessing the power of blockchain and Web3 technologies. 
We aim to provide a secure platform where users can send Bitcoin payments with confidence, while adding personalized messages for greater clarity and transparency. 
With the ability to make multiple transactions in one go, our project will simplify and enhance the payment process, making it more efficient and user-friendly. 
We believe this will create a big impact by improving both the utility and security of everyday digital transactions.

## Project Roadmap / Future Plans
Software Development Plan:<br/>
Define Smart Contract Structure:<br/>

Create a smart contract on the Stellar blockchain that supports Bitcoin token payments.<br/>
Key variables:<br/>
sender, recipients[], amounts[], messages[], transactionID<br/>
Functions:<br/>
sendPayment() to process payments to multiple recipients.<br/>
addMessage() to attach a message to each transaction.<br/>
validateTransaction() to ensure sufficient funds and valid inputs.<br/>
Multi-Recipient Payment Functionality:<br/>

Develop logic to handle payments to multiple recipients in a single transaction.<br/>
Ensure proper fund allocation using amounts[] and update balances.<br/>
Message Attachment Feature:<br/>

Implement the addMessage() function to allow users to add text to each payment.<br/>
Integrate the message data with the transaction for blockchain verification.<br/>
Security & Optimization:<br/>

Add validation functions to check recipient addresses, transaction limits, and prevent unauthorized access.<br/>
Optimize gas fees and performance for multi-recipient payments.<br/>
Front-End Development:<br/>

Design a user-friendly interface allowing users to input recipient addresses, amounts, and messages.<br/>
Display transaction history, messages, and payment status.<br/>
Integrate wallet connection for Bitcoin token transfers.<br/>
Deployment & Testing:<br/>

Deploy the smart contract to Stellar’s testnet for rigorous testing.<br/>
Perform front-end testing to ensure all features work seamlessly.<br/>
Launch on the mainnet after final testing.<br/>

## Programming Language
Python

## Smart Contract Address
GACIHUBRFXJDETZ32ZQYTAF44TZDQW4YYPPHNJZFX7URTYGM7LA7MPSF

P.S.: This is the public key of account that i am using destination address
on my testing transactions. 

## Setup Environment
Bitcoin Multi-Recipient Payment with Message Integration <br/>
This project allows users to send Bitcoin payments to multiple recipients while attaching messages to each transaction, built on the Stellar blockchain.

Features<br/>
Send Bitcoin payments to multiple recipients.<br/>
Attach personalized messages to each transaction.<br/>
Easy-to-use interface for managing payments.<br/>

Prerequisites<br/>
Before you begin, ensure you have met the following requirements:<br/>

Python language installed.<br/>
Stellar SDK installed.<br/>
A Stellar wallet account (you can use the Stellar Laboratory, Testnet, expert etc.).<br/>
Git installed on your machine.<br/>
<br/>
Clone the repository:<br/>

git clone https://github.com/TyfnOz/stellar-project.git<br/>
cd stellar-project<br/>

Install stellar-sdk for python:<br/>
pip install --upgrade stellar-sdk<br/>

Run the code:<br/>
You can run the code. I wrote some test code for you to see results.
I gave destination address above. I am using this account as destination on my test transactions.
To see destination account: https://stellar.expert/explorer/testnet/account/GACIHUBRFXJDETZ32ZQYTAF44TZDQW4YYPPHNJZFX7URTYGM7LA7MPSF<br/>
To see source accounts, Ctrl+LeftClick on the link printed on console with under the title "Account Details".
So you will be able to see source account on testing transactions.
And the tests for getting balance or transaction history will be printed on the console
after all the transactions done.

