class Exercise:
    def _init_(self, name, duration_min, intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity


class User:
    def _init_(self, username):
        self.username = username
        self.exercises = []
        self.goals = {}

    def log_exercise(self, exercise):
        self.exercises.append(exercise)

    def calculate_calories_burned(self):
        total_calories = 0
        for exercise in self.exercises:
            calories = exercise.duration_min * exercise.intensity
            total_calories += calories
        return total_calories

    def set_goal(self, goal_type, target_value):
        self.goals[goal_type] = target_value

    def track_progress(self):
        total_calories_burned = self.calculate_calories_burned()
        if 'calories' in self.goals:
            goal_calories = self.goals['calories']
            progress_percentage = (total_calories_burned / goal_calories) * 100
            return progress_percentage
        else:
            return None


def log_exercise(user):
    name = input("Enter exercise name: ")
    duration = int(input("Enter duration (in minutes): "))
    intensity = int(input("Enter intensity (calories per minute): "))
    exercise = Exercise(name, duration, intensity)
    user.log_exercise(exercise)
    print("Exercise logged successfully!")


def set_goal(user):
    goal_type = input("Enter goal type (e.g., 'calories'): ")
    target_value = int(input("Enter target value: "))
    user.set_goal(goal_type, target_value)
    print("Goal set successfully!")


def track_progress(user):
    progress = user.track_progress()
    if progress is not None:
        print(f"Progress towards goal: {progress:.2f}%")
    else:
        print("No goal set for tracking progress.")


def main():
    username = input("Enter your username: ")
    user = User(username)

    while True:
        print("\nFitness Tracker Menu:")
        print("1. Log Exercise")
        print("2. Set Goal")
        print("3. Track Progress")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            log_exercise(user)
        elif choice == "2":
            set_goal(user)
        elif choice == "3":
            track_progress(user)
        elif choice == "4":
            print("Exiting the Fitness Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if _name_ == "_main_":
    main()
