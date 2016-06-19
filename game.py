from random import randint
secret=randint(1,10)
print("welcome")
guess=0
while guess!=secret:
    g=input("guess the no")
    guess=int(g)
    if guess==secret:
        print("yo win")
    else:
        if guess>secret:
            print("too high")
        else:
            print("too low")
print("game over")
    
