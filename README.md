# pxl-master

This repo is for our open source Python/Javascript project that allows users
to manipulate an LED reader board wirelessly using a Raspberry Pi 2 Model B
or greater, the Adafruit RGB Matrix HAT + RTC for Raspberry Pi - Mini Kit, 
including a pair of matrixed 32x64 LED boards creating a 32x128 LED matrix.

## Description

The result of this project is a programmable color LED reader board that
users can access and interact with through a website. The user interface 
allows reader board control. On the back-end, we store users and those 
users can log in and manipulate their "boards" content, selecting API 
endpoints from a pool we've provided access to. Those endpoints are then
hit and that status is sent the reader board for display. The info is not
updated on any frequency after initial call.

## Hardware

1 - Raspberry Pi 2 Model B

1 - Adafruit LED Reader Board Kit
https://www.adafruit.com/product/2345

1 - Set of Matrixed LED Boards (Pinball DMD)
https://squareup.com/store/fast-pinball-llc/item/rgb-dmd-panel-mounting-bracket-kit


## Setup

**Warning**
The following steps are here broadly and there are many steps and 
requirements that are built into the following steps that need to be 
considered for success. 

Begin by setting up an AWS EC2 and RDS instance and deploying an instance 
of our site to that instance.

(See amazon for details)
https://aws.amazon.com/ec2/
https://aws.amazon.com/rds/


Create an AWS IAM user for your app
http://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html


Install the AWS CLI
http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
https://docs.aws.amazon.com/iot/latest/developerguide/installing-aws-cli.html


Next, following the directions provided by the folks at Adafruit, assemble
and power up your Adafruit RGB Matrix HAT, attaching it to your Raspberry Pi.

Learn more:
https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi/assembly


Following this you'll want to add your Raspberry Pi as a member of the
Internet of Things (IoT) so your AWS instance knows about it.

Using your AWS account go to IoT and create a "thing" then download 
your certs and keys for that thing saving them in a certs folder.

Learn more:
https://aws.amazon.com/iot/
http://docs.aws.amazon.com/iot/latest/developerguide/iot-device-sdk-c.html#iot-c-sdk-prereqs


Running a command on the Pi will start the Pi listening for responses.

Example command:
node amazon-echo.js --thing-name ThingName -f ~/certs_folder


You can also send commands to your device using Boto3.
https://boto3.readthedocs.io/en/latest/reference/services/iot-data.html#client




