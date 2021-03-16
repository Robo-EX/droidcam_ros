## Description
Using DroidCamX apk able to stream android camera data wireless over ROS topic using ROS Node. 
### To run:
directly: `python src/droidcam.py -u http://192.168.0.101:4747/video` (argument -u to set url -g to show a GUI of the camera stream) 

using roslaunch: `roslaunch droidcam_ros droidcam.launch`

running camera_info node: `rosrun droidcam_ros camerainfo.py ~/YOUR_ROS_WORKSPACE_NAME/src/droidcam_ros/calibrationdata/ost.yaml`

### Apk download link
- https://play.google.com/store/apps/details?id=com.dev47apps.droidcamx 
- https://play.google.com/store/apps/details?id=com.dev47apps.droidcam

### Apk features
- Chat using "DroidCam Webcam" on your computer, including Sound and Picture.
- Completely free with no usage limits or watermarks.
- Connect over WiFi.
- Microphone noise cancellation.
- Use other (non camera) apps with DroidCam in the background.
- Keeps working with the screen off to conserve battery.
- IP web camera MJPEG access (access camera via a browser or from another phone/tablet/etc).
- Exposure Lock (can be useful while processing camera data)
