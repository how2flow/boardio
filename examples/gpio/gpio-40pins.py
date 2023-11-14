# SPDX-FileCopyrightText: 2023 Steve Jeong <steve@how2flow.net>
# SPDX-License-Identifier: MIT

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

def main():

  GPIO._CONSUMER = "boardio"

  gpios = [digitalio.DigitalInOut(pin) for pin in gpio40pins]
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
