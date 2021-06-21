#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 00:27:04 2021

@author: rajath
"""

#Create CryptoCurrency
#Flask==0.12.2
#requests==2.18.4

# Importing the libraries
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


# ! CREATING CHAIN
class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions' : self.transactions}
        transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]               #previous_block = chain[0] = block1 = dict = therefore
        block_index = 1                            #previous_block = dict
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender' : sender,
                                'receiver' : receiver,
                                'amount' : amount})
        previous_block = self.get_previous_block()
        return previous_block['index']+1

    def add_node(self, address):
        parsed_url = urlparse(address)
        return self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = length(longest_chain)

        for node in network:
            response = response.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain =  response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True
        return False


# ! MINING - PoW

#node address creation at port 5000
node_address = str(uuid4()).replace('-','')

# Creating flask Web App
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

# Creating a Blockchain obj
blockchain = Blockchain()

# Mining new block
@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()        #1st block : i=1, time, p=1, ph=0, hash = 23523
    previous_proof = previous_block['proof']                #2nd block :i=2, time, p=00003435,  ph = 23523, hash = 4243
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(sender = node_address, receiver = 'rajath', amount = 10)
    block = blockchain.create_block(proof, previous_hash)
    response = {'message': 'Congrats nibba, you mined a block',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions' : block['transactions']}
    return jsonify(response), 200


# ! DECENTRALIZING



# ! POSTMAN
# Getting the entire Blockchain
@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200

# Checking if Blockchain is valid
@app.route('/is_valid', methods = ['GET'])
def is_valid():
    check = blockchain.is_chain_valid(blockchain.chain)
    if check:
        response = {'message' : 'Chain is valid'}
    else :
        response = {'message' : 'Chain is invalid'}
    return jsonify(response), 200

#adding transaction to Blockchain
@app.route('/add_transaction', methods = ['POST'])
def add_transaction():
    json_values = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json_values for key in transaction_keys):
        return 'Please enter all the necessary values', 400
    index = blockchain.add_transaction(json_values['sender'], json_values['receiver'], json_values['amount'])
    response =  {'message' : f'your transaction will be added to block number {index}'}
    return jsonify(response), 201

#Adding/Connecting new nodes to the network
@app.route('/connect_node', methods = ['POST'])
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return 'no node input' , 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message' : 'The nodes present in blazecoin blockchain are : ',
                'total_nodes' : list(blockchain.nodes)}
    return jsonify(response), 201

@app.route('/is_chain_replaced', methods = ['GET'])
def is_chain_replaced():
    check = blockchain.replace_chain()
    if check:
        response = {'message' : 'Nodes had different chains, Block replaced with the longest chain',
                    'curr_chain' : blockchain.chain}
    else :
        response = {'message' : 'Chain in all nodes were the same. No updates. Its all good.',
                    'curr_chain' : blockchain.chain}
    return jsonify(response), 200


# Run app
app.run(host = '0.0.0.0', port = 5000)
