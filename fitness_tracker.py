import sqlite3

# Connect to the SQLite database
db = sqlite3.connect('fitness_tracker.db')
cursor = db.cursor() # Get a cursor object

# Create tables if they don't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS exercise_categories (
             id INTEGER PRIMARY KEY,
             category TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS exercises (
             id INTEGER PRIMARY KEY,
             name TEXT,
             category_id INTEGER,
             FOREIGN KEY (category_id) REFERENCES exercise_categories(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS workout_routines (
             id INTEGER PRIMARY KEY,
             name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS routine_exercises (
             id INTEGER PRIMARY KEY,
             workout_id INTEGER,
             exercise_id INTEGER,
             sets INTEGER,
             reps INTEGER,
             FOREIGN KEY (workout_id) REFERENCES workout_routines(id),
             FOREIGN KEY (exercise_id) REFERENCES exercises(id))''')

cursor.execute('''CREATE TABLE IF NOT EXISTS goals (
             id INTEGER PRIMARY KEY,
             name TEXT,
             category TEXT,
             target INTEGER)''')

# Main menu
def main_menu():
    print("\nFitness Tracker Menu:")
    print("1. Add exercise category")
    print("2. View exercise by category")
    print("3. Delete exercise by category")
    print("4. Create Workout Routine")
    print("5. View Workout Routine")
    print("6. View Exercise Progress")
    print("7. Set Fitness Goals")
    print("8. View Progress towards Fitness Goals")
    print("9. Quit")

# Function to add exercise category
def add_exercise_category():
    category = input("Enter new exercise category: ")
    cursor.execute("INSERT INTO exercise_categories (category) VALUES (?)", (category,))
    db.commit()
    print("Exercise category added successfully.")

# Function to view exercises by category
def view_exercises_by_category():
    category = input("Enter exercise category: ")
    cursor.execute("SELECT * FROM exercises WHERE category_id IN (SELECT id FROM exercise_categories WHERE category=?)", (category,))
    exercises = cursor.fetchall()
    if exercises:
        for exercise in exercises:
            print(exercise)
    else:
        print("No exercises found in this category.")

# Function to delete exercises by category
def delete_exercises_by_category():
    category = input("Enter exercise category: ")
    cursor.execute("DELETE FROM exercises WHERE category_id IN (SELECT id FROM exercise_categories WHERE category=?)", (category,))
    db.commit()
    print("Exercises deleted successfully.")

# Function to create workout routine
def create_workout_routine():
    name = input("Enter workout routine name: ")
    cursor.execute("INSERT INTO workout_routines (name) VALUES (?)", (name,))
    db.commit()
    print("Workout routine created successfully.")

# Function to view workout routine
def view_workout_routine():
    cursor.execute("SELECT * FROM workout_routines")
    routines = cursor.fetchall()
    if routines:
        for routine in routines:
            print(routine)
    else:
        print("No workout routines found.")
    
# Function to view exercise progress
def view_exercise_progress():
    pass  # Placeholder for future implementation

# Function to set fitness goals
def set_fitness_goals():
    name = input("Enter goal name: ")
    category = input("Enter goal category: ")
    target = int(input("Enter target value: "))
    cursor.execute("INSERT INTO goals (name, category, target) VALUES (?, ?, ?)", (name, category, target))
    db.commit()
    print("Fitness goal set successfully.")

# Function to view progress towards fitness goals
def view_progress_towards_fitness_goals():
    pass  # Placeholder for future implementation

# Main program loop
while True:
    main_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        add_exercise_category()
    elif choice == '2':
        view_exercises_by_category()
    elif choice == '3':
        delete_exercises_by_category()
    elif choice == '4':
        create_workout_routine()
    elif choice == '5':
        view_workout_routine()
    elif choice == '6':
        view_exercise_progress()
    elif choice == '7':
        set_fitness_goals()
    elif choice == '8':
        view_progress_towards_fitness_goals()
    elif choice == '9':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection to the database
db.close()
