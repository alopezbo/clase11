#=================================================================
#Ejemplo2 de hacer una sobrecarga de un operador (suma, resta, etc)
#=================================================================

class itspower:
    def __init__(self,x): #inicializar un objeto 'x'
        self.x=x            #le da el atributo al objeto de ser igual a x.
    def __pow__(self,other):  #pow es una funcion integrada dentro de python, por eso podemos usarla como un inicializador
        return self.x**other.x

a=itspower(2)
b=itspower(10)
resultado=a**b
print(resultado) #usando a=2 y b=10 el resultado va a ser 1024. 2 elevado a la 10

#=================================================================
#Ejemplo 3
#=================================================================
def factorial(n):
    f=1
    while n>0:
        f*=n
        n-=1
    print(f)
factorial(4)


    