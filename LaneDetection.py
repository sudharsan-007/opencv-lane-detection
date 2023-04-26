import numpy as np
import cv2
import utlis

####################################################

cameraFeed= False
videoPath = 'highway2.mp4'
cameraNo= 1
frameWidth= 640
frameHeight = 480

if cameraFeed:intialTracbarVals = [24,55,12,100] #  #wT,hT,wB,hB
else:intialTracbarVals = [42,63,14,87]   #wT,hT,wB,hB

####################################################


if cameraFeed:
    # cap = cv2.VideoCapture("https://192.168.1.5:8080/video") To capture from camera in raspberry pi sending frame to this port 
    cap = cv2.VideoCapture(0)
    cap.set(3, frameWidth)
    cap.set(4, frameHeight)
else:
    cap = cv2.VideoCapture(videoPath)
count=0
noOfArrayValues =10
global arrayCurve, arrayCounter
arrayCounter=0
arrayCurve = np.zeros([noOfArrayValues])
myVals=[]
utlis.initializeTrackbars(intialTracbarVals)


while True:

    success, img = cap.read()
    ##img = cv2.imread('test3.jpg')
    if cameraFeed== False:
        img = cv2.resize(img, (frameWidth, frameHeight))
    #img = cv2.resize(img, (frameWidth, frameHeight)) ## since we r using ip adress camera
    imgWarpPoints = img.copy()
    imgFinal = img.copy()
    imgCanny = img.copy()

    imgUndis = utlis.undistort(img)
    imgThres,imgCanny,imgColor = utlis.thresholding(imgUndis)
    src = utlis.valTrackbars()
    imgWarp = utlis.perspective_warp(imgThres, dst_size=(frameWidth, frameHeight), src=src)
    imgWarpPoints = utlis.drawPoints(imgWarpPoints, src)
    imgSliding, curves, lanes, ploty = utlis.sliding_window(imgWarp, draw_windows=True)

    try:
        curverad =utlis.get_curve(imgFinal, curves[0], curves[1])
        lane_curve = np.mean([curverad[0], curverad[1]])
        imgFinal = utlis.draw_lanes(img, curves[0], curves[1],frameWidth,frameHeight,src=src)

        # ## Average
        currentCurve = lane_curve // 50
        if  int(np.sum(arrayCurve)) == 0:averageCurve = currentCurve
        else:
            averageCurve = np.sum(arrayCurve) // arrayCurve.shape[0]
        if abs(averageCurve-currentCurve) >200: arrayCurve[arrayCounter] = averageCurve
        else :arrayCurve[arrayCounter] = currentCurve
        arrayCounter +=1
        if arrayCounter >=noOfArrayValues : arrayCounter=0
        cv2.putText(imgFinal, str(int(averageCurve)), (frameWidth//2-70, 70), cv2.FONT_HERSHEY_DUPLEX, 1.75, (0, 0, 255), 2, cv2.LINE_AA)

    except:
        lane_curve=00
        pass

    imgFinal= utlis.drawLines(imgFinal,lane_curve)
    print(currentCurve)

    imgThres = cv2.cvtColor(imgThres,cv2.COLOR_GRAY2BGR)
    imgBlank = np.zeros_like(img)
    imgStacked = utlis.stackImages(0.7, ([img,imgUndis,imgWarpPoints],
                                         [imgColor, imgCanny, imgThres],
                                         [imgWarp,imgSliding,imgFinal]
                                         ))

    cv2.imshow("PipeLine",imgStacked)
    cv2.imshow("Result", imgFinal)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
