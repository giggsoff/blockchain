from BaseBlockChain import BaseBlockChain
import requests
import hashlib


class QuantumBlockChain(BaseBlockChain):
    def __init__(self):
        super().__init__()
        self.kwip = "127.0.0.1"
        self.kwport = 55554

    def __init__(self, kwip, kwport):
        super().__init__()
        self.kwip = "127.0.0.1"
        self.kwport = 55554
        self.init_kw(kwip, kwport)

    def init_kw(self, kwip, kwport):
        self.kwip = kwip
        self.kwport = kwport

    def getlastkey(self):
        try:
            response = requests.post(f'http://{self.kwip}:{self.kwport}', data="last")
            response.raise_for_status()
        except:
            return 0
        block_string = bytearray.fromhex(response.text)
        hash256 = hashlib.sha256(block_string).hexdigest().upper()
        key = {
            'key': response.text,
            'sha': hash256
        }
        return key

    def getkeybysha(self, sha):
        try:
            response = requests.post(f'http://{self.kwip}:{self.kwport}', data=f'key{sha}')
            response.raise_for_status()
        except:
            return 0
        key = {
            'key': response.text,
            'sha': sha
        }
        return key

    def valid_chain(self, chain,quantum_hash,quantum_proof):
        """
        Determine if a given blockchain is valid

        :param chain: A blockchain
        :return: True if valid, False if not
        """

        last_block = chain[0]
        current_index = 1

        while current_index < len(chain):
            block = chain[current_index]
            print(f'{last_block}')
            print(f'{block}')
            print("\n-----------\n")
            # Check that the hash of the block is correct
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the Proof of Work is correct
            if not self.valid_quantum(last_block['proof'], block['proof'], block['previous_hash']):
                print("error in consistency")
                return False

            last_block = block
            current_index += 1

        quantum_key = self.getkeybysha(quantum_hash)
        if quantum_key == 0:
            print("NO SUCH KEY")
            return False
        guess = f'{chain[-1]["proof"]}{quantum_key["key"]}'.encode()
        guess_proof = hashlib.sha256(guess).hexdigest()
        return guess_proof == quantum_proof


    def proof_of(self, last_block):
        """
        Simple Proof of Work Algorithm:

         - Find a number p' such that hash(pp') contains leading 4 zeroes
         - Where p is the previous proof, and p' is the new proof

        :param last_block: <dict> last Block
        :return: <int>
        """

        last_proof = last_block['proof']
        last_hash = self.hash(last_block)
        raw_proof = f'{last_proof}{last_hash}'.encode()
        proof = hashlib.sha256(raw_proof).hexdigest()
        return proof

    @staticmethod
    def valid_block(last_proof, proof, last_hash):
        """
        Validates the Proof

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :param last_hash: <str> The hash of the Previous Block
        :return: <bool> True if correct, False if not.

        """

        guess = f'{last_proof}{last_hash}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash == proof

    def full_chain(self):
        quantum_key = self.getlastkey()
        guess = f'{self.chain[-1]["proof"]}{quantum_key["key"]}'.encode()
        guess_proof = hashlib.sha256(guess).hexdigest()
        response = {
            'chain': self.chain,
            'length': len(self.chain),
            'quantum_hash': quantum_key['sha'],
            'quantum_proof': guess_proof

        }
        return response