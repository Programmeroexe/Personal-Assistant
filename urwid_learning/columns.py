import urwid
def on_q(key):
    if key in ("q","Q"):
        raise urwid.ExitMainLoop()

text1 = urwid.Text("right Text", align='right')
text2 = urwid.Text("Center Text", align='center')
text3 = urwid.Text("left Text", align = 'left')


col = urwid.Columns([
    (15, urwid.Text("Fixed 15-width")),
    urwid.Text("Expands Automatically"),
    (10, urwid.Text("Fixed 10-width"))
])
fillings = urwid.Filler(col)
loop = urwid.MainLoop(fillings, unhandled_input=on_q)
loop.run()