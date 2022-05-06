from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer


class MainApp(MDApp):
    title = "Simple Video"

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"

        player = VideoPlayer(source="PythonPyQT5XOXGame.mp4")

        player.state = 'stop'

        return player


MainApp().run()