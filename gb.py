try:
    from tkinter import *
except:
    from Tkinter import *

from Behavior import Behavior_render

tk = Tk()

class window:
    def __init__(self, start=True, height='800', width='600', * , name='', icon=''):
        self.name = name
        self.icon = icon if icon != '' else './icon/icone.ico'
        self.height = height
        self.width = width
        self.start = start
        self.args = any
        self.styleArgs = any
        #---------start--------------
        tk.geometry(f'{str(self.height)}x{str(self.width)}')
        tk.title(str(self.name))
        tk.iconbitmap(str(self.icon))

    def render(self, args, styleArgs = None):
        self.args = args
        self.styleArgs = styleArgs
        if type(self.args) == dict:
            res = Behavior_render.renderIt(tk, self.args)
            for x in res:
                print(x) 
        else:
            return 'Valor não corresponde ao esperado'

    def App(self):
        if self.start == True:
            tk.mainloop()

if __name__ == '__main__':
    pass