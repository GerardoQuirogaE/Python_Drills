import sys

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow

from core.plugin_loader import PluginLoader
from core.tool_registry import ToolRegistry


def main():

    app = QApplication(sys.argv)

    # Load plugins
    loader = PluginLoader()
    plugins = loader.load_plugins()

    # Register tools
    registry = ToolRegistry()
    registry.register_plugins(plugins)

    window = MainWindow(registry)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()