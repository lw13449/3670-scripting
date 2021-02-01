import maya.cmds as cmds

sel = cmds.ls(selection=True)
obj = sel[0]
target = sel[1]

obj = cmds.parent(obj, target, a=True)[0]
cmds.makeIdentity(obj, apply=True, t=True, r=True, s=True, n=True)
cmds.delete(obj, ch=True)

obj_shapes = cmds.listRelatives(obj, shapes=True, fullPath=True)
target_shapes = cmds.listRelatives(target, shapes=True, fullPath=True)

for shape in obj_shapes:
    cmds.parent(shape, target, shape=True, relative=True)
    
cmds.delete(target_shapes)
cmds.delete(obj)