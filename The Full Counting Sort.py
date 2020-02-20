#Hari Bol
#Hari Bol
#Hari Bol
n=int(input())
echo=[]
for i in range(n):
    km=[]                                   #creating empty 2d array/list
    echo.append(km)
for i in range(0,n):
    if i<n//2:
        x=input().split()
        echo[int(x[0])].append("-")         #adding elements in 2d array according to there index
    else:
        x=input().split()
        echo[int(x[0])].append(x[1])
for i in echo :
    if len(i)>0:
        print(' '.join(i),end=" ")          #joining and printing the string
