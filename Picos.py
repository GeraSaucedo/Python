
#Pedimos el numero de minutos 
Minutos = input("Introduce el numero de minutos: \n")

#Validamos que solo existan numeros positivos
while Minutos < 0:
    Minutos = input("Numero no valido Ingrese de nuevo los minutos: \n")

if Minutos == 0: picos = 3
else: picos = pow(3,(Minutos+1))

print("Numero de picos: " + `picos`)
  


