annual_salary=int(input("Enter the annual salary:"))
portion_saved=float(input("Enter the percent of salary that be saved:"))
cost_of_house=int(input("Enter the cost of house:"))
current_savings=0
months=0
monthly_salary=annual_salary/12
down_payment=0.25*cost_of_house
annual_return=0.04
while current_savings<down_payment:
    current_savings+=current_savings*annual_return/12
    current_savings+=monthly_salary*portion_saved
    months+=1
print(f"Number of months:{months}")