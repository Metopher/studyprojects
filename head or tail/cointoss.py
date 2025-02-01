import random
choice=input("enter your choice as either h(head) or t(tail):")
choic=choice.lower()
l=["h","t"]
toss=random.choice(l)
print(" the coic fell on ",toss)
if choice==toss:
    print("you win")
else: 
    print("better luck next time")