# Uzrakstiet funkciju get_min_avg_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, 
# aritmētisko vidējo un lielāko vērtību no virknes.
# get_min_avg_max([0,10,1,9]) -> (0,5,10)
# ienākošā sequence var būt tuple vai list ar skaitliskām vērtībām. 
def get_min_avg_max(sequence):
    sequence = list(sequence)
    sequence.sort()
    avg = round(sum(sequence)/len(sequence))
    return (sequence[0], avg, sequence[-1])

res = get_min_avg_max([0,10,1,9])
print(res)
# -------------------------------
# Uzrakstiet funkciju get_min_med_max(sequence), kas atgriež tuple ar trīs vērtībām attiecīgi mazāko, medianu un lielāko vērtību no virknes.
# Median vērtība ir vērtiba, kas sakartotā virknē ir paša vidū. Ja virknes skaits ir pāra tad vidū ir divas vērtības.
# No vidus vērtībām tad ņem vidējo.
# get_min_med_max([1,5,8,4,3]) -> (1,4,8)
# get_min_med_max([2,2,9,9,4,3]) -> (2,3.5,9)
# get_min_med_max("baaac") -> ('a','a','c')
#  # ar string var būt interesanti rezultāti pie pāra skaita ņemot vidējo, tāpēc labak dot abus vidējos
# get_min_med_max("faaacb") -> ('a', 'ab', 'f') 
# ienākošā sequence var būt tuple vai list ar vienāda tipa vērtībām, vai pat string.
def get_min_med_max(sequence):
    sequence = list(sequence)
    sequence.sort()
    l = len(sequence)
    if(l%2 == 0):
        try:
            med = (sequence[ round(l/2) -1 ] + sequence[ round(l/2) ]) / 2
        except:
            med = sequence[ round(l/2) -1 ] + sequence[ round(l/2) ] 
    else:
        med = sequence[ round(l/2) ]
    return (sequence[0], med , sequence[-1])

res = get_min_med_max("faaacb")
print(res)
