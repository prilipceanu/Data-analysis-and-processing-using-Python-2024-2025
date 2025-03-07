
vocale = "aeiouAEIOU"
input_string = "Salutare, ce mai faci?"


#V1
def elimina_vocalele(ch):
    return ch not in vocale


print("".join(filter(elimina_vocalele, input_string)))

#V2
print("".join(filter(lambda x: x not in vocale, input_string)))

#V3

print("".join([ch for ch in input_string if ch not in vocale]))