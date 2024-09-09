def main():
    tasks = []
    while True:
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Supprimer une tâche")
        print("4. Mettre à jour une tâche")
        print("5. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            task = input("Entrez la tâche: ")
            add_task(tasks, task)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            task_number = int(input("Entrez le numéro de la tâche à supprimer: "))
            delete_task(tasks, task_number)
        elif choice == '4':
            task_number = int(input("Entrez le numéro de la tâche à mettre à jour: "))
            new_task = input("Entrez la nouvelle tâche: ")
            update_task(tasks, task_number, new_task)
        elif choice == '5':
            break
        else:
            print("Option invalide, veuillez réessayer.")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Tâche '{task}' ajoutée.")

def display_tasks(tasks):
    if not tasks:
        print("Aucune tâche à afficher.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Tâche '{removed_task}' supprimée.")
    else:
        print("Numéro de tâche invalide.")

def update_task(tasks, task_number, new_task):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1] = new_task
        print(f"Tâche numéro {task_number} mise à jour en '{new_task}'.")
    else:
        print("Numéro de tâche invalide.")

if __name__ == "__main__":
    main()

