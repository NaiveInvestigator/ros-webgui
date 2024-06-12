# ros-webgui
A simple Bootstrap5 GUI using roslibjs that works locally, offline
## Requirements:
* [ros](https://wiki.ros.org/noetic/Installation)
* [mapproxy](https://www.mapproxy.org/)
* python3
* [rosbridge](http://wiki.ros.org/rosbridge_suite)
## Usage:
 ```
git clone https://github.com/NaiveInvestigator/ros-webgui
```
```
roscore
```
```
roslaunch rosbridge_server rosbridge_websocket.launch
```
```
cd ros-webgui
```
```
mapproxy-util serve-develop mapproxy/mapproxy.yaml
```
```
python -m http.server 8000
```
open browser at [http://localhost:8000/map_ros.html](http://localhost:8000/map_ros.html)
## See GUI in ACTION:
to inspect  the ros messages sent and received by the gui do the following:
* list all ros topic with `rostopic list`
* choose a topic from the output and see messages receieved with `rostopic list <topic>`. for e.g `rostopic echo /turtle1/cmd_vel`
## TODO:
- [ ] create a .launch file to start up GUI with one line
- [ ] consolidate camera feeds in gui 
