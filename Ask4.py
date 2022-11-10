# 4)Given the list in (1), create two sublists, one containing all odd numbers and another containing all even numbers. Calculate the sum and product of each number in the two lists (per list) and print them out. For example:
#     The odd numbers are: [21, 33, 95, 17, 29]
#     The even numbers are: [52, 54, 196, 18]
#     The sum of the odd numbers is 195 and their product is 32456655
#     The sum of the even numbers is 320 and their product is 9906624

li = [21, 52, 33, 54, 95, 196, 17, 18, 29]
op = 1
ep = 1
o = []
e = []
for i in li:
    if i % 2 == 0:
        e.append(i)
        ep = ep * i
    else:
        o.append(i)
        op = op * i
print("The odd numbers are:", o)
print("The even  numbers are:", e)
print("The sum of the odd number is", sum(o), "and their product is ", op)
print("The sum of the even number is", sum(e), "and their product is ", ep)

# list comprehension
# map
# for i in o:
# p = p * i
# p(e))
# separate comments
# reverse op and ep
# print ("and their product is ",op)
# print ("and their product is ",ep)