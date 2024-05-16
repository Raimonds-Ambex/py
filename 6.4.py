# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam) pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
while True:
    try:    
        n = int(input("Cik pirmskaitļus gribētos? "))
        break
    except:
        print("Ldzu ievadiet veselu skaitli")

prmsk = [2]
i = 3
# meklējam tikai nepāra skaitļos, vai skaitlis dalās ar kādu no pirmskaitļiem, kas ir masīvā 'prmsk'
while True:

    flag = 1
    for p in prmsk:
        if i % p == 0:
            flag = 0
            break
    if flag == 1:
        prmsk.append(i)
    if len(prmsk)==n:
        break
    i += 2
    
print(prmsk)