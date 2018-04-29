import boto3
import block

sqs = boto3.resource('sqs')

miner = input("miner name")

chain = []

# create initial block if miner a
if (miner == 'a'):
    b = block.Block(miner, 100, 0, "", 0)
    b.mine()
    chain.append(b)

    # send block to everyone
    sqs.get_queue_by_name(QueueName='nodeb').send_message(MessageBody="add," + b.miner + ',' \
        + str(b.coinbase) + ',' + str(b.n) + ',' + str(b.nonce) + ',' + str(b.data) + ',' \
        + str(b.h) + ',' + str(b.prevh))

def checkMsgs():
    msg = sqs.get_queue_by_name(QueueName='node' + miner).receive_messages()
    m = msg[0].body.split(",")
    if m[0] == 'add':
        c = block.Block(miner, 0, "", 0)
        c.otherBlock(m[1], m[2], m[3], m[4], m[5], m[6], m[7])
        chain.append(c)
        msg[0].delete()

def createBlock():
    print("New transaction") 
    f = miner
    amount = input("amount?")
    t = input("to?")
    transaction = f + '|' + amount + '|' + t
    

# main loop
loop = True
while loop:
    print("BLOCKCHAIN")
    print("options - (0) quit, (1) mine, (2) display blockchain, (3) check messages")
    option = input("option?")
    if option == "0":
        loop = False
    elif option == "1":
        print("mining")
    elif option == "2":
        print("displaying blockchain")
        for item in chain[:]:
            item.display()
    elif option == "3":
        print('checking messages')
        checkMsgs()
    else:
        print("not a valid option")
