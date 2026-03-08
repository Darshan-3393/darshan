num=int(input("Enter number: "))
temp=num
sum=0
while num>0:
    digit=num%10
    sum=sum+digit**3
    num=num//10
if sum==temp:
    print(temp,"is an Armstrong Number")
else:
    print(temp,"is not an Armstrong Number")