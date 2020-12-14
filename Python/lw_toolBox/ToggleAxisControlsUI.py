import maya.cmds as cmds

class RiggingAxisUI():
    def __init__(self):
        self.rigging_window = "lwParenting"
        
    def create(self):
        self.delete()
            
        self.parent_window = cmds.window(self.rigging_window, title = "Rigging UI", widthHeight = (200, 200))

        self.layout_var = cmds.rowColumnLayout(parent=self.rigging_window)
        
        cmds.button(label="Channel Box Orient Controls", parent = self.layout_var, c=lambda *x: self.ControlChannelUpdate())
        
        cmds.showWindow(self.rigging_window)
        
    def delete(self):
        if cmds.window(self.rigging_window, exists=True):
            cmds.deleteUI(self.rigging_window)
    
    def ControlChannelUpdate(self):
        sel = cmds.ls(selection=True)
        cmds.toggle(la=True)
        
        for s in sel:
            cmds.setAttr(s+'.jointOrientX', cb=True)
            cmds.setAttr(s+'.jointOrientY', cb=True)
            cmds.setAttr(s+'.jointOrientZ', cb=True)
            cmds.setAttr(s+'.displayLocalAxis', cb=True)
                    
rigging_window = RiggingAxisUI()

rigging_window.create()     
