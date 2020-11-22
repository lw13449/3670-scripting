import maya.cmds as cmds
import random

class RandomGenUI():
    def __init__(self):
        self.random_window = "lwSequentialRenamingWindow"
                
    def create(self):
        self.delete()
            
        self.random_window = cmds.window(self.random_window, title = "Sequential Renamer", widthHeight = (200, 200))
        
        #cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
        self.layout_var = cmds.rowColumnLayout(parent=self.random_window,  numberOfColumns=5, columnWidth=[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100)])
        
        cmds.text(label="Number of Duplicates", parent = self.layout_var)
        self.duplicate_num = cmds.intField(parent = self.layout_var)
        cmds.text(label="Min X", parent = self.layout_var)
        self.min_x = cmds.intField(parent = self.layout_var)
        cmds.text(label="Max X", parent = self.layout_var)
        self.max_x = cmds.intField(parent = self.layout_var)
        cmds.text(label="Min Y", parent = self.layout_var)
        self.min_y = cmds.intField(parent = self.layout_var)
        cmds.text(label="Max Y", parent = self.layout_var)
        self.max_y = cmds.intField(parent = self.layout_var)
        cmds.text(label="Min Z", parent = self.layout_var)
        self.min_z = cmds.intField(parent = self.layout_var)
        cmds.text(label="Max Z", parent = self.layout_var)
        self.max_z = cmds.intField(parent = self.layout_var)
        cmds.button(label="Submit", parent = self.layout_var, c=lambda *x: self.RandomGenerator())
        
        cmds.showWindow(self.random_window)
    
    def delete(self):
        if cmds.window(self.random_window, exists=True):
            cmds.deleteUI(self.random_window)
            
    def RandomGenerator(self):
        sel = cmds.ls(selection=True)
        field_int = cmds.intField(self.duplicate_num, q=True, value=True)
        min_x_int = cmds.intField(self.min_x, q=True, value=True)
        max_x_int = cmds.intField(self.max_x, q=True, value=True)
        min_y_int = cmds.intField(self.min_x, q=True, value=True)
        max_y_int = cmds.intField(self.max_x, q=True, value=True)
        min_z_int = cmds.intField(self.min_x, q=True, value=True)
        max_z_int = cmds.intField(self.max_x, q=True, value=True)
        
        for obj in range(len(cmds.ls(selection=True))):
            index = obj
            
            for obj in range(field_int):
                tempObj = (cmds.duplicate(sel[index], rr=True))
                randomX = random.uniform(min_x_int, max_x_int)
                randomY = random.uniform(min_y_int, max_y_int)
                randomZ = random.uniform(min_z_int, max_z_int)
    
                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])

random_window = RandomGenUI()

random_window.create()
