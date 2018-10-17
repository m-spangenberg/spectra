# spectral
A python script to generate a time-based colour spectrum composed of frames sampled at predetermined intervals from a given video file.

#### OVERVIEW
The name spectral was inspired by [visible light spectroscopy](https://en.wikipedia.org/wiki/Spectroscopy "Spectroscopy") and [emission spectrums](https://en.wikipedia.org/wiki/Emission_spectrum "Emission spectrum"). This attempt to 'fingerprint' a video file's colour spectrum is part of my self-learning process in Python, it is mostly bashed together from trial and error and there is a lot of room for improvement!

#### EXAMPLE
##### Big Buck Bunny - 320x180 - 00:09:56
Below are output images at various sample settings. 500 steps seem to be the most pleasing to look at while 50 steps is drastically under-sampled. A new cluster-sampling method will have to be implemented to avoid muddy or overly dark results that come with the bicubic interpolation method used to find the averaged frame colour.

| 50 Steps | 250 Steps | 500 Steps | 1000 Steps |
| --- | --- | --- | --- |
| ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_50steps.png "spectral 50 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_250steps.png "spectral 250 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_1000steps.png "spectral 1000 samples") |

#### SAMPLES
All sample images are generated at 500 steps.

| Title | Resolution | Duration | Time | Output |
| --- | --- | --- | --- | --- |
| Big Buck Bunny | 320x180 | 00:09:56 | 00:04 | ![alt text](https://github.com/m-spangenberg/spectral/blob/master/samples/spectral_bigbuckbunny_500steps.png "spectral 500 samples") |

#### TODO
+ basic error handling
+ clean up code and refactor to make use of functions
+ test alternative averaging or cluster-sampling methods
+ reduce disk I/O with caching
+ speed up with threading [?]
+ build simple GUI

#### DEPENDENCIES
spectral is written in Python 3 and makes use of opencv, ffmpeg, numpy and pillow.

#### PLEASE NOTE
This script is a work in progress and I take no responsibility if it destroys or otherwise mangles your files.
