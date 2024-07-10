import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    sim_config = os.path.join('/opt/jderobot/Launchers/sim_config')

    gazebo_assets = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('as2_gazebo_assets'), 'launch'),
            '/launch_simulation.py']),
        launch_arguments={
            'namespace': LaunchConfiguration('namespace'),
            'use_sim_time': 'true',
            'headless': 'true',
            'verbose': 'true',
            'run_on_start': 'true',
            'simulation_config_file': sim_config + '/rescue_people.json'
        }.items(),
    )

    platform_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('as2_platform_gazebo'), 'launch'),
            '/platform_gazebo_launch.py']),
        launch_arguments={
            'namespace': LaunchConfiguration('namespace'),
            'use_sim_time': 'true',
            'simulation_config_file': sim_config + '/rescue_people.json',
        }.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument('namespace', default_value='drone0',
                              description='Drone namespace'),
        platform_gazebo,
        gazebo_assets
    ])