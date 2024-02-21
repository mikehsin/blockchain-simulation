import threading
from AdvancedBlockchain import BlockchainV2, Transaction
from BasicBlockchain import Blockchain, Block
from crypto_utils import generate_keys, sign_transaction, verify_signature
import time

def run_blockchain_1():
    blockchain1 = Blockchain()
    blockchain1.add_block(Block(1, time.time(), "First Block Data"))
    blockchain1.add_block(Block(2, time.time(), "Second Block Data"))
    print("Blockchain 1 Valid:", blockchain1.is_chain_valid())

def run_blockchain_2():
    # Initialize the blockchain with a difficulty level
    blockchain2 = BlockchainV2(difficulty=2)

    # Generate key pairs for two users (Alice and Bob)
    alice_private_key, alice_public_key = generate_keys()
    bob_private_key, bob_public_key = generate_keys()

    # Create a transaction from Alice to Bob
    # Note: Assuming `Transaction` constructor accepts public key objects and `sign_transaction`
    # returns a bytes object representing the signature.
    transaction1 = Transaction(sender=alice_public_key, receiver=bob_public_key, amount=50)

    # Prepare transaction data for signing (serialize transaction data)
    transaction_data_to_sign = transaction1.to_string()

    # Sign the transaction with Alice's private key
    signature = sign_transaction(alice_private_key, transaction_data_to_sign)
    transaction1.signature = signature

    # Verify the transaction signature before adding it to the blockchain
    if verify_signature(alice_public_key, transaction_data_to_sign, signature):
        print("Transaction signature verified successfully.")
    else:
        print("Failed to verify transaction signature.")
        return

    # Add the verified transaction to the blockchain
    blockchain2.add_new_block([transaction1])

    # Output the blockchain contents
    for block in blockchain2.chain:
        print(f"Block {block.index}:")
        print(f"Hash: {block.hash}")
        for transaction in block.transactions:
            print(f"From: {transaction.sender}, To: {transaction.receiver}, Amount: {transaction.amount}")


if __name__ == "__main__":
    thread1 = threading.Thread(target=run_blockchain_1)
    thread2 = threading.Thread(target=run_blockchain_2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("Both blockchains executed concurrently.")

