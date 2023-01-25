from typingtest.scenes.base import Scene
from typingtest.scenes.choice_complexity import ChoiceComplexity
from typingtest.scenes.end import EndScene
from typingtest.scenes.type_text import TypeText

scenes: list = [ChoiceComplexity, TypeText, EndScene]


def switch_scenes(scene: Scene) -> Scene:
    return scenes[scenes.index(scene) + 1]


def get_start_scene() -> Scene:
    return scenes[0]
