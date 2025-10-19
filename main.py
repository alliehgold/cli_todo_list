import csv

def main():
    user_choice = input("Please enter one of the following options:\n" \
                        "1. Create a new to-do list\n" \
                        "2. Modify an existing to-do list\n" \
                        "3. Delete an existing to-do list\n" \
                        "3. View an existing to-do list\n")

    if user_choice == "1":
        list_name = input("Please enter the name of the list you would like to create:\n")
        header = ["Task Number", "Task", "Priority"]

        file_name = f"{list_name}.csv"


        with open(file_name, mode='w', newline='') as file:

            writer = csv.writer(file)

            writer.writerow(header)

            print(f"to-do list {list_name} successfully created!")

    if user_choice == "2":

        list_name = input("Please enter the name of the to-do list you would like to open:\n")

        file_name = f"{list_name}.csv"

        answer = "y"

        while answer == "y":

            with open(file_name, mode='r', newline='') as file:
                reader = csv.reader(file)

                rows = list(reader)

                index = len(rows)

            with open(file_name, mode='a', newline='') as file:

                writer = csv.writer(file)
                

                task = input("Please enter the task you would like to add:\n")

                priority = input("Is this low, medium, or high priority?\n")

                data = [index, task, priority]

                writer.writerow(data)

                print("Task added!")

            answer = input("Would you like to add another task to this list?\n")




if __name__ == '__main__':
    main()