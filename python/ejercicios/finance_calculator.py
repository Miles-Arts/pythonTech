# print("Welcome!")

# name: str= "Bob"
# print(name)

def calculate_finances(monthly_income: float, taxt_rate: float, currency: str) -> None:
    monthly_tax: float = monthly_income * (taxt_rate / 100)
    monthly_net_income: float = monthly_income - monthly_tax
    yearly_salary: float = monthly_income * 12
    yearly_tax: float = monthly_tax  * 12
    yearly_net_income: float = yearly_salary - yearly_tax




















