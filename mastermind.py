from random import randint

def generate():
        global numl
    
        for i in range(4):
            x = randint(1,9)
            numl.append(x)

def generate_2():
    global num
    num = numl[0]*1000+numl[1]*100+numl[2]*10+numl[3]
    
        
def colour(count):
    if(count == 0):
        return "BLUE"
    elif(count == 1):
        return "WHITE"
    elif(count == 2):
        return "RED"

def check(guess_num,guess_pos):
    global numl
    
    count = 0
    if guess_num in numl:
        count = 1
        for i in range(len(numl)):
            if(guess_num == numl[i]):
                if(guess_pos == i+1):
                    count = 2
    
    ret = colour(count)
    return ret
    

print("WELCOME TO MASTERMIND")
print("ALL NUMBERS ARE 4 DIGITS");
print("RED - position and number are correct")
print("WHITE - correct number but wrong position")
print("BLUE - wrong number and wrong position\n")

numl = []
num = 0
generate()
generate_2()


for i in range(12):
    guess_num = int(input("enter number to guess :"))
    guess_pos = int(input("enter position of number :"))
    
    ret = check(guess_num,guess_pos)
    print(ret)
    
    br = input("Press 'Y' if you think that you have guessed the number else press anything else :")
    print("\n")
    if(br in "Yy"):
        break
    
answer = int(input("enter final answer :"))

if(answer == num):
    print("CORRECT")
    print("number was -",num)
else:
    print("WRONG")
    print("number was -",num)

