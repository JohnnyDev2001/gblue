from tkinter import *

#txt
params = ['']
class renderlegend:
    def __init__(self, tk, *, args=None, kwargs=None):
        self.tk =tk
        self.value = args if args != None else kwargs
        if type(self.value) is str:
            pass
        elif type(self.value) is dict:
            for key, value in self.value.items():
                if key == 'text':
                    params[0] = value


    def __repr__(self):
        legend = Label(self, text=params[0])
        legend.pack()
        return f'{legend}'