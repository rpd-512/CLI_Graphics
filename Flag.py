from termcolor import colored
from os import system
system("clear")
greet = """
010001000100011111011111010001000011111011000010111100111110111110111110110000101111001111101100001001111011111000011110000100010001
010001001010010001010001001010000000100010100010100010100000100010100000101000101000101000001010001010000010000000010001001010001010
011111011111011111011111000100000000100010010010100010111110111110111110100100101000101111101001001010000011111000010001011111000100
010001010001010000010000000100000000100010001010100010100000100000100000100010101000101000001000101010000010000000010001010001000100
010001010001010000010000000100000011111010000110111100111110100000111110100001101111001111101000011001111011111000011110010001000100
"""
wh ="""##########################*|*###########################
########################*\*|*/*#########################
#######################****|****########################
########################*/*|*\*#########################
##########################*|*###########################"""

sym = "X"

print(5*"\n")
print (colored(34*" "+" / \\","magenta"))
print (colored(34*" "+"|   |","magenta"))
print (colored(34*" "+" \\ /","magenta"))
for i in range(5):
    print(colored(35*" "+"| |","magenta"),end = "")
    for f in range(55):
        print(colored("#","yellow"),end = "")
    print()
    

for i in wh.split("\n"):
    print(colored(35*" "+"| |",'magenta'),end = "")
    for f in i:
        if(f=="#"):
            print(colored("#","white"),end = "")
        elif(f == "\\" or f == "/"):
            print(colored(f,"cyan"),end = "")
        elif(f == "*"):
            print(colored("*","blue"),end = "")
    print()
for i in range(5):
    print(colored(35*" "+"| |","magenta"),end = "")
    for f in range(55):
        print(colored("#","green"),end = "")
    print()
    
for i in range(20):
    print(colored(35*" "+"| |","magenta"))
print(colored(17*" "+"-"*70,"magenta"),)
for i in greet:
    if(i == "0"):
        print(" ",end = "")
    elif(i == "1"):
        print(sym,end = "")
    else:
        print()
print(5*"\n")

