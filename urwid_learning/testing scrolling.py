import urwid

class ScrollListBox(urwid.ListBox):
    def __init__(self, body):
        super().__init__(body)
        self.scrollbar = urwid.Text("")

    def render(self, size, focus=False):
        canvas = super().render(size, focus)
        maxcol, maxrow = size
        
        # Calculate scrollbar position
        body_length = len(self.body)
        if body_length <= maxrow:
            scrollbar = ""
        else:
            # Compute the position of the scrollbar
            focus_widget, position = self.body.get_focus()
            scrollbar_size = max(1, int((maxrow / body_length) * maxrow))  # Minimum size 1
            scrollbar_position = int((position / (body_length - 1)) * (maxrow - scrollbar_size))

            # Create scrollbar as a string of spaces and blocks
            scrollbar = ["░"] * maxrow
            for i in range(scrollbar_position, scrollbar_position + scrollbar_size):
                scrollbar[i] = "█"

            scrollbar = "\n".join(scrollbar)

        self.scrollbar.set_text(scrollbar)
        return canvas

class App:
    def __init__(self):
        self.list_walker = urwid.SimpleFocusListWalker(
            [urwid.Text(f"Text {i}") for i in range(50)]
        )
        self.listbox = ScrollListBox(self.list_walker)
        
        # Wrap in Columns for scrollbar on the right
        self.layout = urwid.Columns([self.listbox, ("fixed", 1, urwid.AttrWrap(self.listbox.scrollbar, "scrollbar"))])

        self.mainloop = urwid.MainLoop(self.layout, palette=[("scrollbar", "white", "black")], unhandled_input=self.handle_input)

    def handle_input(self, key):
        if key in ("esc", "q"):  # Exit
            raise urwid.ExitMainLoop()
        elif key in ("up", "down", "page up", "page down"):  # Scroll events
            self.listbox.scrollbar.set_text(self.listbox.render((20, 20)).text)

    def run(self):
        self.mainloop.run()

if __name__ == "__main__":
    App().run()
