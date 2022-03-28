# Use MPV to play YT videos with resolution constraints

Currently, web browsers are having a hard time using hardware acceleration in Linux, so YT videos' playback often suffers from stuttering and lagging. MPV can be used to play YT videos making the most of hardware acceleration.

Using `--ytdl-format="format-string"` we can set resolution constraints on the video using [`youtube-dl` format](https://mpv.io/manual/stable/#options-ytdl-format).

```sh
mpv --ytdl-format="bestvideo[height<=?1080]+bestaudio/best" https://youtu.be/LXb3EKWsInQ
```

[Source](https://github.com/mpv-player/mpv/issues/4241)
