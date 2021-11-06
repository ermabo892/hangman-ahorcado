import os
import random

# abrir archivo data
def open_file():
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        data=[linea.strip() for linea in f]
        return data
        

# Seleccionar palabra aleatoria 
def selected_word(data):
    palabra=random.choice(data)
    return palabra
    

def run():
    data=open_file()
    word=selected_word(data)
    secret_word=["-" for i in range(len(word))]
    #    secret.append("-")
    contador=0
    puerta=True
    while puerta:
        os.system ("cls")
        print("adivina la palabra!")
        print(*secret_word)
        entrada=input("ingrese letra ")
        for i in range(len(word)):
            if entrada == word[i]:
                secret_word[i]=entrada
        for j, chars in enumerate(secret_word):
            if word[j] == chars:
                contador+=1
                if contador == (len(word)):
                    os.system ("cls")
                    print(*secret_word)
                    puerta=False
        contador=0
                
    print("Ganaste, la palabra secreta era " + word)

    


if __name__=="__main__":
    run()