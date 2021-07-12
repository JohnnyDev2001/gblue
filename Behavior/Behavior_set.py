from tkinter import *

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

params = ['#829CAF', TOP, 600, 200, None, False, 0, 'raised', None, 0]

def frameConfig(name, tk):
    name = name
    MainFrame = Frame(tk, bg=params[0], width=params[2], height=params[3], highlightbackground=params[8], highlightthickness=params[9], borderwidth=params[6], relief=params[7])
    MainFrame.pack(side=params[1], expand=params[5] ,fill=params[4])    
    #MainFrame.grid()
    #MainFrame.Place()
    return MainFrame

def setFrame(name, tk, styleMain=None):
    name = name
    tk = tk
    styleMain = styleMain

    if type(styleMain) is dict:
        for key, value in styleMain.items():
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

    return frameConfig(name, tk)