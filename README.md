# boardio

The python scripts for testing gpio/alts of boards.

## Support
```
.
|-- bananapi/
|   |-- bpim2plus
|   |-- bpim2zero
|   `-- bpim5
|-- beagleboard/
|   |-- beaglebone_ai
|   |-- beaglebone_black
|   |-- beaglebone_blue
|   |-- beaglebone_pocketbeagle
|   `-- beaglev_starlight
|-- binho_nova
|-- clockworkcpi3
|-- coral_dev_board
|-- coral_dev_board_mini
|-- dragonboard_410c
|-- feather_can_u2if
|-- feather_epd_u2if
|-- feather_huzzah
|-- feather_rfm_u2if
|-- feather_u2if
|-- ftdi_ft2232h
|-- ftdi_ft232h
|-- generic_linux_pc
|-- giantboard
|-- greatfet_one
|-- hardkernel/
|   |-- odroidc2
|   |-- odroidc4
|   |-- odroidm1
|   |-- odroidm1s
|   |-- odroidn2
|   `-- odroidxu4
|-- hifive_unleashed
|-- itsybitsy_u2if
|-- kb2040_u2if
|-- khadas/
|   `-- khadasvim3
|-- lemaker/
|   `-- bananapro
|-- librecomputer/
|   |-- aml_s905x_cc_v1
|   `-- roc_rk3328_cc
|-- lichee_rv
|-- linksprite/
|   |-- pcduino2
|   `-- pcduino3
|-- list
|-- lubancat/
|   |-- lubancat1
|   |-- lubancat2
|   |-- lubancat4
|   |-- lubancat_imx6ull
|   |-- lubancat_stm32mp157
|   `-- lubancat_zero
|-- macropad_u2if
|-- microchip_mcp2221
|-- nanopi/
|   |-- duo2
|   |-- neo
|   `-- neoair
|-- nodemcu
|-- nvidia/
|   |-- clara_agx_xavier
|   |-- jetson_nano
|   |-- jetson_nx
|   |-- jetson_orin
|   |-- jetson_orin_nx
|   |-- jetson_tx1
|   |-- jetson_tx2
|   |-- jetson_tx2_nx
|   `-- jetson_xavier
|-- onion/
|   `-- omega2
|-- orangepi/
|   |-- orangepi3
|   |-- orangepi4
|   |-- orangepi5
|   |-- orangepipc
|   |-- orangepir1
|   |-- orangepizero
|   |-- orangepizero2
|   |-- orangepizeroplus
|   `-- orangepizeroplus2h5
|-- pico_u2if
|-- pine64
|-- pineH64
|-- qt2040_trinkey_u2if
|-- q_u2if
|-- radxa/
|   |-- radxacm3
|   |-- radxazero
|   |-- rock5
|   |-- rockpi3a
|   |-- rockpi4
|   |-- rockpie
|   `-- rockpis
|-- raspberrypi/
|   |-- pico
|   |-- raspi_1b_rev1
|   |-- raspi_1b_rev2
|   |-- raspi_40pin
|   |-- raspi_4b
|   |-- raspi_5b
|   `-- raspi_cm
|-- siemens/
|   `-- siemens_iot2050
|-- soPine
|-- stm32/
|   |-- osd32mp1_brk
|   |-- osd32mp1_red
|   `-- stm32mp157c_dk2
|-- tritium-h3
|-- udoo_x86ultra
`-- x86j41x5
```


### requirements
```
python3 (>= 3.7)
python3-dev
```

### setup
```
$ ./setup.sh
$ udevadm trigger
$ python3 -m pip install -r requirements.txt
```

##### contact

e-mail: <steve@how2flow.net>
