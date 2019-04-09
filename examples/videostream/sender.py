
from npsocket import SocketNumpyArray
import cv2

cap = cv2.VideoCapture(0)
sock_sender = SocketNumpyArray()

sock_sender.initialize_sender('localhost', 9999)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (620, 480))
    sock_sender.send_numpy_array(frame)
