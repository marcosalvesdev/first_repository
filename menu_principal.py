from titulo import Titulo, Linha


def MenuPrincipal():
      Titulo('MENU PRINCIPAL')
      print('1 - VER CURRÍCULO\n'
            '2 - ENTRAR EM CONTATO DIRETO PELO WHATSAPP\n'
            '3 - DEIXAR UM FEEDBACK\n'
            '4 - VISTAR MEU GitHub\n'
            '5 - VISITAR MEU Linkedin\n'
            '6 - SAIR DO SISTEMA')
      Linha()
      escolha = int(input('Opção: '))
      return escolha
