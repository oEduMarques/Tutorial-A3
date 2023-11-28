import pessoa

class Paciente(pessoa.Pessoa):
    
    def __init__(self, cpf, nome, datanasc, sexo, estado, cidade, email, telefone):
        super().__init__(cpf, nome, datanasc, sexo, estado, cidade, email, telefone)
        self.consulta_agendada = False
        self.dados_consulta = {}

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

        # Armazena os dados da consulta
        self.dados_consulta = {
            'nome_paciente': nome_paciente,
            'cpf_paciente': cpf_paciente,
            'local': local,
            'mes_consulta': mes_consulta,
            'dia_consulta': dia_consulta
        }

        self.consulta_agendada = True
        print("Consulta agendada com sucesso!")

    def verificar_consulta(self):
        if self.consulta_agendada:
            print("Dados da Consulta:")
            print(f"Nome do Paciente: {self.dados_consulta['nome_paciente']}")
            print(f"CPF do Paciente: {self.dados_consulta['cpf_paciente']}")
            print(f"Local da Consulta: {self.dados_consulta['local']}")
            print(f"Mês da Consulta: {self.dados_consulta['mes_consulta']}")
            print(f"Dia da Consulta: {self.dados_consulta['dia_consulta']}")
        else:
            print("Nenhuma consulta agendada.")