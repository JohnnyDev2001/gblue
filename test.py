from gb import window

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
    })
    win.App()