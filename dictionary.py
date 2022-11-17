dict1={'fruit':'apple','climate':'cold','price(kg)':120,'quantity':5}
print(dict1)
print(dict1['fruit'])
dict1.pop("fruit")
print(dict1)
dict1.update({"vegetable":"tomato"})
print(dict1)
dict1.update({"climate":"hot"})
print(dict1)

x=dict1.copy()
y=dict1.keys()
z=dict1.values()
print(x)
print(y)
print(z)



