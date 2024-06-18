

# If an integer number is preceded by an 0O or 0o prefix (zero-o),
# it will be treated as an octal value.
# This means that the number must contain digits taken from the [0..7] range only.
print(0o123) # 0o123 is an octal number with a (decimal) value equal to 83.

#The second convention allows us to use hexadecimal numbers.
# Such numbers should be preceded by the prefix 0x or 0X (zero-x).
print(0x123) # 0x123 is a hexadecimal number with a (decimal) value equal to 291.

#To avoid writing out so many zeros, physics textbooks use an abbreviated form, which you have probably already seen: 3 x 108.
# It reads: three times ten to the power of eight.
# In Python, the same effect is achieved in a slightly different way ‒ take a look: 3E8
print(3E8)
