def diamond_printer():
    try:
        user_odd_integer = int(input("Please enter an odd integer: "))
        if user_odd_integer % 2 != 0:  
            for i in range(user_odd_integer // 2 + 1):
                spaces = ' ' * (user_odd_integer // 2 - i)
                stars = '*' * (2 * i + 1)
                print(spaces + stars)
            
            for i in range(user_odd_integer // 2 - 1, -1, -1):
                spaces = ' ' * (user_odd_integer // 2 - i)
                stars = '*' * (2 * i + 1)
                print(spaces + stars)
        else:
            print("Please provide an odd integer.")
            diamond_printer()
    except ValueError:  
        print("Please enter a valid integer.")
        diamond_printer() 

diamond_printer()
