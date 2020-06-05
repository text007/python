# 变量和名字

# 给变量 cars 赋值
cars = 100

# 给变量 space_in_a_car 赋值
space_in_a_car = 4.0

# 给变量 drivers 赋值
drivers = 30

# 给变量 passengers 赋值
passengers = 90

# 计算 cars - drivers 的值
cars_not_driven = cars - drivers

# 给变量 cars_driven 赋 drivers 的值
cars_driven = drivers

# 计算 cars_driven * space_in_a_car 的值
carpool_capacity = cars_driven * space_in_a_car

# 计算 passengers / cars_driven 的值
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("we can transport", carpool_capacity, "people today.")
print("we have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car, "in each car.")
