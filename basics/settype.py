s={10,20,30,'XYZ', 10,20,10}
print(s)
print(type(s))

s.update([88,99])
print(s)

#print(s*3)

s.remove (30)
print(s)
#nema duplikata, ne radi indexind, slicing, repetition ali rade update i remove1

f=frozenset(s)
f.update(20)

#frozenset ne moze update i remove, nema menjanja samo gledanje

