class APNsBody(dict):
    def __init__(self):
        super().__init__()
        self.addKey('aps',{})
        
    def addKey(self,key,value):
        self.setdefault(key,value)
        return self
    
    def withAlert(self,title:str,subtitle:str,message:str,launch_image:str=None,title_loc_key:str=None,title_loc_args:dict=None,subtitle_loc_key:str=None,subtitle_loc_args:dict=None,loc_key:str=None,loc_args:dict=None):
        values={
                "title" : title,
                "subtitle" : subtitle,
                "body" : message,
                "launch-image":launch_image,
                "title-loc-key":title_loc_key,
                "title-loc-args":title_loc_args,
                "subtitle-loc-key":subtitle_loc_key,
                "subtitle-loc-args":subtitle_loc_args,
                "loc-key":loc_key,
                "loc-args":loc_args
        }
        self['aps'].setdefault('alert',values)
        return self
    
    def withSound(self,sound='default'):
        self['aps'].setdefault('sound',sound)
        return self

    def withBadge(self,badge:int):
        self['aps'].setdefault('badge',badge)
        return self
