

culori = ["alb" , "rosu", "negru", "verde"]
## rezutat = []

def lungimea_5(cuvant):
    return len(cuvant) == 5

print(list(filter(lungimea_5, culori))) 


print(list(filter(lambda cuvant: len(cuvant) == 4 , culori)))

