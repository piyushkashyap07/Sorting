from sys import stdin

def pushZerosAtEnd(arr, n) :
    nonzero =0
    for i in  range(n):
        if arr[i] !=0:
            temp =arr[i]
            arr[i]=arr[nonzero]
            arr[nonzero]=temp
            nonzero +=1
    
    #Your code goes here

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0:
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split()))
    return arr, n
  

#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")

    print()


#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()

    pushZerosAtEnd(arr, n)
    printList(arr, n)

    t -= 1
























