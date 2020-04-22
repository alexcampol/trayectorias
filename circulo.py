import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import sys

def pose_callback(pose):
	rospy.loginfo("Circulo X = %f : Y = %f : Z = %f\n",pose.x,pose.y,pose.theta)


def move_circle(linvel,angvel):

    rospy.init_node('move_circle', anonymous = False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size = 10)

    rospy.Subscriber('/turtle1/pose',Pose, pose_callback)

    rate = rospy.Rate(10)

    vel = Twist()
    while not rospy.is_shutdown():

	vel.linear.x = linvel
	vel.linear.y = 0
	vel.linear.z = 0

	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = angvel

        rospy.loginfo("LinearVel = %f: AngularVel = %f",linvel,angvel)
        pub.publish(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_circle(float(sys.argv[1]),float(sys.argv[2]))
    except rospy.ROSInterruptException:
        pass
