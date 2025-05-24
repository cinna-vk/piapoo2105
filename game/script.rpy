define ell = Character("Ell",color="#ffe032")
define tasks = []

default speaker = "Ell"
default lines = [
    "Hello Manager! Welcome back.",
    "You can access your tasks, shop, \nand more.",
    "Let me know if you need any help!"
]
default line_index = 0
default line = lines[line_index]

label start:
    return

label create_task:
    #show ell at (0.35,0.58)
    hide screen main_menu
    call loadingscreen
    show screen create_task_screen
    python:
        title = renpy.input("What's the title of the task?")
        title = title.strip()

        description = renpy.input("Do you have a description to add??")
        description = description.strip()

        priority = renpy.input("What's the priority? (Low / Medium / High)")
        priority = priority.strip()

        due_date = renpy.input("When is it due? (DD-MM-YYYY)")
        due_date = due_date.strip()

    # Optional: confirm with the player
    ell "Great! Here's what you've entered:"
    
    ell "Do you want to save this task?"

    menu:
        "Do you want to save this task?"
        "Yes":
            $ new_task = Task(title, description, priority, due_date, "ONGOING")
            $ persistent.tasks = tasks.append(new_task)
            #$ renpy.save_persistent()
            "Task saved!"
        "No":
            "Okay, discarded the task."
