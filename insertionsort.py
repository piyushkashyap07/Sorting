from sys import stdin

def insertionSort(arr, n) :
    for i in range(len(arr)):
        for j in range( 0 , len(arr) - i - 1 ):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j + 1 ]) = (arr[j + 1 ], arr[j])


























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
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
    insertionSort(arr, n)
    printList(arr, n)

    t-= 1