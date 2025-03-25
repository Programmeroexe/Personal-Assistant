"""
WHAT THIS SOFTWARE WILL BE ABLE TO:
speak
log my weight and stuff like that
log my irl goals
log my irl study goals
log my audio as dairy or somethng else
log my text into audio as dairy or somethng else
act as a dairy 
act as motivation
idk stuff like that
"""
import brain
from pyfiglet import Figlet
import urwid

# Set 256-color mode for Urwid
screen = urwid.raw_display.Screen()
screen.set_terminal_properties(colors=256)

def ascii_text(text, font="3D-ASCII", width=120):
    f = Figlet(font=font, width=width)
    return f.renderText(text)

def on_q(key):
    if key in ('esc',):
        raise urwid.ExitMainLoop()

# ✅ Use named colors OR enable 256-color mode
palette = [
    ('banner', '#ff8400', 'black')  # ✅ Using named colors instead of hex
]

window = urwid.Text(('banner', ascii_text("PERSISTENCE", font="big")))

filler = urwid.Filler(window)
engine = urwid.MainLoop(filler, screen=screen, unhandled_input=on_q, palette=palette)
engine.run()
