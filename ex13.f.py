x = -9
y = 1

a = x & y
b = x | y 

c = ~x           # 4 = ..0000 0100 
                 # complement fata de 2 = ..1111 1011
d = x ^ 5        # ~4 = - 0101 (-5)  : se inv toti bitii pana la ultimul 1, el ramane nemodif + ce e dupa el
e = x >> 2         # din nr negativ in ~ => invers nr poz + 1 si mai inv o data
f = x << 2
print(a, b, c, d, e, f)