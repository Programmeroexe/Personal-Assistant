import urwid
from pyfiglet import Figlet


count = 0
def q(k):
    if k in ('q',"Q"):
        raise urwid.ExitMainLoop()
def ascii_text(text, font="small", width=120):
    f = Figlet(font=font,width=width)
    return str(f.renderText(str(text)))

def changing(loop, user_data=None):
    text.set_text(ascii_text(str(count+1)))
    count += 1
    loop.set_alarm_in(1,changing)


text = urwid.Text(ascii_text(count),"center")
filling = urwid.Filler(text, "middle")


loop = urwid.MainLoop(filling, unhandled_input=q)
loop.set_alarm_in(1,changing)
loop.run()
