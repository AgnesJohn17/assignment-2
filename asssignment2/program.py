from plant import Plant

def run():
    print("============ PLANT GROWTH COMPARISON PROGRAM ============")
    print("Welcome! Simulate and compare the growth of two plants.")
    
    plant1_name = input("Enter name of the first plant: ")
    plant1_start_height = float(input("Enter starting height (cm) of the first plant: "))
    plant1_growth_rate = float(input("Enter daily growth rate of the first plant (cm/day): "))
    
    plant2_name = input("\nEnter name of the second plant: ")
    plant2_start_height = float(input("Enter starting height (cm) of the second plant: "))
    plant2_growth_rate = float(input("Enter daily growth rate for second plant (cm/day): "))
    
    plant1 = Plant(plant1_name, plant1_start_height, plant1_growth_rate)
    plant2 = Plant(plant2_name, plant2_start_height, plant2_growth_rate)
    
    while True:
        print("\n*** Menu ***")
        print("1) Display plant information")
        print("2) Projected growth over time")
        print("3) Project day when fastest rate is tallest")
        print("4) Change plant information")
        print("5) Quit program")
        
        choice = input("\nEnter your choice: ")
        
        if choice == "1":
            
            print(f"{plant1.name} is {plant1.height} cm tall and has a daily growth rate of {plant1.daily_growth_rate} cm/day")
            print(f"{plant2.name} is {plant2.height} cm tall and has a daily growth rate of {plant2.daily_growth_rate} cm/day")
            
        elif choice == "2":
            days = int(input("How many days of growth "))
            plant1.grow(days)
            plant2.grow(days)
            
            
            for day in range(1, days+1):
                
                print(f"{day}:{plant1.name} is {plant1.height} cm and {plant2.name} is {plant2.height} cm tall.")
            print(f"After {days}days, {plant1.name} will be {plant1.height} and {plant2.name} will be {plant2.height}cm tall")
             
            
        elif choice == "3":
            day = 0
            while plant1.is_taller(plant2):
                day += 1
                plant1.grow(1)
                plant2.grow(1)
            
            if day > 0:
                print(f"{day}:{plant1.name} is {plant1.height} and {plant2.name} is {plant2.height}cm tall.")
                print(f"\nAfter {day} days, {plant2.name} will be taller than or equal to {plant1.name}.")
           
            else:
                print(f"\n{plant2.name} is already taller than or equal to {plant1.name}.")
                
        elif choice == "4":
            plant1_name = input(f"\nEnter new name for {plant1.name}: ")
            plant1_start_height = float(input(f"Enter new starting height (cm) for {plant1.name}: "))
            plant1_growth_rate = float(input(f"Enter new daily growth rate for {plant1.name} (cm/day): "))
            
            plant2_name = input(f"\nEnter new name for {plant2.name}: ")
            plant2_start_height = float(input(f"Enter new starting height (cm) for {plant2.name}: "))
            plant2_growth_rate = float(input(f"Enter new daily growth rate for {plant2.name} (cm/day): "))
            
            plant1.name = plant1_name
            plant1.height = plant1_start_height
            plant1.daily_growth_rate = plant1_growth_rate
            
            plant2.name = plant2_name
            plant2.height = plant2_start_height
            plant2.daily_growth_rate = plant2_growth_rate
            
        elif choice == "5":
            print("\nThank you for using the program. Have a great day!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")
run()
