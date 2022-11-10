# 2)Given the same list of numbers as in (1), iterate over each number and print the number and whether it is odd or even. For example:
# 21 is odd
# 52 is even
# 33 is odd
# 54 is even
# 95 is odd
# 196 is even
# 17 is odd
# 18 is even
# 29 is odd

li = [21, 52, 33, 54, 95, 196, 17, 18, 29]
for i in li:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd”)