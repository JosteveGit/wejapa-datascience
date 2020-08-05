# Use this playground to experiment with list methods, using Test Run

a = ['a', 'b', 'c', 'k', 'e', 'f', 'g', "z"]
print(a)

b = a.copy()
print(b)

print(a.count("a"))

a.extend([1, 2, 3])
print(a)

print(a.index("a"))

a.pop(2)
print(a)

a.remove('a')
print(a)

a.reverse()
print(a)

b.sort()
print(b)

a.clear()
print(a)
