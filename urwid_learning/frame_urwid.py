import urwid

def on_q(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()

header1 = urwid.Text("This is a header.", align= "center")
footer1 = urwid.Text("Press Q to quit.", align="center")
content = urwid.Filler(urwid.Text("Main content goes here.", align="center"))

frame = urwid.Frame(content,header=header1, footer=footer1)


# fillings = urwid.Filler(frame) frame dont need filler support

loop = urwid.MainLoop(frame,unhandled_input=on_q)
loop.run()