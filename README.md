# MediaFlash

MediaFlash is a [Conky](https://github.com/brndnmtthws/conky) widget that displays metadata from media playing on an [MPRIS](https://specifications.freedesktop.org/mpris-spec/latest)-enabled media player using [Playerctl](https://github.com/altdesktop/playerctl) as a back-end. By default, it only displays when a specified player is actually playing content.

<img src="screenshot.png" width="45%" />

## Dependencies

* [Conky](https://github.com/brndnmtthws/conky)
* [Playerctl](https://github.com/altdesktop/playerctl)

## Install

1. Clone this repo
2. `cd media-flash`
3. `chmod +x ./install.py && ./install.py`
4. `conky -qc /INSTALL/PATH/MediaFlash/media-flash`