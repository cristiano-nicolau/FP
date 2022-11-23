# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)
    print("Can you guess my secret?")
    x=0
    y=0
    n= int(input('Escolhe um número de 1 a 100! '))
    while n !=secret:
        if y==0:
            if n> secret:
                print('High')
                x+=1
            elif n<secret:
                print('Low')
                x+=1
            else:
                print('Right number')
                x+=1
            y+=1
        else:
            n= int(input('Escolhe um número de 1 a 100! '))
            if n> secret:
                print('High')
                x+=1
            elif n<secret:
                print('Low')
                x+=1
            else:
                print('Right number')
                x+=1
        
    print('Efetuou',x,'tentativas')

main()
