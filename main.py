import csv

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"


def analyze_students(file_name):
    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)

        print("\n📊 Student Grade Report\n")

        for row in reader:
            name = row['name']

            # Convert marks to integers
            marks = [
                int(row['math']),
                int(row['physics']),
                int(row['chemistry']),
                int(row['biology']),
                int(row['english'])
            ]

            total = sum(marks)
            percentage = total / len(marks)

            grade = calculate_grade(percentage)

            print(f"{name} → Total: {total}, %: {percentage:.2f}, Grade: {grade}")


if __name__ == "__main__":
    analyze_students("students.csv")