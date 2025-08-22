InsuranceName = input("Enter the name of insurance company.")
NumEmployees = input("How many employees work at this company?")
Location = input("Where is this company located? 'City, OR Country, OR State'")
LowPrice = input("Enter the lowest price of the policy.")
HiPrice = input("Enter the highest price of the policy.")

print(f'We are {InsuranceName} located in {Location}. Our {NumEmployees} employees can help you find the policy that is right for you with policies ranging from ${LowPrice} to ${HiPrice} per month!')