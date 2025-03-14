import urwid

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

# Creating some text widgets
widgets = [urwid.Button(f"Btn {i}") for i in range(1, 10)]

# GridFlow Layout: (Fixed width per item, wraps automatically)
grid = urwid.GridFlow(widgets, cell_width=10, h_sep=1, v_sep=2, align="center")

filler = urwid.Filler(grid)
loop = urwid.MainLoop(filler, unhandled_input=exit_on_q)
loop.run()
