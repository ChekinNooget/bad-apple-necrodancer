#this exports all of the data in the video
#90% stolen from the internet again

import cv2
cap = cv2.VideoCapture("bad_apple trimmed resized.mp4")

print(cap.get(cv2.CAP_PROP_FRAME_COUNT))

allFrames = []

#i just did a for loop with a large number because while loops don't have indexes (or if there are idk how to use it lol)
for i in range(1000):
    #setup one frame at a time
    oneFrame = []
    #we need to choose a specific frame because crypt doesn't run at 30fps.
    #so we just find the closest frame at a specific point and it works ok
    #thank god bad apple is a consistent bpm lol
    #2.3 comes from the bpm: 138bpm = 2.3bps.
    #it's all divided by 4 because bolt + double tempo means it's 4 times faster than 2.3bps
    #and times by 30 because the bad apple video is in 30fps
    frame = int(i/2.3*30/4)
    if not frame % 100:
        print(int((i/2.3*30/4)))
    if frame < int(cap.get(cv2.CAP_PROP_FRAME_COUNT)):
        cap.set(1, frame)
        res, frame = cap.read() #frame has your pixel values

        #Get frame height and width to access pixels
        height, width, channels = frame.shape

        #Accessing BGR pixel values    
        for x in range(0, height) :
            oneFrame.append([])
            for y in range(0, width) :
                oneFrame[x].append([])
                if frame[x,y,2] > 100:
                    oneFrame[x][y] = 1
                else:
                    oneFrame[x][y] = 0
        allFrames.append(oneFrame)
    else:
        break

#write it in a format that's easy to copy to lua lol
with open("output.txt", "w") as f:
  f.write(str(allFrames).replace("[", "{").replace("]", "}").replace(" ", ""))
#once you have this just copy and paste it over to dataFile.lua in the necrodancer folder