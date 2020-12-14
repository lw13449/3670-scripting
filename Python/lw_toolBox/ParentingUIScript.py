import maya.cmds as cmds

class ParentingUI():
    def __init__(self):
        self.parent_window = "lwParenting"
        
    def create(self):
        self.delete()
            
        self.parent_window = cmds.window(self.parent_window, title = "Parenting UI", widthHeight = (200, 200))

        self.layout_var = cmds.rowColumnLayout(parent=self.parent_window)
        
        cmds.button(label="Group", parent = self.layout_var, c=lambda *x: self.ParentGroup())
        cmds.button(label="Parent/Scale Constrain", parent = self.layout_var, c=lambda *x: self.ParentScaleConstrain())
        cmds.text(label="Select Parent, then Child", parent = self.layout_var)
        
        cmds.showWindow(self.parent_window)
        
    def delete(self):
        if cmds.window(self.parent_window, exists=True):
            cmds.deleteUI(self.parent_window)

    def ParentGroup(self):
        sel = cmds.ls(selection=True)    
        
        for obj in sel:
            group_var = cmds.group(em=True)
            cmds.parent(obj, group_var)
                
    def ParentScaleConstrain(self):
        sel = cmds.ls(selection=True)
        
        if len(sel) % 2 == 1:
            cmds.error('Uneven selection. Please try again')
        else:                
            for obj in range(0, len(sel), 2):
                cmds.parentConstraint(sel[obj], sel[obj+1])
                cmds.scaleConstraint(sel[obj], sel[obj+1])
                            
parent_window = ParentingUI()

parent_window.create()
