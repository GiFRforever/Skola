import cv2
import numpy as np

# Load the user-selected frame from video 1
video1 = cv2.VideoCapture('video1.mp4')
frame_number = 100  # Adjust this to the frame you want to select
video1.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
ret, frame1 = video1.read()

# Load video 2
video2 = cv2.VideoCapture('video2.mp4')

# Define a function to calculate image similarity
def calculate_image_similarity(image1, image2):
    # Convert images to grayscale for comparison
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate structural similarity index (SSIM)
    ssim = cv2.SSIM(gray1, gray2)

    return ssim

# Loop through frames of video 2 and compare with the selected frame from video 1
while True:
    ret, frame2 = video2.read()
    if not ret:
        break

    similarity = calculate_image_similarity(frame1, frame2)
    print(f'Similarity between selected frame and current frame: {similarity}')

video1.release()
video2.release()
cv2.destroyAllWindows()
