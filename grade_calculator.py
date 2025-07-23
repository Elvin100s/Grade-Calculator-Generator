#!/usr/bin/env python3
"""
Project: Lab 1 - Grade Generator Calculator
C

Grade Calculator that handles assignment data, applies weights,
categorizes grades, and computes final GPA with pass/fail status.
"""

import datetime
from typing import List, Dict, Tuple


class Assignment:
    """Represents a single assignment with name, category, weight, and grade."""
    
    def __init__(self, name: str, category: str, weight: float, grade: float):
        self.name = name
        self.category = category
        self.weight = weight
        self.grade = grade
        self.weighted_grade = (grade / 100) * weight
    
    def __str__(self):
        return f"{self.name}: {self.grade}% (Weight: {self.weight}%)"


class GradeCalculator:
    """Main calculator class for managing assignments and computing final grades."""
    
    def __init__(self):
        self.assignments: List[Assignment] = []
        self.formative_total_weight = 0.0
        self.summative_total_weight = 0.0
    
    def validate_category(self, category: str) -> bool:
        """Validate that category is either 'Formative' or 'Summative' (case-insensitive)."""
        return category.lower() in ["formative", "summative"]
    
    def normalize_category(self, category: str) -> str:
        """Convert category to proper case format."""
        return category.lower().capitalize()
    
    def validate_grade(self, grade: float) -> bool:
        """Validate that grade is between 0 and 100."""
        return 0 <= grade <= 100
    
    def validate_weight(self, weight: float) -> bool:
        """Validate that weight is between 0 and 100."""
        return 0 <= weight <= 100
    
    def check_weight_limit(self, category: str, weight: float) -> bool:
        """Check if adding this weight would exceed 100% for the category."""
        if category == "Formative":
            return (self.formative_total_weight + weight) <= 100
        else:  # Summative
            return (self.summative_total_weight + weight) <= 100
    
    def add_assignment(self, name: str, category: str, weight: float, grade: float) -> bool:
        """Add an assignment after validation. Returns True if successful."""
        # Normalize and validate inputs
        if not self.validate_category(category):
            print(f"❌ Error: Category must be 'Formative' or 'Summative', got '{category}'")
            return False
        
        # Convert to proper case
        category = self.normalize_category(category)
        
        if not self.validate_grade(grade):
            print(f"❌ Error: Grade must be between 0-100, got {grade}")
            return False
        
        if not self.validate_weight(weight):
            print(f"❌ Error: Weight must be between 0-100, got {weight}")
            return False
        
        if not self.check_weight_limit(category, weight):
            current_weight = self.formative_total_weight if category == "Formative" else self.summative_total_weight
            print(f"❌ Error: Adding {weight}% would exceed 100% limit for {category} category")
            print(f"   Current {category} weight: {current_weight}%")
            return False
        
        # Add assignment
        assignment = Assignment(name, category, weight, grade)
        self.assignments.append(assignment)
        
        # Update weight totals
        if category == "Formative":
            self.formative_total_weight += weight
        else:
            self.summative_total_weight += weight
        
        print(f"✅ Added: {assignment}")
        return True
    
    def calculate_category_totals(self) -> Tuple[float, float]:
        """Calculate total weighted grades for each category."""
        formative_total = sum(a.weighted_grade for a in self.assignments if a.category == "Formative")
        summative_total = sum(a.weighted_grade for a in self.assignments if a.category == "Summative")
        return formative_total, summative_total
    
    def calculate_final_grade(self) -> float:
        """Calculate the overall course grade."""
        formative_total, summative_total = self.calculate_category_totals()
        return formative_total + summative_total
    
    def convert_to_gpa(self, grade: float) -> float:
        """Convert percentage grade to GPA scale (0-5)."""
        if grade >= 90:
            return 5.0
        elif grade >= 80:
            return 4.0
        elif grade >= 70:
            return 3.0
        elif grade >= 60:
            return 2.0
        else:
            return 1.0
    
    def determine_pass_fail(self) -> str:
        """Determine if student passes based on category averages.
        
        Lab requirement: 'Pass: The student must score at or above the average total grade 
        for both the Formative and Summative categories.'
        
        Interpretation: 'Average total grade' = 50% of total possible points in each category.
        This is the standard academic interpretation.
        """
        formative_total, summative_total = self.calculate_category_totals()
        
        # Calculate weighted averages as percentages of total possible points
        formative_avg = formative_total / self.formative_total_weight * 100 if self.formative_total_weight > 0 else 0
        summative_avg = summative_total / self.summative_total_weight * 100 if self.summative_total_weight > 0 else 0
        
        # Pass if both categories achieve at least 50% (average total grade)
        if formative_avg >= 50 and summative_avg >= 50:
            return "✅ Passed the course"
        else:
            return "❌ Fail and Repeat"
    
    def display_summary(self):
        """Display comprehensive grade summary."""
        if not self.assignments:
            print("No assignments recorded.")
            return
        
        print("\n" + "="*60)
        print("📊 GRADE CALCULATOR SUMMARY")
        print("="*60)
        
        # Assignment details
        print("\n📋 Assignment Details:")
        print("-" * 60)
        formative_assignments = [a for a in self.assignments if a.category == "Formative"]
        summative_assignments = [a for a in self.assignments if a.category == "Summative"]
        
        if formative_assignments:
            print("🔵 Formative Assignments:")
            for assignment in formative_assignments:
                print(f"   • {assignment.name}: {assignment.grade}% (Weight: {assignment.weight}%, Weighted: {assignment.weighted_grade:.2f})")
        
        if summative_assignments:
            print("🔴 Summative Assignments:")
            for assignment in summative_assignments:
                print(f"   • {assignment.name}: {assignment.grade}% (Weight: {assignment.weight}%, Weighted: {assignment.weighted_grade:.2f})")
        
        # Category totals
        formative_total, summative_total = self.calculate_category_totals()
        print(f"\n📈 Category Totals:")
        print("-" * 30)
        print(f"🔵 Total Formative Grade: {formative_total:.2f}% (Weight: {self.formative_total_weight}%)")
        print(f"🔴 Total Summative Grade: {summative_total:.2f}% (Weight: {self.summative_total_weight}%)")
        
        # Final results
        final_grade = self.calculate_final_grade()
        gpa = self.convert_to_gpa(final_grade)
        result = self.determine_pass_fail()
        
        print(f"\n🎯 Final Results:")
        print("-" * 20)
        print(f"📊 Overall Grade: {final_grade:.2f}%")
        print(f"🎓 GPA: {gpa:.1f}/5.0")
        print(f"📋 Result: {result}")
        print("="*60)
    
    def save_to_file(self, filename: str = "grade_report.txt"):
        """Save grade report to a text file."""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("GRADE CALCULATOR REPORT\n")
                f.write("="*50 + "\n")
                f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write("Assignment Details:\n")
                f.write("-" * 30 + "\n")
                for assignment in self.assignments:
                    f.write(f"{assignment.category}: {assignment.name}\n")
                    f.write(f"  Grade: {assignment.grade}%, Weight: {assignment.weight}%\n")
                    f.write(f"  Weighted Score: {assignment.weighted_grade:.2f}\n\n")
                
                formative_total, summative_total = self.calculate_category_totals()
                final_grade = self.calculate_final_grade()
                gpa = self.convert_to_gpa(final_grade)
                result = self.determine_pass_fail()
                
                f.write(f"Category Totals:\n")
                f.write(f"Formative: {formative_total:.2f}%\n")
                f.write(f"Summative: {summative_total:.2f}%\n\n")
                f.write(f"Final Grade: {final_grade:.2f}%\n")
                f.write(f"GPA: {gpa:.1f}/5.0\n")
                # Remove emoji from result for file compatibility
                clean_result = result.replace('✅ ', '').replace('❌ ', '')
                f.write(f"Result: {clean_result}\n")
            
            print(f"✅ Report saved to {filename}")
        except Exception as e:
            print(f"❌ Error saving file: {e}")


