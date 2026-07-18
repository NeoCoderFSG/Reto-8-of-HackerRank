# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

def resolver_agenda():
    #lee toda la entrada estandar de golpe
    entrada = sys.stdin.read().splitlines()
    
    if not entrada:
        return
        
    # El primer elemento es el numero de amigos en la agenda
    
    n = int(entrada[0])
    
    # creamos el diccionario para la aagenda telefonica 
    agenda = {}
    
    # llamamos la agenda con las siguientes 'n' lineas
    for i in range(1, n + 1):
        nombre, telefono = entrada[i].split()
        agenda[nombre]= telefono
        
    # las lineas rstantes despues de 'n' son las consultas 
    consultas = entrada[n + 1:]
    
    # procesamos cada consulta 
    for nombre_consultado in consultas:
        if nombre_consultado in agenda:
            print(f"{nombre_consultado}={agenda[nombre_consultado]}")
        else:
            print("Not found")
            
            
if __name__=="__main__": 
    resolver_agenda()
    
        