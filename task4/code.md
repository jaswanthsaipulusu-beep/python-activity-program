## Problem Statement

Design a validation system to check student course registrations represented as tuples. The program must identify duplicate course registrations per student, validate selections against disallowed or incompatible course combinations, and flag students whose selections violate the specified rules.

---

## Algorithm

1. **Input Ingestion:** Accept a collection of student course registrations (as tuples or lists of tuples) and a set of invalid or conflicting course combination rules.
2. **Student Record Grouping:** Map each student identifier to their selected list of courses.
3. **Duplicate Check:** Iterate through each student's course selections to verify if duplicate course codes exist within the same registration.
4. **Rule Violation Check:** Compare the student's registered course set against defined prerequisite or mutually exclusive combination rules.
5. **Report Generation:** Compile a list of non-compliant students with their specific violations (duplicates or illegal combinations) and return the validation status.

---

## Flowchart

```mermaid
flowchart TD
    A[Start: Input Registrations & Rules] --> B[Group Registrations by Student]
    B --> C[Loop Through Each Student's Course Selections]
    C --> D{Are there duplicate courses?}
    D -- Yes --> E[Log Duplicate Registration Error] --> F
    D -- No --> F{Do selections violate combination rules?}
    F -- Yes --> G[Log Invalid Combination Error] --> H
    F -- No --> H[Mark Student Registration Valid]
    H --> I{More students to check?}
    I -- Yes --> C
    I -- No --> J[Return Validation Summary & Flagged Students] --> K[End]

```

---



---

## Sample Input

```python
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

```

---

## Sample Output

```json
{
  "Alice": [
    "Duplicate course registration found."
  ],
  "Bob": [
    "Invalid course combination: ['CS101', 'EE201']"
  ],
  "Charlie": [
    "Invalid course combination: ['PH101', 'PH102']"
  ]
}

```
