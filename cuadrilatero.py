lado_a = int(input("lado 1:"))
lado_b = int(input("lado 2:"))
lado_c = int(input("lado 3:"))
lado_d = int(input("lado 4:"))

if lado_a > 0 and lado_b > 0 and lado_c > 0 and lado_d > 0:
    if lado_a == lado_b == lado_c == lado_d:
        print("es un cuadrado")
    elif (lado_a == lado_d and lado_b == lado_c) or (lado_a == lado_c and lado_b == lado_d) or (
            lado_a == lado_b and lado_c == lado_d):
        print("es un rectangulo")
    else:
        print("es otro cuadrilatero, se necesitan angulos para determinar")
else:
    print("no es un cuadrilatetro valido")
