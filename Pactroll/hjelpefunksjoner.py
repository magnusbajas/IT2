import random 

def finn_unik_pos(bredde, hoyde, matbiter, hindere, troll):
    # en funksjon som returnerer en posisjon som ikke allerede er tatt
    unik = False # sikrer første kjøring av while-løkken
    while not unik: # "while not False"
        unik = True
        x = random.randint(0, bredde)
        y = random.randint(0, hoyde)
        for matbit in matbiter: # sjekker om det allerede finnes noen matbiter i de nye random x og y posisjonene
            if matbit.rect.collidepoint(x, y):
                unik = False
        for hinder in hindere:
            if hinder.rect.collidepoint(x, y):
                unik = False
        if troll.rect.collidepoint(x, y): 
            unik = False
    return x, y # returnerer en unik posisjon som ikke er der det allerede er matbit, hinder eller troll