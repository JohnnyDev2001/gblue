from tkinter import *


from Behavior import Behavior_render

tk = Tk()

class window:
    def __init__(self, start=True, height='800', width='600', * , bg='#44475A', name='', icon=''):
        self.name = name
        self.icon = icon if icon != '' else './icon/icone.ico'
        self.height = height
        self.width = width
        self.start = start
        self.bg = bg
        self.args = any
        self.styleArgs = any
        #---------start--------------
        tk.geometry(f'{str(self.height)}x{str(self.width)}')
        tk.configure(background=self.bg)
        tk.title(str(self.name))
        tk.iconbitmap(str(self.icon))

    def render(self, args, *, styleArgs=None, styleMain=None):
        self.args = args
        self.styleArgs = styleArgs
        self.styleMain = styleMain
        if type(self.args) == dict:
            res = Behavior_render.renderIt(tk, self.args, styleMain=self.styleMain)
            for x in res:
                return f'{x}'
        else:
            return f'Valor não corresponde ao esperado'

    def App(self):
        if self.start == True:
            tk.mainloop()

if __name__ == '__main__':
    pass