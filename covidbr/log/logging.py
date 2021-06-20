from .puts import puts

show_console = False


def log(*txt,sep=' '):
    if show_console:
        return puts(*txt,sep=sep)
    else:
        pass