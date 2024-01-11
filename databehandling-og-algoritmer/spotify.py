land = input("Hvilket land er du fra? ")

if land.lower == "norge":
    print("$0.44 per sang")
elif land.lower == "sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")




antall_streams = int(input("Hvor mange streams har du? "))

if antall_streams > 30_000_000:
    print("Penger tjent per sang er lik 70%")
elif antall_streams > 1_400_000:
    print("Penger tjent per sang er lik 40%")
else:
    print("Penger tjent per sang er lik 0%")


