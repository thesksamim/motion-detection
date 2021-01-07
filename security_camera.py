import cv2 #importing opencv 
import winsound
cam = cv2.VideoCapture(0) # declaring the camera what is it going to do 
while cam.isOpened(): # when camera is opened 
    ret, frame1 = cam.read() # reading the variables of the camera
    ret, frame2 = cam.read()
    different = cv2.absdiff(frame1, frame2) # measuring the difference in two point 
    gray = cv2.cvtColor(different, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0) # adding some blur effect to the gray differnce 
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # to findout the area of the video

    # cv2.drawContours(frame1, contours, -1, (0,255,0), 2)
    for c in contours:
        if cv2.contourArea(c) < 4000: # for recording only element that is big enough 
            continue
        x, y, w, h = cv2.boundingRect(c) 
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0,255,0), 2) # 2 for thickness 
        winsound.Beep(500, 200)



    cv2.imshow('security camera', frame1) # to show the image if a difference is occured 

    if cv2.waitKey(10) == ord('q'): # break the pop up window when someone user press 'q'
        break

