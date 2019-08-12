lst=[20,30,40,234]
print(type(lst))
b=bytes(lst)
print(type(b))

lst[3]=22 #ovo za byte ne radi --- b[3]=22 --- nema modifikovanja bytea
print(lst)

b1=bytearray(lst)
print(type(b1))
b1[2]=33 #u bytearray moze da se modifikuje

#indexing radi samoza bytearray
'''slicing i repetition ne radi ni na jednom'''
