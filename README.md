# spectra
Generate colour palettes from video files using `opencv | ffmpeg, numpy & pillow`

![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_1000steps.png "spectral 1000 samples")

#### OVERVIEW
This script creates a palette that shows colour trends along the duration of a video.

It currently uses a bicubic interpolation to find the average colour of each frame grab by simply scaling the frame down to a single pixel. This approach seems to be efficient but does not truly represent dominant colours in each frame. A new cluster-sampling method (K-Means Color Clustering) will have to be implemented to achieve more vivid and accurate results.

This script is inspired by [visible light spectroscopy](https://en.wikipedia.org/wiki/Spectroscopy "Spectroscopy") and [emission spectrums](https://en.wikipedia.org/wiki/Emission_spectrum "Emission spectrum").

#### EXAMPLE
##### Big Buck Bunny - 320x180 - 00:09:56
Below are output images at various sample settings - in the first example a sample of 50 frames are grabbed from the video generating a lower detail colour palette. As the samples increase, colour trends become more apparent. 500 samples seem to be a generous enough amount to get a well defined cross section of colour data from the video file while still remaining quite quick to process.

| 50 Steps | 250 Steps | 500 Steps | 1000 Steps |
| --- | --- | --- | --- |
| ![alt text](https://github.com/m-spangenberg/spectral/blob/master/examples/spectral_bigbuckbunny_50steps.png "spectral 50 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/examples/spectral_bigbuckbunny_250steps.png "spectral 250 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/examples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/examples/spectral_bigbuckbunny_1000steps.png "spectral 1000 samples") |

#### SAMPLE SPECTRA
All sample images are generated at 500 steps.

| Title | Resolution | Duration | Output | Output |
| --- | --- | --- | --- | --- |
| Big Buck Bunny | 320x180 | 00:09:56 | 002.91S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/examples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") |
| Akira (1988) | 848x480 | 02:04:52 | 162.28S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_akira_500steps.png "spectral 500 samples")
| Blade Runner (1982) | 1280x528 | 01:58:52 | 233.74S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bladerunner_500steps.png "spectral 500 samples") |
| Ghost In The Shell (1995) | 1280x694 | 01:23:30 | 208.18S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_ghostintheshell_500steps.png "spectral 500 samples") |

#### TODO
+ test alternative averaging or cluster-sampling methods
+ reduce disk I/O with caching
+ speed up with threading [?]
+ build simple GUI

#### RUN SPECTRA
Before starting make sure you have python3, python3-venv, pip3 and ffmpeg installed.

Clone this repo:
```
git clone https://github.com/m-spangenberg/spectra.git && cd ./spectra
```
Set up a virtual environment:
```
python3 -m venv . && source bin/activate
```
Make sure the dependencies are met:
```
pip3 install -r requirements.txt
```
Place a video file in the cloned folder and run spectra:
```
python3 spectra.py
```

#### NOTICE
This is my first Python project and GitHub repository.
Please inspect any code before running it.
