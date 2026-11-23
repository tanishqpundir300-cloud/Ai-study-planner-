from datetime import datetime, timedelta

# Base Class
class StudyPlanner:

    def __init__(self):
        self.subjects = []

    # Get Study Routine
    def get_routine(self):

        print("\n----- ENTER YOUR STUDY ROUTINE -----")

        self.leave_days = int(
            input("How many preparation leave days do you have? ")
        )

        self.start_time = input("Study starting time (HH:MM): ")
        self.end_time = input("Study ending time (HH:MM): ")

    # Add Subjects
    def add_subject(self):

        n = int(input("\nHow many subjects do you have? "))

        for i in range(n):

            print("\nSubject", i + 1)

            name = input("Enter subject name: ")

            exam_date = datetime.strptime(
                input("Enter exam date (DD-MM-YYYY): "),
                "%d-%m-%Y"
            )

            difficulty = int(input("Difficulty (1-5): "))
            chapters = int(input("Enter total chapters: "))

            subject = {
                "name": name,
                "date": exam_date,
                "difficulty": difficulty,
                "chapters": chapters
            }

            self.subjects.append(subject)

    # Calculate Priority
    def calculate_priority(self, subject):

        today = datetime.now()

        days_left = (subject["date"] - today).days

        return (100 - days_left) + (subject["difficulty"] * 2) + subject["chapters"]

    # Generate Timetable
    def generate_timetable(self):

        if len(self.subjects) == 0:
            print("Please add subjects first!")
            return

        self.subjects.sort(
            key=self.calculate_priority,
            reverse=True
        )

        first_exam = min(
            subject["date"] for subject in self.subjects
        )

        start_date = first_exam - timedelta(
            days=self.leave_days
        )

        print("\n===== YOUR PERSONAL STUDY TIMETABLE =====")

        for day in range(self.leave_days):

            date = start_date + timedelta(days=day)

            print("\n-----------------------------")
            print("DATE:", date.strftime("%d-%m-%Y"))
            print("-----------------------------")

            current = datetime.strptime(
                self.start_time, "%H:%M"
            )

            end = datetime.strptime(
                self.end_time, "%H:%M"
            )

            session = day % len(self.subjects)

            while current + timedelta(minutes=50) <= end:

                subject = self.subjects[session]

                study_end = current + timedelta(minutes=50)

                print(
                    current.strftime("%I:%M %p"),
                    "-",
                    study_end.strftime("%I:%M %p"),
                    ": Study", subject["name"]
                )

                current = study_end

                break_end = current + timedelta(minutes=10)

                if break_end <= end:
                    print(
                        current.strftime("%I:%M %p"),
                        "-",
                        break_end.strftime("%I:%M %p"),
                        ": Short Break"
                    )

                current = break_end

                session = (session + 1) % len(self.subjects)


# Child Class
class SmartStudyPlanner(StudyPlanner):

    def generate_timetable(self):

        print("\n===== SMART STUDY PLANNER =====")
        super().generate_timetable()


# Main Program
planner = SmartStudyPlanner()

planner.get_routine()
planner.add_subject()
planner.generate_timetable()

print("\nYour timetable has been generated successfully!")
