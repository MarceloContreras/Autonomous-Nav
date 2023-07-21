## *********************************************************
##
## File autogenerated for the dwa_planner package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'max_vel_trans', 'type': 'double', 'default': 0.55, 'level': 0, 'description': 'The absolute value of the maximum translational velocity for the robot in m/s', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_trans', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'The absolute value of the minimum translational velocity for the robot in m/s', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_vel_x', 'type': 'double', 'default': 0.55, 'level': 0, 'description': 'The maximum x velocity for the robot in m/s', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_x', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'The minimum x velocity for the robot in m/s', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_vel_y', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'The maximum y velocity for the robot in m/s', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_y', 'type': 'double', 'default': -0.1, 'level': 0, 'description': 'The minimum y velocity for the robot in m/s', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_vel_theta', 'type': 'double', 'default': 1.0, 'level': 0, 'description': 'The absolute value of the maximum rotational velocity for the robot in rad/s', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'min_vel_theta', 'type': 'double', 'default': 0.4, 'level': 0, 'description': 'The absolute value of the minimum rotational velocity for the robot in rad/s', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'acc_lim_x', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'The acceleration limit of the robot in the x direction', 'min': 0.0, 'max': 20.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'acc_lim_y', 'type': 'double', 'default': 2.5, 'level': 0, 'description': 'The acceleration limit of the robot in the y direction', 'min': 0.0, 'max': 20.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'acc_lim_theta', 'type': 'double', 'default': 3.2, 'level': 0, 'description': 'The acceleration limit of the robot in the theta direction', 'min': 0.0, 'max': 20.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'acc_lim_trans', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'The absolute value of the maximum translational acceleration for the robot in m/s^2', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'prune_plan', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Start following closest point of global plan, not first point (if different).', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'xy_goal_tolerance', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Within what maximum distance we consider the robot to be in goal', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'yaw_goal_tolerance', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Within what maximum angle difference we consider the robot to face goal direction', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'trans_stopped_vel', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Below what maximum velocity we consider the robot to be stopped in translation', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'theta_stopped_vel', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'Below what maximum rotation velocity we consider the robot to be stopped in rotation', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'sim_time', 'type': 'double', 'default': 1.7, 'level': 0, 'description': 'The amount of time to roll trajectories out for in seconds', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'sim_granularity', 'type': 'double', 'default': 0.025, 'level': 0, 'description': 'The granularity with which to check for collisions along each trajectory in meters', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'angular_sim_granularity', 'type': 'double', 'default': 0.1, 'level': 0, 'description': 'The granularity with which to check for collisions for rotations in radians', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'path_distance_bias', 'type': 'double', 'default': 0.6, 'level': 0, 'description': 'The weight for the path distance part of the cost function', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'goal_distance_bias', 'type': 'double', 'default': 0.8, 'level': 0, 'description': 'The weight for the goal distance part of the cost function', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'occdist_scale', 'type': 'double', 'default': 0.01, 'level': 0, 'description': 'The weight for the obstacle distance part of the cost function', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'twirling_scale', 'type': 'double', 'default': 0.0, 'level': 0, 'description': 'The weight for penalizing any changes in robot heading', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'stop_time_buffer', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'The amount of time that the robot must stop before a collision in order for a trajectory to be considered valid in seconds', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'oscillation_reset_dist', 'type': 'double', 'default': 0.05, 'level': 0, 'description': 'The distance the robot must travel before oscillation flags are reset, in meters', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'oscillation_reset_angle', 'type': 'double', 'default': 0.2, 'level': 0, 'description': 'The angle the robot must turn before oscillation flags are reset, in radians', 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'forward_point_distance', 'type': 'double', 'default': 0.325, 'level': 0, 'description': 'The distance from the center point of the robot to place an additional scoring point, in meters', 'min': -inf, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'scaling_speed', 'type': 'double', 'default': 0.25, 'level': 0, 'description': "The absolute value of the velocity at which to start scaling the robot's footprint, in m/s", 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'max_scaling_factor', 'type': 'double', 'default': 0.2, 'level': 0, 'description': "The maximum factor to scale the robot's footprint by", 'min': 0.0, 'max': inf, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'vx_samples', 'type': 'int', 'default': 3, 'level': 0, 'description': 'The number of samples to use when exploring the x velocity space', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'vy_samples', 'type': 'int', 'default': 10, 'level': 0, 'description': 'The number of samples to use when exploring the y velocity space', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'vth_samples', 'type': 'int', 'default': 20, 'level': 0, 'description': 'The number of samples to use when exploring the theta velocity space', 'min': 1, 'max': 2147483647, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'use_dwa', 'type': 'bool', 'default': True, 'level': 0, 'description': 'Use dynamic window approach to constrain sampling velocities to small window.', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}, {'name': 'restore_defaults', 'type': 'bool', 'default': False, 'level': 0, 'description': 'Restore to the original configuration.', 'min': False, 'max': True, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'bool', 'cconsttype': 'const bool'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

