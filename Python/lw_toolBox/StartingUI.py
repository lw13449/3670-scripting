import maya.cmds as cmds
import lw_toolBox
help(lw_toolBox)

starting_window = 'lwStartingWindowUI'

if cmds.window(starting_window, exists=True):
    cmds.deleteUI(starting_window)
        
renaming_window = cmds.window(starting_window, title = "ToolBox UI")
layout_type = cmds.rowColumnLayout()

import lw_toolBox.RenamerUIScript
renamerUI = lw_toolBox.RenamerUIScript.RenameUI()

cmds.button(label="Sequential Renmaer", parent = layout_type, c='renamerUI.create()')

import lw_toolBox.RandomUIScript

randomUI = lw_toolBox.RandomUIScript.RandomGenUI()

cmds.button(label="Random Generator", parent = layout_type, c='randomUI.create()')

import lw_toolBox.FreezeTran

freezeUI = lw_toolBox.FreezeTran.FreezeAndDelUI()

cmds.button(label="Freeze Transformations", parent = layout_type, c='freezeUI.FreezeTransform()')

import lw_toolBox.FreezeTran

freezeUI = lw_toolBox.FreezeTran.FreezeAndDelUI()

cmds.button(label="Delete History", parent = layout_type, c='freezeUI.DelHistory()')

import lw_toolBox.ParentingUIScript

parentGroupUI = lw_toolBox.ParentingUIScript.ParentGroup()

cmds.button(label="Parent Group", parent = layout_type, c='parentGroupUI.ParentGroup()')

import lw_toolBox.ParentingUIScript

parentGroupUI = lw_toolBox.ParentingUIScript.ParentScaleConstrain()

cmds.button(label="Parent Constraint", parent = layout_type, c='parentGroupUI.ParentScaleConstrain()')
cmds.text(label="Select Parent, then Child", parent = self.layout_var)

import lw_toolBox.ToggleAxisControlsUI

toggleAxisUI = lw_toolBox.ToggleAxisControlsUI.ToggleAxis()

cmds.button(label="Toggle Local Axis", parent = layout_type, c='toggleAxisUI.ToggleAxis()')

import lw_toolBox.ToggleAxisControlsUI

ChannelBoxUI = lw_toolBox.ToggleAxisControlsUI.ControlChannelUpdate()

cmds.button(label="Channel Box Jnt Orient", parent = layout_type, c='ChannelBoxUI.ControlChannelUpdate()')


cmds.showWindow(starting_window)