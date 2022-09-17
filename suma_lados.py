# dados 3 numeros a, b y c verificar si pueden formar los lados de un triangulo


#input
a=int(input("digite el valor de a: "))
b= int(input("digite el valor de b: "))
c= int(input("digite el valor de c: "))

#procesing
n=a+b
n2=a+c
n3=b+c
if n>c and n2>b and n3>a:
    print("la suma de "+str(a)+" y "+str(b)+" es igual a "+str(n))
    print("la suma de "+str(a)+" y "+str(c)+" es igual a "+str(n2))
    print("la suma de "+str(c)+" y "+str(b)+" es igual a "+str(n3))

    print("es un triangulo")

else: 
    print("no es un triangulo")
    print("la suma de "+str(a)+" y "+str(b)+" es igual a "+str(n))
    print("la suma de "+str(a)+" y "+str(c)+" es igual a "+str(n2))
    print("la suma de "+str(c)+" y "+str(b)+" es igual a "+str(n3))