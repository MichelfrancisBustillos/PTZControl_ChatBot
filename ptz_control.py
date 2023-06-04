from onvif import ONVIFCamera

cameraIP = "0.0.0.0"
cameraPort = 80
cameraUser = "admin"
cameraPassword = "admin"

xCoordinate = 0
yCoordinate = 0
zoom = 0

camera = ONVIFCamera(cameraIP, cameraPort, cameraUser, cameraPassword)
media = camera.create_media_service()
ptz = camera.create_ptz_service()
media_profile = media.GetProfiles()[0]

moveRequest = ptz.create_type('AbsoluteMove')
moveRequest.ProfileToken = media_profile.token
moveRequest.Position = ptz.GetStatus({'ProfileToken': media_profile.token}).position

try:
    moveRequest.Position.PanTilt.x = float(xCoordinate)
    moveRequest.Position.PanTilt.y = float(yCoordinate)
    moveRequest.Position.Zoom.x = float(zoom)
except:
    pass

ptz.AbsoluteMove(moveRequest)