#i used this script to generate a beatmap for the song after the introduction
#because the introduction slowly speeds up i used crypt's built in beat detector for that
#but then i just used a consistent 138 bpm for everything after

bpm = 138
mspb = 60/bpm
length = 216
offset = 14.5473

currentBeat = 0
currentTime = 0
final = "0"
while currentTime < length:
    currentBeat = currentBeat + 1
    final = final + "\n" + str(int(mspb*currentBeat*1000 + offset*1000)/1000)
    currentTime = currentTime + mspb
print(final)