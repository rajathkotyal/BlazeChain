import json
from Flask import flask, jsonify
import hashlib
import datetime

class blockchain(self):
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash=0)


    def create_block(self, proof, previous_hash):
        block = {'index' : len(str(chain)),
                'timestamp' : datetime.datetime.now(),
                'proof' : proof,
                'previous_hash' : previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(chain):
        return chain[-1]


    def hash(self, block):
        x = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(x).hexdigest()


    def proof_of_work(self, previous_proof, chain):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            proof = hashlib.sha256(str(previous_proof**2 - new_proof**2).encode()).hexdigest()
            if proof[:4] == '0000':
                check_proof = True
            else new_proof +=1
        return new_proof


    def check_proof():
        previous_block = chain[0]
        block_index = 1

        while block_index != len(chain):
            curr_block = chain[block_index]
            if curr_block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            curr_proof = curr_block['proof']
            hashOp = hashlib.sha256(str(previous_proof**2 - curr_proof**2).encode()).hexdigest()
            if hashOp[:4] != '0000':
                return False
            previous_block = curr_block
            block_index +=1
        return True

        
