import random
tentativas=0
num_aleatorio = random.randint(1,100)
print(f"O número aleatório gerado pelo sistema é {num_aleatorio}")

while True: 

    palpite= int(input("Insira um palpite de número aleatório"))

    if num_aleatorio<palpite:
        print("Você passou do número aleatório, tente um número menor")
        tentativas+= 1
    elif num_aleatorio>palpite:
        print("Você passou do número aleatório, tente um número maior")
        tentativas+= 1
    else:
        print("Você adivinhou o número {numero_aleatório} em {tentativas} tentativas!")
    
        break




        
         


    

    


 

    