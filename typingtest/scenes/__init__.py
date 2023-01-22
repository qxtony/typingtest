from typing import List

from typingtest.scenes.base import Scene

from typingtest.scenes.start import StartScene
from typingtest.scenes.type_text import TypeText

scenes: List[Scene] = [StartScene(), TypeText()]


def switch_scenes(scene: Scene) -> Scene:
    return scenes[scenes.index(scene) + 1]
