import pymel.core as pm

for item in pm.selected():
	if pm.objectType(item, isType='transform'):
		new=pm.duplicate(item)
		oldname='null'
		replacename='null'
		docolor=False
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
				if 'l' in oldname.lower() and 'r' in replacename.lower:
					docolor=True
					color=13
				else if 'r' in oldname.lower() and 'l' in replacename.lower:
					docolor=True
					color=6


				for i in new:
					i.rename(i.name().replace (str(old+'1'),str(replace)))
					for j in pm.listRelatives(i, allDescendents=True, type='transform'):
						j.rename(j.name().replace (str(old),str(replace)))
					
					
				i=pm.getAttr(item.translateX)*(-1)
				j=pm.getAttr(item.scaleX)*(-1)
				k=pm.getAttr(item.rotateY)*(-1)
				for duped in new:
					pm.setAttr(duped.translateX, i)
					pm.setAttr(duped.scaleX,j)
					pm.setAttr(duped.rotateY,k)
					pm.settattr(duped.overrideEnabled,1)
					pm.settattr(duped.overrideColor,color)

			
