# Search:
			self.inventoryTab.append(self.GetChild("Inventory_Tab_05"))
# Add after:
			if app.ENABLE_DS_GRADE_MYTH:
				self.inventoryTab.append(self.GetChild("Inventory_Tab_06"))



# Search:
		self.inventoryTab[4].SetEvent(ui.__mem_func__(self.SetInventoryPage),4)
# Add after:
		if app.ENABLE_DS_GRADE_MYTH:
			self.inventoryTab[5].SetEvent(ui.__mem_func__(self.SetInventoryPage),5)



# Search:
			self.inventoryTab[(page+1)%5].SetUp()
			self.inventoryTab[(page+2)%5].SetUp()
			self.inventoryTab[(page+3)%5].SetUp()
			self.inventoryTab[(page+4)%5].SetUp()
# Replace with:
		if app.ENABLE_DS_GRADE_MYTH:
			self.inventoryTab[(page+1)%6].SetUp()
			self.inventoryTab[(page+2)%6].SetUp()
			self.inventoryTab[(page+3)%6].SetUp()
			self.inventoryTab[(page+4)%6].SetUp()
			self.inventoryTab[(page+5)%6].SetUp()
		else:
			self.inventoryTab[(page+1)%5].SetUp()
			self.inventoryTab[(page+2)%5].SetUp()
			self.inventoryTab[(page+3)%5].SetUp()
			self.inventoryTab[(page+4)%5].SetUp()



# Search:
			return (self.DSKindIndex * 5 * player.DRAGON_SOUL_PAGE_SIZE) + self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE + local_slot_pos
# Replace with:
		if app.ENABLE_DS_GRADE_MYTH:
			return (self.DSKindIndex * player.DRAGON_SOUL_PAGE_COUNT * player.DRAGON_SOUL_PAGE_SIZE) + self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE + local_slot_pos
		else:
			return (self.DSKindIndex * 5 * player.DRAGON_SOUL_PAGE_SIZE) + self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE + local_slot_pos



# Search (pass this step if you don't found it):
	if app.ENABLE_MAILBOX:
		def SetCantMouseEventSlot(self, index):
			slot_index = index
			slot_index = index - (self.DSKindIndex * 5 * player.DRAGON_SOUL_PAGE_SIZE) - self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE
			
			if slot_index < 0 or slot_index >= player.DRAGON_SOUL_PAGE_SIZE:
				return
			
			self.wndItem.SetCantMouseEventSlot( slot_index )
# Replace with:
	if app.ENABLE_MAILBOX:
		def SetCantMouseEventSlot(self, index):
			slot_index = index
			if app.ENABLE_DS_GRADE_MYTH:
				slot_index = index - (self.DSKindIndex * player.DRAGON_SOUL_PAGE_COUNT * player.DRAGON_SOUL_PAGE_SIZE) - self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE
			else:
				slot_index = index - (self.DSKindIndex * 5 * player.DRAGON_SOUL_PAGE_SIZE) - self.inventoryPageIndex * player.DRAGON_SOUL_PAGE_SIZE
			
			if slot_index < 0 or slot_index >= player.DRAGON_SOUL_PAGE_SIZE:
				return
			
			self.wndItem.SetCantMouseEventSlot( slot_index )