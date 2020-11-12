import maya.cmds as cmds

def SequentialRenamer(stringName):
    sel = cmds.ls(selection=True)
    selection_count = 1
    
    for obj in sel:
        selection_input = stringName.count("#")
        string_parts = stringName.partition("#" * selection_input)
        sequential_numbering = str(selection_count)
        
        if string_parts[1]:
            print "Characters are sequential."
            #change the # signs into a sequential number system
            #txt = str(selection_count)
            sequential_numbering = sequential_numbering.zfill(3)
            cmds.rename(string_parts[0] + sequential_numbering + string_parts[2])
            
        else:
            cmds.error("Characters are not sequential. Input another.")
            
        selection_count += 1            
            
SequentialRenamer("R_Leg_###_Jnt")