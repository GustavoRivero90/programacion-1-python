#1
print("Hola Mundo")

#2
nombre = input("Ingresa tu nombre ")
print(f"Hola {nombre}!")

#3
nombre = input("Ingresa tu nombre ")
apellido = input("Ingresa tu apellido ")
edad = input("Ingresa tu edad ")
lugar_de_residencia = input("Ingresa tu lugar de residencia ")
print(f"Hola soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#4
radio = float(input("tu radio "))
pi = 3.14
area = pi*radio**2
perimetro = 2*pi*radio
print("El area del circulo es", area)
print("El perimetro del circulo es", perimetro)

#5
segundos = int(input("La cantidad de segundos es: "))
horas = segundos/3600
print("La cantidad de horas es:", horas)

#6
numero = int(input("Ingreso un numero "))
print(f"La tabla de multiplicar de {numero} ")
for i in range(1,11):
    print(f"{numero}x{i} = {numero*i}")

num_1 = int(input("Ingrese el primer numero: distinto de 0  "))
num_2 = int(input("Ingrese el segundo numero: distinto de 0  ")) 


if num_1==0 or num_2==0:
   print("Error: los numeros deben ser distintos de 0")

else:
    suma= num_1 + num_2
    resta= num_2 - num_1
    multiplicacion= num_1 * num_2
    division= num_2 / num_1
    print("Resultados")
    print("Suma", suma)
    print("Resta", resta)
    print("Multiplicacion", multiplicacion)
    print("Division", division)


altura= float(input("Ingrese su altura en metros "))
peso= float(input("Ingrese su peso "))

imc= peso/(altura**2)
print("La imc es", imc)


celsius= float(input("Ingrese la temperatura "))
farenheit= (9/5) * celsius +32

print(f"{celsius} °C equivalen a {farenheit}°F")


num_1 = float(input("EScriba el 1er numero" ))
num_2 = float(input("Escriba el 2do numero "))
num_3 = float(input("Escriba el 3er numero "))

promedio = (num_1 + num_2 + num_3) / 3
print(f"El promedio de {num_1}, {num_2}, {num_3} es {promedio}")