def calc_new_height():
    width = float(input("Enter the current width: "))
    height = float(input("Enter the current height: "))
    new_width = float(input("Enter the desired width: "))
    ratio = width / height
    new_height = new_width/ratio
    print(f"The corresponding height is: {new_height}")

calc_new_height()