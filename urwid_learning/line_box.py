import urwid

def on_exit(k):
    if k in ('esc'):
        raise urwid.ExitMainLoop()
def answered(button,user_data=None):
    if user_data == "y":
        raise urwid.ExitMainLoop()
    elif user_data == 'n':
        pass

text = urwid.Text("Do you want to Quit?")
yes = urwid.Button("Yes", user_data="y",on_press=answered)
no = urwid.Button("No", user_data="n",on_press=answered)

col = urwid.Columns([(8, yes),(8,no)],dividechars=5)
pile = urwid.Pile([text,col])
linebox = urwid.Padding(urwid.LineBox(pile, title="Quit?", title_align="left"),align='center', width=40)

fillings =urwid.Filler(linebox, "middle") 

loop = urwid.MainLoop(fillings, unhandled_input=on_exit)
loop.run()