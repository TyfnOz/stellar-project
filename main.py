"""
Ödeme ve Mesajlaşma Sistemi
    XLM transferi yapma  +
    Transfer işlemlerine kısa mesaj ekleme +
    Bakiye sorgulama (get_balance) +
Ek Özellikler:
    Düzenli ödemeler -
    Çoklu alıcıya transfer (multi_transfer) +
    İşlem geçmişi görüntüleme (get_transaction_history) +

NOT: Testnet deploy'u yok (smart contract kullanılmadığı için)

"""

from stellar_sdk import Server, Keypair, TransactionBuilder, Network, Asset
import requests

def create_account():
    """
        Creates an account and returns its keypair
    """
    keypair = Keypair.random()
    url = "https://friendbot.stellar.org"
    _response = requests.get(url, params={"addr": keypair.public_key})
    return keypair

# Configure horizon testnet server
server = Server(horizon_url="https://horizon-testnet.stellar.org")

base_fee = 100

def single_transfer(source:str, transfer_data:dict):
    """
        params:
            `source` (str): Secret key of source account \n

            `transfer_data` (dict): Dictionary with destination address, message and amount info

        returns (Dict[str, any]): 
            If current balance is less than amount to be transferred, raise Exception,
            else do the transfer and return horizon server's response.
    """
    source_keypair = Keypair.from_secret(source)
    
    if get_balance(source_keypair.public_key) < transfer_data["amount"]:
        raise Exception("Not enough balance to make this payment.")
    
    source_account = server.load_account(source_keypair)

    transaction = (
    TransactionBuilder(
        source_account=source_account,
        network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
        base_fee=base_fee,
    )
    .add_text_memo(transfer_data["message"])  # Add a message
    # Add a payment operation to the transaction
    # Send `amount` of XLM to dest address
    .append_payment_op(transfer_data["dest"], Asset.native(), str(transfer_data["amount"]))
    .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
    .build()
    )

    # Sign this transaction with the secret key
    transaction.sign(source_keypair)
    # Submit the transaction to the Horizon server.
    response = server.submit_transaction(transaction)
    print(f"Transfer success: {response['successful']}")
    return response


def multi_transfer(source:str, transfer_data:list) -> str:
    """
        params:
            `source` (str): Secret key of source account \n

            `transfer_data` (list(dict)): List of dictionaries with destination addresses, messages and amount informations

        returns (str): 
            If current balance is less than total amount to be transferred, raise Exception,
            else do the transfers and return success message.
    """
    source_keypair = Keypair.from_secret(source)

    amount = 0
    for i in range(len(transfer_data)):
        amount = amount + transfer_data[i]["amount"]

    if get_balance(source_keypair.public_key) < amount:
        raise Exception("Not enough balance to complete all these transfers")
    
    source_account = server.load_account(source_keypair)
    
    for i in range(len(transfer_data)):
        try:
            transaction = (
                TransactionBuilder(
                    source_account=source_account,
                    network_passphrase=Network.TESTNET_NETWORK_PASSPHRASE,
                    base_fee=base_fee,
                )
                .add_text_memo(transfer_data[i]["message"])  # Add a message
                # Add a payment operation to the transaction
                # Send `amount` of XLM to receiver
                .append_payment_op(transfer_data[i]["dest"], Asset.native(), str(transfer_data[i]["amount"]))
                .set_timeout(30)  # Make this transaction valid for the next 30 seconds only
                .build()
            )

            transaction.sign(source_keypair)
            response = server.submit_transaction(transaction)
            print(f"Transaction {i}, successful: {response['successful']}")
        except Exception as err:
            print(f"Unexpected error {err=}, {type(err)=} occurred.")
            raise

    return str("All transfers completed successfully.")

def get_balance(account_id:str) -> float:
    """
        params:
            `account_id` (str): Public key of account to get balance
        
        returns (float): 
            Current balance of account
    """
    url = f"https://horizon-testnet.stellar.org/accounts/{account_id}"
    _request = requests.get(url)
    jsonResponse = _request.json()
    balance = float(jsonResponse["balances"][0]["balance"])
    return balance


def get_transaction_history(account_id:str, limit = 10) -> list:
    """
    Prints transactions to console and returns list of last `limit` amount of transactions.
        params:
            `account_id` (str): Public key of account to get transactions
            `limit` (int): Number of last transaction to be listed 
        returns:
            List of all transactions with information of source, dest., date, success, amount and message 
    """
    url = f"https://horizon-testnet.stellar.org/accounts/{account_id}/payments?limit={limit}&order=desc"
    _request = requests.get(url)
    jsonResponse = _request.json()
    
    transactionRecords = jsonResponse["_embedded"]["records"]
    transaction_list = list()

    print("###### TRANSACTION HISTORY ######")
    for i in range(len(transactionRecords)):
        if 'from' not in transactionRecords[i]:
            continue
        else:
            frm = transactionRecords[i]['from']
            to = transactionRecords[i]['to']
            transaction_success = transactionRecords[i]['transaction_successful']
            amount = transactionRecords[i]['amount']
            created = transactionRecords[i]['created_at']
            transaction_hash = transactionRecords[i]['transaction_hash']

            url = f"https://horizon-testnet.stellar.org/transactions/{transaction_hash}"
            _request = requests.get(url)
            jsonResponse = _request.json()
        
            if 'memo' not in jsonResponse:
                continue
            else:
                message = jsonResponse['memo']
                transaction_list.append((frm, to, created, transaction_success, amount, message))

                print(f"From: {frm}")
                print(f"To: {to}")
                print(f"Created at: {created} \nSuccess: {transaction_success} \nAmount: {amount} \nMessage: {message}")
                print(f"Transaction hash: {transaction_hash}")
                print()
    return transaction_list

if __name__ == "__main__":
    # Tests
    source_keypair = create_account()
    source_secret = source_keypair.secret
    source_public = source_keypair.public_key
    print(f"Account id: {source_public}")
    print("Account details:")
    print(f"https://stellar.expert/explorer/testnet/account/{source_public}")

    balance = get_balance(source_public)
    print(f"Balance before transfers: {balance}")

    first_transfer = { "dest": create_account().public_key, "message": "stellar", "amount": 1.23}
    second_transfer = { "dest": create_account().public_key, "message": "soroban", "amount": 4.56}
    third_transfer  = { "dest": create_account().public_key, "message": "risein", "amount": 7.89}
    
    multi_transfer_data = [first_transfer, second_transfer, third_transfer]

    multi_transfer(source_secret, multi_transfer_data)

    get_transaction_history(source_public, limit=5)

    single_transfer_data = {"dest": create_account().public_key, "message": "risein stellar bootcamp", "amount": 3.57}
    single_transfer(source_secret, single_transfer_data)

    get_transaction_history(source_public, limit=5)

    balance = get_balance(source_public)
    print(f"Balance after transfers: {balance}")
