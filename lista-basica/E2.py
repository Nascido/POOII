user = input("Crie o nome de usuário: ")
senha = input("Crie uma senha: ")

while user == senha:
    print("Senha inválida: Proteção muito baixa")
    user = input("Crie o nome de usuário: ")
    senha = input("Crie uma senha: ")

print("Cadastro finalizdo")