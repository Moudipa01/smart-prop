from django.shortcuts import render
from django.http import HttpResponse
from web3 import Web3, HTTPProvider
from eth_account import Account
import json
from eth_utils import to_wei
from .forms import TransferForm
from django.views import View

ganache_url = 'http://127.0.0.1:7545'

# load the compiled bytecode and ABI for the smart contract
abi =json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"message","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address payable","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"string","name":"_message","type":"string"}],"name":"transfer","outputs":[],"stateMutability":"payable","type":"function"}]')

# define the smart contract address
contract_address = Web3.to_checksum_address('0x550061F4fE23cD83963B9682cDC789cE823F5b33')

# create a Web3 object to interact with the Ethereum network
w3 = Web3(HTTPProvider('http://127.0.0.1:7545'))

# create a contract object using the ABI and contract address
contract = w3.eth.contract(address=contract_address, abi=abi)

# create a new Ethereum account to interact with the smart contract
private_key = '0x23ae680c76b67c0f8cbc6cb66a04e277bcdbf16a52679b581786127628713e98'
account = Account.from_key(private_key)

class TransferView(View):
    def get(self,request):
        form = TransferForm()
        return render(request, 'transact.html', {'form': form})

    def post(self,request):
        form = TransferForm(request.POST or None)
        if form.is_valid():
            recipient_address = form.cleaned_data.get('receiver_address')
            amount = int(form.cleaned_data.get('amount'))
            message = form.cleaned_data.get('message')
            txn = {
                'from': account.address,
                'to': recipient_address,
                'value': to_wei(amount, 'ether'),
                'gas': 200000,
                'gasPrice': to_wei('50', 'gwei'),
                'nonce': w3.eth.get_transaction_count(account.address),
            }

            # Signing the transaction with private key
            signed_txn = account.signTransaction(txn)

            # Sending the transaction to Ethereum network
            txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            # Waiting for the transaction to be mined
            txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)

            form = TransferForm()
            
            # Displaying the success message
            return render(request, 'success.html',{'hash':txn_hash,'receipt':txn_receipt})
        else:
            return render(request, 'fail.html')

