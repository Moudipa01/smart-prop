# Smart Prop
Smart Prop is a secure land transaction platform built on top of the blockchain technology. The platform is designed to facilitate transactions between buyers and sellers of land in a secure and transparent manner. The project is implemented using Django web framework and uses Ganache Server to connect to the Ethereum network.

The smart contract that governs the transactions is deployed on Remix IDE, and its ABI is used to interact with it. The platform allows the seller to transfer land ownership to the buyer in exchange for cryptocurrency, making the transaction fast, secure, and transparent.

## How to run

To run the project, follow these steps:

- Clone the repository to your local machine.
- Create a virtual environment and activate it.
- Install the required dependencies using the command `pip install -r requirements.txt`
- Set up a Ganache server and connect to it using the ganache_url variable in the code (views.py file).
- Deploy the smart contract given in the code on Remix IDE or any other IDE and get its ABI and contract address.
- Set the ABI and contract address in the code using the abi and contract_address variables, respectively.
- Set up a private key for the seller's account and store it in the code. 
- Run the Django server using the command `python manage.py runserver`
- Open your browser and go to `http://127.0.0.1:8000/` to access the platform.


