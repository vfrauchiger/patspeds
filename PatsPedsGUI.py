import PySimpleGUI as sg 

import PatsPedsClaims as pdc 
import PatsPedsClaimsWrapper as pdw 
import PatsPedsFileWrapper as pdf 

sg.theme('Dark Blue 2')

layout = [[sg.Text('Application ID'), sg.InputText(), sg.Button('Filewrapper (A)'), sg.Button('Latest Claims (A)')], \
            [sg.Text('Pre-Grant PublNo or Patent No'), sg.InputText(), sg.Button('Latest Claims (P)'), sg.Button('Get Term Extension (P)')], \
            [ sg.Button('Exit'), sg.Text('(c) by Vinz Frauchiger, 2021')] ]

window = sg.Window('PatsPedsGUIVersion', layout)


while True:
    event, values = window.read()
    if event == 'Latest Claims (P)':
        print('get Claims (Patent)')
        print(pdw.get_appl(str(values[1]), go_back='full'))
    elif event == 'Get Term Extension (P)':
        extension, disclaimer = pdw.get_appl(str(values[1]), go_back='delay')
        sg.popup("Extension [d]:" + extension, 'Disclaimer present:'+str(disclaimer))
    elif event == 'Latest Claims (A)':
        print('get Claims (Appl Id)')
        print(pdc.get_claims(str(values[0])))
    elif event == 'Filewrapper (A)':
        print('Filewrapper (Appl Id)')
        print(pdf.get_filewrapper(str(values[0])))
    elif event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    print('You entered ', values)

window.close()