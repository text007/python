# 字典

stuff = {"name": "zed", "age": 39, "height": 6 * 12 + 2}
print(stuff["name"])
print(stuff["age"])
print(stuff["height"])
print("----------")

stuff["city"] = "sf"
print(stuff)
print(stuff["city"])
print("----------")

stuff[1] = "wow"
stuff[2] = "Neato"
print(stuff)
print(stuff[1])
print(stuff[2])
print("----------")

del stuff["city"]
del stuff[1]
del stuff[2]
print(stuff)