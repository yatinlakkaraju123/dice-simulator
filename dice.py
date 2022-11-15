import random
print("******welcome to dice simulator enter any integer to roll the dice and  -1 to stop*******")

inp = 0
while(inp!=-1):
        try:
                inp = int(input("enter:"))
        except:
                print("the entered input is not an integer please enter an integer")
        else:
                if(inp!=-1):
                        print("dice:",random.randrange(1,6))
