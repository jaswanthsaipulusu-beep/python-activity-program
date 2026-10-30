def validate_registrations(registrations, invalid_combinations):
    student_courses = {}
    for student, course in registrations:
        if student not in student_courses:
            student_courses[student] = []
        student_courses[student].append(course)
    
    violations = {}
    
    for student, courses in student_courses.items():
        student_violations = []
        
        if len(courses) != len(set(courses)):
            student_violations.append("Duplicate course registration found.")
            
        course_set = set(courses)
        for rule in invalid_combinations:
            if rule.issubset(course_set):
                student_violations.append(f"Invalid course combination: {list(rule)}")
                
        if student_violations:
            violations[student] = student_violations
            
    return violations

if __name__ == "__main__":
    registration_data = [
        ("Alice", "CS101"),
        ("Alice", "MA101"),
        ("Alice", "CS101"),
        ("Bob", "CS101"),
        ("Bob", "EE201"),
        ("Charlie", "PH101"),
        ("Charlie", "PH102")
    ]
    
    forbidden_rules = [
        {"CS101", "EE201"},
        {"PH101", "PH102"}
    ]
    
    invalid_records = validate_registrations(registration_data, forbidden_rules)
    print("Validation Violations:", invalid_records)
