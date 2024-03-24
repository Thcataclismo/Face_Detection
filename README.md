# Face Detection Project

This project demonstrates real-time face detection using OpenCV.

## Features

- Captures video from a webcam.
- Detects faces in each frame using a Haar cascade classifier.
- Draws rectangles around the detected faces.
- Displays the live video output with detected faces.
- Provides instructions for installation and running.

## Installation

### Install OpenCV

Follow the official installation instructions for your operating system from [OpenCV website](https://opencv.org/).

### Download Haar Cascade Classifier

Download the `haarcascade_frontalface_default.xml` file from the [OpenCV GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades) and place it in a folder named `data` within the project directory.

## Running the Code

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Execute the script using Python:
    ```bash
    python face_detection.py
    ```

Use the code with caution.

## Usage

- A window titled "FaceDetect" will open, displaying the live webcam feed.
- Rectangles will be drawn around detected faces.
- Press "Q" or "Esc" to quit the program.

## Additional Notes

- Ensure you have a webcam connected and working properly.
- If you encounter errors, check OpenCV installation and file paths.
- Experiment with different Haar cascade classifiers for different types of object detection.

## Enhancements

- Multiple Face Tracking: Track individual faces across frames for more engaging interactions.
- Face Recognition: Identify specific individuals using trained face recognition models.
- Performance Optimization: Explore techniques to improve detection speed and accuracy.
- User Interface: Create a graphical interface for easier control and configuration.

## License

This project is licensed under the MIT License.

## Acknowledgments

- OpenCV team for their amazing library and resources.
- The contributors and maintainers of the Haar cascade classifiers.
