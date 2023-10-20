# Cum vom scrie un program care să seteze un anumit bit False?
# de ex, numărul 25 se scrie în binar 000...0011001
# dacă se cere setarea bitului 3, atunci numărul devine (10001) 17
# dacă se cere setarea bitului 2, atunci numărul devine (rămâne tot) 25
nr = 25
bitNumber = 3                         # 0000 0000 0001 1001 = 25
rezultat = nr & ~(1 << bitNumber)     # 0000 0000 0000 1000 = 8 (1 << 3)
print(rezultat)                       # compl fata de 2 a nr 8: ..1111 0111
                                      # ~8 = - 9 (- 1001) 
                                      # 25 & -9 = 0001 1001 & 1111 0111 = 0001 0001 = 17
                                      #              25  &  compl 2 a lui -9 = 17