from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from cv2 import aruco
import numpy as np
from PyQt5.QtWidgets import QFileDialog
from detect import HomoBgDtector


detector = HomoBgDtector()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Adding Background
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(
            QtGui.QPixmap("photo-1617118602031-1edde7582212.jpg")
            )
        self.label.setObjectName("label")
        # Add pushbutton for Live Capture
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.livecapture)
        self.pushButton.setGeometry(QtCore.QRect(410, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: #e5e5e5")
        self.pushButton.setObjectName("pushButton")
        # Add pushbutton for Browsing Image
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.browse)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 120, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Mistral")
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: #e5e5e5\n")
        self.pushButton_2.setObjectName("pushButton_2")
        # Giving Title
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(240, 30, 291, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "MainWindow"))
        self.pushButton.setText(_translate("MainWindow",
                                           "Live Capturing"))
        self.pushButton_2.setText(_translate("MainWindow",
                                             "Browse for Pictures"))
        self.label_2.setText(_translate("MainWindow", "MeasureCraft"))
    
    def browse(self):
        # Open a file dialog to select an image file
        self.fl = QFileDialog.getOpenFileName(filter='Image (*.*)')[0]
        if self.fl:

            # load Aruco detector
            para = cv2.aruco.DetectorParameters()
            dict_aruco = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)

            # Read the selected image
            img = cv2.imread(self.fl)

            # Detect the Aruco markers in the image
            corner, _, _ = cv2.aruco.detectMarkers(img, dict_aruco,
                                                   parameters=para)

            if corner:
                # Draw the detected Aruco marker perimeter on the image
                intcorners = np.int0(corner)
                cv2.polylines(img, intcorners, True, (0, 255, 0), 5)

                # Calculate the perimeter of the Aruco marker
                arucoperimeter = cv2.arcLength(corner[0], True)


                # Converting Pixels to cm
                if arucoperimeter:
                    scalecmpix = arucoperimeter / 20

                contour = detector.detect_objects(img)
                for points in contour:
                    # Calculate the minimum area rectangle enclosing each object 
                    (x, y), (w, h), angle = cv2.minAreaRect(points)

                    # Coverting everything(object dimensions) to cm
                    if scalecmpix:
                        w /= scalecmpix
                        h /= scalecmpix

                    #Display the object dimensions on the image
                    cv2.putText(img, f"Width:{round(w,1)}cm", (int(x-70),
                                                               int(y-30)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
                    cv2.putText(img, f"Height:{round(h,1)}cm", (int(x-70),
                                                                int(y+50)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
                    
                    # Mark the centre of the object with a circle
                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

                    # Draw the minimum area rectangle around the object
                    box = cv2.boxPoints(cv2.minAreaRect(points))
                    box = np.int0(box)
                    cv2.polylines(img, [box], True, (0, 255, 255), 2)
                    print(box)
            else:
                contour = detector.detect_objects(img)
                for points in contour:

                    # Calculate the minimum area rectangle enclosing each object
                    (x, y), (w, h), angle = cv2.minAreaRect(points)

                    # Display the object dimensions in pixels on the image
                    cv2.putText(img, f"Width:{round(w,1)}pix", (int(x-70),
                                                                int(y-30)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
                    cv2.putText(img, f"Height:{round(h,1)}pix", (int(x-70),
                                                                 int(y+50)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)

                    # Mark the centre of the object with a circle 
                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)

                    # Draw the minimun area rectangle around the object
                    box = cv2.boxPoints(cv2.minAreaRect(points))
                    box = np.int0(box)
                    cv2.polylines(img, [box], True, (0, 255, 255), 2)
                    print(box)

                    # Display the annotated image
            cv2.imshow("image", img)
            cv2.waitKey(0)
    def livecapture(self):
        # To detect the aruco marker
        para = aruco.DetectorParameters()
        dict_aruco = aruco.getPredefinedDictionary(aruco.DICT_5X5_50)
        # Starting the Video Capture
        cap = cv2.VideoCapture(0)
        # Setting the resolution of the frame
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        
        while True:
            # For continuos measurement
            _, img = cap.read()

            corner, _, _ = cv2.aruco.detectMarkers(img, dict_aruco,
                                                   parameters=para)
            if corner:

                # If Aruco Marker is present
                intcorners = np.int0(corner)
                # To Draw boundary lines around the aruco marker
                cv2.polylines(img, intcorners, True, (0, 255, 0), 5)

                # Finding the perimeter of the aruco marker
                arucoperimeter = cv2.arcLength(corner[0], True)
                # Uncomment the line below to see the perimeter of the marker
                # print(arucoperimeter)

                # Converting Pixels to cm
                scalecmpix = arucoperimeter / 20
                # Uncomment the line below to see the ratio
                # print(scalecmpix)
                
                contour = detector.detect_objects(img)
                for points in contour:
                    # To make the boundary as a rectangle
                    (x, y), (w, h), angle = cv2.minAreaRect(points)

                    # Coverting everything to cm
                    w /= scalecmpix
                    h /= scalecmpix
                    
                    # To display the Height and the Width of the Object Detected
                    cv2.putText(img, f"Width:{round(w,1)}", (int(x-70),
                                                             int(y-30)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
                    cv2.putText(img, f"Height:{round(h,1)}", (int(x-70),
                                                              int(y+50)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 0), 2)
                    # To mark the Object's Center
                    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
                    box = cv2.boxPoints(cv2.minAreaRect(points))
                    box = np.int0(box)
                    cv2.polylines(img, [box], True, (0, 255, 255), 2)
                    

            # to disply the frame on the screen
            cv2.imshow("image", img)
            k = cv2.waitKey(1)
            # To stop the Capturing
            if k == 27:
                break
                
        # To close the Window
        cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())    
    
        
    
        
        
        

        
        
