import urwid

def exit_on_q(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()

text = urwid.Text("LEFTENED TEXT", align='left')
text1 = urwid.Text("CENTERED TEXT", align="center")
text2 = urwid.Text("RIGHTENED TEXT", align = "right")

pile = urwid.Pile([text,text1,text2])
fill = urwid.Filler(pile, valign="middle") # --> top, middle, bottom
loop = urwid.MainLoop(fill, unhandled_input=exit_on_q)
loop.run()