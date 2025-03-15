import urwid

def on_q(k):
    if k in ("q","Q"):
        raise urwid.ExitMainLoop()

progressBar = urwid.Padding(urwid.ProgressBar('normal', 'complete', current=10,done=200 ), align='center')

fillings = urwid.Filler(progressBar, valign="middle")

loop = urwid.MainLoop(fillings , unhandled_input=on_q)
loop.run()