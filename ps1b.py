annual_salary=int(input("Enter the annual salary: "))
portion_saved=float(input("Enter the percent of salary to be saved: "))
cost_of_house=int(input("Enter the cost of house: "))
semi_annual_rise=float(input("Enter the semi annual rise: "))
current_savings=0
months=0
down_payment=0.25*cost_of_house
annual_return=0.04
monthly_return=annual_return/12
while current_savings < down_payment:
    monthly_salary=annual_salary/12
    current_savings+=current_savings*monthly_return
    current_savings+= monthly_salary*portion_saved
    months+= 1
    if months % 6 == 0:
        annual_salary+=annual_salary*semi_annual_rise

print(f"Number of months: {months}")