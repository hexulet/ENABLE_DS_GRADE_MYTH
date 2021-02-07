// Search:
	"grade_legendary",
// Add after:
#ifdef ENABLE_DS_GRADE_MYTH
	"grade_myth",
#endif



// Search:
				if (DRAGON_SOUL_GRADE_MAX != vec_probs.size())
				{
					sys_err ("In %s group of RefineStepTables, probability list size is not %d.",
						m_vecDragonSoulNames[i].c_str(), DRAGON_SOUL_GRADE_MAX);
					return false;
				}
// Replace with:
				if (DRAGON_SOUL_STEP_MAX != vec_probs.size())
				{
					sys_err ("In %s group of RefineStepTables, probability list size is not %d.", m_vecDragonSoulNames[i].c_str(), DRAGON_SOUL_STEP_MAX);
					return false;
				}