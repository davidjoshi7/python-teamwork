# def sum_by_ten(a):
#     return a+10


# s=lambda a:a+10

# print(s(10))
# print(sum_by_ten(2))


def myfuc(n):
    return lambda x:x*n

#lambda x:x*2
doubler=myfuc(2)
#lamda x:x*3
tripler=myfuc(3)

print(doubler(10))
print(tripler(30))
