import pytesseract 
from googletrans import Translator
import cv2
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

class TranslateTAR:

    def checkText(self, img_bw):

        print(img_bw.size)
        flag = 0
        for i in range(img_bw.shape[0]):
            for j in range(1, img_bw.shape[1], 10):
                if abs(int(img_bw[i][j-1]) - int(img_bw[i][j])) > 200: 
                    flag += 1 

        print(flag)
        if flag > img_bw.size/5000:
            return 1
        return 0

    # cv2.imshow("BW", img_bw)
    # cv2.waitKey(0)

    def extractFromImg(self, img_bw, translate = False):

        d = pytesseract.image_to_data(img_bw, output_type = pytesseract.Output.DICT, lang='eng')

        n_boxes = len(d['level'])
        text_pos_list = {}

        for i in range(n_boxes):
            text = d['text'][i].strip()
            if len(text) == 0:
                continue    
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            text_pos_list[text] = (x, y, w, h)
            cv2.rectangle(img_bw, (x, y), (x + w, y + h), (255, 255, 255), -1)

        if translate:
            trtext_pos_list = {}
            p = Translator()

            for text in text_pos_list.keys():
                p_translated = p.translate(text, dest='french')
                trtext_pos_list[str(p_translated.text)] = text_pos_list[text]
            
            return trtext_pos_list, img_bw

        return text_pos_list, img_bw

    def printText(self, img, trtext_pos_list, wait):
        for text in trtext_pos_list.keys():
            img = cv2.putText(img, text, (trtext_pos_list[text][0], trtext_pos_list[text][1]), cv2.QT_FONT_NORMAL, 
                            0.4, (0, 0, 0), 1, cv2.LINE_4)

        cv2.imshow("Translated AR", img)
        if wait:
            cv2.waitKey(0)

    def runOnFrame(self, img, translate = True, wait = False):
        img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, img_bw) = cv2.threshold(img_bw, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        text_dict = {}
        frame = img_bw
        
        if self.checkText(img_bw=img_bw):
            text_dict, frame = self.extractFromImg(img_bw=img_bw, translate=translate)

        if translate and text_dict != None:
            self.printText(img=frame, trtext_pos_list=text_dict, wait=wait)

        if translate == False:
            for text in text_dict:
                print(text, "", end = "")
            
        print()


TAR = TranslateTAR()
img = cv2.imread("TRAIL3.png")

TAR.runOnFrame(img, translate=False, wait = True)