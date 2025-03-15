import urwid

def on_select(button, state):
    if state:  # Only print when the button is selected
        text.set_text(f"Selected: {button.label}")

group = []  # A list to hold the group of radio buttons

radio1 = urwid.RadioButton(group, "Option 1", state=True, on_state_change=on_select)
radio2 = urwid.RadioButton(group, "Option 2", on_state_change=on_select)
radio3 = urwid.RadioButton(group, "Option 3", on_state_change=on_select)
text = urwid.Text("")
# Arrange in a pile (vertical list)
pile = urwid.Pile([radio1, radio2, radio3,text])

# Add padding and start the loop
loop = urwid.MainLoop(urwid.Filler(pile, valign="top"))
loop.run()
