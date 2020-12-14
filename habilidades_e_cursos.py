def Cursos():
    cursos = {'Curso 1: ': 'Python 3 - [120Horas]',
              'Curso 2: ': 'MySQL Server - [40horas]',
              'Curso 3: ': 'Git e GitHUb - [20Horas]',
              'Curso 4: ': 'Linux - [40Horas]',
              'Curso 5: ': 'Rede de Computadores - [20Horas]'}
    for k, v in cursos.items():
     print(f'{k}{v.rjust(55 - len(k))}')


def Habilidades_Programacao():
    skill_developer = ['+ Python 3',
                       '+ Banco de Dados Relacionais',
                       '+ Flutter',
                       '+ Dart',
                       '+ JavaScript',
                       '+ ReactNative']
                       
    for v in skill_developer:
        print(v)


def Habilidades_TI():
    skill_list_ti = ['+ Montagem e manutenção de computadores',
                     '+ Manutenção de celulares',
                     '+ Conhecimentos intermediários em eletrônica e elétrica',
                     '+ Rede de computadores']
    for v in skill_list_ti:
        print(v)
