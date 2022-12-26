def JIJJJJJIIIIJJJIIJJIIJJIIJJIJIJIJIIJIIJJIJIJJIIIJIJJJIJ():
    from faker import Faker
    from termcolor import colored
    fake = Faker()
    def JIJJJJJIIIIJJJIIJJIIJJIIJJIJIIIIIJIJJJIJ():
        print(colored("Full Name:", "green"), f"{fake.prefix_male()} {fake.first_name_male()} {fake.last_name_male()}") 
        print(colored("Address:", "green"), f"{fake.address()}") 
        print(colored("Birthday:", "green"), f"{fake.date_of_birth(minimum_age=20, maximum_age=86)}")
        print("==================================")
    def JIJJJJJIIIIJJJIIJJJIIJJIJIIJIIIJIJJJIJ():
        print(colored("Full Name:", "green"), f"{fake.prefix_female()} {fake.first_name_female()} {fake.last_name_female()}")
        print(colored("Address:", "green"), f"{fake.address()}")
        print(colored("Birthday:", "green"), f"{fake.date_of_birth(minimum_age=20, maximum_age=86)}")
        print("==================================")
    print("[1] Male | [2] Female")
    JIJJJJJIIIIJJJIIJJIIJIIJJIIIIIJIJIJJJIJ = int(input("Select Option: "))
    if JIJJJJJIIIIJJJIIJJIIJIIJJIIIIIJIJIJJJIJ == 1:
        print("==================================")
        for i in range(3):
            JIJJJJJIIIIJJJIIJJIIJJIIJJIJIIIIIJIJJJIJ()
        input(colored("Press Enter to exit ...", 'red'))
    elif JIJJJJJIIIIJJJIIJJIIJIIJJIIIIIJIJIJJJIJ == 2:
        print("==================================")
        for i in range(3):
            JIJJJJJIIIIJJJIIJJJIIJJIJIIJIIIJIJJJIJ()
        input(colored("Press Enter to exit ...", 'red'))