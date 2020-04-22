import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def rotate_turtle(speed, angle):

     rospy.init_node('turtle_cleaner', anonymous=True)
     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
     vel_msg = Twist()
     speed_ang = speed * 2 * PI / 360
     rel_ang = angle * 2 * PI / 360
     vel_msg.angular.z = abs(speed_ang)
     t0 = rospy.Time.now().to_sec()
     current_ang = 0

     while(current_ang < rel_ang):
         velocity_publisher.publish(vel_msg)
         t1 = rospy.Time.now().to_sec()
         current_ang = speed_ang * (t1 - t0)

     vel_msg.angular.z = 0
     velocity_publisher.publish(vel_msg)

def move_square(speed, distance):
     rospy.init_node('turtle_cleaner', anonymous=True)
     velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)
     vel_msg = Twist()
     vel_msg.linear.x = abs(speed)
     t0 = rospy.Time.now().to_sec()
     current_dist = 0
     while(current_dist < distance):
         velocity_publisher.publish(vel_msg)
         t1 = rospy.Time.now().to_sec()
         current_dist = speed*(t1-t0)
     vel_msg.linear.x = 0
     velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
     try:
	 move_square(1,2)
	 rotate_turtle(30,90)
	 move_square(1,4)
	 rotate_turtle(30,90)
	 move_square(1,4)
	 rotate_turtle(30,90)
	 move_square(1,4)
	 rotate_turtle(30,90)
	 move_square(1,2)
     except rospy.ROSInterruptException:
         pass
