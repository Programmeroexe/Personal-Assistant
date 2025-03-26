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
from brain import brain
from pyfiglet import Figlet
import urwid

class TUI():
    def __init__(self):
        ascii_title = self.text_into_ascii("PERSISTENCE", font="BIG")
        style = []
        self.time_variable = f"{brain.current_date()} {brain.current_time()}"
        self.current_time_text = urwid.Text(f"Current Time: {self.time_variable}")
        # add color to dividors
        self.tui_list = [
            urwid.Text(("title", ascii_title), align="center"),
            self.current_time_text,
            urwid.Divider("-"),
            urwid.Divider('-',bottom=2),
            urwid.Columns([urwid.Button("Log Weight")]),
            urwid.Columns([urwid.Button("View Weight Log")]),
            urwid.Columns([urwid.Button("Delete Weight Log")]),
            ]


        piling = urwid.Pile(self.tui_list)
        self.window = urwid.MainLoop(urwid.Filler(piling, valign="top"),palette=style, unhandled_input=self.testing_quit)
        self.window.screen.register_palette_entry("title",f"{urwid.BROWN}",urwid.BLACK)
        self.window.set_alarm_in(1,self.update_current_time)
    def text_into_ascii(self, text, font = "big"):
        figlet_setting = Figlet(font=font)
        string = figlet_setting.renderText(text)
        return str(string)

    def update_current_time(self, loop, user_data=None):

        self.time_variable = f"{brain.current_date()} {brain.current_time()}"
        self.current_time_text.set_text(f"Current Time: {self.time_variable}")
        loop.set_alarm_in(1, self.update_current_time)
    def testing_quit(self, key):
        if key in ("esc",):
            raise urwid.ExitMainLoop()

    def run(self):
        self.window.run()

app = TUI()
app.run()