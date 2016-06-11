'''
A script for mirroring group/spline trees in maya.
for right handed coordinates only, mirrors over the YZ plane.
allows for the renaming of all objects in tree, and recolors
splines red or blue if using right/left naming conventions.

Select a root group and run this script. It will prompt you
for a substring to replace(something like _R or _Right), and
for a new substring(_L and _Left, respectively).
'''

import pymel.core as pm
OLDNAME = ''
REPLACENAME = ''
DOCOLOR = False
COLOR = 0
OLDCOLOR = 0
for item in pm.selected():
    if pm.objectType(item, isType='transform'):
        trans1 = pm.getAttr(item.translateX)*(-1)
        trans2 = pm.getAttr(item.scaleX)*(-1)
        trans3 = pm.getAttr(item.rotateY)*(-1)
        trans4 = pm.getAttr(item.rotateZ)*(-1)

        temp = pm.promptDialog(
            message='Find in: \n'+item.name(),
            button=['Ok', 'Cancel'],
            defaultButton='Ok',
            cancelButton='Cancel',
            dismissString='Cancel',
            style='text',
            text=OLDNAME
            )
        if temp == 'Ok':
            oldname = pm.promptDialog(
                query=True,
                text=True
                )
        elif temp == 'Cancel':
            break
        temp = pm.promptDialog(
            message='Replace'+ oldname+' with',
            button=['Ok', 'Cancel'],
            defaultButton='Ok',
            cancelButton='Cancel',
            dismissString='Cancel',
            style='text',
            text=REPLACENAME
            )
        if temp == 'Ok':
            replacename = pm.promptDialog(
                query=True,
                text=True
                )
        elif temp == 'Cancel':
            break
        if oldname.lower().find('l') and replacename.lower().find('r'):
            docolor = True
            color = 6
            oldcolor = 13
        elif oldname.lower().find('r') and replacename.lower().find('l'):
            docolor = True
            color = 13
            oldcolor = 6
        new = pm.duplicate(item)
        for i in new:
            i.rename(i.name().replace(str(oldname+'1'), str(replacename)))
            pm.setAttr(i.translateX, trans1)
            pm.setAttr(i.scaleX, trans2)
            pm.setAttr(i.rotateY, trans3)
            pm.setAttr(i.rotateZ, trans4)
            for j in pm.listRelatives(i, allDescendents=True, type='transform'):
                j.rename(j.name().replace(str(oldname), str(replacename)))
                if docolor and j.overrideColor.get() == oldcolor:
                    j.overrideEnabled.set(True)
                    j.overrideColor.set(color)
