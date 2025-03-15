import urwid

# Initial popup position
popup_x = 30
popup_y = 10

def on_exit(key):
    global popup_x, popup_y

    if key in ("esc", "q"):
        raise urwid.ExitMainLoop()

    # Move popup
    if key == "up":
        popup_y = max(2, popup_y - 2)  # Move up
    elif key == "down":
        popup_y = min(20, popup_y + 2)  # Move down
    elif key == "left":
        popup_x = max(5, popup_x - 5)  # Move left
    elif key == "right":
        popup_x = min(50, popup_x + 5)  # Move right

    # Redraw popup if it's open
    if isinstance(loop.widget, urwid.Overlay):
        open_closable_pop_up(None)

def quit_popup(button, userdata=None):
    loop.widget = fillings

def open_closable_pop_up(button, userdata=None):
    text = urwid.Text("Use Arrow Keys to Move\nPress Quit to Close")
    button = urwid.Button("Quit", on_press=quit_popup)

    pile = urwid.Pile([
        urwid.Divider("─"),
        text,
        urwid.Divider("─"),
        button,
        urwid.Divider("─"),
    ])

    padded_pile = urwid.Padding(pile, left=2, right=2)
    popup_filler = urwid.Filler(padded_pile, valign="middle")

    popup_linebox = urwid.LineBox(popup_filler, title="Movable Pop-up")

    overlay = urwid.Overlay(
        popup_linebox, fillings,
        align="left", valign="top",
        width=30, height=10,  # FIXED: Added width and height
        left=popup_x, top=popup_y
    )

    loop.widget = overlay

button = urwid.Button("Open Pop-up!", on_press=open_closable_pop_up)

fillings = urwid.Filler(button, valign="middle")
loop = urwid.MainLoop(fillings, unhandled_input=on_exit)
loop.run()
