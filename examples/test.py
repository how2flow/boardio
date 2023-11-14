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
import board
import digitalio

gpio40pins = [board.D3,
              board.D5,
              board.D7,  board.D8,
                         board.D10,
              board.D11, board.D12,
              board.D13,
              board.D15, board.D16,
                         board.D18,
              board.D19,
              board.D21, board.D22,
              board.D23, board.D24,
                         board.D26,
              board.D27, board.D28,
              board.D29,
              board.D31, board.D32,
              board.D33,
              board.D35, board.D36]

gpios = [digitalio.DigitalInOut(pin) for pin in gpio40pins]
for gpio in gpios:
    gpio.direction = digitalio.Direction.OUTPUT

while True:
    for gpio in gpios:
        gpio.value = True
        time.sleep(0.5)
        gpio.value = False
        time.sleep(0.5)
