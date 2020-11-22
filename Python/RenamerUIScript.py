import maya.cmds as cmds

class RenameUI():
    def __init__(self):
        self.renaming_window = "lwSequentialRenamingWindow"
        
    def create(self):
        self.delete()
            
        self.renaming_window = cmds.window(self.renaming_window, title = "Sequential Renamer", widthHeight = (200, 200))
        
        #cmds.columnLayout( columnAttach=('both', 5), rowSpacing=10, columnWidth=250 )
        self.layout_var = cmds.rowColumnLayout(parent=self.renaming_window,  numberOfColumns=5, columnWidth=[(1, 100), (2, 100), (3, 100), (4, 100), (5, 100)])
        
        cmds.text(label="Input", parent = self.layout_var)
        self.name_var = cmds.textField(parent = self.layout_var)
        cmds.button(label="Submit", parent = self.layout_var, c=lambda *x: self.SequentialRenamer())
        cmds.showWindow(self.renaming_window)
    
    def delete(self):
        if cmds.window(self.renaming_window, exists=True):
            cmds.deleteUI(self.renaming_window)

   
    def SequentialRenamer(self):
        sel = cmds.ls(selection=True)
        selection_count = 1
        field_string = cmds.textField(self.name_var, q=True, text=True)
        
        for obj in sel:
            selection_input = field_string.count("#")
            string_parts = field_string.partition("#" * selection_input)
            sequential_numbering = str(selection_count)
            
            if string_parts[1]:
                print "Characters are sequential."
                sequential_numbering = sequential_numbering.zfill(3)
                cmds.rename(string_parts[0] + sequential_numbering + string_parts[2])
                
            else:
                cmds.error("Characters are not sequential. Input another.")
                
            selection_count += 1 

renaming_window = RenameUI()

renaming_window.create()
