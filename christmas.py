import random
import string
from os import system

def grand():
    rawData = string.punctuation+" "*50
    rand_pswd = ''.join(random.choice(rawData) for i in range(1))
    return rand_pswd
def grandtxt():
    rawData = "$#&"
    rand_pswd = ''.join(random.choice(rawData) for i in range(1))
    return rand_pswd

try:
    system("clear")
except:
    system("cls")

sl = "/"
bsl = "\\"
print(" "*80+"**")
print(" "*80+"**")
dist = 80
i = 0
num = 0
col = 10
while(num<3):
    print(" "*dist+sl,end="")
    for n in range(i*2):
        print(grand(),end="")
    print(bsl)
    dist -=1
    i+=1
    if(i == col and dist > 5):
        print(" "*dist+"_"*((i*2)+2))
        i -= 5
        dist += 5
        num += 1
        col += 5
for i in range(5):
    print(" "*78+"|     |")    

art = """
110001101111011111011111010001000001111110100010111110101111101111101100011000100011111
101010101000010001010001001010000001000000100010100010101000000010001010101001010010000
100100101111011111011111000100000001000000111110111110101111100010001001001010001011111
100000101000010100010100000100000001000000100010101000100000100010001000001011111000001
100000101111010011010011000100000001111110100010100110101111100010001000001010001011111
"""
for a in art:
    sym = grandtxt()
    if(a == "1"):
        print(sym,end="")
    elif(a == "0"):
        print(" ",end="")
    else:
        print()
print("\n"*10)
