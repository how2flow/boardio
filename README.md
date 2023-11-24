# boardio

The python scripts for testing gpio/alts of boards.

## Support

Use `Ctrl + F` to find your target is supported.

**controllers:**
```
.
|-- allwinner/
|   |-- D1
|   |-- a20
|   |-- a33
|   |-- a64
|   |-- h3
|   |-- h5
|   |-- h6
|   `-- h616
|-- am335x
|-- am65xx
|-- amlogic/
|   |-- a311d
|   |-- meson_g12_common
|   |-- s905
|   |-- s905x
|   |-- s905x3
|   |-- s905y2
|   `-- s922x
|-- atheros/
|   `-- ar9331
|-- bcm2711
|-- bcm2712
|-- bcm283x
|-- dra74x
|-- esp8266
|-- ftdi_mpsse/
|   |-- ft2232h
|   |-- ft232h
|   `-- mpsse
|-- hfu540
|-- mcp2221
|-- mips24kec
|-- mt8167
|-- nova
|-- nxp_imx6ull
|-- nxp_imx8m
|-- nxp_lpc4330
|-- pentium/
|   |-- j4105
|   `-- n3710
|-- rockchip/
|   |-- rk3308
|   |-- rk3328
|   |-- rk3399
|   |-- rk3566
|   |-- rk3568
|   |-- rk3568b2
|   `-- rk3588
|-- rp2040
|-- rp2040_u2if
|-- sama5
|-- samsung/
|   `-- exynos5422
|-- snapdragon/
|   `-- apq8016
|-- starfive/
|   |-- JH71x0
|-- stm32/
|   |-- stm32f405
|   `-- stm32mp157
`-- tegra/
    |-- t186
    |-- t194
    |-- t210
    `-- t234

```
<br>

**boards:**
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
