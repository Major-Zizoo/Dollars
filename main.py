dollar = int(input("Enter amount:"))

dollar100 = dollar // 100
dollar50 = (dollar%100) // 50
dollar10 = ((dollar%100))%50 //10

print("100$ needed is:",dollar100)
print("50$ needed is:",dollar50 )
print("10$ needed is:",dollar10 )