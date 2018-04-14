import boto3
import block

miner = input("miner name")

# create initial block if it doesn't exist
b = block.Block(miner, 0, 0, "", 0)
b.mine()
chain = []
chain.append(b)

# main loop
loop = True
while loop:
    print("BLOCKCHAIN")
    print("options - (0) quit, (1) mine, (2) display blockchain")
    option = input("option?")
    if option == "0":
        loop = False
    elif option == "1":
        print("mining")
    elif option == "2":
        print("displaying blockchain")
        for item in chain[:]:
            item.display()
    else:
        print("not a valid option")
