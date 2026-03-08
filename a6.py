num=int(input("Enter number: "))
temp=num
sum=0
while num>0:
    digit=num%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i
    sum=sum+fact
    num=num//10
if sum==temp:
    print(temp,"is a Strong Number")
else:
    print(temp,"is not a Strong Number")