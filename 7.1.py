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