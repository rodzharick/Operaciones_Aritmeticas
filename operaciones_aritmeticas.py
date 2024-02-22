# Ejercicio N.2 programa para calcular  la suma,resta,multiplicacion,division,division entera.modulo y potencia de X y Y

#input 

X=int(input("digite primer valor de X: "))
Y=int(input("digite segundo valor de Y: "))

# Processing
S= X+Y
R= X-Y
M= X*Y
D= X/Y
DE= X//Y
MOD= X%Y
P= X**Y

# Output

print("---------")
print("la suma de " + str(X) + " + " + str(Y) + " es " +str(S))
print("la resta de " + str(X) + " -" + str(Y) + " es " +str(R))
print("la multiplicacion de " + str(X) + " * " + str(Y) + " es " +str(M))
print("la division  de " + str(X) + " /" + str(Y) + " es " +str(D))
print("la division  entera de " + str(X) + " //" + str(Y) + " es " +str(DE))
print("el modulo de " + str(X) + " % " + str(Y) + " es " +str(MOD))
print("la potencia de " + str(X) + " ** " + str(Y) + " es " +str(P))