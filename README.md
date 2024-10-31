# Jupiter2 Robot Hand Control Using Computer Vision  
_Final Year Project by Muhammad Tareq Adam, supervised by Dr. Zati_

## Project Overview
This project is developed for **Jupiter2**, an open, ROS-based, integrated AI application development platform by LattePanda, running on Linux (Ubuntu). Jupiter2 is built for practical service robot development and includes AI application modules that enhance robot functionality and control. By leveraging OpenCV and Mediapipe hand-tracking, this project allows the manipulation of the Jupiter2 robot's arm and gripper through hand gestures instead of relying on the MoveIt! application.

## Objective
The aim of this project is to explore direct, vision-based control of the Jupiter2 robot’s arm and gripper using hand detection, eliminating the need for GUI-based control interfaces like MoveIt!. This involves tracking hand positions and using them to control multiple robot arm joints while adjusting the gripper position based on the relative distance between the user’s index fingertip and thumb tip.

## Project Features
- **Autonomous Object Picking**: The gripper was able to pickup an object autonomously.
- **ROS Integration**: Uses ROS publishers to command joint positions for responsive control.
- **Alternative Control Method**: Demonstrates the potential of direct hand control over the gripper, avoiding MoveIt! for simpler interaction.
  
## Technologies Used
- **ROS (Robot Operating System)**: Communicates with the Jupiter2 robot's arm joints and gripper.
- **Python and OpenCV**: Handles video capture and image processing for hand detection.
- **Mediapipe**: Performs real-time hand landmark tracking.
  
## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Jupiter2-Hand-Control.git
   cd Jupiter2-Hand-Control
   ```
2. Install the necessary packages:
   ```bash
   pip install opencv-python mediapipe rospy
   ```
3. Run the script to begin hand-based control of the robot:
   ```bash
   python hand_robot_control.py
   ```

## Usage
The control script captures the user's hand via a webcam. The wrist coordinates control `arm1` to `arm4`, while the distance between the thumb tip and index fingertip adjusts the gripper. Press `q` to exit the program at any time.

## Future Enhancements
- [x] **Override the MoveIt App**: Find a way to use python scripts directly to bypass the use of the MoveIt app
- [ ] **Smooth Movement**: Refine hand position tracking to reduce any jerky movement in the robot's response.
- [ ] **Computer Vision Integration**: Further develop CV-based object recognition and grasp planning.
- [ ] **Camera Integration**: Utilize external or built-in camera feeds to enhance tracking and visualization.
- [ ] **Interface Design**: Develop a GUI for more flexible robot control.
- [ ] **Inverse Kinematics**: Implement IK for more accurate and natural arm movements.

## Acknowledgments
This project is supervised by **Dr. Zati** and developed as part of my final year project at the University. Special thanks to the **Makerspace@UM** and the LattePanda team for their platform and support.
