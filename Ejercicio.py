def cal_cil(pi, radio, altura):
    volumen = pi * (radio ** 2) * altura
    return volumen

pi = 3.14159
radio = 5
altura = 10

# Llamar a la función y almacenar el resultado
volumen = cal_cil(pi, radio, altura)

# Imprimir el resultado
print(f"El volumen del cilindro es {volumen}")


def cal_cono(piC, radioC, alturaC ):
    volumenCono = piC *(radio**2)*alturaC
    return volumenCono

piC= 3.14159/3
radioC = 5
alturaC= 10

volumenCono = cal_cono(piC, radioC, alturaC)

print(f"El volumen del cono es {volumenCono}")




