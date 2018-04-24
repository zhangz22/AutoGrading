import cv2


class Box(object):
    def __init__(self, my_contour):
        self.contour = my_contour
        self.area = cv2.contourArea(my_contour)
        self.centre = self.find_centre()

    def find_centre(self, printed=False):
        x_axis = []
        y_axis = []
        for point in self.contour:
            x_axis.append(point[0][0])
            y_axis.append(point[0][1])
        if printed:
            pass
            # print(cnts[0][0][0][0])
        x_axis = sorted(x_axis)
        y_axis = sorted(y_axis)
        x_centre = int((x_axis[0] + x_axis[-1]) / 2)
        y_centre = int((y_axis[0] + y_axis[-1]) / 2)
        return x_centre, y_centre

    def getCentre(self):
        return self.centre

    def getContour(self):
        return self.contour

    def getArea(self):
        return self.area