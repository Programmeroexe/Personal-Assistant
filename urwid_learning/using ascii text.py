import urwid
from pyfiglet import Figlet


f = Figlet(font="small")

fillings= urwid.Filler(urwid.Text(str(f.renderText("Hello World")), align="center"), valign="middle")
loop = urwid.MainLoop(fillings)
loop.run()