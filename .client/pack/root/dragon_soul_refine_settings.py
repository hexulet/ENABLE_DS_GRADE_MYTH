# Search:
default_grade_need_count = [2, 2, 2, 2]
default_grade_fee = [30000, 50000, 70000, 100000]
# Replace with:
if app.ENABLE_DS_GRADE_MYTH:
	default_grade_need_count = [2, 2, 2, 2, 2]
	default_grade_fee = [30000, 50000, 70000, 100000, 150000]
else:
	default_grade_need_count = [2, 2, 2, 2]
	default_grade_fee = [30000, 50000, 70000, 100000]



# Search:
default_strength_max_table = [
	[2, 2, 3, 3, 4],
	[3, 3, 3, 4, 4],
	[4, 4, 4, 4, 4],
	[4, 4, 4, 4, 5],
	[4, 4, 4, 5, 6],
]
# Replace with:
if app.ENABLE_DS_GRADE_MYTH:
	default_strength_max_table = [
		[2, 2, 3, 3, 4],
		[3, 3, 3, 4, 4],
		[4, 4, 4, 4, 4],
		[4, 4, 4, 4, 5],
		[4, 4, 4, 5, 6],
		[4, 4, 4, 5, 6],
	]
else:
	default_strength_max_table = [
		[2, 2, 3, 3, 4],
		[3, 3, 3, 4, 4],
		[4, 4, 4, 4, 4],
		[4, 4, 4, 4, 5],
		[4, 4, 4, 5, 6],
	]