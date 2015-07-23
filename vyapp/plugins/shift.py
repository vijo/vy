class Shift(object):
    def __init__(self, area, width=4, char=' '):
        self.width = width
        self.char  = char
        area.install((1, '<Key-greater>', lambda event: event.widget.shift_sel_right(self.width, self.char)),
                     (1, '<Key-less>', lambda event: event.widget.shift_sel_left(self.width)))


install = Shift
