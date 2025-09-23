def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    print(f"The number of days is: {get_days(hours, minutes, seconds):.4f}")

def get_days(hours, minutes, seconds):
    days_hours = hours/24
    days_minutes = minutes/60/24
    days_seconds = seconds/60/60/24
    number_of_days = days_hours+days_minutes+days_seconds
    return number_of_days

convert_to_days()