import csv

# -----------------------------
# SAVE DATA TO CSV
# -----------------------------
def save_to_csv(name, marks, total, avg, grade):
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, marks, total, avg, grade])


# -----------------------------
# ANALYZE STUDENT
# -----------------------------
def analyze_student():
    name = input("Enter student name: ")

    marks = []
    for i in range(5):
        mark = float(input(f"Enter mark {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    avg = total / len(marks)

    # Grade logic
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("\nAverage:", round(avg, 2))
    print("Grade:", grade)

    save_to_csv(name, marks, total, avg, grade)
    print("✅ Data saved to students.csv\n")


# -----------------------------
# VIEW STUDENTS
# -----------------------------
def view_students():
    try:
        with open("students.csv", "r") as file:
            print("\n===== ALL STUDENTS =====")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No student data found.\n")


# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    while True:
        print("===== STUDENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            analyze_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.\n")


# -----------------------------
# RUN PROGRAM
# -----------------------------
if __name__ == "__main__":
    main()