from doc_converter import converter
import cv2
import argparse
import numpy as np

#Argument Parser for CLI
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required = True, help = "Path to document image")
args = vars(ap.parse_args())

#For script input
'''args = { "input": "Enter document path between inveted commas" }'''

image = cv2.imread(args["input"])
outlined_image, warped_image = converter(image)
#Show results    
cv2.imwrite(r"output/doc scan/output.jpg", warped_image);
cv2.imshow("Outlined v/s Scanned", np.hstack([outlined_image, warped_image]))
cv2.waitKey(0)