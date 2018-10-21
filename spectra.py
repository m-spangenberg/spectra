import os
import glob
import sys
import cv2
import time
import numpy as np
from PIL import Image

def main():

    class VideoInfo():
        """Generate information for a given video file"""
        def __init__(self, step_size):
            self.input_file = self.get_video()
            self.step_size = step_size
            self.video_file = cv2.VideoCapture(self.input_file)
            self.framecount = int(self.video_file.get(cv2.CAP_PROP_FRAME_COUNT))
            self.fps = int(self.video_file.get(cv2.CAP_PROP_FPS))
            self.width = int(self.video_file.get(cv2.CAP_PROP_FRAME_WIDTH))
            self.height = int(self.video_file.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.current_directory = os.getcwd()
            self.duration = self.playback_duration()

        def get_video(self):
            """find video file inside project folder"""
            filetypes = ['*.avi', '*.mkv', '*.mp4']
            
            for filetype in filetypes:
                for input_file in glob.glob(os.path.join(os.getcwd(), filetype)):
                    return input_file

        def playback_duration(self):
            """find the duration of playback in seconds"""
            try:
                duration = (self.framecount / self.fps)
                return duration
            except:
                print('> Video file not found, please add one.')
                quit()

        def generate_folders(self):
            """generate needed folders if they don't exist"""
            try:
                outut_folder = os.mkdir(os.path.join(self.current_directory, 'tmp'))
            except:
                print('> folders exist, moving on.')

        def calculate_frame_step(self):
            """get the gap in frames between each frame grab"""
            frame_step = self.framecount / self.step_size
            step_gap = round(frame_step)
            return step_gap

        def generate_frames(self):
            """generate frames from video file at step count"""
            count = 0
            generated_image_count = 0
            active = True

            while active:
                active,image = self.video_file.read()
                if count%self.calculate_frame_step()== 0 :
                     cv2.imwrite(os.path.join(self.current_directory,'tmp','frame%d.jpg'%count),image)
                     print('grabbing frame: ', generated_image_count)
                     generated_image_count+=1
                count+=1

        def generate_pixels(self):
            """scale the frames down to 1px using bicubic interpolation"""
            pixel = (1, 1)
            for infile in glob.glob(os.path.join(self.current_directory,'tmp','*.jpg')):
                im = Image.open(infile)
                im.thumbnail(pixel, Image.ANTIALIAS)
                im.save(infile)

        def generate_pixel_line(self):
            """generate a pixel line from available pixels"""
            image_list = map(Image.open, glob.glob(os.path.join(self.current_directory,'tmp','*.jpg')))
            imgs_comb = np.hstack(image_list)
            imgs_comb = Image.fromarray( imgs_comb)
            imgs_comb.save(os.path.join(self.current_directory,'tmp','spectra_tmp.png'))

        def generate_spectra(self):
            """scale pixel line to final dimensions"""
            final_dimensions = 2000, 600
            im = Image.open(os.path.join(self.current_directory,'tmp','spectra_tmp.png'))
            im_resized = im.resize(final_dimensions, Image.ANTIALIAS)
            im_resized.save("spectra_output.png")

        def housekeeping(self):
            """remove tmp directory"""
            try:
                for tmpimage in glob.glob(os.path.join(self.current_directory,'tmp', 'frame*.jpg')):
                    os.remove(tmpimage)
                for tmpimage in glob.glob(os.path.join(self.current_directory,'tmp', '*.png')):
                    os.remove(tmpimage)
                os.rmdir(os.path.join(self.current_directory,'tmp'))
            except:
                print('> The temporary directory or it\'s contents could not be removed')

        def printjob(self):
            """print job details to console"""
            output_time = time.time() - start_timer
            print(f'filename: {self.input_file} | resolution: {self.width}x{self.height} | duration: {self.duration:.2f} seconds | output: {output_time:.2f} seconds')


    # start timer
    start_timer = time.time()
        
    # set frame grab step size
    step_size = 500

    # initialize video file and get info
    video = VideoInfo(step_size)

    # call jobs
    video.get_video()
    video.generate_folders()
    video.generate_frames()
    video.generate_pixels()
    video.generate_pixel_line()
    video.generate_spectra()
    video.housekeeping()
    video.printjob()
    
if __name__ == "__main__":
    main()
