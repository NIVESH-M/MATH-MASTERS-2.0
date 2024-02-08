import random as rd
import tkinter as tk
print("STORY BEGINS!!\n\n\n")
print("You are a Police who is in search of a mathematician who is using math to do crime.\n")
print("His friends are coming to see him and he will escape tonight through ship with his friends\n")
print("For his friends, he left some clues in his house about his secret place inside the house\n")
print("CRACK the clues to find the criminal.\nUse your math skills to beat him and save maths from these cruel people's hand")

#globache conjecture
def prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1

def p(l):
    g=int(input("Number 1:"))
    h=int(input("Number 2:"))
    if list([g,h]) in l or list([h,g]) in l:
        print("DOOR OPENS!!!")
        print("Take a note of it and Take the note in front of you\n")
        return 0,[g,h]
    else:
        print("Wrong")
        p(l)

def chin(b1,c1,b2,c2):
    inp1=int(input("ENTER YOUR ANSWER:"))
    if inp1%b1==c1 and inp1%b2==c2:
        print("Lets MOVE!!\nTake a parabolic path and find a paper on a table with paper weight on it\n")
        return 0
    else:
        print("Wrong")
        chin(b1,c1,b2,c2)

print("\nAT DOOR: SOLVE AND GET THE CLUE\n")   
a=rd.randrange(100,1000,2)
print("USE GOLDBACH CONJECTURE:",a)
l=[]
for i in range(3,int(a/2)+1):
    if prime(i)==1 and prime(a-i)==1:
        l.append([i,a-i])
print(l)
d2=p(l)

#chinese remainder
if d2[0]==0:
    print("\n\n")
    b1=rd.randrange(1,10)
    c1=rd.randrange(0,b1)
    d1=rd.randrange(1,10)
    e1=b1*d1+c1
    print(b1,"Rem:",c1)
    b2=rd.randrange(1,10)
    c2=e1%b2
    print(b2,"Rem:",c2)
    m=chin(b1,c1,b2,c2)
    if m==0:
        print("Find the area of the house using 2 prime numbers you came across\n")
        while True:
            ar=int(input())
            if ar==d2[1][0]*d2[1][1]:
                print("CRIMINAL: HELLO FRIEND!!OMG, ITS YOu....I AM CAUGHT :( \n")
                print("YOU WON!!!")
                break
            else:
                print("Wrong")
                continue

    '''
    SOLUTION CODE:

    while True:
        if m%b1==c1 and m%b2==c2:
            print("Wrong, correct answer:",m)
            break
        else:
            m+=1'''
