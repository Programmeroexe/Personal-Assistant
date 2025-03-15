import urwid
from pyfiglet import Figlet

count = 0  # No need for global now

def q(k):
    if k in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def ascii_text(text, font="small", width=120):
    f = Figlet(font=font, width=width)
    return str(f.renderText(str(text)))

def changing(loop, user_data=None):
    global count  # Use global to modify outside variable
    count += 1  # Increment count
    text.set_text(ascii_text(count))  # Update UI
    loop.set_alarm_in(1, changing)  # Reschedule function

text = urwid.Text(ascii_text(count), "center")
filling = urwid.Filler(text, "middle")

loop = urwid.MainLoop(filling, unhandled_input=q)
loop.set_alarm_in(1, changing)  # Start updating
loop.run()
