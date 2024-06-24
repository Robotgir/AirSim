# Use the specified ROS2 Foxy image
FROM althack/ros2:foxy-cuda-full

# Install necessary dependencies
RUN sudo apt-get update \
    sudo apt-get upgrade \
    sudo apt-get install gcc-8 g++-8 \
    sudo apt-get install ros-${ROS_DISTRO}-tf2-sensor-msgs ros-${ROS_DISTRO}-tf2-geometry-msgs ros-${ROS_DISTRO}-mavros* libyaml-cpp-dev \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Add the ROS 2 apt repository
RUN curl -sSL http://repo.ros2.org/repos.key | apt-key add - \
    && sh -c 'echo "deb http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" > /etc/apt/sources.list.d/ros2-latest.list'

# Update and install ros-foxy-mavros
RUN apt-get update && apt-get install -y \
    ros-${ROS_DISTRO}-mavros* libyaml-cpp-dev \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /workspace

# Copy the entrypoint script into the container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Run the entrypoint script to keep the container running
ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
