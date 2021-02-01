import maya.cmds as cmds

class ParentingUI():
    def __init__(self):
        self.parent_window = "lwParenting"

    def create_locator(self):
        sel = cmds.ls(selection=True)
        
        bbox = cmds.exactWorldBoundingBox(sel)
        x_pos = (bbox[0] + bbox[3]) / 2
        y_pos = (bbox[1] + bbox[4]) / 2
        z_pos = (bbox[2] + bbox[5]) / 2
        
        locator = cmds.spaceLocator()[0]
        cmds.xform(locator, ws=True, translation=[x_pos, y_pos, z_pos])
        
        return locator