import sys
import cv2
import pdb
from run import process

"""
main.py

 How to run:
 python3 main.py

"""

# ------------------------------------------------- main()
def main():

	#Read input image
	dress = cv2.imread("input2.jpg")
	h, w = dress.shape[:2]
	dress = cv2.resize(dress, (512,512), interpolation=cv2.INTER_CUBIC)

	#Process
	watermark = process(dress)
	watermark = cv2.resize(watermark, (w, h), interpolation=cv2.INTER_CUBIC)

	# Write output image
	cv2.imwrite("output2.png", watermark)

	#Exit
	sys.exit()

if __name__ == '__main__':
	main()