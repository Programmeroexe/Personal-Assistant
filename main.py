import brain
from pyfiglet import Figlet
import colorama
colorama.init()
from colorama import Fore, Style, Back
from pyfiglet import Figlet
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

def ascii_text(text, font="3D-ASCII", width=120):
    f = Figlet(font=font,width=width)
    print(Fore.GREEN + Back.BLACK + Style.BRIGHT+ f.renderText(text))

ascii_text("WELCOME",font='small')
ascii_text("BACK!",width=150,font='small')
