# Åpne og lese fil i Python
fil = open("tullefil.txt", encoding="utf8") # åpner fila tullefil.txt med utf8-enkoding (lar oss bruke æøå)
data = fil.read() # leser innholdet i fila 
fil.close() # lukker fila -> frigjør minne

# Alternativt
with open("tullefil.txt", encoding="utf8") as fil:
    data = fil.read()

linjer = data.split("\n") # splitter på newline (\n), linjer er nå en liste der hver linje er et 
print(linjer)



# Lese json-filer
import json # importerer json-biblioteket

fil = open("sanger.json", encoding="utf8") # åpner fila sanger.json
sanger = json.load(fil) # leser innholdet og tolker det i json-format (sanger er her en liste med ordbøker)
fil.close()

print(sanger[0])

# Alternativt:
with open("sanger.json", encoding="utf8") as fil:
    sanger = json.load(fil)

# Eksempeloppgave
# Hvor mange sanger av artisten Taylor Swift er det på topplista?

antall = 0

for sang in sanger:
    if sang["artist"] == "Taylor Swift":
        antall += 1

print(antall)

antalll = 0

for sang in sanger:
    if sang["artist"] == "The Weeknd":
        antalll += 1

print(antalll)

# Hvilken artist har flest sanger på topplista

print(len(sanger))

## Tankegang: 
# Lag en tom ordbok
artister = {}
for sang in sanger:
    if sang["artist"] in artister:
        artister[sang["artist"]] += 1
    else: 
        artister[sang["artist"]] = 1


# Sorter osv.. 
høyeste_artist = ""
høyeste_antall = -1

for artist in artister:
    antall_sanger = artister[artist]
    if antall_sanger > høyeste_antall:
        høyeste_artist = artist
        høyeste_antall = antall_sanger

    
print(høyeste_artist, høyeste_antall)
    
