dict1={1:"John", 2: "Bob", 4: "Bill"} 
'''Prvo je KEY, drugo je VALUE'''
print(dict1)

'''izlistava kijeve samo'''
k=dict1.keys()
for i in k:
    print(i)
    
'''izlistava value samo'''
v=dict1.values()
for i in v:
    print(i)
    
'''da izlista onaj VALUE gde je KEY 4'''
print(dict1[4])

'''DELETE, da obrise onaj rekord gde je KEY 2'''
del dict1[2]
print(dict1)

