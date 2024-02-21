import hashlib
import time
import random
from crypto_utils import generate_keys, sign_transaction, verify_signature
from cryptography.hazmat.primitives import serialization

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender  # This would now represent the sender's public key
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def to_string(self):
        # Handle the case where sender and receiver are not actual public key objects
        sender_key_str = (self.sender.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')) if hasattr(self.sender, 'public_bytes') else str(self.sender)
        
        receiver_key_str = (self.receiver.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')) if hasattr(self.receiver, 'public_bytes') else str(self.receiver)
        
        return f"From: {sender_key_str}, To: {receiver_key_str}, Amount: {self.amount}, Signature: {self.signature}"

    def sign_transaction(self, private_key):
        self.signature = sign_transaction(private_key, self)

    def is_valid(self):
        # Check if the transaction has a signature and verify it
        if self.signature is None:
            return False
        return verify_signature(self.sender, self, self.signature)

class BlockV2:
    def __init__(self, index, timestamp, transactions, previous_hash='0'):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions  # A list of transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self):
        block_string = f"{self.index}{self.timestamp}{[transaction.to_string() for transaction in self.transactions]}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        # The Proof of Work algorithm
        # Adjust the nonce until the hash meets the difficulty criteria
        required_prefix = '0' * difficulty
        while not self.hash.startswith(required_prefix):
            self.nonce += 1
            self.hash = self.compute_hash()
        print(f"Block mined: {self.hash}")


class BlockchainV2:
    def __init__(self, difficulty=2):
        self.chain = [self.create_origin_block()]
        self.difficulty = difficulty
        self.node_balances = {"Node1": 1, "Node2": 2}
    
    def create_origin_block(self):
        # Creates the first block in the blockchain, the genesis block
        # Use None or a special placeholder for genesis transaction sender and receiver
        genesis_tx = Transaction("Genesis", "Genesis", 0, signature="GenesisSignature")
        return BlockV2(0, time.time(), [genesis_tx], "0")


    def add_new_block(self, transactions):
        miner = self.select_miner()
        print(f"Selected {miner} as the miner.")

        # Assuming you have a way to get the miner's public key or a placeholder
        miner_public_key = "MinerPublicKeyPlaceholder"

        # Create and sign a miner reward transaction (simplified, consider how you'd actually sign this)
        miner_reward_tx = Transaction("Network", miner_public_key, 1)
        # In a real scenario, the Network's signature would be required
        miner_reward_tx.signature = "NetworkSignaturePlaceholder"

        transactions_with_reward = transactions + [miner_reward_tx]
        
        # Get the last block's hash to link the new block
        last_block_hash = self.get_last_block().hash
        
        # Create a new block with the validated transactions
        new_block = BlockV2(len(self.chain), time.time(), transactions_with_reward, last_block_hash)
        
        # Mine the new block
        new_block.mine_block(self.difficulty)
        
        # Add the newly mined block to the blockchain
        self.chain.append(new_block)

    def select_miner(self):
        # Simplified miner selection based on balance
        total_stakes = sum(self.node_balances.values())
        select_point = random.randint(1, total_stakes)
        current = 0
        for node, balance in self.node_balances.items():
            current += balance
            if current >= select_point:
                return node
            
    def adjust_difficulty(self):
        if len(self.chain) % self.adjust_difficulty_interval == 0:
            last_block = self.chain[-1]
            prev_adjustment_block = self.chain[-self.adjust_difficulty_interval]
            time_expected = 10 * self.adjust_difficulty_interval  # 10 seconds per block, for example
            time_taken = last_block.timestamp - prev_adjustment_block.timestamp

            if time_taken < time_expected:
                self.difficulty += 1
            else:
                self.difficulty = max(1, self.difficulty - 1)

    def get_last_block(self):
        return self.chain[-1]

    def is_valid(self):
    # Check the integrity of the block and its transactions
        # for i in range(1, len(self.chain)):
        #     current = self.chain[i]
        #     previous = self.chain[i - 1]

        #     # Validate block hash
        #     if current.hash != current.compute_hash():
        #         print("Invalid block hash detected.")
        #         return False
        #     if current.previous_hash != previous.hash:
        #         print("Invalid chain linkage detected.")
        #         return False

        #     # Extend validation to include transaction signatures within each block
        #     for transaction in current.transactions:
        #         if not transaction.is_valid():
        #             print("Invalid transaction detected.")
        #             return False
                    
        # return True
        transaction_data = self.to_string()  # Serialize transaction data for verification
        # No need to encode the public_key here, pass it directly
        return verify_signature(self.sender, transaction_data, self.signature)



if __name__ == "__main__":
    blockchain = BlockchainV2(difficulty=2)
    transactions = [Transaction("Alice", "Bob", 50, "example_signature"), Transaction("Charlie", "Dave", 25, "another_example_signature")]

    # Adding blocks without specifying a miner_address
    blockchain.add_new_block(transactions)
    blockchain.add_new_block(transactions)

