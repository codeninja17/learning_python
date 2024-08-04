
a = 1
print(type(a))

a = 6.2
print(type(a))

c = True
print(type(c))

d = True+True
print(d)

complex_n = 3 + 8j
print(type(complex_n))

print(complex_n.conjugate())

str = "Ankit Kumar"
print(len(str)) # 11 length

print(str[0]) # A
print(str[-1]) # r
print(str[0:5]) # Ankit
print(str[0:5:2]) #Akt , forward jump of 2
print(str[10:5:-2]) #rmK , backward jump of 2
print(str[14:5:2]) # Empty String as going backward with a forward jump
print(str[::-1]) # reverse
print(str[-1:-6:-1]) # ramuK
print(str[::1]) # prints full string
# str[0] = 'B' String is immutable , hence index based operations are not supported

for i in str:
    print(i, end="")
print()

for i in range(len(str)):
    print(str[i], end="")
print()

for i in range(0, len(str), 2):
    print(str[i], end="")
print()

# i = int(input())
# print(i)

print(str.isalnum())

str2= "123ABC"
print(str2.isalnum())
print(str2.expandtabs())
print(str2.center(30, 'S'))