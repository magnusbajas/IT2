land_info = [
    {"land": "Kina", "hovedstad": "Beijing", "befolkning": 1410000000, "språk": ["Mandarin"]},
    {"land": "India", "hovedstad": "New Delhi", "befolkning": 1390000000, "språk": ["Hindi", "Engelsk"]},
    {"land": "USA", "hovedstad": "Washington, D.C.", "befolkning": 331000000, "språk": ["Engelsk"]},
    {"land": "Indonesia", "hovedstad": "Jakarta", "befolkning": 273000000, "språk": ["Indonesisk"]},
    {"land": "Pakistan", "hovedstad": "Islamabad", "befolkning": 225000000, "språk": ["Urdu", "Engelsk"]},
    {"land": "Brasil", "hovedstad": "Brasília", "befolkning": 213000000, "språk": ["Portugisisk"]},
    {"land": "Nigeria", "hovedstad": "Abuja", "befolkning": 211000000, "språk": ["Engelsk"]},
    {"land": "Bangladesh", "hovedstad": "Dhaka", "befolkning": 166000000, "språk": ["Bengali"]},
    {"land": "Russland", "hovedstad": "Moskva", "befolkning": 146000000, "språk": ["Russisk"]},
    {"land": "Mexico", "hovedstad": "Mexico City", "befolkning": 128000000, "språk": ["Spansk"]},
    {"land": "Japan", "hovedstad": "Tokyo", "befolkning": 125000000, "språk": ["Japansk"]},
    {"land": "Etiopia", "hovedstad": "Addis Ababa", "befolkning": 118000000, "språk": ["Amharisk"]},
    {"land": "Filippinene", "hovedstad": "Manila", "befolkning": 113000000, "språk": ["Filippinsk"]},
    {"land": "Egypt", "hovedstad": "Kairo", "befolkning": 104000000, "språk": ["Arabisk"]},
    {"land": "Vietnam", "hovedstad": "Hanoi", "befolkning": 97400000, "språk": ["Vietnamesisk"]},
    {"land": "DR Kongo", "hovedstad": "Kinshasa", "befolkning": 90000000, "språk": ["Fransk"]},
    {"land": "Turkey", "hovedstad": "Ankara", "befolkning": 83700000, "språk": ["Tyrkisk"]},
    {"land": "Iran", "hovedstad": "Teheran", "befolkning": 83700000, "språk": ["Persisk"]},
    {"land": "Tyskland", "hovedstad": "Berlin", "befolkning": 83000000, "språk": ["Tysk"]},
    {"land": "Thailand", "hovedstad": "Bangkok", "befolkning": 70000000, "språk": ["Thai"]},
    {"land": "Frankrike", "hovedstad": "Paris", "befolkning": 67000000, "språk": ["Fransk"]},
    {"land": "Storbritannia", "hovedstad": "London", "befolkning": 67000000, "språk": ["Engelsk"]},
    {"land": "Italia", "hovedstad": "Roma", "befolkning": 60300000, "språk": ["Italiensk"]},
    {"land": "Sør-Afrika", "hovedstad": "Pretoria, Cape Town, Bloemfontein", "befolkning": 60000000,
     "språk": ["Afrikaans", "Engelsk", "isiNdebele", "isiXhosa", "isiZulu", "sesotho", "Setswana", "siSwati", "Tshivenda", "Xitsonga"]},
    {"land": "Myanmar", "hovedstad": "Naypyidaw", "befolkning": 54400000, "språk": ["Burmese"]},
    {"land": "Sør-Korea", "hovedstad": "Seoul", "befolkning": 51700000, "språk": ["Koreansk"]},
    {"land": "Colombia", "hovedstad": "Bogotá", "befolkning": 50300000, "språk": ["Spansk"]},
    {"land": "Kenya", "hovedstad": "Nairobi", "befolkning": 49000000, "språk": ["Swahili", "Engelsk"]},
    {"land": "Spania", "hovedstad": "Madrid", "befolkning": 47000000, "språk": ["Spansk"]},
    {"land": "Argentina", "hovedstad": "Buenos Aires", "befolkning": 45000000, "språk": ["Spansk"]},
]

print(land_info[-1]) 

for land in land_info:
    print(f"land: {land['land']}, hovedstad: {land['hovedstad']}, antall språk: {len(land['språk'])}")

flest_språk = land_info[0]
for land in land_info:
    if len(land['språk']) > len(flest_språk['språk']):
        flest_språk = land
print(f"Landet med flest språk er {flest_språk['land']} som har {len(flest_språk['språk'])} språk")

språk_antall_land = {} 
 
for land in land_info:
    for språk in land['språk']:
        if språk in språk_antall_land:
            språk_antall_land[språk] += 1
        else:
            språk_antall_land[språk] = 1
 
print(språk_antall_land)

språk_sortert = sorted(språk_antall_land.items(), key=lambda språk:språk[1]) 
print(språk_sortert[-1][0], språk_sortert[-1][1])