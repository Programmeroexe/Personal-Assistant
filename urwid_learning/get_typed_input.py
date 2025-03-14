import urwid

def on_key_press(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
    elif key == 'enter':
        user_text = input_box.get_edit_text()
        if user_text in ('q','Q'):
            raise urwid.ExitMainLoop()
        inputed_text.set_text(user_text)

input_box = urwid.Edit("Enter Text: ", align='center')
inputed_text = urwid.Text("",align = 'center')

pile = urwid.Pile([input_box,inputed_text])
filling = urwid.Filler(pile)
loop = urwid.MainLoop(filling, unhandled_input=on_key_press)
loop.run()