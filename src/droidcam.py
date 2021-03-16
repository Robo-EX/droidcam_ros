#!/usr/bin/env python
import sys
import cv2
import argparse
import roslib
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError


class RosNode:
    def __init__(self, url):
        rospy.init_node("droidcam_node")
        rospy.loginfo("Starting RosNode.")
        try:
            self.vcap = cv2.VideoCapture(url)
        except:
            rospy.logerr('Unable to open ip camera stream: ' + str(url))
            sys.exit()
        self.image_pub = rospy.Publisher(
            "/camera/image_raw", Image, queue_size=10)
        self.bridge = CvBridge()
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='droidcam.py', description='reads a given url string and dumps it to a ros_image topic')
    parser.add_argument('-g', '--gui', action='store_true',
                        help='show a GUI of the camera stream')
    parser.add_argument(
        '-u', '--url', default='http://192.168.0.101:4747/video', help='camera stream url to parse')
    args = parser.parse_args(rospy.myargv()[1:])

    print("Opening Camera")
    ip_camera = RosNode(args.url)
    print('Successfully opened ip camera')

    while not rospy.is_shutdown() and ip_camera.vcap.isOpened():
        ret, frame = ip_camera.vcap.read()
        if ret == False:
            print('Could not read frame')
            break

        img_msg = ip_camera.bridge.cv2_to_imgmsg(frame, "bgr8")
        img_msg.header.stamp = rospy.get_rostime()
        ip_camera.image_pub.publish(img_msg)

        if args.gui:
            cv2.imshow('Droid Camera', frame)
            if cv2.waitKey(1) == 27:
                break

    ip_camera.vcap.release()
    cv2.destroyAllWindows()
