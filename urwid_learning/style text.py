import urwid
# Shows available color names
def on_exit(k):
    if k in ('esc',):
        raise urwid.ExitMainLoop()
palette = [
    ('banner', 'light green', 'dark blue'),  # Foreground: white, Background: dark blue
    ('button_normal', 'white', 'black'),
    ('button_focus', 'light green', 'black'),
]

text = urwid.Text("Styled Text!",align="center")
styling = urwid.AttrMap(text, "banner")

window = urwid.Filler(styling,valign="middle")


loop = urwid.MainLoop(window,palette=palette, unhandled_input=on_exit)
loop.run()