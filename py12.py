def print_next_five_days():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    current_day_index = days_of_week.index("Saturday")

    for _ in range(5):
        print(days_of_week[current_day_index])
        current_day_index = (current_day_index + 1) % 7

print_next_five_days()
