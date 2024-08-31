def main():
    time = input("write time here: ")
    final_time = convert(time)
    if final_time >= 7 and final_time <= 8:
        print("Breakfast Time")
    elif final_time >= 12 and final_time <= 13:
        print("Lunch Time")
    elif final_time >= 18 and final_time <= 19:
        print("Dinner Time")

def convert(x):
    hours, minutes = x.split(":")
    cal_time = float(hours) + float(float(minutes) / 60)
    return cal_time

if __name__ == "__main__":
    main()
