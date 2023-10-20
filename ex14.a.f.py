# Considerăm un număr întreg.
# a. Cum vom scrie un program care să afișeze True sau False în funcție de
# valoarea unui bit anume?
# de ex, numărul 25 se scrie în binar 000...0011001
# bitul 3 (de la dreapta la stânga, începând cu bitul 0) este True (1)
# bitul 2 este 0
nr = 25
bitNumber = 3
rezultat = (nr >> bitNumber) & 1
if rezultat == 1:                   # 0000 0000 0001 1001 = 25
    print("True")                   # 0000 0000 0000 0011 = 3 (25 >> 3) 
else:                               # 0011 & 0001 = 0001 (3 & 1 = 1 = True)
    print("False")