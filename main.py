import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img=cv2.imread('Screenshot (576).png')
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
##detecting characters

himg,wimg,_=img.shape
# print(pytesseract.image_to_boxes(img))
# boxes=pytesseract.image_to_boxes(img)
# for b in boxes.splitlines():
#     # print(b)
#     b=b.split(' ')
#     # print(b)
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,244),1)
#     cv2.putText(img,b[0],(x,himg-y+2),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),2)

##detecting words
himg,wimg,_=img.shape
# print(pytesseract.image_to_boxes(img))
boxes=pytesseract.image_to_data(img)
print(boxes)
for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b=b.split()
        print(b)
        if len(b)==12:
            x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
            cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,244),1)
            cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),2)

# ##detecting digits
# himg,wimg,_=img.shape
# confi=r'--oem 3 --psm 6 outputbase digits'
# # print(pytesseract.image_to_boxes(img))
# boxes=pytesseract.image_to_data(img,config=confi)
# print(boxes)
# for x,b in enumerate(boxes.splitlines()):
#     if x!=0:
#         b=b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9])
#             cv2.rectangle(img,(x,y),(w+x,y+h),(0,0,244),1)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(50,50,255),2)



cv2.imshow("result",img)
cv2.waitKey(0)
