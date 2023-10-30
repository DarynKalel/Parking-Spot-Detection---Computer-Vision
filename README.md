# Parking Spot Status Detection using OpenCV

In this project a developed a Python program for detecting the status of parking spots in a video feed using OpenCV. The script processes a video file, identifies parking spots, and determines whether they are empty or occupied. It provides a visual representation of the parking spots and displays the count of available spots in real-time.

# Prerequisites
Before running the script, you have to install the following dependencies:

OpenCV: You can install it using pip install opencv-python.
NumPy: You can install it using pip install numpy.
Matplotlib: You can install it using pip install matplotlib.

# Usage

Prepare the following input files:

mask_1920_1080.png: This image file represents the parking lot's layout, highlighting parking spots.
parking_1920_1080_loop.mp4: This is the video file of the parking lot you want to analyze.
Edit the script to specify the correct file paths for mask and video_path:

mask = './mask_1920_1080.png'
video_path = './samples/parking_1920_1080_loop.mp4'

Run the script:
python parking_spot_detection.py

The script will process the video frame by frame and display the parking spots with colored rectangles indicating their status (green for empty and red for occupied). It also shows the count of available spots in the top left corner of the video window.

Press the 'q' key to exit the video display window.

# How it Works
The script starts by reading the provided mask image to identify parking spots in the layout.

It opens the video file and processes each frame.

At specified intervals (controlled by the step variable), it calculates the difference between the current frame and the previous frame for each parking spot. This difference helps determine whether a spot has changed its status.

The script then identifies parking spots with significant status changes and updates their status as "empty" or "occupied" based on image analysis.

The updated status of each parking spot is displayed on the video frame as colored rectangles.

The count of available parking spots is displayed at the top of the video frame in real-time.

# Output
The script provides a real-time visualization of parking spot statuses and the count of available spots in the video feed.

# Customization
You can adjust the step variable to control how frequently the script checks for status changes. A smaller step means more frequent updates, while a larger step reduces the update rate.

You can modify the threshold value in the empty_or_not function to fine-tune the detection of empty and occupied spots based on your specific dataset.

You can further customize the visualization, such as changing the colors of the rectangles and the text displayed on the video frame.






