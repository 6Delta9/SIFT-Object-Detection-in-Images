#zeyad mohamed elsharkawy 120210208
import cv2
import numpy as np

# Load images with absolute paths
query_image = cv2.imread('C:\\Users\\zizo\\Desktop\\Lab Assignment 2\\query.jpg', cv2.IMREAD_GRAYSCALE)
target_image = cv2.imread('C:\\Users\\zizo\\Desktop\\Lab Assignment 2\\target.jpg', cv2.IMREAD_GRAYSCALE)

if query_image is None or target_image is None:
    print("Error: Could not load one or both images.")
    exit()

# Initialize SIFT
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(query_image, None)
kp2, des2 = sift.detectAndCompute(target_image, None)

if des1 is None or des2 is None:
    print("Error: No descriptors found in one or both images.")
    exit()

# Match keypoints
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
matches = bf.match(des1, des2)
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches
matched_image = cv2.drawMatches(
    query_image, kp1, 
    target_image, kp2, 
    matches[:50], 
    None, 
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Save and display
cv2.imwrite('C:\\Users\\zizo\\Desktop\\Lab Assignment 2\\matched_output.jpg', matched_image)
cv2.imshow('Matches', matched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()