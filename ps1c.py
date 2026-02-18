annual_salary=float(input("Enter the annual salary:"))
house_cost=1000000
down_payment=0.25*house_cost
annual_return=0.04
semi_annual_return=0.07
months=36
current_savings=0
salary=annual_salary
for m in range(1,months+1):
    monthly_salary=salary/12
    current_savings+=current_savings*(annual_return/12)
    current_savings+=monthly_salary
    if m%6==0:
        salary+=salary*semi_annual_return
if current_savings<down_payment:
    print("it is not possible to pay the down payment in three years")
else:
    low=0
    high=1
    steps=0
    best_rate=0
    while True:
        steps+=1
        rate=(low+high)/2
        current_savings=0
        salary=annual_salary
        for m in range(1,months+1):
            monthly_salary=salary/12
            current_savings+=current_savings*(annual_return/12)
            current_savings+=monthly_salary*rate
            if m%6==0:
                salary+=salary*semi_annual_return
        if abs(current_savings-down_payment)<=100:
            best_rate=rate
            break
        elif current_savings<down_payment:
            low=rate
        else:
            high=rate
print(f"Savings rate={round(best_rate,4)}")
print(f"steps in bisection search={steps}")