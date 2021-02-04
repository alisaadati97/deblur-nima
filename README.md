Finding blured objects in a picture with known background
=============
extracting frames from a video 
-------------
where you have a video file you can use video_to_frames.py to get all of the frames. the argument of the command should be the name of the video file in the same directory :
```bash
python video_to_frame.py shoe.mp4
```
in the same directory you will have all of the video frames numbered and you can choose the one which only is the background and then the one wich the blured object is in it.

finding the blured object 
-------------
You will have the blured output when you run this code and determine which video you used .
```bash
python bluerd-object.py shoe
```
this will subtract two image from eachother and find the non zero pixels.
