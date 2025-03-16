import urwid
def on_exit(k):
    if k in ("esc",):
        raise urwid.ExitMainLoop()
def clicked(button, userdata=None):
    pass

palette = [('btn_normal', 'white', 'black'),
('btn_hover', 'white,strikethrough', 'black')

]

button1 = urwid.Button("Styled Button", on_press=clicked)
styled_button1 = urwid.AttrMap(button1, 'btn_normal','btn_hover')
button2 = urwid.Button("Styled Button", on_press=clicked)
styled_button2 = urwid.AttrMap(button2, 'btn_normal','btn_hover')
button3 = urwid.Button("Styled Button", on_press=clicked)
styled_button3 = urwid.AttrMap(button3, 'btn_normal','btn_hover')

piling = urwid.Pile([styled_button1,styled_button2,styled_button3])
fillings = urwid.Filler(piling)
loop = urwid.MainLoop(fillings,palette=palette,unhandled_input=on_exit)
loop.run()