#!/usr/bin/env python

import rospy
from sensor_msgs.msg import NavSatFix
import math

def hexagon_vertices(center, radius):
    cx, cy = center
    vertices = []
    radius = radius * 0.000001  # convert meters to lat and long
    for i in range(6):
        angle_deg = 60 * i
        angle_rad = math.radians(angle_deg)
        x = cx + radius * math.cos(angle_rad)
        y = cy + radius * math.sin(angle_rad)
        vertices.append((x, y))
    return vertices

def publish_hexagon_vertices():
    rospy.init_node('hexagon_publisher', anonymous=True)
    pub = rospy.Publisher('/hex', NavSatFix, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    center = (0, 0)
    radius = 10
    vertices = hexagon_vertices(center, radius)

    rospy.loginfo("Waiting for subscribers to connect...")
    while pub.get_num_connections() == 0:
        rospy.loginfo("No subscribers yet. Waiting...")
        rospy.sleep(1)

    rospy.loginfo("Subscribers connected. Starting to publish hexagon vertices.")

    for vertex in vertices:
        navsatfix_msg = NavSatFix()
        navsatfix_msg.latitude = vertex[0]
        navsatfix_msg.longitude = vertex[1]
        navsatfix_msg.altitude = 0  # Assuming 0 altitude for simplicity
        navsatfix_msg.header.stamp = rospy.Time.now()
        navsatfix_msg.header.frame_id = "hexagon_frame"
        rospy.loginfo(f"Publishing vertex: lat={vertex[0]}, lon={vertex[1]}")
        pub.publish(navsatfix_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_hexagon_vertices()
    except rospy.ROSInterruptException:
        pass
