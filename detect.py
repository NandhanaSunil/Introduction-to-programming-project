# Add OPEN-CV library to use images and camera features
import cv2

# Creating the class module that will be used in main file
class HomoBgDtector():
    def __init__(self):
        pass

    '''
    # Function used for detecting objects 
    # Uses open-cv capabilities to detect images
    '''
    def detect_objects(self, frame):


        # Convert Image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        """
        The code creates a mask by converting the image to grayscale. 
        Adaptive thresholding is then applied to the grayscale image. 
        This means that a threshold value is calculated based on the average brightness of the surrounding pixels. 
        The resulting image is binary, meaning that each pixel is either black or white. In this case, 
        the binary image is inverted, so white represents the areas of interest in the image.
        """
        mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)


        """
        This code finds the boundaries of connected regions in the binary image (mask) using a process called contour detection. 
        It only considers the outer boundaries (external contours) and approximates them with a simplified representation.
        """
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        # Uncomment the line below to display the mask
        objects_contours = []

        # Iterate over the detected contours
        for cnt in contours:
            # Calculate the area of the contour
            area = cv2.contourArea(cnt)
            if area > 2000:
                # Uncomment the line below to approximate the contour shape
                #cnt = cv2.approxPolyDP(cnt, 0.03 * cv2.arcLength(cnt, True), True)
                objects_contours.append(cnt)

        # Return the list of contours representing the detected objects
        return objects_contours
