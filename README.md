# NpSocket
## About
This python module was built to transfer the Numpy array over a TCP/IP socket. There is [Numpy Socket package](https://github.com/sabjorn/NumpySocket)
orginally written by [@sabjorn](https://github.com/sabjorn/) to stream video frames from OpenCV  which only works for python2. But I couldn't find the decent solution for python3. So based on a [thread in stackoverflow](https://stackoverflow.com/questions/30988033/sending-live-video-frame-over-network-in-python-opencv), this module was written to send the numpy array over the TCP/IP sokcet. This module make use of the code sample of the answer given by [@nareddyt](https://stackoverflow.com/users/4402434/nareddyt) in the same stackoverflow thread. 

I'm actually using this module to send the video frame captured through opencv, make a prediction on the image, and send
back the modified image to the Pi client.

## Installation 
1. First clone this repository. 
2. cd into the cloned directory. 
3. Run `python3 setup.py install` in the terminal. 
4. You should have a working NpSocket module. 
5. Varify this by running the following commands in terminal: 
```
>>> import npsocket
>>> from npsocket import SocketNumpyArray
>>> exit() 

```
## Examples:
1. Initalize the Receiver: 
```
from npsocket import SocketNumpyArray
sock_receiver = SocketNumpyArray()
sock_receiver.initalize_receiver(9999) # the 9999 is the port you can change it with your own. 
while True:
    frame = sock_receiver.receive_array()  # Receiving the image as numpy array. 
    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
```
2. Intialize the Sender: 
```
from npsocket import SocketNumpyArray
import cv2

cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()

sock_sender.initialize_sender('localhost', 9999)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (620, 480))
    sock_sender.send_numpy_array(frame)
```
3. Run the 'reciver' for and the the 'sender'. You should be able to see the frame being sent by the sender and displayed by the receiver in the CV2 window. 

In the same way, you should be able to transfer any Numpy Array. There is an example files in the videostream directory, where the above example is shown. If you simply want to run and see it, then you can first run `python3 receiver.py` and then `python3 sender.py` and see it working. 

## Contributors
1. [Bibek](https://github.com/bbkchdhry)
2. [Vaghawan](https://github.com/vaghawan)
