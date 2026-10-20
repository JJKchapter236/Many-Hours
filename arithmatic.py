import math
def add(a,b,counta,countb):
    #basic math first
    schoolCount=0
    frontEndCount=0
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
    compensationCount = 0
    best_adjustment = None
    place = 10
    limit = 10 ** (counta + 1)          # one place beyond a's length
    while place <= limit:
        convenient = ((a + place - 1) // place) * place
        adjustment = convenient - a
        compensationCount += 1
        if best_adjustment is None or abs(adjustment) < abs(best_adjustment):
            best_adjustment = adjustment
            compensationCount += 1
        place *= 10
    adjusted_a = a + best_adjustment
    compensationCount += 1
    total = adjusted_a + b
    compensationCount += 1
    result = total - best_adjustment
    compensationCount += 1
    
    print("Sum is", a+b, "traditional math takes",schoolCount ,"steps, compensation addition takes", compensationCount)
    return
#recursive function called when borrowing is nessacary nickyG is tempVar
def borrow(array,num):
    if array[len(array)-num-1]!=0:
        array[len(array)-num-1]-=1
        array[len(array)-num-2]+=10
    else:
        for x in range(len(array)-num-1,-1,-1):
            if array[x]!=0:
                array[x]-=1
                for y in range(x+1, len(array)-num-1):
                    array[y]=9
                break
        array[len(array)-num-1]+=10
     
def sub(a,b,counta,countb):
    schoolCount=0
    if counta>countb:
        arrayA=[0]*counta
        arrayB=[0]*counta
        schoolMethod=[0]*(counta)
    else:
        arrayA=[0]*countb
        arrayB=[0]*countb
        schoolMethod=[0]*(countb)
    for x in range(counta):
            arrayA[len(arrayA)-x-1]=(a//pow(10,x))%10
    for x in range(countb):
            arrayB[len(arrayB)-x-1]=(b//pow(10,x))%10
    ''' Count here once if A digit is smaller than B digit for carry, then also once for the actual computation and once for subtracting one from 
    the greater digit idk how to explain reducing the value of the digit to the left.
    '''
    for x in range(len(arrayA)):
        if arrayA[len(arrayA)-x-1]<arrayB[len(arrayA)-x-1]:
            schoolCount+=1
            borrow(arrayA,x)
            schoolCount+=1
            schoolMethod[len(schoolMethod)-x-1]=arrayA[len(arrayA)-x-1]-arrayB[len(arrayA)-x-1]
        else:
            schoolMethod[len(schoolMethod)-x-1]=arrayA[len(arrayA)-x-1]-arrayB[len(arrayA)-x-1]
        schoolCount+=1
    print("The difference is", a-b, "the amount of steps it takes for traditional arithmatic is", schoolCount)
    return
    

def mult(a,b,counta,countb):
    #basic math first
    schoolCount=0
    if counta>countb:
        arrayA=[0]*counta
        arrayB=[0]*counta
        schoolMethod=[0]*(counta+countb)
    else:
        arrayA=[0]*countb
        arrayB=[0]*countb
        schoolMethod=[0]*(countb+counta)
    for x in range(counta):
        arrayA[len(arrayA)-x-1]=(a//pow(10,x))%10
    for x in range(countb):
        arrayB[len(arrayB)-x-1]=(b//pow(10,x))%10
    #basic math first
    '''schoolCount for this goes up in several ways, firstly when two numbers are multiplied together in a column
    nextly it increases once when a carry is needed, finally it will go up when a carry is required to be added as well
    '''
    
    partialProducts = [[0] * (counta + countb) for x in range(countb)]
    for y in range(len(partialProducts)):
        carry=0
        for x in range(len(arrayA)):
            if carry!=0:
                schoolCount+=1
            var=arrayA[len(arrayA)-x-1]*arrayB[len(arrayB)-y-1]+carry
            carry=var//10
            if carry>=1:
                schoolCount+=1
            partialProducts[y][len(schoolMethod)-x-1-y]=var%10
            schoolCount+=1
        partialProducts[y][counta+countb-len(arrayA)-y-1] = carry
    carry2=0  
    for monkey in range (len(partialProducts[0])-1,-1,-1): 
        schoolCount+=1
        storage=carry2
        if carry2!=0:
            schoolCount+=1
        for z in range(len(partialProducts)):
            storage+=partialProducts[len(partialProducts)-1-z][monkey]
        schoolMethod[monkey]=storage%10
        carry2=storage//10
        if carry2!=0:
            schoolCount+=1
    '''Russian peasent Multiplication'''
    sum=0
    russiaCount=0
    chuda=a
    chudb=b
    while chuda>=1:
        if chuda%2==1:
            sum+=chudb
            russiaCount+=1
        chuda=chuda//2
        chudb=chudb*2
        russiaCount+=2
    print("The product is", a*b, "the number of steps using traditional arthmatic is " ,schoolCount, "the number of steps using russian peasant multiplication is " ,russiaCount)
    return
def divy(a,b,counta,countb):
    #basic math first
    schoolCount=0
    if counta>countb:
        arrayA=[0]*counta
        arrayB=[0]*countb
        schoolMethod=[0]*(counta+countb)
    else:
        arrayA=[0]*countb
        arrayB=[0]*countb
        schoolMethod=[0]*(counta+countb)
    for x in range(counta):
        arrayA[len(arrayA)-x-1]=(a//pow(10,x))%10
    for x in range(countb):
        arrayB[len(arrayB)-x-1]=(b//pow(10,x))%10
    '''count goes up for each time you check against the number,
    each time digits are subtracted and other stuff'''
    remainder=0
    quotient=[0]*counta
    for x in range(counta):
        remainder=remainder*10+arrayA[len(arrayA)-counta+x]
        schoolCount+=1
        while remainder>=b:
            remainder-=b
            quotient[x]+=1
            schoolCount+=1
        schoolMethod[len(schoolMethod)-counta+x]=quotient[x]
    print("The quotient is", a//b, "the number of steps in tradiational multiplication is", schoolCount, "if there is a remainder it is", remainder)
    return
def calculate(a, b, operation):
    counta = len(str(a)) if a else 1
    countb = len(str(b)) if b else 1
    if operation in ('+', 'add'):
        return add(a, b, counta, countb)
    elif operation in ('-', 'sub'):
        return sub(a, b, counta, countb)
    elif operation in ('*', 'mult'):
        return mult(a, b, counta, countb)
    elif operation in ('/', 'div'):
        return divy(a, b, counta, countb)
    else:
        return "Invalid operation"

