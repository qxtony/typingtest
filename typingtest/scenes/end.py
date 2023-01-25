from typingtest.config import TIMER_COLOR
from typingtest.gui import Text
from typingtest.resources import statistic
from typingtest.scenes.base import Scene


class EndScene(Scene):
    def __init__(self) -> None:
        super().__init__(font_size=30)

        self.texts = [
            Text(
                self.font,
                f"Скорость печати: {statistic.words_per_minute} слов в минуту",
                center=True,
                indent_y=-50,
                color=TIMER_COLOR,
            ),
            Text(
                self.font,
                f"Аккуратность: {statistic.accuracy}%",
                center=True,
                color=TIMER_COLOR,
            ),
            Text(
                self.font,
                f"Всего: {statistic.all_typed} символов",
                center=True,
                indent_y=50,
                color=TIMER_COLOR,
            ),
            Text(
                self.font,
                f"Допущено ошибок: {statistic.wrongly_typed} символов",
                center=True,
                indent_y=100,
                color=TIMER_COLOR,
            ),
        ]

        for text in self.texts:
            self.add_element(text)

    def on_key_press(self, _: int) -> None:
        pass
