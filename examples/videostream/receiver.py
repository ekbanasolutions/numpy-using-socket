
import cv2
from npsocket import SocketNumpyArray

sock_receiver = SocketNumpyArray()
sock_receiver.initalize_receiver(9999)

while True:
    frame = sock_receiver.receive_array()

    # Display
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
