import PySimpleGUI as pg
import qrcode
pg.theme_background_color('#EEB0B0')
layout = [
    [pg.Input(key = 'Text_input', font = ('Open Sans', 12))],
    [pg.Text('Fill color', font = ('Open Sans', 12), background_color = '#EEB0B0'), pg.Input(key = 'fill_color', size = 6, font = ('Open Sans', 12), default_text = 'Black'),
     pg.Text('Back color', font = ('Open Sans', 12), background_color = '#EEB0B0'), pg.Input(key = 'back_color', size = 6, font = ('Open Sans', 12), default_text = 'White')],
     [pg.Button('Create', key = 'create_button', font = ('Open Sans', 12), button_color = '#001D6E')],
     [pg.Image('', key = 'Image_key')]
]

window = pg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    
    input = values['Text_input']
    Fill_color = values['fill_color']
    Back_color = values['back_color']

    if not input:
         pg.popup('Enter Text', title = "Error", background_color = '#EEB0B0', button_color = '#001D6E')
    else:
        try:
           qr = qrcode.QRCode(border=2, box_size=13)
           qr.add_data(input)
           image = qr.make_image(fill_color = Fill_color, back_color = Back_color)
           image.save('qrcode.png')
           window['Image_key'].update('qrcode.png')
        except:
            pg.popup('Invalid Input')