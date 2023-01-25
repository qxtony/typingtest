from typingtest.gui import Choicer, Text, get_random_words_from_complexity
from typingtest.resources import statistic
from typingtest.scenes.base import Scene


class ChoiceComplexity(Scene):
    def __init__(self) -> None:
        super().__init__(font_size=60)

        self.text = Text(
            self.font, "Выберите сложность", center=True, indent_y=-200
        )
        self.choicer = Choicer(
            self.font, ["Легко", "Средне", "Сложно"], center=True
        )

        self.add_element(self.text)
        self.add_element(self.choicer)

    def on_key_press(self, key: int) -> bool:
        complexity = self.choicer.on_key_press(key)

        if complexity is not None:
            statistic.words = get_random_words_from_complexity(complexity)
            return True

        return False
