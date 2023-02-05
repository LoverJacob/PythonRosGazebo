cmake_minimum_required(VERSION 3.0.2)
project(package1)


set(OpenCV_DIR /mnt/wslg/distro/usr/lib/x86_64-linux-gnu/cmake/opencv4)
find_package(catkin REQUIRED COMPONENTS
  OpenCV
  rospy
  sensor_msgs
  std_msgs
  gazebo_ros
)

catkin_package(

)
catkin_install_python(PROGRAMS scripts/publisher_node.py scripts/subscriber_node.py scripts/open_subscriber.py scripts/open_publisher.py
 DESTINATION $(CATKIN_PACKAGE_BIN_DESTINATION)
)
find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(

  ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS}
)