# create a hash table
items1 = dict({"key1" : 1, "key2" : 2, "key3" : "three"})
print(items1)


# create a hashtable progressively
items2 = {}
items2["key1"] = 1
items2["key2"] = 2
items2["key3"] = 3
print(items2)

# create a nonexistent key
# print(items1["key6"])

# replace an item
items2["key2"] = "two"
print(items2)

# iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key:", key, " value:", value)
    