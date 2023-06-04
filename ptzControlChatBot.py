from onvif import ONVIFCamera
import pytchat

class Preset:
    chatCommand = "" #Chat command to trigger preset
    x = 0 #Destination X Coordinate for PTZ Camera Movement
    y = 0 #Destination Y Coordinate for PTZ Camera Movement
    zoom = 0 #Destination Zoom Value for PTZ Camera

#Global Variables
videoID = "" #ID of livestream
cameraIP = "0.0.0.0" #IP of PTZ Camera
cameraPort = 80 #PTZ Camera Interface Port
cameraUser = "admin" #PTZ Camera Username
cameraPassword = "admin" #PTZ Camera Password

preset1 = Preset() #Test preset
preset1.chatCommand = "/bot preset1"
preset1.x = 10
preset1.y = 10
preset1.zoom = 100

#Create PTZ Camera Objects
camera = ONVIFCamera(cameraIP, cameraPort, cameraUser, cameraPassword)
media = camera.create_media_service()
ptz = camera.create_ptz_service()
media_profile = media.GetProfiles()[0]

def main():
    if (getChat() == preset1.chatCommand):
        moveCamera(preset1)

def moveCamera(Preset):
    newView = Preset
    moveRequest = ptz.create_type('AbsoluteMove')
    moveRequest.ProfileToken = media_profile.token
    moveRequest.Position = ptz.GetStatus({'ProfileToken': media_profile.token}).position

    try:
        moveRequest.Position.PanTilt.x = float(newView.x)
        moveRequest.Position.PanTilt.y = float(newView.y)
        moveRequest.Position.Zoom.x = float(newView.zoom)
    except:
        pass

    ptz.AbsoluteMove(moveRequest)
    
def getChat():
    message = ""
    chat = pytchat.create(video_id=videoID)
    while chat.is_alive():
        try:
            for c in chat.get().sync_items():
                print(f"{c.datetime} [{c.author.name}]- {c.message}")
                message = c.message
        except AttributeError:
            print("Error occurred. Restarting...")
            chat = pytchat.create(video_id=videoID)
    return message