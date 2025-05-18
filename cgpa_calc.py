# Grade point mapping based on the standard 5.0 scale
GRADE_POINTS = {
   'A': 5.0,
   'B': 4.0,
   'C': 3.0,
   'D': 2.0,
   'E': 1.0,
   'F': 0.0
}

def calculate_cgpa(courses=None):
   if courses is None:
       courses = []
       total_units = 0
       total_points = 0.0
       print("Enter your courses, units, and grades. Type 'done' when finished.")
       while True:
           course = input("Course name (or 'done' to finish): ").strip()
           if course.lower() == 'done':
               break
           try:
               units = int(input(f"Units for {course}: ").strip())
               grade = input(f"Grade for {course} (A-F): ").strip().upper()
               if grade not in GRADE_POINTS:
                   print("Invalid grade. Please enter a valid grade (A-F).")
                   continue
               points = GRADE_POINTS[grade] * units
               courses.append({"name": course, "units": units, "grade": grade, "points": points})
               total_units += units
               total_points += points
           except ValueError:
               print("Invalid input for units. Please enter a valid number.")
   else:
       total_units = sum(course['units'] for course in courses)
       total_points = sum(course['points'] for course in courses)

   if total_units == 0:
       print("No courses entered. Unable to calculate CGPA.")
   else:
       cgpa = total_points / total_units
       print(f"\nTotal Units: {total_units}")
       print(f"Total Points: {total_points:.2f}")
       print(f"CGPA: {cgpa:.2f}")


def simulate_inputs():
   sample_courses = [
       {"name": "Engineering Mathematics", "units": 3, "grade": "A", "points": GRADE_POINTS['A'] * 3},
       {"name": "Circuit Analysis", "units": 4, "grade": "A", "points": GRADE_POINTS['A'] * 4},
       {"name": "Digital Logic Design", "units": 2, "grade": "A", "points": GRADE_POINTS['A'] * 2},
       {"name": "Electromagnetic Fields", "units": 3, "grade": "A", "points": GRADE_POINTS['A'] * 3},
       {"name": "Signals and Systems", "units": 3, "grade": "A", "points": GRADE_POINTS['A'] * 3}
   ]
   print("Simulated Input Results:")
   calculate_cgpa(sample_courses)


if __name__ == "__main__":
   #calculate_cgpa()
   simulate_inputs()
