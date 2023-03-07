# Locksound - configuration for Raspberry Pi 4
## Audio configuration

### Create pulseaudio sinks

This command creates a virtual input/output audio device

`sudo modprobe snd-aloop`

Audio will then be send to input, and output will go to the **audio_processing** program

Input will be listed as device `0` and output as device `1`

To persist the configuration, add `snd_aloop` to `/etc/modules-load.d/snd-aloop.conf`



### Enable multi audio outputs (dont work with ncspot)

Pulseaudio configuration for two audio outputs

Here audio is routed to **hw:0,1** (goes to the LED display) and **hw:1,0** (goes to usb output)

Put the code below in **/etc/asound.conf** to persist the configuration
```
pcm.double_out plug:both

ctl.double_out {
  type hw
  card 0
}

pcm.both {
  type route;
  slave.pcm {
      type multi;
      slaves.a.pcm "hw:0,1";
      slaves.b.pcm "hw:1,0";
      slaves.a.channels 2;
      slaves.b.channels 2;
      bindings.0.slave a;
      bindings.0.channel 0;
      bindings.1.slave b;
      bindings.1.channel 1;

  }

  ttable.0.0 1;
  ttable.1.1 1;

}

ctl.both {
  type hw;
  card 0;
}
```

### Enable multi audio outputs (works with ncspot)
At the top of the `/etc/pulse/default.pa` file (before modules loading), add :
```
load-module module-alsa-sink device=<device_name>
load-module module-combine-sink sink_name=combine
set-default-sink combined
```
it adds a second audio device to pulseaudio default output
where `<device_name>` is the added device, (ex. `hw:0,1`)

### Set a default sink for Pulseaudio
`pactl set-default-sink <sink_name>`

### Set defalut volume for a sink
In `/etc/pulse/default.pa`, add this line :
`pactl set-sink-volume <sink_name> <volume>`

### Launch ncspot from ssh
`DISPLAY=:0 ncspot`


## Network configuration
### Restart wifi from ssh
`sudo ip link set wlan0 down && sudo ip link set wlan0 up`

### Connect to specific network
`sudo nmcli connection up id <network_name>`
