"""
Franco Tool: Il tool definitivo per la formattazione corretta delle stringhe multilinea in Python3

Authors: Porchetta
         Azzeccagarbugli
"""

# Valore consigliato, si prega di non toccare se non si assolutamente cosa si sta andando a modificare
# PERICOLO ESPLOSIONE!!1!!!!

chars_for_break = 22
# Ottenimento stringa mediante la funzione input presente in Python, che si è ritenuta essere la migliore per questo caso e per la vita
text = input("Inserisci la stringa da formattare: ")
# Stringa provvisoria per l'output
converted_text = ""

# Variable di appoggino per le gambe quando si è stanchi
char_i = 0
# For-each che scorre(ggia) (Franco was here) tutti i caratteri della stringa
for char in text:
    # Se si ha a che fare con il primo carattere, allora si ha a che fare con il primo carattere
    if(char_i == 0):
        converted_text += "\""

    converted_text += char

    # Se si ha a che fare con il carattere chars_for_break, allora si ha che fare con il carattere chars_for_break
    if(char_i == chars_for_break):
        char_i = -1
        converted_text += "\" \\\n"

    # Non siamo avari e siamo generosi quindi incrementiamo le variabili
    char_i += 1

# Aggiunta dell'ultimo carattere, necessario per far comprendere a Python che il nostro lavoro è bello che finito
converted_text += "\""

# E Gutenberg muto
print(converted_text)
