import maya.cmds as cmds
import random

def RandomGenerator(numCopies, minX, maxX, minY, maxY, minZ, maxZ):
    sel = cmds.ls

    for obj in range(len(cmds.ls)):
        index = obj

        for obj in range(numCopies):
            tempObj = (cmds.duplicate(sel[index], rr=True))
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)

            cmds.select(tempObj)
            cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])


RandomGenerator(3,0,5,0,5,0,5)