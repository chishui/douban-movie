import urwid

palette = [
    ('body', 'dark cyan', ''),
    ('gray', 'light gray', ''),
    ('focus','black','light gray'),
    ('footer', 'white', ''),
    ]

loop = None

class ListItem(urwid.WidgetWrap):
    def __init__(self, movie):
        self.data = movie
        item = [
            ('pack', urwid.AttrWrap(urwid.Text(movie.title), 'body', 'focus')),
            (5, urwid.AttrWrap(urwid.Text(' ' + str(movie.year)), 'gray', 'focus')),
        ]
        w = urwid.Columns(item)
        blank = urwid.Divider()
        p = urwid.Pile([w, urwid.AttrWrap(urwid.Text(movie.sub_title), 'gray', 'focus'), blank])
        urwid.WidgetWrap.__init__(self, p)

    def selectable(self):
        return True

    def keypress(self, size, key):
        return key


class ListView(urwid.Frame):
    def __init__(self, movies):
        footer=urwid.AttrWrap(urwid.Text('Press q to exit, use up and down arrow to navigate, press Enter to select'), 'footer')
        items = self.make_items(movies)
        self.listbox = urwid.ListBox(urwid.SimpleListWalker(items))
        top = urwid.Overlay(self.listbox, urwid.SolidFill(' '),
            align='center', width=('relative', 60),
            valign='middle', height=('relative', 60),
            min_width=20, min_height=9)
        urwid.Frame.__init__(self, urwid.AttrWrap(top, 'body'), footer=footer)

    def make_items(self, movies):
        items = []
        for movie in movies:
            item = ListItem(movie)
            items.append(item)
        return items

    def keypress(self, size, key):
        global loop
        if key is 'enter':
            loop.data = self.listbox.get_focus()[0].data
            raise urwid.ExitMainLoop()

        return urwid.Frame.keypress(self, size, key)

def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

def run(movies):
    global loop
    list_view = ListView(movies)
    loop = urwid.MainLoop(list_view, palette, unhandled_input=exit_on_q)
    loop.screen.set_terminal_properties(colors=256)
    loop.run()
    return loop.data if hasattr(loop, 'data') else None
