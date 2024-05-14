# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
arr = []
while True:
    x = input("Lūdzu ievadiet skaitli vai iziet ar q: ")
    if x == 'q':
        break;
    else:
        arr.append(float(x))
        print(f'Vidējā vērtība {sum(arr)/len(arr)}')
# ---------------------------------------------------------
# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli. Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads 
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
x = round(float(input('Lūdzu ievadiet sākuma skaitli: ')))
y = round(float(input('Lūdzu ievadiet beigu skaitli: ')))

visi_kubi = []
while x <= y:
    print(f'{x}  kubā: {x**3}')
    visi_kubi.append(x**3)
    x += 1
print(f'Visi kubi: {visi_kubi}')