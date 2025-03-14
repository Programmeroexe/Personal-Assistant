import urwid
def on_q(k):
    if k in ('q','Q'):
        raise urwid.ExitMainLoop()

def clicked(button, state, user_data):
    text1.set_text(f"button: {button.label}\nstate:{state}\nuser_data: {user_data}")

group = []
radio_button1 = urwid.RadioButton(group, "radio button 1", True, on_state_change=clicked,user_data="RB1")
radio_button2 = urwid.RadioButton(group, "radio button 2", False, on_state_change=clicked,user_data="RB2")
radio_button3 = urwid.RadioButton(group, "radio button 3", False, on_state_change=clicked,user_data="RB3")
string= ""
for i in range(len(group)):
    string= string+str(group[i])+"\n"
text1 = urwid.Text(string)
wrapping = urwid.Padding(urwid.Pile([radio_button1,radio_button2,radio_button3,text1]),align="center")

window = urwid.MainLoop(urwid.Filler(wrapping,"middle"),unhandled_input=on_q)
window.run()