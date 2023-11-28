import pessoa

class Paciente(pessoa.Pessoa):

    def __init__(self, cpf, nome, datanasc, sexo, estado, cidade, email, telefone):
        super().__init__(cpf, nome, datanasc, sexo, estado, cidade, email, telefone)
        
    def criar_consulta(self):
        nome_paciente = input("Digite o seu nome: ")
        cpf_paciente = input("Digite o seu CPF: ")
        while cpf_paciente != self.cpf:
            cpf_paciente = input("CPF incorreto, digite novamente: ")
                 
        local = input(f"Escolha um local perto de {self.cidade}: 1 - Hospital Moinhos de Vento\n 2 - Hospital Cristo Redentor\n 3 - Santa Casa de Misericórdia")
        
        mes_consulta = int(input("Escolha o mês da sua consulta (1 - 12): "))
        while mes_consulta < 1 or mes_consulta > 12:
            mes_consulta = int(input("Mês inválido, escolha o mês da sua consulta (1 - 12): "))
        
        dia_consulta = int(input("Escolha o dia da sua consulta (1 - 31): "))
        while dia_consulta < 1 or dia_consulta > 31:
            dia_consulta = int(input("Dia inválido, escolha um dia para a sua consulta (1 - 31): "))
        
    def consulta():
        consulta = {
            print(f"Nome: {nome_paciente}")
            print(f"CPF: {cpf_paciente}")
            print(f"Local: {local}")
                
        }

    def verconsulta():