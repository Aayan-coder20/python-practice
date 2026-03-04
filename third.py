BasicSalary = float(input("Enter basic salary: "))
DA = 0.7 * BasicSalary
TA = 0.3 * BasicSalary
HRA = 0.1 * BasicSalary
gross_salary = BasicSalary + DA + TA + HRA
print("Salary Details: ")
print(f"Basic Salary:    {BasicSalary}")
print(f"DA (70%):        {DA}")
print(f"TA (30%):        {TA}")
print(f"HRA (10%):       {HRA}")
print(f"Gross Salary:    {gross_salary}")
