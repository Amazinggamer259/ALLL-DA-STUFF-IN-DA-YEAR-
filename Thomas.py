# python code
#
# script_name: EarSketch Demo
#
# author: The EarSketch Team
#
# description: Using fitMedia() to add a clip to the DAW.
#
#
#

#Setup
from earsketch import *

init()
setTempo(120)


#def kiana():
bass = OS_LOWTOM01
#Music
dub = DUBSTEP_BASS_WOBBLE_001

fitMedia(MRPRESIDENTDT_GEORGE_MICHAEL_CARELESS_WHISPER, 1,1, 30)
fitMedia(MRPRESIDENTDT_RICK_ASTLEY_NEVER_GONNA_GIVE_YOU_UP, 2, 30, 60)
for measure in range(1,3):
  fitMedia(dub, 4, measure, measure + 1)
setEffect(3, DELAY, DELAY_TIME, 50)

setEffect(1, VOLUME, GAIN, -60, 1, 0, 5 ) 
#Finish
finish()
