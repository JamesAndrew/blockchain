import boto3
import hashlib

# define object Block with attributes miner name, block number n, nonce, data, hash h, and previous hash
class Block:
    miner = ''
    coinbase = 0
    n = 0
    nonce = 0
    data = []
    h = 0
    prevh = 0

    def __init__(self, miner, coinbase, n, data, prevh):
        print('new block attempt')
        self.miner = miner
        self.coinbase = coinbase
        self.n = n
        self.data = data
        self.prevh = prevh

    # create local copy of a block from another miner
    def otherBlock(self, miner, coinbase, n, nonce, data, h, prevh):
        self.miner = miner
        self.coinbase = coinbase
        self.n = n
        self.nonce = nonce
        self.data = data
        self.h = h
        self.prevh = prevh

    def display(self):
        print('Peer ' + self.miner)
        print('coinbase = ' + str(self.coinbase))
        print('# ' + str(self.n) + ", nonce = " + str(self.nonce))
        print(self.data)
        print('hash = ' + self.h)
        print('prevhash = ' + str(self.prevh))

    def mine(self):
        print('mining started')

        # is block being mined
        mining = True
        while(mining):
            hashV = self.miner + str(self.coinbase) + str(self.n) + str(self.nonce) + str(self.data) + str(self.prevh)
            self.h = hashlib.sha256()
            self.h.update(hashV.encode('UTF-8'))
            s = self.h.hexdigest()
            if s[0] == '0' and s[1] == '0' and s[2] == '0' and s[3] == '0':
                mining = False
                self.h = s 
            else:
                self.nonce = self.nonce + 1        
