import numpy as np
from . import PERIOD

def generate_wave(offset: float):
    """
    parameters:
        - offset: float, must be a float value between 0 and 1
    """
    range_seconds = [
        (2 * np.pi) * (x/PERIOD + -offset)
        for x in range(0, PERIOD, 1)
    ]
    wave = (np.sin(range_seconds) + 1) * 0.5
    return wave
