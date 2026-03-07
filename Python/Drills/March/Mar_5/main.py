from prompt_toolkit.application import Application
from prompt_toolkit.patch_stdout import patch_stdout
from prompt_toolkit.layout import Layout, Window, Container, FormattedTextControl, VSplit, HSplit, VerticalAlign, WindowAlign, D
from prompt_toolkit.formatted_text import StyleAndTextTuples
from prompt_toolkit.key_binding import KeyBindings, merge_key_bindings
from prompt_toolkit.keys import Keys
from prompt_toolkit.widgets import Box
from prompt_toolkit.styles import Style, merge_styles
from prompt_toolkit import print_formatted_text, HTML
try:
    from prompt_toolkit.output.win32 import NoConsoleScreenBufferError  # noqa
except AssertionError:
    pass
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from cli_chess.core.main import MainPresenter

main_view: Container

class MainView:
    def __init__(self, presenter: MainPresenter):
        try:
            self.presenter = presenter
            self.color_depth = terminal_config.get_value(terminal_config.Keys.TERMINAL_COLOR_DEPTH)
            self._container = self._create_main_container()

            """
            That creates the full terminal interface."""
            self.app = Application(
                layout=Layout(self._container),
                color_depth=lambda: self.color_depth,
                mouse_support=True,
                full_screen=True,
                style=self._get_combined_styles(),
                refresh_interval=0.5
            )