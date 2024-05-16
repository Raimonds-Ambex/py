# 1. Lielais rezultāts
# Uzrakstiet funkciju add_mult, kurai nepieciešami trīs parametri/argumenti
# Atgriež rezultātu, kas ir 2 mazāko argumentu summa reizināta ar lielāko argumenta vērtību.
# PS Uzskatīsim, ka funkcijai vienmēr tiks padoti skaitliski parametri, varam tipus nepārbaudīt.
# Iespējami dažādi risinājumi, piemēram ar list struktūru varētu būt tīri eleganti.
# Piemērs add_mult(2,5,4) -> atgriezīs (2+4)*5 = 30

def add_mult(x:int,y:int,z:int):
    if x >= y and x >= z:
        return x*(y+z)
    if y >= x and y >= z:
        return y*(x+z)
    if z >= x and z >= y:
        return z*(x+y)

print(add_mult(7,1,6))

# --------------------------------------------------------------------
# uzrakstiet funkciju is_palindrome(text)
# kas atgriež bool True vai False atkarībā vai vārds vai teikums ir lasāms vienādi no abām pusēm.
# PS no sākuma varat sākt ar viena vārda risinājumu, bet pilns risinājums ignorēs atstarpes(whitespace) un lielos/mazos burtus
# is_palindrome("Alus ari ira   
#   sula") -> True


def is_palindrome(text):
    rev_text = text[::-1]
    if text.lower() == rev_text.lower():
        return True
    return False

text = input("Vai vārds vai teikums ir lasāms vienādi no abām pusēm? ")
print(is_palindrome(text))