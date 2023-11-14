# Copyright (C) 2023 Steve Jeong <steve@how2flow.net>
#  
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#  
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import time
import digitalio
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin as GPIO

'''
This script was written for hardware validation
before the board was ported to the Python package.

It needs to be modified to suit the target board.
gpio mapping is based on gpiod notations.

e.g.
GPIO((0, 0)) is gpiochip0/gpio0
'''

gpio40pins = [GPIO((3, 14)),
              GPIO((3, 13)),
              GPIO((0, 14)), GPIO((2, 4)),
                             GPIO((2, 3)),
              GPIO((0, 16)), GPIO((2, 7)),
              GPIO((0, 17)),
              GPIO((0, 18)), GPIO((2, 13)),
                             GPIO((2, 14)),
              GPIO((3, 17)),
              GPIO((3, 18)), GPIO((2, 8)),
              GPIO((3, 19)), GPIO((3, 1)),
                             GPIO((2, 9)),
              GPIO((0, 12)), GPIO((0, 11)),
              GPIO((2, 16)),
              GPIO((2, 15)), GPIO((2, 10)),
              GPIO((0, 13)),
              GPIO((2, 5)) , GPIO((2, 6))]

gpios = [digitalio.DigitalInOut(pin) for pin in gpio40pins]
for gpio in gpios:
    gpio.direction = digitalio.Direction.OUTPUT

while True:
    for gpio in gpios:
        gpio.value = True
        time.sleep(0.5)
        gpio.value = False
        time.sleep(0.5)
