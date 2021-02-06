// Search:
	return col_type * DRAGON_SOUL_STEP_MAX * DRAGON_SOUL_BOX_SIZE + row_type * DRAGON_SOUL_BOX_SIZE;
// Replace with:
#ifdef ENABLE_DS_GRADE_MYTH
	return col_type * (DRAGON_SOUL_STEP_MAX + 1) * DRAGON_SOUL_BOX_SIZE + (row_type * DRAGON_SOUL_BOX_SIZE);
#else
	return col_type * DRAGON_SOUL_STEP_MAX * DRAGON_SOUL_BOX_SIZE + row_type * DRAGON_SOUL_BOX_SIZE;
#endif