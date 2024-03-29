# Audio Reactive LEDs
![Audio Reactive LEDs demo](./img/audio-reactive-leds.gif)

A python program to display audio reactive animations, on a Raspberry Pi equiped with an RGB LEDs matrix.
You can find instructions to build such a setup in [this tutorial from Adafruit](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi).

This program relies on Henner Zeller's [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) to interact with the LEDs matrix.
The LED-matrix library is (c) Henner Zeller [h.zeller@acm.org](h.zeller@acm.org), licensed with [GNU General Public License Version 2.0](http://www.gnu.org/licenses/gpl-2.0.txt)

## Installation
### Install the rgb-led-matrix python binding
On a Raspberry Pi equiped with an RGB LEDs Matrix, first clone the Henner Zeller's `rpi-rgb-led-matrix` reposistory : 

    git clone https://github.com/hzeller/rpi-rgb-led-matrix.git

Then follow theses instructions to install the rgb-led-matrix python binding : [rgb-led-matrix python binding install](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python)

### Install the audio-reactive-LEDs program
Clone the current repository on your Raspberry Pi :

    git clone git@github.com:nicolas415/audio-reactive-LEDs.git

### Install the necessary python librairies
You will also need `numpy` and `pyaudio` librairies to make this program work. 
Enter the following command on the Raspberry to install them for `python3` :

    python3 -m pip numpy pyaudio


## Configuration

Modify the configuration inside `./config.json` to match your setup :
* `animation_name` : the name of the animtion to display. You should create new animation class with a `name` property, and save them under `./src/animations/` (the app comes with a default spectrogram animation)
* `input_device_name`: the audio card triggering the animations. You can get a list of the available input devices by entering `arecord -l` on your Raspberry Pi terminal.
* `stream_data_chunks` the number of audio frames the signal is split into. Increasing the value increases the length of the array containing the audio signal representation
* `matrix_columns`: the number of columns of each matrix
* `matrix_rows`: the number of rows of each matrix
* `matrix_chain_length`: the number of matrix in the setup
* `matrix_brightness`: the brightness of the LEDs, goes from `0` to `100`
* `matrix_hardware_mapping`: the name of the electronic card interfacing with le LEDs matrix

## Launching the application
At the root of the audio-reactive-LEDs project, enter the following command :

    sudo ./start.py
