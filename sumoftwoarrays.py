from sys import stdin

def sumOfTwoArrays(arr1, n, arr2, m, output) :
    li_1=arr1
    li_2=arr2
    i=len(li_1)-1
    j=len(li_2)-1
    li_ans=[]
    carry=0
    while(1):
        if(i >= 0 and j >= 0):
            temp=li_1[i]+li_2[j]+carry
            carry=temp//10
            temp=temp%10
            li_ans.insert(0,temp)
            i=i-1
            j=j-1
        else:
            if(i==j):
                li_ans.insert(0,carry)
            while(i>=0):
                temp=li_1[i]+carry
                carry=temp//10
                temp=temp%10
                li_ans.insert(0,temp)
                i=i-1
            while(j>=0):
                temp=li_2[j]+carry
                carry=temp//10
                temp=temp%10
                li_ans.insert(0,temp)
                j=j-1
            break
    while(len(li_ans)<=len(li_1) or len(li_ans)<=len(li_2)):
        temp=0
        li_ans.insert(0,temp)
    for e in li_ans:
        print(e,end=" ")
        


























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
        return list(), 0
    
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


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
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    #printList(output, outputSize)
    
    t -= 1