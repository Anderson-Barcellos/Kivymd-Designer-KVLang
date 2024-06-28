from kivy.config import Config

Config.set("graphics", "width", "800")
Config.set("graphics", "height", "1200")
Config.set("graphics", "resizable", "0")
import textwrap
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
import os
from kivy.config import Config
from kivymd.uix.screen import MDScreen

#!PATH
file_path = "test.kv"

# Create the file if it does not exist
if not file_path in os.listdir():
    with open(file_path, "w") as f:
        f.write(str())


#!WIDGETS


class KvApp(MDApp):
    """Application class. Main entry point to the application.
    Inherits from the MDApp class.
    """

    def __init__(self, kvfile=None, **kwargs):
        """Initialize the application."""
        super().__init__(**kwargs)
        self.kvfile = kvfile
        self.rendered = str()

    def on_start(self):
        """Start the application."""
        if self.kvfile:
            Clock.schedule_interval(self.cicle, 0)

    def build(self):
        """Build the root widget."""

        self.root = MDFloatLayout(
            size_hint=(1, 1), pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.root.md_bg_color = "black"

        # Create widget placeholder
        self.kv_display = MDLabel(
            text="KV Display",
            size_hint=(1, 1),
            theme_text_color="Custom",
            text_color="white",
        )
        self.kv_display.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        self.root.add_widget(self.kv_display)

        return self.root

    def cicle(self, *args):
        """Check if the KV file has changed. Differently than using watchdog, this method is a simple reading-comparing method."""
        with open(file_path, "r") as f:
            compare = f.read()
            if compare != self.rendered:
                self.rendered = compare
                self.update(self.rendered)

    def update(self, *args):
        """Update the KV display widget when the TextInput changes."""
        self.root.remove_widget(self.kv_display)
        try:
            # Use textwrap.dedent on value to remove any indentation1
            self.kv_display = Builder.load_string(textwrap.dedent(self.rendered))
            self.root.add_widget(self.kv_display)
            self.kv_display.size_hint = (1, 1)

        except Exception as e:
            self.kv_display = MDLabel(
                text=str(e),
                size_hint=(None, None),
                width="250sp",
                pos_hint={"center_x": 0.5, "center_y": 0.5},
                theme_text_color="Custom",
                text_color="white",
                font_style="Body2",
            )
            self.root.add_widget(self.kv_display)


if __name__ == "__main__":
    try:
        KvApp(kvfile=file_path).run()
    except Exception as e:
        print(str(e))
        KvApp(kvfile=file_path).run()
