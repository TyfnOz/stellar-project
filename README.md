## PayChat

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
Software Development Plan:

Define Smart Contract Structure:

Create a smart contract on the Stellar blockchain that supports Bitcoin token payments.
Key variables:
sender, recipients[], amounts[], messages[], transactionID
Functions:
sendPayment() to process payments to multiple recipients.
addMessage() to attach a message to each transaction.
validateTransaction() to ensure sufficient funds and valid inputs.
Multi-Recipient Payment Functionality:

Develop logic to handle payments to multiple recipients in a single transaction.
Ensure proper fund allocation using amounts[] and update balances.
Message Attachment Feature:

Implement the addMessage() function to allow users to add text to each payment.
Integrate the message data with the transaction for blockchain verification.
Security & Optimization:

Add validation functions to check recipient addresses, transaction limits, and prevent unauthorized access.
Optimize gas fees and performance for multi-recipient payments.
Front-End Development:

Design a user-friendly interface allowing users to input recipient addresses, amounts, and messages.
Display transaction history, messages, and payment status.
Integrate wallet connection for Bitcoin token transfers.
Deployment & Testing:

Deploy the smart contract to Stellar’s testnet for rigorous testing.
Perform front-end testing to ensure all features work seamlessly.
Launch on the mainnet after final testing.

## Programming Language
Python

## Smart Contract Address
GACIHUBRFXJDETZ32ZQYTAF44TZDQW4YYPPHNJZFX7URTYGM7LA7MPSF

P.S.: This is the public key of account that i am using destination address
on my testing transactions. 

## Setup Environment
Bitcoin Multi-Recipient Payment with Message Integration
This project allows users to send Bitcoin payments to multiple recipients while attaching messages to each transaction, built on the Stellar blockchain.

Features
Send Bitcoin payments to multiple recipients.
Attach personalized messages to each transaction.
Easy-to-use interface for managing payments.

Prerequisites
Before you begin, ensure you have met the following requirements:

Python language installed.
Stellar SDK installed.
A Stellar wallet account (you can use the Stellar Laboratory, Testnet, expert etc.).
Git installed on your machine.

Clone the repository:

git clone https://github.com/TyfnOz/stellar-project.git
cd stellar-project

Install stellar-sdk for python:
pip install --upgrade stellar-sdk

Run the code:
You can run the code. I wrote some test code for you to see results.
I gave destination address above. I am using this account as destination on my test transactions.
To see destination account: https://stellar.expert/explorer/testnet/account/GACIHUBRFXJDETZ32ZQYTAF44TZDQW4YYPPHNJZFX7URTYGM7LA7MPSF
To see source accounts, Ctrl+LeftClick on the link printed on console with under the title "Account Details".
So you will be able to see source account on testing transactions.
And the tests for getting balance or transaction history will be printed on the console
after all the transactions done.

