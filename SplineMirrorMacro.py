'''
A script for mirroring group/spline trees in maya. 
for right handed coordinates only, mirrors over the YZ plane.
allows for the renaming of all objects in tree, and recolors 
splines red or blue if using right/left naming conventions. 
'''

import pymel.core as pm

for item in pm.selected():
	if pm.objectType(item, isType='transform'):
		trans1=pm.getAttr(item.translateX)*(-1) 
		trans2=pm.getAttr(item.scaleX)*(-1)
		trans3=pm.getAttr(item.rotateY)*(-1)
		new=pm.duplicate(item)
		oldname='null'
		replacename='null'
		docolor=False
		color=0
		oldcolor=0
		temp=pm.promptDialog(
			message='Find in: \n'+item.name(),
			button=['Ok','Cancel'],
			defaultButton='Ok',
			cancelButton='Cancel',
			style='text'

			)
		if temp=='Ok':
			oldname=pm.promptDialog(
				query=True,
				text=True
				)

			temp=pm.promptDialog(
				message='Replace'+ oldname+' with',
				button=['Ok','Cancel'],
				defaultButton='Ok',
				cancelButton='Cancel',
				style='text'
				)
			if temp=='Ok':
				replacename=pm.promptDialog(
					query=True,
					text=True
					)
				if oldname.lower().find('l') and replacename.lower().find('r'):
					docolor=True
					color=6
					oldcolor=13
				elif oldname.lower().find('r') and replacename.lower().find('l'):
					docolor=True
					color=13
					oldcolor=6


				for i in new:
					i.rename(i.name().replace (str(oldname+'1'),str(replacename)))
					pm.setAttr(i.translateX, trans1)
					pm.setAttr(i.scaleX,trans2)
					pm.setAttr(i.rotateY,trans3)

					for j in pm.listRelatives(i, allDescendents=True, type='transform'):
						j.rename(j.name().replace (str(oldname),str(replacename)))
						if docolor and j.overrideColor.get()==oldcolor:
							j.overrideEnabled.set(True)
							j.overrideColor.set(color)

					

