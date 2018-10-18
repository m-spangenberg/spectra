# spectra

#### OVERVIEW
This script attempts to visually 'fingerprint' a video file's colour palette by creating a spectrum composed of the average colours present over a given video file's playback duration. 

It currently uses a very 'hacky' bicubic interpolation approach for finding the average frame colour by simply scaling the frame down to a single pixel. This is computationally efficient but does not truly represent dominant colours and a new cluster-sampling method (K-Means Color Clustering) will have to be implemented to achieve vivid and accurate results.

This script is inspired by [visible light spectroscopy](https://en.wikipedia.org/wiki/Spectroscopy "Spectroscopy") and [emission spectrums](https://en.wikipedia.org/wiki/Emission_spectrum "Emission spectrum").

#### EXAMPLE
##### Big Buck Bunny - 320x180 - 00:09:56
Below are output images at various sample settings. 500 steps seem to be the most pleasing to look at while 50 steps is drastically under-sampled.

| 50 Steps | 250 Steps | 500 Steps | 1000 Steps |
| --- | --- | --- | --- |
| ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_50steps.png "spectral 50 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_250steps.png "spectral 250 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_1000steps.png "spectral 1000 samples") |

#### SAMPLES
All sample images are generated at 500 steps.

| Title | Resolution | Duration | Output | Output |
| --- | --- | --- | --- | --- |
| Big Buck Bunny | 320x180 | 00:09:56 | 002.91S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") |
| Akira (1988) | 848x480 | 02:04:52 | 162.28S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_akira_500steps.png "spectral 500 samples")
| Blade Runner (1982) | 1280x528 | 01:58:52 | 233.74S | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bladerunner_500steps.png "spectral 500 samples") |

#### TODO
+ basic error handling
+ clean up code and refactor to make use of functions
+ test alternative averaging or cluster-sampling methods
+ reduce disk I/O with caching
+ speed up with threading [?]
+ build simple GUI

#### DEPENDENCIES
spectra is written in Python 3 and makes use of opencv, ffmpeg, numpy and pillow.

#### PLEASE NOTE
This script is a work in progress and I take no responsibility if it destroys or otherwise mangles your files.
