from enum import Enum

class PushType(Enum):
    alert='alert'
    background='background'
    complication='complication'
    controls='controls'
    fileprovider='fileprovider'
    liveactivity='liveactivity'
    location='location'
    mdm='mdm'
    pushtotalk='pushtotalk'
    voip='voip'
    widgets='widgets'
