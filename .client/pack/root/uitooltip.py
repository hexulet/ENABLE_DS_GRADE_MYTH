# Search:
	## 헤어인가?
	def __IsHair(self, itemVnum):
		return (self.__IsOldHair(itemVnum) or 
		self.__IsNewHair(itemVnum) or
		self.__IsNewHair2(itemVnum) or
		self.__IsNewHair3(itemVnum) or
		self.__IsCostumeHair(itemVnum)
		)
# Replace with:
	## 헤어인가?
	def __IsHair(self, itemVnum):
		if app.ENABLE_DS_GRADE_MYTH:
			return (self.__IsOldHair(itemVnum) or 
			self.__IsNewHair(itemVnum) or
			self.__IsNewHair2(itemVnum) or
			self.__IsNewHair3(itemVnum))
		else:
			return (self.__IsOldHair(itemVnum) or 
			self.__IsNewHair(itemVnum) or
			self.__IsNewHair2(itemVnum) or
			self.__IsNewHair3(itemVnum) or
			self.__IsCostumeHair(itemVnum)
			)

	if not app.ENABLE_DS_GRADE_MYTH:
		def __IsCostumeHair(self, itemVnum):
			return self.__IsNewHair3(itemVnum - 100000)



# Search:
		elif self.__IsNewHair2(itemVnum):
			itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum))
# Add after:
		elif not app.ENABLE_DS_GRADE_MYTH and self.__IsCostumeHair(itemVnum):
			itemImage.LoadImage("icon/hair/%d.sub" % (itemVnum - 100000))