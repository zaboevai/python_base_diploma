# -*- coding: utf-8 -*-

# pip install astrobox

from astrobox.space_field import SpaceField
from zaboev import RedWings

if __name__ == '__main__':
    scene = SpaceField(
        speed=5,
    )

    for drone in range(5):
        d = RedWings()

    scene.go()
