def printl(s):
    for i in s:
        print(i,end=' ')

def position_add(pos):
    global dash
    for i in range(len(wordl)):
        if(i == pos):
            dash[i] = wordl[i]
    

def check(guess):
    flag = False
    for i in range(len(wordl)):
        if(guess == wordl[i]):
            position_add(i)
            flag = True
    
    if flag == False:
        print("Nope")
    
    printl(dash)

def guess_check():
    for i in dash:
        if(i == '_'):
            return 1
    return 2

print("welcome to hangman")
print("You will be given 10 tries to guess the word letter by letter")
print("lets play")

word = input("enter a word :")
wordl = list(word)
len_word = len(word)
vowel_count = 0
dash = []

for i in range(len(wordl)):
    dash += '_'

for i in wordl:
    if(i in "AEIOUaeiou"):
        vowel_count += 1

print("the word has {} letters and {} vowels".format(len_word,vowel_count))

for i in range(10):
    guess = input("enter a letter to guess :")
    check(guess)
    x = guess_check()
    if(x == 2):
        print("\nYEP YOU GUESSED IT. WELL DONE")
        break