def Experiencias_Profissionais(empresa='<nome_empresa>', ano_contrato=0,
                               cargo='<desconhecido>',  contratado=False):
    empresa = 'March Automação Industrial'
    ano_contrato = 'Novembro de 2020'
    contratado = True
    cargo = 'Programador Junior'
    if contratado:
        print(f'Empresa:{empresa.rjust(55 - len("Empresa:"))}')
        print(f'Ano de início:{ano_contrato.rjust(55 - len("Ano de início:"))}')
        print(f'Função:{cargo.rjust(55 - len("Função:"))}')
