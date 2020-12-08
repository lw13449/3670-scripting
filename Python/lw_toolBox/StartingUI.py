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


cmds.showWindow(starting_window)