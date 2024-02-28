# SPDX-FileCopyrightText: 2024 Steve Jeong <steve@how2flow.net>
# SPDX-License-Identifier: MIT

def get_gpio_line():
  while True:
    try:
      bank, group, offset =\
        input("Input gpio info(bank group offset): ").split()

      bank, offset = map(int, (bank, offset))
      group = ord(group.upper()) - ord('A')

      if not (0 <= bank <= 4 and 0 <= group <= 3 and 0 <= offset <= 7):
        raise ValueError

      return (int(bank) * 32) + (group * 8) + int(offset)

    except ValueError:
      print("\nInvalid input. Please enter valid bank (0-4), group (A-D), and offset (0-7).")
      print("your input: bank({0}), group({1}), offset({2})\n"\
        .format(bank, chr(group + 65), offset))

    except KeyboardInterrupt:
      raise

  return None

def return_gpio_line(line):
  if line is not None:
    print("line: {}\n".format(line))

def main():
  print("This is the program that returns value of gpio line (For Rockchip)")
  print("Enter bank, group and offset of gpio separated by space.")
  print("")
  print("(e.g.)")
  print("If you want to know the gpio line of GPIO0_A0, ")
  print("Input gpio bank info(bank group offset): 0 A 0")
  print("")
  print("...")
  print("")

  try:
    while True:
      gpio_line = get_gpio_line()
      return_gpio_line(gpio_line)

  except KeyboardInterrupt:
    print("\nExit by keyboard interrupt.")

if __name__ == "__main__":
  main()
