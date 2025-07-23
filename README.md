# Grade Generator Calculator - Lab 1

**Course:** Introduction to Python Programming and Databases  
**University:** African Leadership University  
**Trimester:** BSE Year 1 - Trimester 2

## 📋 Project Overview

This Grade Generator Calculator is a comprehensive Python program that manages student assignments, applies weighted grading, and computes final GPA with pass/fail determination.

## ✨ Features

### Core Functionality
- ✅ **Input Validation**: Validates assignment names, categories, weights, and grades
- ✅ **Weight Management**: Ensures category weights don't exceed 100%
- ✅ **Weighted Calculations**: Computes weighted grades for each assignment
- ✅ **Category Separation**: Handles Formative and Summative assignments separately
- ✅ **GPA Conversion**: Converts percentage grades to 5.0 GPA scale
- ✅ **Pass/Fail Logic**: Determines course outcome based on category averages

### Bonus Features
- 🎯 **Object-Oriented Design**: Uses `Assignment` and `GradeCalculator` classes
- 💾 **File Export**: Saves detailed reports to text files
- 🛡️ **Error Handling**: Comprehensive try-except blocks and input validation
- 🎨 **User-Friendly Interface**: Clear prompts and formatted output

## 🚀 How to Run

1. **Navigate to the project directory:**
   ```bash
   cd "Grade Calculator Generator"
   ```

2. **Run the program:**
   ```bash
   python grade_calculator.py
   ```

3. **Follow the prompts:**
   - Enter number of assignments
   - For each assignment, provide:
     - Assignment name
     - Category (Formative/Summative)
     - Weight percentage (0-100)
     - Grade percentage (0-100)

## 📊 GPA Scale

| Grade Range | GPA |
|-------------|-----|
| 90-100%     | 5.0 |
| 80-89%      | 4.0 |
| 70-79%      | 3.0 |
| 60-69%      | 2.0 |
| Below 60%   | 1.0 |

## 🎯 Pass/Fail Criteria

- **Pass**: Both Formative AND Summative category averages ≥ 50%
- **Fail and Repeat**: Either category average < 50%

## 📁 Project Structure

```
GradeGeneratorLab1/
├── grade_calculator.py    # Main program file
├── README.md             # This documentation
└── grade_report.txt      # Generated report (after running)
```

## 💡 Example Usage

```
🎓 Welcome to the Grade Generator Calculator!
==================================================

Enter number of assignments: 3

📝 Assignment 1:
--------------------
Name: Quiz 1
Category (Formative/Summative): Formative
Weight (%): 20
Grade (%): 85
✅ Added: Quiz 1: 85.0% (Weight: 20.0%)

📝 Assignment 2:
--------------------
Name: Midterm Exam
Category (Formative/Summative): Summative
Weight (%): 40
Grade (%): 78
✅ Added: Midterm Exam: 78.0% (Weight: 40.0%)

📝 Assignment 3:
--------------------
Name: Final Project
Category (Formative/Summative): Summative
Weight (%): 40
Grade (%): 88
✅ Added: Final Project: 88.0% (Weight: 40.0%)
```

## 🔧 Validation Features

- **Category Validation**: Only accepts "Formative" or "Summative"
- **Grade Range**: Ensures grades are between 0-100
- **Weight Limits**: Prevents category weights from exceeding 100%
- **Input Type Checking**: Handles invalid number inputs gracefully

## 📄 Report Generation

The program can generate detailed text reports including:
- Individual assignment details
- Category totals and weights
- Final grade and GPA
- Pass/fail status
- Timestamp of generation

## 🛠️ Technical Implementation

### Classes Used:
- **`Assignment`**: Represents individual assignments with automatic weighted grade calculation
- **`GradeCalculator`**: Main calculator with validation, computation, and reporting methods

### Key Methods:
- `validate_category()`: Ensures valid category input
- `validate_grade()`: Checks grade range (0-100)
- `validate_weight()`: Checks weight range (0-100)
- `check_weight_limit()`: Prevents exceeding 100% per category
- `calculate_category_totals()`: Computes weighted totals per category
- `convert_to_gpa()`: Converts percentage to GPA scale
- `determine_pass_fail()`: Applies pass/fail logic

## 🎓 Learning Objectives Met

1. ✅ Input handling and validation
2. ✅ Data storage using lists and dictionaries
3. ✅ Mathematical calculations (weighted averages)
4. ✅ Conditional logic (pass/fail determination)
5. ✅ File I/O operations
6. ✅ Object-oriented programming
7. ✅ Error handling and user experience
8. ✅ Code documentation and structure

## 🤝 Contributing

This is a lab assignment for educational purposes. Feel free to extend the functionality or improve the code structure as part of your learning journey!

---
**Author:** [Your Full Name]  
**Student ID:** [Your Student ID]  
**Date:** [Submission Date]
