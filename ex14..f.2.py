#  Daca vreau sa setez 2 biti alesi ca fiind FALSE, iar restul sa ramana neschimbati: de ex schimbarea bitilor 3 si 5: 15 => 7
numar = 15
bitNumber1 = 3
bitNumber2 = 5

mask = 2 ** bitNumber1 + 2 ** bitNumber2
numar = numar & ~mask 

                                      # mask = 2^3 + 2^5 = 40
                                      # numar | mask :  0000 0000 0000 1111 & ~(0000 0000 0010 1000)
                                      #                 0000 0000 0000 1111 & 1111 1111 1101 0111 => 0000 0000 0000 0111
                                      # 0000 0000 0000 1111 = 15
                                      #             5  3    
print(numar)                          # 0000 0000 0000 0111 = 7