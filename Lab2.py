def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    x = [1.3,5.2,6.4,7.5,2.6]
    list = x #.split(",")
    num_list=[]
    for value in list:
        num_list.append(float(value))
    print(num_list)
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

def sort_temperature(val):
    return sorted(val)

def calc_median_temperature(val):
    x = len(val)%2
    y= int(len(val)/2)
    if x == 1:
        #odd
        middle = val[y]
    else:
        #even
        middle = (val[y]+val[y-1])/2
    return middle

def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    find_min_max(num_list)
    sorted = sort_temperature(num_list)
    print(sorted)
    print(calc_median_temperature(sorted))
    
if __name__ == "__main__":
    main()