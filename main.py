from queue import PriorityQueue
import os

separator = "========================================="
projects_file = "projects.txt"
completed_file = "complete.txt"

unique_id = 0

class Project:
    def __init__(self, title, id, priority):
        self.title = title
        self.id = id
        self.priority = priority

    def print_info(self):
        print(separator)
        print(f"Document Title: {self.title}")
        print(f"Priority Level: {self.priority}")
        print(f"Document ID: {self.id}")


def main():
    project_queue = None
    running = True

    while running:
        print(separator)
        print("[1] Input Project Details")
        print("[2] View Projects")
        print("[3] Schedule Projects")
        print("[4] Get Projects")
        print("[5] Exit")
        choice = input("Enter choice: ")
        print(separator)
        input("Press enter to continue...")
        match choice:
            case "1":
                os.system("cls" if os.name == "nt" else "clear")
                title = input("Enter Document Title: ")
                priority = int(input("Enter Priority Level: "))
                print(separator)
                input_to_file(title, priority)
                print("Project Inputted")
                input("Press enter to continue...")
                unique_id += 1
                os.system("cls" if os.name == "nt" else "clear")
            case "2":
                os.system("cls" if os.name == "nt" else "clear")
                print("[1] One Project")
                print("[2] Completed")
                print("[3] All Projects")
                print(separator)
                v_choice = input("Enter choice: ")
                print(separator)
                if v_choice == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    find_project(projects_file)
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                elif v_choice == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    view_completed(completed_file)
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                elif v_choice == "3":
                    os.system("cls" if os.name == "nt" else "clear")
                    view_all(projects_file)
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Invalid choice!")
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
            case "3":
                os.system("cls" if os.name == "nt" else "clear")
                print("[1] Create Schedule")
                print("[2] View Updated Schedule")
                print(separator)
                s_choice = input("Enter choice: ")
                if s_choice == "1":
                    os.system("cls" if os.name == "nt" else "clear")
                    project_queue = PriorityQueue()
                    create_schedule(projects_file, project_queue)
                    print("Schedule created!")
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                elif s_choice == "2":
                    os.system("cls" if os.name == "nt" else "clear")
                    if project_queue is None:
                        print("No schedule found, please create a schedule first.")
                    elif project_queue.empty():
                        print("All projects have been completed!")
                    else:
                        view_schedule(project_queue)
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Invalid choice!")
                    input("Press enter to continue...")
                    os.system("cls" if os.name == "nt" else "clear")
            case "4":
                os.system("cls" if os.name == "nt" else "clear")
                if project_queue is None:
                    print("No schedule found, please create a schedule first.")
                elif project_queue.empty():
                    print("All projects have been completed!")
                else:
                    get_project(project_queue)
                input("Press enter to continue...")
                os.system("cls" if os.name == "nt" else "clear")
            case "5":
                print("Thank you for using my program! BYE")
                input("Press enter to continue...")
                os.system("cls" if os.name == "nt" else "clear")
                running = False
            case _:
                os.system("cls" if os.name == "nt" else "clear")
                print("Invalid choice")
                input("Press enter to continue...")
                os.system("cls" if os.name == "nt" else "clear")


def count_lines(filepath):
    try:
        with open(filepath, "r") as file:
            line_count = 0
            for line in file:
                line_count += 1
            return line_count
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1


def input_to_file(title, priority):
    with open(projects_file, "a") as file:
        file.write(separator + "\n")
        file.write(f"Document Title: {title}\n")
        file.write(f"Priority Level: {priority}\n")
        file.write(f"Document ID: {unique_id :04d}\n")


def find_project(filepath):
    doc_id = input("Enter document ID: ")
    with open(filepath, "r") as file:
        found = False
        lines = file.readlines()
        for i in range(count_lines(projects_file)):
            if lines[i].strip() == separator:
                title = lines[i + 1].strip().split(": ")
                prio = lines[i + 2].strip().split(": ")
                id = lines[i + 3].strip().split(": ")
                if id[0] == "Document ID" and id[1] == doc_id:
                    print(separator)
                    print(f"Document Title: {title[1]}")
                    print(f"Priority Level: {prio[1]}")
                    print(f"Document ID: {id[1]}")
                    found = True
                    break
        if not found:
            print("ID not found!")


def view_completed(filepath):
    with open(filepath, "r") as file:
        line = file.read()
        print("Completed Projects")
        print(line)


def view_all(filepath):
    with open(filepath, "r") as file:
        line = file.read()
        print("All Projects")
        print(line)


def create_schedule(filepath, project_queue):
    with open(filepath, "r") as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i].strip() == separator:
                title = lines[i + 1].strip().split(": ")
                prio = lines[i + 2].strip().split(": ")
                id = lines[i + 3].strip().split(": ")

                new_project = Project(title[1], int(id[1]), int(prio[1]))
                project_queue.put((new_project.priority, new_project))
            else:
                continue
        with open(projects_file, "w") as file:
            pass


def view_schedule(project_queue):
    temp_list = []
    while not project_queue.empty():
        item = project_queue.get()
        temp_list.append(item)
        item[2].print_info()

    for item in temp_list:
        project_queue.put(item)


def get_project(project_queue):
    priority, project = project_queue.get()
    with open(completed_file, "a") as file:
        file.write(separator + "\n")
        file.write(f"Document Title: {project.title}\n")
        file.write(f"Priority Level: {project.priority}\n")
        file.write(f"Document ID: {project.id}\n")
    print(f"Document: {project.title} is done!")


if __name__ == "__main__":
    main()
