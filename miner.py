import boto3
import block

sqs = boto3.resource('sqs')

miner = input("miner name")

chain = []

def sendMsgs(m):
    for char in 'abcd':
        if char != miner:
            sqs.get_queue_by_name(QueueName='node' + char).send_message(MessageBody=m)

def checkMsgs():
    msg = sqs.get_queue_by_name(QueueName='node' + miner).receive_messages()
    m = msg[0].body.split(",")
    if m[0] == 'add':
        c = block.Block(miner, 0, 0, "", 0)
        c.otherBlock(m[1], m[2], m[3], m[4], m[5], m[6], m[7])
        chain.append(c)
        msg[0].delete()
    elif m[0] == 'verfy':
        print("varifying")
    elif m[0] == 'verified':
        print("varified")
    else:
        print("not a valid msg")

def createBlock():
    first = input("your first block?")
    if first == 'y':
        coins = 100
    else:
        coins = 0
    print("New transaction") 
    f = miner
    amount = input("amount?")
    t = input("to?")
    tx = f + '|' + amount + '|' + t
    lblock = chain[-1]
    num = lblock.n + 1
    ph = lblock.h
    newb = block.block(miner, coins, num, tx, ph)
    if newb.verify():
        newb.mine()
        chain.append(newb)
        # send block to everyone
        sendMsgs("add," +newb.miner + ',' + str(newb.coinbase) + ',' + str(bnew.n) + ',' \
            + str(newb.nonce) + ',' + str(newb.data) + ',' + str(newb.h) + ',' + str(newb.prevh))
            
# create initial block if miner a
if (miner == 'a'):
    b = block.Block(miner, 100, 0, "", 0)
    b.mine()
    chain.append(b)

    # send block to everyone
    sendMsgs("add," + b.miner + ',' + str(b.coinbase) + ',' + str(b.n) + ',' + str(b.nonce) + ',' \
        + str(b.data) + ',' + str(b.h) + ',' + str(b.prevh))

# main loop
loop = True
while loop:
    print("BLOCKCHAIN")
    print("options - (0) quit, (1) mine, (2) display blockchain, (3) check messages")
    option = input("option?")
    if option == "0":
        loop = False
    elif option == "1":
        print("create block")
        createBlock()
    elif option == "2":
        print("displaying blockchain")
        for item in chain[:]:
            item.display()
    elif option == "3":
        print('checking messages')
        checkMsgs()
    else:
        print("not a valid option")
