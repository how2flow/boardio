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

gpio40pins = [GPIO((0, 3)),
              GPIO((0, 5)),
              GPIO((0, 7)), GPIO((0, 8)),
                            GPIO((0,10)),
              GPIO((0,11)), GPIO((0,12)),
              GPIO((0,13)),
              GPIO((0,15)), GPIO((0,16)),
                            GPIO((0,18)),
              GPIO((0,19)),
              GPIO((0,21)), GPIO((0,22)),
              GPIO((0,23)), GPIO((0,24)),
                            GPIO((0,26)),
              GPIO((0,27)), GPIO((0,28)),
              GPIO((0,29)),
              GPIO((0,31)), GPIO((0,32)),
              GPIO((0,33)),
              GPIO((0,35)), GPIO((0,36)),
                            GPIO((0,38))]

gpios = [digitalio.DigitalInOut(pin) for pin in gpio40pins]
for gpio in gpios:
    gpio.direction = digitalio.Direction.OUTPUT

while True:
    for gpio in gpios:
        gpio.value = True
        time.sleep(0.5)
        gpio.value = False
        time.sleep(0.5)