def check_exit_command(user_input: str) -> bool:
    """Check if user wants to exit the program."""
    return user_input.lower().strip() in ['exit', 'quit', 'q']

def get_user_input():
    """Get and validate user input for assignment data."""
    calculator = GradeCalculator()
    
    print("🎓 Welcome to the Grade Generator Calculator!")
    print("=" * 50)
    print("💡 Tip: Type 'exit', 'quit', or 'q' at any time to exit the program")
    
    # Get number of assignments
    while True:
        try:
            user_input = input("\nEnter number of assignments: ").strip()
            if check_exit_command(user_input):
                return None  # Signal to exit
            
            num_assignments = int(user_input)
            if num_assignments <= 0:
                print("❌ Please enter a positive number.")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number.")
    
    # Collect assignment data
    for i in range(num_assignments):
        print(f"\n📝 Assignment {i + 1}:")
        print("-" * 20)
        
        while True:
            # Get assignment name
            name = input("Name: ").strip()
            if check_exit_command(name):
                return None  # Signal to exit
            if not name:
                print("❌ Assignment name cannot be empty.")
                continue
            
            # Get category
            while True:
                category = input("Category (Formative/Summative): ").strip()
                if check_exit_command(category):
                    return None  # Signal to exit
                if calculator.validate_category(category):
                    category = calculator.normalize_category(category)
                    break
                print("❌ Please enter 'Formative' or 'Summative' (case-insensitive)")
            
            # Get weight
            while True:
                try:
                    weight_input = input("Weight (%): ").strip()
                    if check_exit_command(weight_input):
                        return None  # Signal to exit
                    
                    weight = float(weight_input)
                    if calculator.validate_weight(weight):
                        if calculator.check_weight_limit(category, weight):
                            break
                        else:
                            current = calculator.formative_total_weight if category == "Formative" else calculator.summative_total_weight
                            print(f"❌ Weight {weight}% would exceed 100% limit for {category}")
                            print(f"   Current {category} total: {current}%")
                            print(f"   Maximum allowed: {100 - current}%")
                    else:
                        print("❌ Weight must be between 0-100")
                except ValueError:
                    print("❌ Please enter a valid number.")
            
            # Get grade
            while True:
                try:
                    grade_input = input("Grade (%): ").strip()
                    if check_exit_command(grade_input):
                        return None  # Signal to exit
                    
                    grade = float(grade_input)
                    if calculator.validate_grade(grade):
                        break
                    else:
                        print("❌ Grade must be between 0-100")
                except ValueError:
                    print("❌ Please enter a valid number.")
            
            # Try to add assignment
            if calculator.add_assignment(name, category, weight, grade):
                break
            else:
                print("❌ Failed to add assignment. Please try again.")
    
    return calculator


def main():
    """Main program function."""
    while True:
        try:
            # Get user input and create calculator
            calculator = get_user_input()
            
            # Check if user exited during input
            if calculator is None:
                print("\n👋 Exiting Grade Calculator. Goodbye!")
                break
            
            # Display results
            calculator.display_summary()
        
            # Ask if user wants to save to file
            save_choice = input("\n💾 Save report to file? (y/n): ").strip().lower()
            if save_choice in ['y', 'yes']:
                filename = input("Enter filename (or press Enter for 'grade_report.txt'): ").strip()
                if not filename:
                    filename = "grade_report.txt"
                calculator.save_to_file(filename)
            
            # Ask if user wants to calculate another set of grades
            restart_choice = input("\n🔄 Calculate grades for another student? (y/n): ").strip().lower()
            if restart_choice not in ['y', 'yes']:
                print("\n🎉 Thank you for using the Grade Calculator!")
                break
            else:
                print("\n" + "="*60)
            
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An unexpected error occurred: {e}")
            restart_choice = input("\n🔄 Try again? (y/n): ").strip().lower()
            if restart_choice not in ['y', 'yes']:
                break


if __name__ == "__main__":
    main()
