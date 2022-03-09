import maya.cmds as cmds

class JointGenerator():
    def __init__(self):
        self.joint_window = "lwJntGen"

    def create_joints(self):
        sel = cmds.ls(selection=True)
        
        for obj in sel:
            joint_var = cmds.joint(obj)
            cmds.select(joint_var)
            cmds.rename(joint_var, obj+"_Jnt")
            cmds.parent(w=True)