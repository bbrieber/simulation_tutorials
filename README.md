simulation_tutorials
====================

This repositroy contains a set of examples/tutorials for gazebo and ros




packages
--------
|package| description|
--------|-------------|
|suzanne_robot_controller|contains configuration files and scripts to control the robots|
|suzanne_robot_description|conatins urdf and sdf descriptions of the robot |
|suzanne_robot_gazebo|conatins launch and world files to start the simulator|



Usage
-----


use:   

```
roslaunch suzanne_robot_gazebo start_simulator.launch
```

to start the simulation with two robots one fleeing one following the other robot...




to start only a robot position x = 10 in the namespace foo use:

```
roslaunch suzanne_robot_description spawn_robot.launch x:=10 __ns:=foo
```


to run the script alone use:
```
rosrun suzanne_robot_controller follow.py <name> <target_name> --flee __ns:=<name> 
```
<name> and <target_name> have to be replaced by the actual robot name


use
```
rosrun suzanne_robot_controller follow.py --help

```
to see the help message
