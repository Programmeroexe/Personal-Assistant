import urwid
import datetime
global want_to_quit
want_to_quit = False
def on_q(key):
    want_to_quit = False
    if key in ("q","Q"):
        want_to_quit = True
        raise urwid.ExitMainLoop()

current_time = str(datetime.datetime.now())
text = urwid.Text(current_time, align="center")
filling = urwid.Filler(text,valign= "middle")
while True:
    text.set_text(current_time)
    loop = urwid.MainLoop(filling, unhandled_input=on_q)
    loop.start()
    if want_to_quit:
        break