from .Behavior_view import renderview
from .Behavior_legend import renderlegend
from .Behavior_button import renderbutton
from .Behavior_set import setFrame

Return = []

def startIt(tk, arg, styleMain=None):
    for name, val in arg.items():
        for key, value in styleMain.items():
            if key in arg.keys():
                id = setFrame(name, tk, value)
            else:
                id = setFrame(name, tk)
                
        Return.append(id)
        for key, value in val.items():
            if key == 'View':
                if type(value) is str:
                    Return.append(renderview(id, args=value)) #passar o id.................
                elif type(value) is dict:
                    Return.append(renderview(id, kwargs=value))
                else:
                    Return.append(f'Wrong Argumment: {value}')
            if key == 'Legend':
                if type(value) is str:
                    Return.append(renderlegend(id, args=value))
                elif type(value) is dict:
                    Return.append(renderlegend(id, kwargs=value))
                else:
                    Return.append(f'Wrong Argumment: {value}')
            if key == 'Button':
                if type(value) is str:
                    Return.append(renderlegend(id, args=value))
                elif type(value) is dict:
                    Return.append(renderlegend(id, kwargs=value))
                else:
                    Return.append(f'Wrong Argumment: {value}')


def renderIt(tk, kwargs, *, styleMain=None):
    tk = tk
    kwargs = kwargs
    styleMain = styleMain
    startIt(tk, kwargs, styleMain)
    return Return
    
    