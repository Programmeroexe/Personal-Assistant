import urwid

def on_q(k):
    if k in ("Q", "q"):
        raise urwid.ExitMainLoop()

# Create list items
items = [urwid.Text(f"Text {i}") for i in range(1, 6)]
listwalker = urwid.SimpleListWalker(items)
listbox = urwid.ListBox(listwalker)

# Wrap the ListBox with BoxAdapter for fixed height
wrapped_listbox = urwid.BoxAdapter(listbox, height=5)

# Place it inside a center-aligned Padding and a middle-aligned Filler
padded_listbox = urwid.Padding(wrapped_listbox, align="center", width=("relative", 5))
filled_listbox = urwid.Filler(padded_listbox, valign="middle")

# Run UI
loop = urwid.MainLoop(filled_listbox, unhandled_input=on_q)
loop.run()
