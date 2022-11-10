# 1) Given the list of numbers: [21,52,33,54,95,196,17,18,29] print the sum of the numbers and their product

p = 1
li = [21, 52, 33, 54, 95, 196, 17, 18, 29]
print("The sum of the list is:", sum(li))
for i in li:
    p = p * i
print("The product of the list is:", p)
