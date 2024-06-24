import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    output = DeclareLaunchArgument(
        "output",
        default_value='log')

    publish_clock = DeclareLaunchArgument(
        "publish_clock",
        default_value='False')
    
    isENU_ = DeclareLaunchArgument(
        "isENU_",
        default_value='False')

    is_vulkan = DeclareLaunchArgument(
        "is_vulkan",
        default_value='True')

    host = DeclareLaunchArgument(
        "host",
        default_value='localhost')
  
    airsim_node = Node(
            package='airsim_ros_pkgs',
            executable='airsim_node',
            name='airsim_node',
            output='screen',
            remappings=[
            #    ("/airsim_node/drone_1/bottom_center_custom/Scene", "/camera"),  #uncomment for mono
            #     ("/airsim_node/drone_1/front_left_custom/Scene","/camera/left"),
            #     ("/airsim_node/drone_1/front_right_custom/Scene","/camera/right"),  # Remap original_topic to new_topic
            #     ("/airsim_node/drone_1/imu/Imu","/imu")
                ("/airsim_node/drone_1/bottom_center_custom/Scene","/camera/rgb/image_rect_color"),
                ("/airsim_node/drone_1/bottom_center_custom/Scene/camera_info","/camera/rgb/camera_info"),  # Remap original_topic to new_topic
                ("/airsim_node/drone_1/bottom_center_depth_custom/DepthPerspective","/camera/depth_registered/image_raw")
                # ("/airsim_node/drone_1/lidar/lidar_1","/scan_cloud")
                # ("/airsim_node/drone_1/odom_local_ned","/odom")
            ],
            parameters=[{
                'is_vulkan': False,
                'update_airsim_img_response_every_n_sec': 0.05,
                'update_airsim_control_every_n_sec': 0.01,
                'update_lidar_every_n_sec': 0.01,
                'publish_clock': LaunchConfiguration('publish_clock'),
                'isENU_': LaunchConfiguration('isENU_'),
                'host_ip': LaunchConfiguration('host')
            }])

    static_transforms = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('airsim_ros_pkgs'), 'launch/static_transforms.launch.py')
        )
    )

    # Create the launch description and populate
    ld = LaunchDescription()

    # Declare the launch options
    ld.add_action(output)
    ld.add_action(publish_clock)
    ld.add_action(isENU_)
    ld.add_action(is_vulkan)
    ld.add_action(host)
  
    ld.add_action(static_transforms)
    ld.add_action(airsim_node)

    return ld
