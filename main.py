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

class TUI():
    def __init__(self):

        self.window = urwid.MainLoop(urwid.Filler(urwid.Text('')))
    
    def text_into_ascii(self, text, font = "big"):
        figlet_setting = Figlet(font=font)
        string = figlet_setting.renderText("persistence".upper())
        return str(string)

    def run(self):
        self.window.run()

app = TUI()
app.text_into_ascii("hi")