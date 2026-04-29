#!/usr/bin/env python3
"""Extract yaw from IMU quaternion and publish as Float64."""

import math

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64


def quaternion_to_yaw(qx, qy, qz, qw):
    """Convert quaternion to yaw (Euler Z) in radians."""
    siny_cosp = 2.0 * (qw * qz + qx * qy)
    cosy_cosp = 1.0 - 2.0 * (qy * qy + qz * qz)
    return math.atan2(siny_cosp, cosy_cosp)


class ImuYawPublisher(Node):
    def __init__(self):
        super().__init__('imu_yaw_publisher')
        self._pub = self.create_publisher(Float64, 'imu/yaw', 10)
        self._sub = self.create_subscription(
            Imu,
            'imu/data',
            self._imu_callback,
            10
        )

    def _imu_callback(self, msg: Imu):
        q = msg.orientation
        yaw = quaternion_to_yaw(q.x, q.y, q.z, q.w)
        out = Float64()
        out.data = yaw
        self._pub.publish(out)


def main(args=None):
    rclpy.init(args=args)
    node = ImuYawPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
