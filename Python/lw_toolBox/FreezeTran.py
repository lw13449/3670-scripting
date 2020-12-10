import maya.cmds as cmds

class FreezeAndDelUI():
    def __init__(self):
        self.freeze_window = "lwFreezeAndDelete"
                
    def create(self):
        self.delete()
            
        self.random_window = cmds.window(self.freeze_window, title = "Freeze and Delete", widthHeight = (200, 200))

        self.layout_var = cmds.rowColumnLayout(parent=self.freeze_window,  numberOfColumns=5, columnWidth=[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100)])
        
        cmds.button(label="Freeze Transformations", parent = self.layout_var, c=lambda *x: self.FreezeTransform())
        cmds.button(label="Delete History", parent = self.layout_var, c=lambda *x: self.DelHistory())
        
        cmds.showWindow(self.freeze_window)
    
    def delete(self):
        if cmds.window(self.freeze_window, exists=True):
            cmds.deleteUI(self.freeze_window)

    def FreezeTransform(self):
        sel = cmds.ls(selection=True)    
        
        for obj in sel:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
            
            
    
    def DelHistory(self):
        sel = cmds.ls(selection=True)
        
        for obj in sel:
            cmds.delete(constructionHistory=True)
        