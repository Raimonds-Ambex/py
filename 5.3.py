# Izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Nav nemaz tik slikts tas biezpiens. Tas biezpiens nav nemaz tik slikts.

txt = input("Jūsu teksts: ")
lower_txt = txt.lower()

while True:
    x = lower_txt.rfind('nav')
    y = lower_txt.rfind('slikts')

    if x == -1 and y == -1:
        break
    else:
        txt = txt[0:x] + 'ir labs' + txt[y+6:]
        lower_txt = lower_txt[0:x] + 'ir labs' + lower_txt[y+6:]

txt = txt[0].upper() + txt[1:]
print(f"Salabotais teksts: {txt}")