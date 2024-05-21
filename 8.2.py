# 2. Vārdnīcu labotājs
# Uzrakstīt replace_dict_value(d, bad_val, good_val), kas atgriež vārdnīcu ar nomainītām vērtībām
# Funkcijas parametri ir vārdnīca d, kas jāapstrādā, un vērtības bad_val kura jānomaina uz good_val
# clean_dict_value({'a':5,'b':6,'c':5}, 5, 10) -> {'a':10,'b':6,'c':10} , jo 5 bija vērtība, kas jānomaina.

def replace_dict_value(d, bad_val, good_val):
    dc = d.copy()
    for k, v in dc.items():
        if v == bad_val:
            dc[k] = good_val
    
    return(dc)
    
print(replace_dict_value({'a':5,'b':6,'c':5}, 5, 10))
