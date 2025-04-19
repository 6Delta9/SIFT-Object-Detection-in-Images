# SIFT Feature Extraction and Matching

## Overview

This project implements a feature extraction and matching task using the Scale-Invariant Feature Transform (SIFT) algorithm in OpenCV, as part of a computer vision lab assignment. The script detects an object from a query image in a complex target image and draws keypoints on the detected object, fulfilling the requirements of the main task (Section 2.1) from the SIFT assignment.

**Author**: Zeyad Mohamed Elsharkawy\
**Student ID**: 120210208

## Assignment Details

- **Objective**: Locate a single object from a query image (e.g., a book cover) in a target image (e.g., the book in a cluttered scene) using SIFT.
- **Output**: An image (`matched_output.jpg`) showing keypoints on the object in the target image, with lines connecting matches to the query image (resembling Figure 7 in the assignment).
- **Requirement**: Draw keypoints, not a rectangle, on the detected object.
- **Deadline**: April 20, 2025

## Files

- `Lab Assignment 2 - 120210208.py`: Python script implementing SIFT feature extraction and matching.
- `query.jpg`: Input image of a single object (e.g., a book cover).
- `target.jpg`: Input image of the same object in a complex scene.
- `matched_output.jpg`: Output image showing keypoints and matches.

## Requirements

- **Python**: 3.13
- **Libraries**:
  - OpenCV (`opencv-contrib-python` 4.11.0 or later, includes SIFT)
  - NumPy
- **Operating System**: Windows (script uses Windows file paths)

Install dependencies:

```bash
pip install opencv-contrib-python numpy
```

## Usage

1. **Prepare Input Images**:

   - Place `query.jpg` (single object, e.g., book cover) and `target.jpg` (object in a complex scene) in `C:\Users\<your-username>\Desktop\Lab Assignment 2\`.
   - Ensure images are textured for good SIFT keypoints (e.g., avoid plain objects).

2. **Update File Paths**:

   - Open `Lab Assignment 2 - 120210208.py`.
   - Replace `C:\\Users\\zizo\\Desktop\\Lab Assignment 2\\` with your username’s path (e.g., `C:\\Users\\your-username\\Desktop\\Lab Assignment 2\\`).

3. **Run the Script**:

   ```bash
   python "Lab Assignment 2 - 120210208.py"
   ```

   - The script loads `query.jpg` and `target.jpg`, performs SIFT feature matching, and saves `matched_output.jpg`.
   - A window displays the output (keypoints and matches).

4. **Check Output**:

   - Open `matched_output.jpg` in `C:\Users\<your-username>\Desktop\Lab Assignment 2\`.
   - Verify keypoints are on the correct object in the target image.

## Notes

- The script uses absolute paths for Windows. Update paths if running on another system or directory.
- If matches are poor, use images with more texture or increase matches in the script (e.g., change `matches[:50]` to `matches[:100]`).
- This script fulfills the main task (Section 2.1). The bonus task (video processing) is not included.

## Deliverables

- `Lab Assignment 2 - 120210208.py`
- `matched_output.jpg`
- Optional: `query.jpg`, `target.jpg` (if required by instructor)