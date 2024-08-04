a = [1,2,3,4]
print(a)

b = [12,345,455]
x = a + b
print(x)

b.extend(a)
print(b)

b.append(a)
print(b)

l = ['sweta', 'anshu']
l1 = ['ankit', 'kittu']

#inserts at index 1 using a zero length slice
l[1:1] = l1
print(l)

# replaces slice of length 1 (1:2) in the list
l1[1:2] = ['patna', 'bihar']
print(l1)

# l2 = l + 3 not allowed

l2 = l + [3]
print(l2)

l3 = l + l1
print(l3)

l3.remove('ankit') #removes first occurrence
print(l3)

# Tuples

t = (1,3,4)

print(t)
print(t[0])
#t[0] = 123 not allowed

t = t[::-1]

print(t)

i1, i2, i3 = t

print(i1)

#can be used without ()

t2 = 1,3,6
j1, j2, j3 = t2
print(j2)

x1, x2 = 100, 102
print(x2)

x1, x2 = x2, x1 #swap
print(x2)

# List Comprehension

squares = [num * num for num in range(10)]
print(squares) 

str = "The quick brown fox"
v = [char for char in str if char in "aeiou"]
print(v)

#set comprehension

v_set = {char for char in str if char in "aeiou"}
print(v_set)


v_map = {number: number**(1/2) for number in range(12)}
print(v_map)


def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)

def infinite_sequence():
    num = 0
    while True:
        yield num
        print("here")
        num += 19

gen = infinite_sequence()

print(next(gen))
print(next(gen))