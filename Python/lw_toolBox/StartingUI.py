import maya.cmds as cmds
import lw_toolBox

class LW_ToolBox():
    def __init__(self):
        self.starting_window = 'lwStartingWindowUI'
        
    def create(self):
        self.delete()
            
        self.starting_window = cmds.window(self.starting_window, title = "ToolBox UI", widthHeight = (200, 200))

        self.layout_var = cmds.rowColumnLayout(parent=self.starting_window)
        
        cmds.button(label="Sequential Renamer UI", parent = self.layout_var, c=lambda *x: self.sequential_renamer())
        cmds.button(label="Random Generator UI", parent = self.layout_var, c=lambda *x: self.random_generator())
        cmds.button(label="Freeze Transformations", parent = self.layout_var, c=lambda *x: self.freeze_transforms())
        cmds.button(label="Delete History", parent = self.layout_var, c=lambda *x: self.delete_history())
        cmds.button(label="Parent Group", parent = self.layout_var, c=lambda *x: self.parent_group())
        cmds.button(label="Parent/Scale Constraint", parent = self.layout_var, c=lambda *x: self.parent_scale_constraint())
        cmds.text(label="Select Parent, then Child", parent = self.layout_var)
        cmds.button(label="Toggle Local Axis", parent = self.layout_var, c=lambda *x: self.toggle_local_axis())
        cmds.button(label="Create Locator", parent = self.layout_var, c=lambda *x: self.locator_generator())        
        cmds.button(label="Create Joints", parent = self.layout_var, c=lambda *x: self.joint_generator())               
        cmds.button(label="Controls UI", parent = self.layout_var, c=lambda *x: self.controls_UI())
        
        cmds.showWindow(self.starting_window)
    
    def delete(self):
        if cmds.window(self.starting_window, exists=True):
            cmds.deleteUI(self.starting_window)
            
    def sequential_renamer(self):
        import lw_toolBox.RenamerUIScript
        reload(lw_toolBox.RenamerUIScript)
        renamerUI = lw_toolBox.RenamerUIScript.RenameUI()
        renamerUI.create()
        
    def random_generator(self):
        import lw_toolBox.RandomUIScript
        reload(lw_toolBox.RandomUIScript)
        randomUI = lw_toolBox.RandomUIScript.RandomGenUI()
        randomUI.create()
        
    def freeze_transforms(self):
        import lw_toolBox.FreezeTran
        reload(lw_toolBox.FreezeTran)
        freezeUI = lw_toolBox.FreezeTran.FreezeAndDelUI()
        freezeUI.FreezeTransform()
        
    def delete_history(self):
        import lw_toolBox.FreezeTran
        reload(lw_toolBox.FreezeTran)
        freezeUI = lw_toolBox.FreezeTran.FreezeAndDelUI()
        freezeUI.DelHistory()
        
    def parent_group(self):
        import lw_toolBox.ParentingUIScript
        reload(lw_toolBox.ParentingUIScript)
        parentGroupUI = lw_toolBox.ParentingUIScript.ParentingUI()
        parentGroupUI.ParentGroup()
        
    def parent_scale_constraint(self):
        import lw_toolBox.ParentingUIScript
        reload(lw_toolBox.ParentingUIScript)
        parentGroupUI = lw_toolBox.ParentingUIScript.ParentingUI()
        parentGroupUI.ParentScaleConstrain()
        
    def toggle_local_axis(self):
        import lw_toolBox.ToggleAxisControlsUI
        reload(lw_toolBox.ToggleAxisControlsUI)
        ChannelBoxUI = lw_toolBox.ToggleAxisControlsUI.RiggingAxisUI()
        ChannelBoxUI.ControlChannelUpdate()
        
    def locator_generator(self):
        import lw_toolBox.LocatorGenerator
        reload(lw_toolBox.LocatorGenerator)
        ChannelBoxUI = lw_toolBox.LocatorGenerator.LocatorGen()
        ChannelBoxUI.create_locator()
        
    def joint_generator(self):
        import lw_toolBox.JointGenerator
        reload(lw_toolBox.JointGenerator)
        ChannelBoxUI = lw_toolBox.JointGenerator.JointGenerator()
        ChannelBoxUI.create_joints()
        
    def controls_UI(self):
        import lw_toolBox.ControlsUI
        reload(lw_toolBox.ControlsUI)
        ChannelBoxUI = lw_toolBox.ControlsUI.ControlGenerator()
        ChannelBoxUI.create()
        
starting_window = LW_ToolBox()

starting_window.create()