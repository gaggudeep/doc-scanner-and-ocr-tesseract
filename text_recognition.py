from pytesseract import Output
import pytesseract
import argparse
import cv2
from doc_converter import converter
import imutils

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-c", "--min-conf", type=int, default=0, help="mininum confidence value to filter weak text detection")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

#Uncomment below line if you want to use with document scanner
#_, image = converter(image)

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type = Output.DICT)

#Looping over text detected areas
for i in range(0, len(results["text"])):
    
    #Extract coordinates of text bounding box region
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    
    #Extract text along with model's confidence on the text
    text = results["text"][i]
    conf = int(results["conf"][i])
    
    if conf > args["min_conf"]:
        
        print("Confidence:", conf)
        print("Text:", text)
        print()
        
    #Exclude non-ASCII text sw we can draw text on image, then draw bounding box
    text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1)

cv2.imwrite(r"output/text recognition/output.jpg", image)
cv2.imshow("Image with text", imutils.resize(image, height = 720))
cv2.waitKey(0)
    

