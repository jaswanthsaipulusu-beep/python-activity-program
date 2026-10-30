def shortlist_candidates(applicants, criteria, quota):
    eligible_applicants = []
    rejected_applicants = []
    
    for student, data in applicants.items():
        marks = data["marks"]
        attendance = data["attendance"]
        income = data["income"]
        
        if (marks >= criteria["min_marks"] and 
            attendance >= criteria["min_attendance"] and 
            income <= criteria["max_income"]):
            eligible_applicants.append({
                "student": student,
                "marks": marks,
                "attendance": attendance,
                "income": income
            })
        else:
            rejected_applicants.append(student)
            
    ranked_applicants = sorted(
        eligible_applicants,
        key=lambda x: (x["marks"], -x["income"]),
        reverse=True
    )
    
    selected_recipients = ranked_applicants[:quota]
    waitlist = ranked_applicants[quota:]
    
    return selected_recipients, waitlist, rejected_applicants

if __name__ == "__main__":
    criteria = {
        "min_marks": 75.0,
        "min_attendance": 80.0,
        "max_income": 500000.0
    }
    
    applicants_data = {
        "Student_1": {"marks": 88.5, "attendance": 85.0, "income": 400000.0},
        "Student_2": {"marks": 65.0, "attendance": 90.0, "income": 300000.0},
        "Student_3": {"marks": 92.0, "attendance": 92.0, "income": 450000.0},
        "Student_4": {"marks": 78.0, "attendance": 70.0, "income": 200000.0},
        "Student_5": {"marks": 85.0, "attendance": 88.0, "income": 350000.0}
    }
    
    scholarship_quota = 2
    selected, waitlisted, rejected = shortlist_candidates(applicants_data, criteria, scholarship_quota)
    print("Selected:", selected)
    print("Waitlisted:", waitlisted)
    print("Rejected:", rejected)
