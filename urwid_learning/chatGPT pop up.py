import urwid

class MyPopUpLauncher(urwid.PopUpLauncher):
    def __init__(self):
        # Create a button that will trigger the pop-up
        super().__init__(urwid.Button("Open Pop-Up", on_press=self.open_pop_up))

    def create_pop_up(self):
        """Create the actual pop-up widget."""
        close_button = urwid.Button("Close", on_press=lambda _: self.close_pop_up())
        pop_up_widget = urwid.LineBox(urwid.Pile([urwid.Text("Hello! This is a pop-up!"), close_button]))
        return pop_up_widget

    def get_pop_up_parameters(self):
        """Define the size and position of the pop-up."""
        return {'left': 5, 'top': 2, 'overlay_width': 30, 'overlay_height': 7}

# Create the main UI with the pop-up launcher
launcher = MyPopUpLauncher()
main_widget = urwid.Filler(launcher)

# Run the UI loop
loop = urwid.MainLoop(main_widget, pop_ups=True)
loop.run()
