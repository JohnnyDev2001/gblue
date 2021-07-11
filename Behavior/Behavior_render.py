from .Behavior_view import renderKey

Return = []

def startIt(tk, arg):
    for val in arg.values():
        for key, value in val.items():
            if key == 'View':
                if type(value) is str:
                    Return.append(renderKey(tk, args=value))
                elif type(value) is dict:
                    Return.append(renderKey(tk, kwargs=value))
                else:
                    Return.append(f'Wrong Argumment: {value}')


def renderIt(tk, kwargs):
    tk = tk
    kwargs = kwargs
    startIt(tk, kwargs)
    return Return
    
    