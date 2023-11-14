#!/bin/bash

set -e

bash .rules | sudo tee /etc/udev/rules.d/60-boardio.rules > /dev/null 2>&1
