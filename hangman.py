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
                                                                                                                     
                                                                                                                                                              
    """)

def menu():
    banner()
    menu_selection = input("""
    Elija una opcion:

    1. Jugar
    2. ver palabras
    3. Anadir palabra
    4. Eliminar palabra
    5. salir
    
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



# Seleccionar palabra aleatoria 
def selected_word(data):
    palabra=random.choice(data)
    return palabra
    

def run():
    data=open_file()
    menu_selection = input("""
    Elija una opcion:

    1. Jugar
    2. ver palabras
    3. Anadir palabra
    4. Eliminar palabra
    5. salir
    
    """)
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
            entrada=input("ingrese una letra ").lower()
            for i in range(len(word)):
                if entrada == word[i]:
                    secret_word[i]=entrada
            for j, chars in enumerate(secret_word):
                if word[j] == chars:
                    counter+=1
                    if counter == (len(word)):
                        os.system ("cls")
                        print(*secret_word)
                        puerta=False
            counter=0
                    
        print("Ganaste, la palabra secreta era " + word)
    
    elif menu_selection == "2":
        data.sort()
        for i in range(len(data)):
            print(data[i], end=", ")
            if i % 10 == 0 and i > 1:
                print("")
    
    elif menu_selection == "3":
        add_word(input("ingrese nueva palabra: "))

    elif menu_selection == "4":
        remove_word(input("Digite palabra a eliminar: "))
            
    else:
        exit()

    


if __name__=="__main__":
    run()