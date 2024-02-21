# Blockchain Simulation Project

This project is a simplified blockchain simulation written in Python. It demonstrates the core concepts of blockchain technology, including creating blocks, managing transactions with digital signatures, and implementing a basic Proof of Stake (PoS) consensus mechanism. The project is intended for educational purposes, illustrating how blockchain technology works under the hood.

## Features

- **Block Creation**: Generates new blocks and adds them to the blockchain, ensuring integrity through hashing.
- **Transaction Management**: Handles transactions, including the creation, signing with digital signatures, and verification.
- **Proof of Stake (PoS) Consensus**: Simulates a basic PoS mechanism for miner selection based on stake.
- **Multi-threading**: Demonstrates concurrent blockchain operations using Python's threading module.


## Getting Started

### Prerequisites

- Python 3.7 or higher
- `cryptography` library

### Installation

1. **Clone the Repository**

```sh
git clone https://github.com/mikehsin/blockchain-simulation.git
```


2. **Navigate to the Project Directory**

```sh
cd blockchain-simulation
```

3. **Install Dependencies**

Make sure you have Python installed on your system. Then, install the required Python packages:

```sh
pip install cryptography
```


### Running the Simulation

Execute the `main.py` script to start the blockchain simulation:

```sh
python main.py
```


This will initiate two concurrent blockchain processes, showcasing the creation and validation of blocks and transactions.

## Project Structure

- `crypto_utils.py`: Contains cryptographic utilities for key generation, signing, and verifying signatures.
- `AdvancedBlockchain.py`: Implements the blockchain logic, including block creation, transaction handling, and the PoS consensus mechanism.
- `main.py`: The entry point of the simulation, demonstrating concurrent blockchain operations.

## How It Works

1. **Key Generation**: Public-private key pairs are generated for transaction signing and verification.
2. **Creating Transactions**: Transactions are created, signed by the sender, and verified using digital signatures.
3. **Adding Blocks**: Valid transactions are grouped into blocks, which are then added to the blockchain following the PoS consensus rules.
4. **Validation**: The integrity of the blockchain is maintained through cryptographic hashes and signature verification.

## Advanced Features

### Multi-Programming

This project also demonstrates the use of multi-programming to simulate concurrent blockchain operations. By leveraging Python's `threading` module, the simulation can run multiple blockchain processes in parallel, showcasing how a real-world blockchain system might handle simultaneous transactions and block creation across different nodes.

To see multi-programming in action, refer to the `main.py` script, where multiple threads are initiated to run different blockchain instances concurrently. This approach highlights the blockchain's ability to operate in a distributed and parallelized environment, which is fundamental to its scalability and efficiency.

### Usage Examples

#### Signing and Verifying a Transaction

Below is an example of how to use the `sign_transaction` function within this project to sign transaction data with a private key and then verify the signature with the corresponding public key:

```python
from crypto_utils import generate_keys, sign_transaction, verify_signature

# Generate public and private keys
private_key, public_key = generate_keys()

# Serialize the transaction data
transaction_data = "Sender: Alice, Receiver: Bob, Amount: 100"

# Sign the transaction data using the private key
signature = sign_transaction(private_key, transaction_data)

# Verify the signature using the public key
is_signature_valid = verify_signature(public_key, transaction_data, signature)

print(f"Signature Valid: {is_signature_valid}")
```

## Contributing

We welcome contributions to this project! Please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
