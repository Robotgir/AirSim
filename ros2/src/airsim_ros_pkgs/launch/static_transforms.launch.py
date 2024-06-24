from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    ld = LaunchDescription()

    # Static transform from "odom" to "laser" frames
    node1 = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="ned_to_enu_pub",
        output="screen",
        arguments=['0', '0', '0', '1.57', '0', '3.14', 'world_ned', 'world_enu']
    )

    # Static transform from "world_ned" to "map" frames
    node2 = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="world_enu_to_map",
        output="screen",
        arguments=["0", "0", "0", "0", "0", "0", "world_ned" , "map"]
    )

    # Static transform from "world_ned" to "map" frames
    node3 = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="drone_1_to_bottom_center_custom_optical",
        output="screen",
        arguments=["0", "0", "0", "0", "0", "0", "drone_1", "drone_1/odom_local_ned" ]
    )

    # # Static transform from "world_ned" to "map" frames
    # node4 = Node(
    #     package="tf2_ros",
    #     executable="static_transform_publisher",
    #     name="drone_1_to_bottom_center_custom_optical",
    #     output="screen",
    #     arguments=["0", "0", "0", "0", "0", "0", "drone_1", "drone_1/bottom_center_depth_custom_optical/static" ]
    # )

    # # Static transform from "world_ned" to "map" frames
    # node4 = Node(
    #     package="tf2_ros",
    #     executable="static_transform_publisher",
    #     name="drone_1_odom_local_ned_to_front_center_depth_custom_optical_static",
    #     output="screen",
    #     arguments=["0", "0", "0", "1.57", "0", "0", "drone_1/odom_local_ned", "drone_1/front_center_depth_custom_optical/static"]
    # )
    # # Static transform from "world_ned" to "map" frames
    # node4 = Node(
    #     package="tf2_ros",
    #     executable="static_transform_publisher",
    #     name="",
    #     output="screen",
    #     arguments=["0", "0", "0", "1.57", "0", "0", "drone_1/odom_local_ned", "rtabmap/odom"]
    # )

    ld.add_action(node1)
    ld.add_action(node2)
    ld.add_action(node3)
    # ld.add_action(node4)




    return ld
