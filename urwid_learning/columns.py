import urwid
def on_q(key):
    if key in ("q","Q"):
        raise urwid.ExitMainLoop()

text1 = urwid.Text("right Text", align='right')
text2 = urwid.Text("Center Text", align='center')
text3 = urwid.Text("left Text", align = 'left')


col = urwid.Columns([text1, text2, text3])  
fillings = urwid.Filler(col)
loop = urwid.MainLoop(fillings, unhandled_input=on_q)
loop.run()