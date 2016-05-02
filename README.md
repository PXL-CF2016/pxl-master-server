# pxl-master

This repo is for our open source Python/Javascript project that allows users
to manipulate an LED reader board wirelessly using a Raspberry Pi 2 Model B
or greater, the Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit, and matrixed
pair of LED boards creating a 32x128 LED matrix.

## Description

The result of this project is a programmable LED reader board that
users can access and interact with through a website and user interface
that allows full reader board control. On the back-end, users would have
accounts from which upon login, could manipulate the board and save
customized preferences for what they like to show on the reader.

## Hardware

1 - Raspberry Pi 2 Model B

1 - Adafruit LED Reader Board Kit
https://www.adafruit.com/product/2345

2 - Matrixed LED Boards / DMD
https://squareup.com/store/fast-pinball-llc/item/rgb-dmd-panel-mounting-bracket-kit


## Setup

Begin by setting up an AWS instance and deploying an instance of our site
to that instance.

(details to come)


Following this you'll want to add your Raspberry Pi as a member of the
Internet of Things (IoT) your AWS instance knows about.

Learn more:

http://docs.aws.amazon.com/iot/latest/developerguide/iot-device-sdk-c.html#iot-c-sdk-prereqs


Next, following the directions provided by the folks at Adafruit, assemble
and power up your Adafruit RGB Matrix HAT, attaching it to your Raspberry Pi.

Learn more:

https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly
