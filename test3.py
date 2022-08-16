import cv2
import yolov5.detect
import os

video_capture = cv2.VideoCapture(0)
detect_api = yolov5.detect.DetectAPI(exist_ok=True)

while True:
	k = cv2.waitKey(1)
    ret, frame = video_capture.read()
    
    path = '你的目录/yolov5-master/data/myimages'
    cv2.imwrite(os.path.join(path, 'test.jpg'), frame)
    
    label = detect_api.run()
    print(str(label))
    
    image = cv2.imread('你的目录/yolov5-master/runs/detect/myexp/test.jpg', flags=1)
    cv2.imshow("video", image)

    if k == 27:  # 按下ESC退出窗口
        break

video_capture.release()

