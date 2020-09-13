import cv2


class autoFocus:

    def __init__(self, _name):
        self.name = _name
        self.imgPath = './img/H&A/'
        self.img = cv2.imread(self.name, 0)

    def getImgVarLaplacian(self):
        imgVar = cv2.Laplacian(self.img, cv2.CV_64F).var()
        print('Laplacian score: ', imgVar)
        return round(imgVar,2)

    def getImgVarTenengrad(self):
        imgVar = cv2.Sobel(self.img, cv2.CV_64F, 1, 1).var()
        print('Sobel score: ', imgVar)
        return round(imgVar, 2)



if __name__== '__main__':
    autoFocus('S1.bmp').getImgVarTenengrad()
    autoFocus('B692-070AA.PNG').getImgVarTenengrad()
    autoFocus('W5.bmp').getImgVarTenengrad()
    autoFocus('W3.bmp').getImgVarTenengrad()
    autoFocus('W4.bmp').getImgVarTenengrad()

    cv2.waitKey(0)
    cv2.destroyAllWindows()
