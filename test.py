from gb import window
from style import StyleMain, StyleSheet

mainS = StyleMain.create({
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

styles = StyleSheet.create({
    'view':{
        'cor':'#0066ff',
        'side':'left',
        'width': 100,
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
            'View': f'{styles["view"]}'
        }
    }, styleMain=mainS)
    win.App()