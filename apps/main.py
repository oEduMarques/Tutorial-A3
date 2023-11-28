from pessoa import Pessoa

print(pessoa1.senha)

while True:
    opcao = int(input("1 - Mudar Senha\n 2 - Fazer consulta "))
    
    if opcao == 1: 
         pessoa1.mudar_senha()