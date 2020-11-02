from classe_principal import Programador_Iniciante
from titulo import Titulo, Linha
from menu_principal import MenuPrincipal
from habilidades_e_cursos import *
from experiencias_profissionais import Experiencias_Profissionais
from feed_back import CaixaFeedBack
import webbrowser


def ProgramaPrincipal():
    dados = Programador_Iniciante()
    chave = MenuPrincipal()
    if chave == 1:
        Titulo('DADOS PESSOAIS')
        dados.DadosPessoais()
        Titulo('HABILIDADES COM PROGRAMAÇÃO')
        Habilidades_Programacao()
        Titulo('HABILIDADES COM TECNOLOGIA DA INFORMAÇÃO')
        Habilidades_TI()
        Titulo('EXPERIÊNCIAS PROFISSIONAIS')
        Experiencias_Profissionais()
        Titulo('CURSOS REALIZADOS')
        Cursos()
        Linha()
        retornar = int(input('Digite 1 se deseja retornar ao Menu Principal.\n'
                             'Digite 2 para sair do sistema.\n'
                             'Opção: '))
        if retornar == 1:
            ProgramaPrincipal()
        else:
            exit('Obrigado por utilizar este programa! Bye')
    if chave == 2:
        webbrowser.open('https://api.whatsapp.com/send?phone=5544999843840&text=Hello%20Terr%C3%A1queo!%20Em%20alguns'
                        '%20instantes%20voc%C3%AA%20falar%C3%A1%20com%20Marcos%20Vin%C3%ADcius!')

    if chave == 3:
        CaixaFeedBack()
        ProgramaPrincipal()