print("hola")
nombre = input("¿como te llamas? ")
print(f"bienvenido {nombre}")
edad = input("¿cuantos años tienes? ")
print(f"¡que bien {nombre}! entonces tienes {edad} años")
print(f"el año que viene tendras {int(edad)+ 1} años")
print("debes tener una materia favorita")
materia = input("¿cual es el nombre de la materia? ")
while True:
    try:
        calificacion = int(input("¿que calificacion esperas sacar? "))
        break
    except:
        print(f"no lo creo {nombre}, intenta de nuevo")
if calificacion >= 9:
    print(f"¡excelente {nombre}, sigue asi!")
elif calificacion >= 7:
    print(f"no es tan malo, pero podrias mejorar ¡animo {nombre}!")
else:
    print(f"¡tu puedes, no te desanimes {nombre}!")