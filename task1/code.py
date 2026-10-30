def validate_seating_matrix(matrix, reserved_seats=None):
    if not matrix or not all(isinstance(row, list) for row in matrix):
        return False, ["Matrix is empty or not a valid 2D list."]
    
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        return False, ["Matrix dimensions are irregular (non-rectangular)."]
    
    reserved = reserved_seats if reserved_seats is not None else {"RESERVED", None, ""}
    seen_students = set()
    errors = []
    
    for r_idx, row in enumerate(matrix):
        for c_idx, seat in enumerate(row):
            if seat in reserved:
                continue
            if not isinstance(seat, str) or not seat.strip():
                errors.append(f"Invalid student allocation at row {r_idx}, col {c_idx}: {seat}")
                continue
            
            if seat in seen_students:
                errors.append(f"Duplicate roll number '{seat}' found at row {r_idx}, col {c_idx}.")
            else:
                seen_students.add(seat)
            
    if errors:
        return False, errors
    return True, ["Seating matrix is valid."]

if __name__ == "__main__":
    seating_matrix = [
        ["ROLL101", "ROLL102", None],
        ["ROLL103", "RESERVED", "ROLL105"],
        ["ROLL101", "ROLL106", "ROLL107"]
    ]
    
    is_valid, messages = validate_seating_matrix(seating_matrix)
    print(f"Is Valid: {is_valid}")
    print("Messages:", messages)
