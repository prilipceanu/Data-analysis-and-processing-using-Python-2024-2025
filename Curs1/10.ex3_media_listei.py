from functools import reduce


lista = [10, 2, 3, 50, 300, 10]
#V1
print(sum(lista)/len(lista))

#V2
print(reduce(lambda x,y : x+y , lista))