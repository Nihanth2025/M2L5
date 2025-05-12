print("Diamond triangle: ")
sz=int(input("Enter the no.of rows: "))
if sz % 2==0:
    half=int(sz/2)
else:
    half=int(sz/2)+1

sp=half-1

for i in range(1,half+1):
    for j in range(1,sp+1):
        print(end=" ")
    sp=sp-1
    num=1
    for j in range(2*i-1):
        print(end=str(num))
        num=num+1
    print()

sp=1

for i in range(1,half):
    for j in range(1,sp+1):
        print(end=" ")
    sp=sp+1
    num=1
    for j in range(1, 2*(half-i)):
        print(end=str(num))
        num=num+1
    print()
