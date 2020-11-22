import maya.cmds as cmds

renaming_window = "lwSequentialRenamingWindow"
    
if cmds.window(renaming_window, exists=True):
    cmds.deleteUI(renaming_window)
        
renaming_window = cmds.window(renaming_window, title = "Sequential Renamer", widthHeight = (200, 200))
    
form = cmds.formLayout(numberOfDivisions=100)
    
    #cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
layout_var = cmds.rowColumnLayout(parent=renaming_window,  numberOfColumns=5, columnWidth=[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100)])
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.button(label="Reset Tool", parent = layout_var)
cmds.button(label="Tool Help", parent = layout_var)
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.text(label="Input", parent = layout_var)
name_var = cmds.textField(parent = layout_var)
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.canvas()
cmds.button(label="Submit", parent = layout_var, c='SequentialRenamer(name_var)')
 
cmds.formLayout(form, edit=True, )
    
cmds.showWindow(renaming_window)