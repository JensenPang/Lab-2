def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = input()
    list = x.split(",")
    num_list=[]
    for value in list:
        num_list.append(float(value))
    return num_list

def calc_average(val):
    print("calc_average")
    average = sum(val)/len(val)
    print(average)
    return average

def find_min_max(val):
    min_num = round(min(val))
    max_num = round(max(val))
    print([min_num, max_num])
    return [min_num, max_num]

def sort_temperature():
    print()
def calc_median_temperature():
    print()

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)

if __name__ == "__main__":
    main()