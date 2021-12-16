holiday-star

![](https://raw.githubusercontent.com/iayanpahwa/holiday-star/master/assets/iot-star.jpg)

[balena](https://balena.io) ❤️ [adafruitIO](io.adafruit.com) 
## Introduction

A DiY holiday project to demonstrate how you can send data from adafruitIO cloud to a balena edge device 
## Hardware required

- A Raspberry Pi computer 
- 16GB Micro-SD Card (recommended Sandisk Extreme Pro SD cards)
- WS82xx based LED strip, also known as Neopixels connected to DMA enabled pin board.D18 on RPi
- Micro-USB cable
- Power supply(s)

```Danger Note: Powering LED strip directly from the GPIO of Pi can damage the board, refer to [this](https://learn.adafruit.com/neopixels-on-raspberry-pi) guide by adafruit on how to correctly power the neopixel strip and make it with with Raspberry Pi .```

## Software required

- balenaCloud account (free)
- adafruitIO account (free)
- balenaEtcher (optional)(free) - to flash the SD card with balenaOS
- balenaCLI (optional)(free) - if using balena push to deploy the fleet
## Deploy a fleet

You can deploy this app to a new balenaCloud fleet in one click using the button below:
[![](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/iayanpahwa/holiday-star.git)

Or, you can create a fleet in your balenaCloud dashboard and `balena push` this code to it, the traditional way.

#### Configuring LED strip and adafruitIO cloud credentials 

The following [Device Configuration](https://www.balena.io/docs/learn/manage/configuration/#configuration-variables) variables are required, these can be set at balenaCloud dashboard :


| Name                                  | Value                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| NUM_PIXELS                            | total number of LEDs in the strip (default 60)                                            |
| BRIGHTNESS                            | between 0 and 1 (default 0.3)                                                             |
| ADAFRUIT_IO_KEY                       | Obtain from adafruitIO account                                                            |
| ADAFRUIT_IO_USERNAME                  | username of your adafruitIO account                                                       |
| FEED_ID                               | name of the feed you created on adafruitIO                                                |
