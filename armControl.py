#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64
import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen = pygame.display.set_mode((640, 480))

# ROS publishers for the robot arm joints
pub_arm1 = rospy.Publisher('/arm1_joint/command', Float64, queue_size=10)
pub_arm2 = rospy.Publisher('/arm2_joint/command', Float64, queue_size=10)
pub_arm3 = rospy.Publisher('/arm3_joint/command', Float64, queue_size=10)
pub_arm4 = rospy.Publisher('/arm4_joint/command', Float64, queue_size=10)
pub_gripper = rospy.Publisher('/gripper_joint/command', Float64, queue_size=10)

# Initialize ROS node
rospy.init_node('mouse_robot_control', anonymous=True)

# Function to scale mouse movements to joint values
def scale_value(value, min_input, max_input, min_output, max_output):
    return (float(value - min_input) / (max_input - min_input)) * (max_output - min_output) + min_output

# Initial joint positions
arm1_pos = 0.0
arm2_pos = 0.0
arm3_pos = 0.0
arm4_pos = 0.0
gripper_closed = False  # False means open, True means closed

# Main loop
running = True
while running and not rospy.is_shutdown():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Check if "Q" is pressed
                running = False
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle the gripper state when the mouse is clicked
            gripper_closed = not gripper_closed
            if gripper_closed:
                gripper_pos = 0.5  # Example value for closed gripper
            else:
                gripper_pos = 0.0  # Example value for open gripper
            pub_gripper.publish(Float64(gripper_pos))  # Publish the new gripper position

    # Get mouse position (scaled from screen coordinates to joint ranges)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Scale mouse_x and mouse_y to a reasonable range for robot joints
    arm1_pos = scale_value(mouse_x, 0, 640, -1.5, 1.5)  # Example range [-1.5, 1.5] radians
    arm2_pos = scale_value(mouse_y, 0, 480, -1.5, 1.5)
    arm3_pos = scale_value(mouse_x, 0, 640, -1.5, 1.5)
    arm4_pos = scale_value(mouse_y, 0, 480, -1.5, 1.5)

    # Publish scaled joint values
    pub_arm1.publish(Float64(arm1_pos))
    pub_arm2.publish(Float64(arm2_pos))
    pub_arm3.publish(Float64(arm3_pos))
    pub_arm4.publish(Float64(arm4_pos))

    # Update the screen
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # Add a small delay
    pygame.time.delay(50)

if __name__ == '__main__':
    try:
        # Run the main loop
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
