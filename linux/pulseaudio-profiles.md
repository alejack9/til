# Audio Profiles in Pulseaudio

The file `/usr/share/pulseaudio/alsa-mixer/profile-sets/default.conf` contains all audio profiles for the current system named via mapping (e.g. `[Mapping analog-stereo]`).

To add a profile that groups multiple profile, simply  add a `Profile` section at the end of the file.

```
[Profile output:analog-stereo+output:hdmi-stereo]
description = Both PC and HDMI
output-mappings = analog-stereo hdmi-stereo
input-mappings = analog-stereo
```

Notice that `analog-stereo` also has input-mapping entry.

[Source](https://askubuntu.com/a/1000397)
