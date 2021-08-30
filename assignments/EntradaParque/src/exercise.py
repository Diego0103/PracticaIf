#Para la entrada a un parque, solo pueden entrar personas mayores a 4 años.
#De 5 a 10 años se cobra $10 por cada año (infante), si es mayor a 10 años y hasta 15(niño), $12 por cada
#año, y mayor de 15(adulto), $20 por cada año, a menos que sea de 60 años o más, en cuyo caso se cobra
#tarifa única de $800
#Escribe un programa en el que el usuario escriba su edad y se muestre cuánto. Utiliza tres funciones 
#para calcular cuánto debe pagar.
#Si la persona tiene 4 años o menos, se le niega la entrada.
def infante(n):
    costo=n*10
    return costo

def nino(n):
    costo=n*12
    return costo

def adulto(n):
    costo=n*20
    return costo


def main():
    #escribe tu código abajo de esta línea
    edad=int(input("Cuál es su edad: "))
    costoMayor=800
    if edad<=4 and edad>=0:
        print("No puede entrar")
    elif edad>4 and edad<=10:
        print("El costo es: "+str(infante(edad)))
    elif edad>10 and edad<=15:
        print("El costo es: "+str(nino(edad)))
    elif edad>15 and edad<=60:
        print("El costo es: "+str(adulto(edad)))
    elif edad>60 and edad<=100:
        print("El costo es: "+str(costoMayor))
    else:
        print("Edad inválida")
    

    

if __name__=='__main__':
    main()
