import math
#Cilindro área volumen
#Desarrolla un programa en Python que contenga las siguientes funciones:
#una función llamada area_cilindro, que reciba el radio y altura del cilindro y regrese el área calculada.
#una función llamada volumen_cilindro, que reciba el radio y altura del cilindro y regrese el 
# volumen calculado.
#El programa debe leer el radio y la altura de un cilindro, luego llamar a las funciones y finalmente 
# mostrar el área y volumen del cilindro.
#Entrada
#El radio del cilindro
#La altura del cilindro
#Salida
#En el primer renglón el área del cilindro utilizando el mensaje "area=" y después el valor del área
#  formateado con 2 decimales.
#En el segundo renglón el volúmen del cilindro utilizando el mensaje "volumen="
# y después el valor del volúmen formateado con 2 decimales.
#Ejemplo de ejecución del programa
#>>>2.32
#>>>4.3                                                                                                                                           
#area=96.50                                                                                                                                    
#volumen=72.71
def area_cilindro(r,h):
    tapas = 2*math.pi*r**2
    base=2*math.pi*r
    areacuerpo=base*h
    return tapas+areacuerpo
def volumen_cilindro(r,h):
    v=math.pi*r**2*h
    return v
def main():
    #escribe tu código abajo de esta línea
    radio= int(input("r "))
    altura=int(input("h "))
    print(volumen_cilindro(radio,altura))
    print(area_cilindro(radio,altura))
    

if __name__=='__main__':
    main()
