import maya.cmds as cmds

class ControlGenerator():
    def __init__(self):
        self.controls_window = "lwCtrlGen"
        
    def create(self):
        self.delete()
            
        self.controls_window = cmds.window(self.controls_window, title = "Controls UI", widthHeight = (200, 200))

        self.layout_var = cmds.rowColumnLayout(parent=self.controls_window)
        
        cmds.button(label="Circle", parent = self.layout_var, c=lambda *x: self.CreateCircleCtrl())        
        cmds.button(label="Square", parent = self.layout_var, c=lambda *x: self.CreateSquareCtrl())
        
        cmds.showWindow(self.controls_window)
        
    def delete(self):
        if cmds.window(self.controls_window, exists=True):
            cmds.deleteUI(self.controls_window)
        
    def CreateCircleCtrl(self):
        sel = cmds.ls(selection=True)    
        
        for obj in sel:
            joint_name = obj
            string_parts = joint_name.partition("_Jnt")
            
            ctrl_var = cmds.circle(c=(0,0,0))
            group_var = cmds.group(a=True, empty=True, world=True)
            cmds.select(obj, add=True)
            cmds.MatchTransform(group_var, obj, pos=True, rot=True)
            cmds.select(group_var, d=True)
            cmds.select(obj, d=True)
            cmds.select(ctrl_var, add=True)
            cmds.select(group_var, add=True)
            cmds.Parent(ctrl_var, group_var)
            cmds.select(ctrl_var, replace=True)
            cmds.makeIdentity()
            cmds.select(ctrl_var, r=True)
            cmds.rename(string_parts[0] + "_Ctrl")
            cmds.select(group_var, r=True)
            cmds.rename(string_parts[0] + "_Ctrl_Grp")
    
    def CreateSquareCtrl(self):
        sel = cmds.ls(selection=True)    
        
        for obj in sel:
            joint_name = obj
            string_parts = joint_name.partition("_Jnt")
            
            ctrl_var = cmds.nurbsSquare(c=(0,0,0))
            group_var = cmds.group(a=True, empty=True, world=True)
            cmds.select(obj, add=True)
            cmds.MatchTransform(group_var, obj)
            cmds.select(group_var, d=True)
            cmds.select(obj, d=True)
            cmds.select(ctrl_var, add=True)
            cmds.select(group_var, add=True)
            cmds.Parent(ctrl_var, group_var)
            cmds.select(ctrl_var, replace=True)
            cmds.makeIdentity()
            cmds.select(ctrl_var, r=True)
            cmds.rename(string_parts[0] + "_Ctrl")
            cmds.select(group_var, r=True)
            cmds.rename(string_parts[0] + "_Ctrl_Grp")