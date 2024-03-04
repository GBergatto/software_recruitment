import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

# Define the TemperatureLogger node
class TemperatureLogger():
    pass


def main(args=None):
    rclpy.init(args=args)

    logger = TemperatureLogger("log.txt")

    rclpy.spin(logger)

    logger.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
