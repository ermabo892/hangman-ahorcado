import os
import random

def banner():
    print("""
     █████   █████   █████████   ██████   █████   █████████  ██████   ██████   █████████   ██████   █████      █████████    █████████   ██████   ██████ ██████████
   ░░███   ░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░██████ ██████   ███░░░░░███ ░░██████ ░░███      ███░░░░░███  ███░░░░░███ ░░██████ ██████ ░░███░░░░░█
    ░███    ░███  ░███    ░███  ░███░███ ░███  ███     ░░░  ░███░█████░███  ░███    ░███  ░███░███ ░███     ███     ░░░  ░███    ░███  ░███░█████░███  ░███  █ ░ 
    ░███████████  ░███████████  ░███░░███░███ ░███          ░███░░███ ░███  ░███████████  ░███░░███░███    ░███          ░███████████  ░███░░███ ░███  ░██████   
    ░███░░░░░███  ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███ ░░░  ░███  ░███░░░░░███  ░███ ░░██████    ░███    █████ ░███░░░░░███  ░███ ░░░  ░███  ░███░░█   
    ░███    ░███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███      ░███  ░███    ░███  ░███  ░░█████    ░░███  ░░███  ░███    ░███  ░███      ░███  ░███ ░   █
    █████   █████ █████   █████ █████  ░░█████ ░░█████████  █████     █████ █████   █████ █████  ░░█████    ░░█████████  █████   █████ █████     █████ ██████████
    ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░     ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░      ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░     ░░░░░ ░░░░░░░░░░ 
                                                                    by Erick Mantilla
                                                                        ermabo892                                                                                                                
                                                                                                                                                              
    """)

  
        

def without_accent(list: list):
    replacements = (
            ("Á", "A"),
            ("É", "E"),
            ("Í", "I"),
            ("Ó", "O"),
            ("Ú", "U"),
        )
    for i in range(len(list)):
        for a, b in replacements:
            list[i]=list[i].replace(a, b)
    return list
    

# abrir archivo data
def open_file():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        data=[linea.strip().upper() for linea in f]
        data = without_accent(data)
        return data
        
def add_word(word):
    with open("./files/data.txt", "a", encoding="utf-8") as f:
        f.write(word)
        f.write("\n")

def remove_word(word):
    strings=[]
    data = open_file()
    for i in data:
        if word != i:
            strings.append(i)
            
    with open("./files/data.txt", "w", encoding="utf-8") as f:
        for string in strings:
            f.write(string)
            f.write("\n")
    
    if len(data) == len(strings):
        print("Palabra no encontrada")
    else:
        print("palabra eliminada con exito")

def menu():
    os.system("cls")
    banner()
    

# Seleccionar palabra aleatoria 
def selected_word(data):
    palabra=random.choice(data)
    return palabra
    

def run():
    while True:
        data=open_file()
        menu()
        print(
    """
    Elija una opcion:

    1. Jugar
    2. ver palabras
    3. Anadir palabra
    4. Eliminar palabra
    5. salir
    
    """)
        menu_selection = int(input("Selecciona la opcion deseada: "))
        if 1<=menu_selection<=5:            
            if menu_selection == 1:                
                word=selected_word(data)
                secret_word=["-" for i in range(len(word))]
                #    secret.append("-")
                counter=0
                puerta=True
                while puerta:
                    os.system ("cls")
                    banner()        
                    print("adivina la palabra!")
                    print(*secret_word)
                    entrada=input("ingrese una letra ").upper()
                    for i in range(len(word)):
                        if entrada == word[i]:
                            secret_word[i]=entrada
                    for j, chars in enumerate(secret_word):
                        if word[j] == chars:
                            counter+=1
                            if counter == (len(word)):
                                os.system ("cls")
                                banner() 
                                print(*secret_word)
                                print("Ganaste, la palabra secreta era " + word + "!!")
                                input("Presione una tecla para continuar...")
                                puerta=False

                    counter=0
        
                            
                

    #---------------------------------------------------------------------------------------------- 
            
            elif menu_selection == 2:
                menu()
                print("palabras existentes en la base de datos: \n")
                data.sort()
                for i in range(len(data)):
                    print("[" + data[i] + "]", end=", ")
                    
                print()
                print("----------------------------------------------------------------------------------------")
                input("Presione cualquier tecla para continuar: ")

    #---------------------------------------------------------------------------------------------- 

            elif menu_selection == 3:
                menu()
                add_word(input("ingrese nueva palabra: "))
                print("palabra agregada con exito")
                input("presione cualquier tecla para continuar: ")
    #---------------------------------------------------------------------------------------------- 
            
            elif menu_selection == 4:
                menu()
                remove_word(input("Digite palabra a eliminar: ").upper())          
                input("presione cualquier tecla para continuar: ")

    #----------------------------------------------------------------------------------------------                 
            
            elif menu_selection == 5:
                os.system("cls")
                exit()
        else:
            print("Seleccione una opcion valida!")
            input("Presione una tecla para continuar...")
            


    


if __name__=="__main__":
    while True:
        try:
            run()
            break
        except ValueError:
            print("Seleccione una opcion valida")
            input("Presione una tecla para continuar...")
    