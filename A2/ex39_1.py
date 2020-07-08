# 字典

# create a basic set of states and some cities in them
states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

# create a basic set of states and some cities in them
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

# add some more cities
cities["NY"] = "New york"
cities["OR"] = "Portland"

# print out some cities
print("-" * 10)
print("NY State has: ", cities["NY"])
print("OR State has: ", cities["OR"])

# print some states
print("-" * 10)
print("Michigan's abbreviation is: ", states["Michigan"])
print("Florida's abbreviation is: ", states["Florida"])

# do it by using the state then cities dict
print("-" * 10)
print("Michigan has: ", cities[states["Michigan"]])
print("Florida has: ", cities[states["Florida"]])

# print every state abbreviation
print("-" * 10)
# items( ):函数以列表返回可遍历的(键, 值) 元组数组
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print("-" * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has ths the city {city}")

# now do both at the same lime
print("-" * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)
# safely get a abbreviation by state that might not be there
# get( ):函数返回指定键的值，如果值不在字典中返回默认值。
state = states.get("Texas")

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
# get( ):函数返回指定键的值，如果值不在字典中返回默认值。
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
