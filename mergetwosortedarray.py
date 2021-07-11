from sys import stdin

def merge(arr1, n, arr2, m) :
    i=0
    j=0
    n=len(arr1)
    m=len(arr2)
    arr=[]
    while i<n and j<m:
        if (arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i=i+1
        else:
            arr.append(arr2[j])
            j=j+1
    while(i<n):
        arr.append(arr1[i])
        i=i+1
    while(j<m):
        arr.append(arr2[j])
        j=j+1
    return arr
    


























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1, n, arr2, m)
    printList(ans, (n + m))

    t -= 1