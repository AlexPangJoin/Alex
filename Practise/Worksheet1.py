# 2.1.1 Task 1
age = 17
name = "Alex"
print(age)
print(name)

# Task 2
price = 18.15
integer_price = int(price)
print(price)
print(integer_price)

# Task 3
global_count = 0
def increment_count():
    global global_count
    global_count += 1
    print(global_count)

increment_count()
increment_count()
