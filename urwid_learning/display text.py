import urwid


# standard pratice
def exit_on_q(key):
    if key in ("q","Q"):
        raise urwid.ExitMainLoop()

text = urwid.Text("CENTERED TEXT",align="center")
text2 = urwid.Text("LEFT TEXT", align="left")
text3 = urwid.Text("RIGHTENED TEXT", align="right")
pilee = urwid.Pile([text,text2,text3])
fill = urwid.Filler(pilee)

loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()