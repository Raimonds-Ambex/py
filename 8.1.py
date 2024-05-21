# 1a. Uzrakstīt funkciju: get_char_count(text), kas saņem string un izvada
# vārdnīcu ar atsevišķu burtu lietojumu skaitu.
# get_char_count("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, ' ': 1}
# vārdnīcas secībai nav nozīme, un visam alfabetam nav jābut
cc = {}
def get_char_count(text):
    for t in text:
        if t in cc:
            cc[t] += 1
        else:
            cc[t] = 1
    print(cc)
        
get_char_count('hubba bubba')

#----------------------------------------
# 1b. Uzrakstīt funkciju: get_digit_dict(num), kas saņem veselu skaitli kā parametru(var būt ļoti liels
# funkcija  izvada ciparu izmantojumu skaitlī vārdnīcas formā
# Ievada 599637003 -> {'0':2, '1':0,....'7'':1,'8':0,'9':2} # rādam visiem cipariem izmantojamību
result = dict.fromkeys(['0','1','2','3','4','5','6','7','8','9'],0)

def get_digit_dict(num):
    num = str(num)
    for n in num:
        result[n]+=1
    print(result)
    
get_digit_dict(599637003)
