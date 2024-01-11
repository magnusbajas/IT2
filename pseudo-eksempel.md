### Penger tjent per sang

Hent inn land fra bruker (input)
Hvis land er lik Norge:
    Print $0.44
Ellers hvis er lik Sverige:
    Print $0.34
Ellers
    Print $0.22 per sang


### Python-kode

```python
land = input("Hvilket land er du fra? ")

if land.lower == "norge":
    print("$0.44 per sang")
elif land.lower == "sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")
```


### Pseudokode som følger UDIRs standard 

```pseudo
SET land TO READ "Hvilket land er du fra?"
IF land EQUAL TO Norge
    THEN DISPLAY "$0.44 per sang"
ELSE IF land EQUAL TO Sverige
    THEN DISPLAY "$0.44 per sang"
ELSE DISPLAY "$0.22 per sang"
```
### Andel penger tjent per sang

Hent inn antall streams fra bruker
Hvis antall streams er større en 30 000 000
    Print "Penger tjent per sang lik 70%"
Eller hvis antall streams er større en 1 400 000
    Print "Penger tjent per sang lik 40%"
Ellers
    Print "Penger tjent per sang lik 0%"