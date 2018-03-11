# doorbell-detection

Use [Snowboy Hotword Detection](https://github.com/Kitt-AI/snowboy) to detect doorbell rings

## Quick Start Guide & Cheat Sheet

Instructions to setup everything on MacOS and Raspberry Pi 3+

### Dependencies
To run the program you will likely need the following:

* SoX (audio conversion)
* PortAudio or PyAudio (audio capturing)
* SWIG 3.0.10 or above (compiling Snowboy for different languages/platforms)
* ATLAS or OpenBLAS (matrix computation)

#### Mac OS X

`brew` install `swig`, `sox`, `portaudio` and its Python binding `pyaudio`:

    brew install swig portaudio sox
    pip install pyaudio

If you don't have Homebrew installed, please download it [here](http://brew.sh/). If you don't have `pip`, you can install it [here](https://pip.pypa.io/en/stable/installing/).

Make sure that you can record audio with your microphone:

    rec t.wav

#### Ubuntu/Raspberry Pi

First `apt-get` install `swig`, `sox`, `portaudio` and its Python binding `pyaudio`:

    sudo apt-get install swig3.0 python-pyaudio python3-pyaudio sox
    pip install pyaudio

Then install the `atlas` matrix computing library:

    sudo apt-get install libatlas-base-dev

Make sure that you can record audio with your microphone:

    rec t.wav

If you need extra setup on your audio (especially on a Raspberry Pi), please see the [full documentation](http://docs.kitt.ai/snowboy).

### Precompiled Binaries
* 64 bit Ubuntu [14.04](https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/ubuntu1404-x86_64-1.3.0.tar.bz2)
* [MacOS X](https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/osx-x86_64-1.3.0.tar.bz2)
* Raspberry Pi with Raspbian 8.0, all versions
  ([1/2/3/Zero](https://s3-us-west-2.amazonaws.com/snowboy/snowboy-releases/rpi-arm-raspbian-8.0-1.3.0.tar.bz2))