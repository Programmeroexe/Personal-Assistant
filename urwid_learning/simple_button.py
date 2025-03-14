import urwid
def on_q(key):
    if key in ('q','Q'):
        raise urwid.ExitMainLoop()
def pressed_button(button, user_data=None):
    text.set_text(f"here is info returned: {button}, {user_data}")
# ADDING BUTTOONSSS!!
button = urwid.Button("Click Me!",on_press=pressed_button,user_data="Test Button")
text = urwid.Text("")

piling = urwid.Pile([button,text])

filling = urwid.Filler(piling)
window = urwid.MainLoop(filling, unhandled_input=on_q)
window.run()