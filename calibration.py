import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt

chessboard_num = (7, 7)
drawCornersImage = []
cornerspoints = []
objpoints = []

images = glob.glob('.\\camera_calibration\\*.bmp')

objp = np.zeros((chessboard_num[0]*chessboard_num[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:chessboard_num[0], 0:chessboard_num[1]].T.reshape(-1, 2)

for image in images:
    img = cv2.imread(image)
    ## 找出棋盤角點
    ret, corners = cv2.findChessboardCorners(img, chessboard_num, cv2.CALIB_CB_ADAPTIVE_THRESH)
    if ret:
        print(image)
        img = cv2.drawChessboardCorners(img, chessboard_num, corners, ret)
        cornerspoints.append(corners)
        objpoints.append(objp)
        drawCornersImage.append(img)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, cornerspoints, img.shape, None, None)
print(f'matrix : {mtx}')  
print(f'dist : {dist}')
print(f'rvecs : {rvecs}')
print(f'tvecs : {tvecs}')

# for i, img in enumerate(drawCornersImage):
#     plt.subplot(2, 5, i+1)
#     plt.imshow(img)
#     plt.title(i)

# plt.show()
