import urwid

def on_exit(k):
    if k in ("esc",):
        raise urwid.ExitMainLoop()

def quit_popup(button, userdata=None):
    loop.widget = fillings
def open_closable_pop_up(button, userdata = None):
    text = urwid.Text("Press Quit Button to Quit, O_O;")
    button = urwid.Button("Quit", on_press=quit_popup)
    pile = urwid.Padding(urwid.Pile([urwid.Divider(),text, button,urwid.Divider()]), align="left",left=2,right=2)
    popup_linebox = urwid.LineBox(pile, "Pop up!", title_align="left")

    overlay = urwid.Overlay(popup_linebox, fillings, align="center",valign="middle", width=("relative",30), height=("relative",30))
    loop.widget = overlay
button = urwid.Button("Open Pop up!",align="center", on_press=open_closable_pop_up)


fillings = urwid.Filler(button,valign="middle")
loop = urwid.MainLoop(fillings, unhandled_input=on_exit)
loop.run()