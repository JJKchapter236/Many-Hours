import math
def add(a,b,counta,countb):
    #basic math first
    schoolCount=0
    if counta>countb:
        arrayA=[0]*counta
        arrayB=[0]*counta
        schoolMethod=[0]*(counta+1)
    else:
        arrayA=[0]*countb
        arrayB=[0]*countb
        schoolMethod=[0]*(countb+1)
    for x in range(counta):
        arrayA[len(arrayA)-x-1]=(a//pow(10,x))%10
    for x in range(countb):
        arrayB[len(arrayB)-x-1]=(b//pow(10,x))%10
    print (a, b, counta, countb, arrayA, arrayB)
    #basic math first
    '''schoolCount for this goes up in several ways, firstly when two numbers are added together in a column
    nextly it increases once when a carry is needed, finally it will go up when a carry is required to be added as well
    '''
    carry=0
    for x in range(len(arrayA)):
        if carry!=0:
            schoolCount+=1
        var=arrayA[len(arrayA)-x-1]+arrayB[len(arrayA)-x-1]+carry
        carry=var//10
        if carry>=1:
            schoolCount+=1
        schoolMethod[len(schoolMethod)-x-1]=var%10
        schoolCount+=1
    schoolMethod[0]=carry
    for x in range(len(schoolMethod)):
        if x==0: 
            if schoolMethod[x]!=0:
                print(schoolMethod[x], end="")
        else:
            print(schoolMethod[x], end="")
    print(" ", a+b, schoolCount)
    return
    
def sub(a,b,counta,countb):
    if counta>countb:
        arrayA=[0]*counta
        arrayB=[0]*counta
        schoolMethod=[0]*(counta)
    else:
        arrayA=[0]*countb
        arrayB=[0]*countb
        schoolMethod=[0]*(countb)
    for x in range(counta):
        arrayA[counta-x-1]=(a//pow(10,x))%10
    for x in range(countb):
        arrayB[countb-x-1]=(b//pow(10,x))%10
    print (a, b, counta, countb, arrayA, arrayB)
    carry=0
    for x in range(len(arrayA)):
        arrayA[len(arrayA)-x-1]+arrayB[len(arrayA)-x-1]
#def mult(a,b,counta,countb):
#def divy(a,b,counta,countb):
def calculate(a,b):
    counta=0
    countb=0
    ballsa=a
    ballsb=b
    while ballsa>0:
        ballsa//= 10
        counta+=1
    while ballsb>0:
        ballsb//= 10
        countb+=1
    add(a,b,counta,countb)
    return 
def main():
    calculate(199,1)
main()