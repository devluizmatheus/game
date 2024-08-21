import random 

def rolagem_dados(dado_rolado):

    if dado_rolado == 'd20':
        d20 = random.randrange(0, 20)
        return d20
    
    if dado_rolado == 'd6':
        d6 = random.randrange(0, 6)
        return d6
    
    if dado_rolado == 'd100':
        d100 = random.randrange(0, 100)
        return d100

