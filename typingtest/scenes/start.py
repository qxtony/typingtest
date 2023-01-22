from typingtest.gui import Text
from typingtest.scenes.base import Scene


class StartScene(Scene):
    def __init__(self) -> None:
        super().__init__(font_size=60)
        self.add_element(Text(self.font, "Press any key to start", center=True))

    def on_key_press(self, _: int) -> bool:
        return True
