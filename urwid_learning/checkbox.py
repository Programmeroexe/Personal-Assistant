import urwid

def on_q(k):
    if k in ("q","Q"):
         raise urwid.ExitMainLoop()

def on_click(checkbox, state,user_data=None):
    text.set_text(f"{checkbox.label} is {state}")
checkbox1 = urwid.CheckBox("Checkbox 1", state=False, user_data="checkbox1", on_state_change=on_click)
checkbox2 = urwid.CheckBox("Checkbox 2",state= False, user_data="checkbox2",on_state_change=on_click)
checkbox3 = urwid.CheckBox("Checkbox 3", state=True, user_data="checkbox3",on_state_change=on_click)
text = urwid.Text("",align="center")

listbox = urwid.ListBox(urwid.SimpleListWalker([checkbox1,checkbox2,checkbox3,text]))

loop = urwid.MainLoop(listbox,unhandled_input=on_q)
loop.run()