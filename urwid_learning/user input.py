import urwid

def quit_on_q(key):
    if key in ("q","Q"):
        raise urwid.ExitMainLoop()



text = urwid.Edit("Enter Text: ",align="center")

fill = urwid.Filler(text)
loop = urwid.MainLoop(fill , unhandled_input=quit_on_q)
loop.run()