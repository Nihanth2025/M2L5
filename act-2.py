print("Floyd's triangle: ")
m=int(input("Enter the no.of rows: "))
n=1
for i in range(1,m+1):
    for j in range(1,i+1):
        print(n ,end=" ")
        n=n+1

    print()