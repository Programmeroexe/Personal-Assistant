import urwid

text1 = urwid.Text("Top text", align="left")
text2 = urwid.Text("Middle text", align="center")
text3 = urwid.Text("Bottom text", align="right")

pile = urwid.Pile([text1, text2, text3])
fill = urwid.Filler(pile)
loop = urwid.MainLoop(fill)  # ❌ No Filler
loop.run()