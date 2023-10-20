# Considerăm un număr întreg.
# Cum vom scrie un program care să seteze un anumit bit True?
# de ex, numărul 25 se scrie în binar 000...0011001
# dacă se cere setarea bitului 3, atunci numărul devine (rămâne tot) 25
# dacă se cere setarea bitului 2, atunci numărul devine (11101) 29
nr = 25
bitNumber = 3
rezultat = nr | (1 << bitNumber) 
print(rezultat)                   # 0000 0000 0001 1001 = 25
                                  # 0000 0000 0000 1000 = 8 (1 << 3) 
                                  # 0001 1001 | 0000 1000 = 0001 1001 = 25 (25 | 8 = 25)
  