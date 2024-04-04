def cadastrar usuario(n):
    nome= input("Digite seu nome: ")
    cpf= int(input("Digite seu CPF: "))
    senha= int(input("Digite sua senha: "))
    return nome, cpf, senha

def fazer_login(usuarios):
    cpf_l = input("Digite seu CPF: ")
    senha = input("Digite sua senha: ")

    for usuario in usuarios:
        if cpf_l == usuario [1] and senha_1 == usuario[2]:
            print("Login feito com sucesso!")
            return True
        
    print("CPF ou senha incorretos. Tente novamente.")
    return false

def main():
    usuarios = []:
    while True:
        print("1. Cadastrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            novo_usuario = cadastrar_usuario()
            if len(novo_usuario[1]) == 11 and novo_usuario[1].isdigit():
                usuarios.append(novo_usuario)
                print("Usuário cadastrado com sucesso!")
            else:
                print("CPF inválido. O CPF deve conter apenas números e ter 11 dígitos")

        elif opcao == "2":
            if fazer_login(usuarios):
                break        



        elif opcao == "3":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")
                


    

