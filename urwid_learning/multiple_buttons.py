import urwid
def on_q(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
def on_being_clicked(button, user_data):
    text.set_text(f"You Clicked {user_data}")

button1 = urwid.Button("Button 1",on_press=on_being_clicked, user_data="Button 1")
button2 = urwid.Button("Button 2",on_press=on_being_clicked, user_data="Button 2")
button3 = urwid.Button("Button 3",on_press=on_being_clicked, user_data="Button 3")
text = urwid.Text("",align="center")


button_pile = urwid.Padding(urwid.Pile([button1, button2, button3]), align='center', width=12)
pile = urwid.Pile([button_pile,text])
fillings = urwid.Filler(pile)
loop = urwid.MainLoop(fillings, unhandled_input=on_q)
loop.run()