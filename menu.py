def user_menu():
    menu = """
Temas disponibles:
- 1. Cyan
- 2. Aether
- 3. Glitch
"""

    while True:
        print(menu)
        user = input("Que tema quieres usar? [1/2/3]: ")
    
    
        if user == "1":
            return "cyan"
        elif user == "2":
            return "aether"
        elif user == "3":
            return "glitch"
        else:
            print("[Error] Opcion invalida ingrese 1, 2 o 3")