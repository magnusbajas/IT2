# Oppgaver - Algoritmer, pseudokode og flytdiagram

## Oppgave 1 

En while-løkke i programmering er en løkke som kjører så lenge en besemt betingelse er sann


## Oppgave 2

En for-løkke er best egnet når du vet hvor mange ganger du vil at løkken skal kjøre


## Oppgave 3

Hovedprinsippet bak objektorientert programmering er å representere data og funksjoner som objekter


## Oppgave 4

Et typisk kjennetegn på pseudokode er at den kan kjøres direkte på en datamaskin.


## Oppgave 5

ingen ganger


## Oppgave 6

SET i TO 0
FOR hver i LESSER OR EQUAL 4
  PRINT i+1
ENDFOR


## Oppgave 9

SET n TO 1
WHILE n LESSER THAN 10
  DISPLAY n
  INCREMENT n
ENDWHILE


## Oppgave 10

F - 1
H - 2 
A - 3
B - 4
C - 5
G - 6
E - 7
D - 8


## Oppgaven 11

```python
listen = [32, 10, -5, 99, 1]
# 1. (Riktig)
størst = float("-inf")
for tall in listen:
  if tall > størst:
    størst = tall
listen.remove(størst)
nestStørst = float("-inf")
for tall in listen:
  if tall > nestStørst:
    nestStørst = tall
print(nestStørst)
 
# 2.
størst = listen[0]
nestStørst = listen[1]
 
if nestStørst > størst:
  størst, nestStørst = nestStørst, størst # bytter verdier på variablene
for tall in listen[2:]:
  if tall > størst:
    nestStørst = størst
    størst = tall
  elif tall > nestStørst and tall != størst:
    nestStørst = tall
 


# Svar: 1 

listen = [99, 32, 10, 1, -5]
størst =  float("-inf")
nestStørst = float("-inf")

for tall in listen:
  if tall > størst:
    nestStørst = størst
    størst = tall
  elif tall > nestStørst:
    nestStørst = tall
  print(nestStørst)




for tall in listen:
  if tall != listen[:1]:
    print()




```


