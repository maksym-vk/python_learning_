

# Some operators act before others - the hierarchy of priorities:
#   -  the ** operator (exponentiation) has the highest priority;
#   -  then the unary + and - (note: a unary operator to the right of the exponentiation operator
#      binds more strongly, for example 4 ** -1 equals 0.25)
#   -  then: *, /, and %,
#   -  and finally, the lowest priority: binary + and -.


print((5 * ((25 % 13) + 100) / (2 * 13)) // 2) # (5 * ((12 + 100) / 26)) // 2 = 5 * (112/26) // 2 =
                                               # = 5 * 4.3076923 // 2 = 21.5384615 // 2 = 10.0


print((2 ** 3 ** 2))
print(2 % 4) # 2 - (4 * 0)= 2
# clarification:
# 2 // 4 = 0
# 0 * 4 =  0
# 2 - 0 =  2


print(2 % -4) # 2 - (-4 * -1) = -2
# clarification:
# 2 // -4 = -1
# -1 * -4 =  4
# 2 - 4 = -2

print(5 % 2)

print(2//-4)

print (int(1.99))

print(-1/5)
print(-1//5)
# "//" operator is like if a / b = c, then a // b = floor(c), where floor like
# int,
# float etc.