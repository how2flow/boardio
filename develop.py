# SPDX-FileCopyrightText: 2023 Steve Jeong <steve@how2flow.net>
# SPDX-License-Identifier: MIT

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

pinmap = [GPIO((0, 3)),
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

def main():

  GPIO._CONSUMER = "boardio"

  gpios = [digitalio.DigitalInOut(pin) for pin in pinmap]
  for gpio in gpios:
      gpio.direction = digitalio.Direction.OUTPUT

  try:
    while True:
        for gpio in gpios:
            gpio.value = True
            time.sleep(0.5)
            gpio.value = False
            time.sleep(0.5)

  except KeyboardInterrupt:
    print("\nExit by keyboard interrupt.")

if __name__ == "__main__":
  main()
