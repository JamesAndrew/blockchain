import hashlib

class Block:
    miner = ''
    n = 0
    nonce = 0
    data = []
    h = 0
    prevh = 0

    def __init__(self, miner, n, nonce, data, prevh):
        print('new block attempt')
        self.miner = miner
        self.n = n
        self.nonce = nonce
        self.data = data
        self.prevh = prevh

    def display(self):
        print('Peer ' + self.miner)
        print('# ' + str(self.n) + ", nonce = " + str(self.nonce))
        print(self.data)
        print('prevhash = ' + str(self.prevh))

    def mine(self):
        print('mining started')
        hashV = self.miner + str(self.n) + str(self.nonce) + str(self.data) + str(self.prevh)
        print(hashV)
        
        self.h = hashlib.sha256()
        self.h.update(hashV.encode('UTF-8'))
        print(self.h.hexdigest())
