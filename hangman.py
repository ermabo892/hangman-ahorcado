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

  
        


# abrir archivo data
def open_file():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        data=[linea.strip() for linea in f]
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
        menu_selection = input("Selecciona la opcion deseada: ")
        if menu_selection == "1":
            
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
                entrada=input("ingrese una letra ")
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
        
        elif menu_selection == "2":
            menu()
            print("palabras existentes en la base de datos: \n")
            data.sort()
            for i in range(len(data)):
                print(data[i], end=", ")
                if i % 10 == 0 and i > 1:
                    print("")
            print()
            print("----------------------------------------------------------------------------------------")
            input("Presione cualquier tecla para continuar: ")

#---------------------------------------------------------------------------------------------- 

        elif menu_selection == "3":
            menu()
            add_word(input("ingrese nueva palabra: "))
            print("palabra agregada con exito")
            input("presione cualquier tecla para continuar: ")
#---------------------------------------------------------------------------------------------- 
        
        elif menu_selection == "4":
            menu()
            remove_word(input("Digite palabra a eliminar: "))
            print("palabra eliminada con exito")
            input("presione cualquier tecla para continuar: ")

#----------------------------------------------------------------------------------------------                 
        
        else:
            os.system("cls")
            exit()
            


    


if __name__=="__main__":
    run()