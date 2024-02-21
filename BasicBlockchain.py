import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Creating the blockchain and adding blocks
my_blockchain = Blockchain()
my_blockchain.add_block(Block(1, time.time(), "Block 1 Data"))
my_blockchain.add_block(Block(2, time.time(), "Block 2 Data"))

# Verifying the blockchain
print("Is Blockchain valid?", my_blockchain.is_chain_valid())

# Printing the blockchain
for block in my_blockchain.chain:
    print(f"Block {block.index}:\nHash: {block.hash}\nPrevious Hash: {block.previous_hash}\nData: {block.data}\n")
