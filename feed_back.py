import PySimpleGUI as sg

def CaixaFeedBack():
    sg.ChangeLookAndFeel("DarkGrey3")
    caixa_texto = [[sg.Text('Empresa :'), sg.Input(key='nome_empresa')],
                   [sg.Multiline(size=(55, 10), key='feedback')],
                   [sg.Button('Enviar'), sg.Exit('Cancelar')]]
    janela = sg.Window('Feedback').layout(caixa_texto)
    valor = janela.Read()
    nome_empresa = valor[1]['nome_empresa']
    feedback = valor[1]['feedback']
    if nome_empresa == '':
        nome_empresa = '<desconhecida>'
    with open('feed_back.txt', 'a+') as arquivo:
        arquivo.write(f'A empresa {nome_empresa} escreveu:')
        arquivo.write(f'{feedback}')
    janela.close()

