from gb import window
from style import styleMain

mainS = styleMain.create({
    'janela':{
        'side':'left',
        'width': 300,
        'height': 100,
        'fill': 'both',
        'expand': False,
        'borderwidth': 2,
        'relief': 'ridge',
        }
    })

if __name__ == '__main__':
    win = window()
    win.render({
        'janela':{
            'View':{
                'cor':'#0066ff',
                'side':'left',
                'width': 100,
                'height': 100,
                'fill': 'both',
                'expand': False,
                'borderwidth': 2,
                'relief': 'ridge',
                }
            
        }
    }, styleMain=mainS)
    win.App()