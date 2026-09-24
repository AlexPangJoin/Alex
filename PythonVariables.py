# # 2.1.1 Part 1
school_name  = "UWC"

def show_user_info():
    user_name = str("Alex")
    print(user_name)
    user_age = int(16)
    print(user_age)
    is_student = True
    print(is_student)

show_user_info()
print (school_name)

# Part 2
tax_rate = 0.20
def calculate_tax(price):
    global tax_rate
    tax_amount = price * tax_rate
    print(tax_amount)
    tax_rate = 0.25
calculate_tax(100)
calculate_tax(200)
