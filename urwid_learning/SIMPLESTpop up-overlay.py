import urwid

def on_exit(k):
    if k in ("esc",):
        raise urwid.ExitMainLoop()

def open_popup(button, userdata = None):
    pop_up_win = urwid.LineBox(urwid.Text("POP UP! BOOO!"),title="popup!", title_align='left')
    overlay  = urwid.Overlay(pop_up_win,fillings,align="left",valign="top",width=("relative",20),height=("relative",20) )
    loop.widget = overlay

button = urwid.Button("Open Pop up!", on_press=open_popup)




fillings = urwid.Filler(button,  valign="middle")
loop = urwid.MainLoop(fillings, unhandled_input= on_exit)
loop.run()