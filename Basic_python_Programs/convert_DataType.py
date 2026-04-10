a = 34
b = 45.5
c = "Hello"
d = True

# Integer conversion
print(int(b))     
# print(int(c))   # error (non-numeric string)
print(int(d))     # True → 1

# Float conversion
print(float(a))   
# print(float(c)) # error (non-numeric string)
print(float(d))   # True → 1.0

# String conversion
print(str(a))     
print(str(b))
print(str(d))

# Boolean conversion
print(bool(a))    
print(bool(0))    
print(bool(""))   
print(bool(c))    