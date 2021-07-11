from tkinter import *

def arg_unique(val):
    pass

def whatside(value):
    if value.lower() == 'top':
        return TOP
    elif value.lower() == 'left':
        return LEFT
    elif value.lower() == 'right':
        return RIGHT
    elif value.lower() == 'bottom':
        return BOTTOM

def whatfill(value):
    if value.lower() == 'y':
        return Y
    elif value.lower() == 'x':
        return X
    elif value.lower() == 'both':
        return BOTH

        #cor, side, width, height, fill, expand, borderwidth, relief, highlightbackground, highlightthickness
params = ['#fff', LEFT, 0, None, None, False, 0, 'raised', None, 0]
class renderKey:
    def __init__(self, tk, *, args=None, kwargs=None):
        self.tk =tk
        self.value = args if args != None else kwargs
        if type(self.value) is str:
            pass
        elif type(self.value) is dict:
            for key, value in self.value.items():
                if key == 'cor':
                    params[0] = value
                if key == 'side':
                    params[1] = whatside(value)
                if key == 'width':
                    params[2] = value
                if key == 'height':
                    params[3] = value
                if key == 'fill':
                    params[4] = whatfill(value)
                if key == 'expand':
                    params[5] = value
                if key == 'borderwidth':
                    params[6] = value
                if key == 'relief':
                    params[7] = value
                if key == 'highlightbackground':
                    params[8] = value
                if key == 'highlightthickness':
                    params[9] = value

        else:
            pass
    
    def __repr__(self) -> str:
        frame = Frame(self.tk, bg=params[0], width=params[2], height=params[3], highlightbackground=params[8], highlightthickness=params[9], borderwidth=params[6], relief=params[7])
        frame.pack(side=params[1], expand=params[5] ,fill=params[4])        
        return f'{frame}'