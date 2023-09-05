from src.animations.rotate_square import RotateSquareAnimation
from src.animations.samus_anim import SamusAnimation
from src.animations.spectrum import SpectrumAnimation
from src.animations.spectrum_square import SpectrumSquareAnimation

animations = [
    RotateSquareAnimation,
    SamusAnimation,
    SpectrumAnimation,
    SpectrumSquareAnimation
]

def loadAnimation(name):
    for animation in animations:
        if animation.name == name:
            return animation

    # if animation name not found
    return { 'loading_error': True, 'error_msg': 'animation name not found'}