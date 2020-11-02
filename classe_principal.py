

class Programador_Iniciante:

    def __init__(self):
        self.nome = 'Marcos Vinícius'
        self.data_nascimento = {'dia': 13, 'mes': 10, 'ano': 1993} # DD/MM/AAAA. ALTERE APENAS AQUI A DATA DE NASCIMENTO
        self.cidade = 'Sarandi'
        self.contato_whatsapp = 44999843840
        self.e_mail = 'marcosalves.dev@gmail.com'
        self.escolaridade = 'Ensino Médio completo'

    def Idade(self):
        from datetime import date

        idade = date.today().year - self.data_nascimento['ano']

        if self.data_nascimento['mes'] <= date.today().month and self.data_nascimento['dia'] <= date.today().day:
            return idade
        else:
            idade -= 1
            return idade

    def DadosPessoais(self):

        dados = {'Nome: ': self.nome,
                 'Idade: ': str(self.Idade()),
                 'Reside em: ': self.cidade,
                 'Celular de Contato / WhatsApp: ': str(self.contato_whatsapp),
                 'E-mail: ': self.e_mail,
                 'Escolaridade: ': self.escolaridade}
        for k, v in dados.items():
            print(f'{k}{v}')