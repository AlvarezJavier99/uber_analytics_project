# Session Log

---

## Session 1

**Date:**  4/30/2026
**Goal:**  Figure out what columns to keep and what formulas ill be using 

### Tasks
- Clean Uber Data Of unnescceary Columns
- Deciede on what metrics are most valuable insight ful
  
### Completed

* Set up VS Code project structure
* Created clean_data.py script
* Installed and configured pandas correctly
* Resolved Python interpreter issues
* Fixed file path errors and located CSV file
* Successfully loaded Uber dataset into pandas
* Displayed dataset preview (df.head)
* Checked dataset size (df.shape)
* Reviewed column names
* Filtered dataset to only completed trips

### Problems

* Pandas not installed in correct Python environment
* Multiple Python versions causing confusion
* FileNotFoundError due to incorrect file path
* CSV file not in expected directory
* Path duplication issues when referencing Desktop

### Insights

* File paths must match actual file location exactly or code fails
* Always verify location using pwd and dir before debugging
* Relative paths only work when inside the correct project directory
* Filtering only completed trips is critical for accurate revenue analysis
* Dataset successfully loads, meaning environment is now correctly set up
* Ready to move into real data cleaning and metric creation next session

# Next Session Starting Point:

* Continue cleaning data
* Remove invalid trips (0 distance / 0 duration)
* Then create revenue_per_mile and revenue_per_hour


### Files Used
-  