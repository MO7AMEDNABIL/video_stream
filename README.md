Live Video Stream:

First we need to import cv2.

The script captures frames from the default camera (index 0).
Displays the original video stream in a window titled 'Video.'
Interactive Controls:

Pressing 'h' toggles between displaying the video in the HSV color space.
Pressing 'g' toggles between displaying the video in grayscale.
Pressing 'o' toggles between showing the original video stream without additional scales.

Scaling:

Press 'h' for HSV color space.
Press 'g' for grayscale.
Press 'o' for the original video stream.


Frame Saving:

Pressing 's' saves the current frame.
The saved frame depends on the chosen scale: original, grayscale, or HSV.
Saved frames are stored as 'saved_frame.png' in the script's directory.
Dynamic Window Creation and Destruction:

Exit Condition:
Pressing 'q' exits the application.

