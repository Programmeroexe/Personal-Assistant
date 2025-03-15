import urwid
def on_q(k):
    if k in ('q','Q'):
        raise urwid.ExitMainLoop()

def clicked_increase(button,user_data=None):
    if progressNum.current >= 0 and progressNum.current < 100:
        progressNum.current = progressNum.current + 5
    currentValue.set_text(str(progressNum.current)) 
def clicked_decrease(button, user_data=None):
    if progressNum.current > 0:
        progressNum.current = progressNum.current - 5
    currentValue.set_text(str(progressNum.current)) 


currentValue = urwid.Text("0",align='center')
progressNum = urwid.ProgressBar('normal','complete', current=0, done = 100)
button_inc = urwid.Button("Increase by 5%", on_press=clicked_increase,user_data="increase",align='center')
button_dec = urwid.Button("Decrease by 5%", on_press=clicked_decrease,user_data="decrease",align='center')

pile = urwid.Padding(urwid.Pile([currentValue,progressNum,button_inc,button_dec]),align="center")

fillings = urwid.Filler(pile, valign="middle")

loop = urwid.MainLoop(fillings, unhandled_input=on_q)
loop.run()