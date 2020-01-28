import threading
import time

from flask import Flask
from flaskUtils import app
from LEDUtils import PPB
from neopixel import *

if __name__ == '__main__':
	# Start the flask server
	x = threading.Thread(target=app.run, kwargs=dict(host='0.0.0.0',port=80))
	x.daemon = True
	x.start()
	
	while(True):

		# Reset the string at the beginning of each loop
		PPB.displayString = ''

		# Update the BG color if need be
		PPB.updateBGColor()

		# Get the display string components
		PPB.time()
		PPB.date()

		# If the animation speed is not 0, then update the animation
		if PPB.animationSpeed != 0:
			PPB.updateTextAnimation()

		# Write the display string text state if it has differed from the previous string
		if PPB.displayString != PPB.displayStringPrev or PPB.textOriginMoved:
			PPB.writeDisplayString()

		# Update the actual ball color light
		PPB.updateTextColor()
	