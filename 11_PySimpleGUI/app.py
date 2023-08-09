import PySimpleGUI as sg
layout = [[sg.Text('Barra de progreso')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]
window = sg.Window('Barra de progreso', layout)
progress_bar = window['progressbar']
for i in range(1000):
    event, values = window.read(timeout=5)
    if event == 'Cancel'  or event == sg.WIN_CLOSED:
        break
    progress_bar.UpdateBar(i + 1)
window.close()

