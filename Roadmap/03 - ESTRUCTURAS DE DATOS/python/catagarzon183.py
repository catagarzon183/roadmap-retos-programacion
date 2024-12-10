'''

#ESTRUCTURAS DE PYTHON

#Lista

my_list = ["Catalina", "Black", "Camila", "Alex"]
print (my_list)
my_list.append("Castor") #añadir datos
print(my_list)
my_list.remove("Catalina")
print(my_list)
print(my_list[1]) #Acceso
my_list[1] = "Jenny" #Actulizacion
print(my_list)
my_list.sort() #ordenacion
print(my_list)


#Tuplas

my_tuple = ("Catalina", "Garzon" , "Catarsis183", "36")
print(my_tuple[1]) #Acceso
print(my_tuple[3]) #Acceso
my_tuple = tuple(sorted(my_tuple)) #volverlo a tupla que se esta mostrando como lista con el objetivo de que no se pueda transformar nuevamente
print(type(my_tuple))
print(my_tuple)


#SET

my_set =  {"Catalina", "Garzon" , "Catarsis183", "36" } #es una estructura desordenada, es bueno para guardar datos, para recorrer los datos pero no para que los guarde de forma ordenada
my_set.add("catalinagarzon1803@gmail.com")
print(my_set)
my_set.remove("Catalina")
print(my_set)


#Diccionario, no se tienen posiciones, sino nombres que son las claves

my_dict : dict = {
    "name": "Catalina",
    "surname": "Garzon",
    "alias": "Manzana",
    "age": "28"
    }
my_dict["email"] = "catalina111"
my_dict["email"]
del my_dict ["email"]
print(my_dict)
my_dict["age"] = "29" #Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) #Todo esto para que lo ordene con las palabras clave y su respectiva asignacion
print(my_dict)

"Extra"

# - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
# - Utiliza operaciones de inserción, borrado, actualización y ordenación.

my_list1 = ["Aire acondicionado", "Aspiradora", "Bombilla", "Cafetera", "Calentador", "Consola", "Impresora", "Lampara", "Lavadora", "Licuadora", "Microondas", "Radio", "Sanduchera", "Sonido", "Teatro en casa"]
print(my_list1)
my_list1.append("Telefono fijo")
print(my_list1)
my_list1.remove("Aire acondicionado")
print(my_list1)
print(my_list1[1])
my_list1[1]= "Reemplazo"
print(my_list1)
my_list1.sort()
print(my_list1)

my_tupla1 = ("Clases que transforman", "Clases de matemáticas", "Desde 2020", "3017234519")
print(my_tupla1)
print(my_tupla1[1])
my_tupla1 = tuple(sorted(my_tupla1))
print(type(my_tupla1))
print(my_tupla1)

my_set1 = {"Ingeniera", "Eléctrica" , "Catalina", "Garzon", "28" }
my_set1.add("Programadora")
print(my_set1)
my_set1.remove("28")
print(my_set1)

my_dict1 : dict =  {
    "Elemento": "Computador",
    "Función" : "Trabajo",
    "Alias": "El bebe",
    "Tiempo de funcionamiento": "5 años",

}

my_dict1 ["Dueño"] = "Catalina111"
print(my_dict1)
my_dict1 ["Dueño"]
del my_dict1 ["Dueño"]
print(my_dict1)
my_dict1["Tiempo de funcionamiento"] = "6 años"
print(my_dict1)
'''
'''
#Extra reto

my_agent : dict =  {

    "Nombre": "Catalina",
    "De donde le conoce": "Universidad",
    "Número": "3017234519"

    } 

print("Primer contacto del diccionario: ")
for valor in my_agent.values():
    print(valor)

nuevo_nombre = input("Ingrese un nuevo nombre: ")
nuevo_lugar = input("De donde le conoce: ")
while True:
    try:
        nuevo_numero = int(input("Ingrese número de 11 dígitos:")) #convierte la entrada en un número enteroca
        if len(str(nuevo_numero)) <=11:
            break
        else:
            print("El número excede 11 nmeros")
    except ValueError:
        print("Por favor ingrese un número valido")

my_agent = {} # para actualizar el diccionario
my_agent ["Nombre"] = nuevo_nombre
my_agent ["De donde le conoce"] = nuevo_lugar
my_agent ["Número"] = nuevo_numero

print("Nuevos contactos:")
for valor in my_agent.values():
    print(valor)


#if "Nombre" in my_agent:
#    del my_agent  ["Nombre"]

nombre_guardado = my_agent ["Nombre"] #Guardar el nombre ingresado
lugar_guardado = my_agent ["De donde le conoce"]
numero_guardado = my_agent ["Número"]


print("Agenda actualizada")
for valor in my_agent.values():
    print(valor)
'''    

# FORMA EN QUE LO HACE BRAIS


def my_agenda():
    
    agenda  = {}

    while True:
  
         print("1. Buscar contacto")
         print("2. Insertar contacto")
         print("3. Actualizar contacto")
         print("4. Eliminar contacto")
         print("5. Salir")

        option = input("\nSelecciona una opcion: ")
   
        match option:
             case "1": 
                 name = input ("Introduce el nombre del contacto a buscar: ")
                 if name in agenda:
                 print(f"El numero de telefono de {name} es {agenda[name]}.")
                 else :
                 print(f"El contacto {name} no existe.")
             case "2":
                 name = input("\nIntroduce el nombre de contacto: ")            
                 phone = input("\nIntroduce el numero de contacto: ")
                 if phone.isdigit() and len(phone) >0 and len(phone) <= 11:
                  agenda [name] = phone
                 else:
                  print ("Debes introducir un número de teléfono un máximo de 11 digitos")     
             case "3":
                 name = input("Introduce el nombre del contacto a actualizar: ")
                  if name in agenda:
                   phone = input("\nIntroduce el numero de contacto: ")
                     if phone.isdigit() and len(phone) >0 and len(phone) <= 11:
                      agenda [name] = phone
                     else:
                    print("Debes introducir un numero de telefono maximo de 11 digitos.")
                  else:
                    print(f"El contacto {name} no existe.")
             case "4":
                 name = input("Introduce el nombre del contacto a eliminar: ")
                 if name in agenda:
                  del agenda [name]
                 else:
                   print(f"El contacto {name} no existe.")
             case "5":
                print("Saliendo de la agenda")
            break
           
             case _: 
            print("Opcion no válida. Elige una opcion del 1 al 5")

my_agenda()        



