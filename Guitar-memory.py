from datetime import datetime
import csv
import os

Guitar_file = "Guitar.csv"
header = ['Date', 'how_long', 'song', 'discover']
new_guitar = not os.path.exists(Guitar_file)


def Show_records():
    with open("Guitar.csv", 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader, start=0):
            print(f"{index}: {row}")


What_need = input("Do you wanna add more data? (y/n/e): ")
if What_need.lower() == "y":
    Your_practice_time = input("Enter your time: ")
    Your_practice_song = input("Enter your song: ")
    Your_discover = input("Enter your discover: ")
    now = datetime.now().strftime("%Y-%m-%d")
    What_time = input("Please enter a valid time: ")
    if What_time == "":
        what_time = now
    else:
        what_time = What_time

    with open(Guitar_file, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar="\\")
        if new_guitar:
            writer.writerow(header)
            new_guitar = False
        writer.writerow([what_time, Your_practice_time, Your_practice_song,
                         Your_discover])

    print("Data saved to Guitar.csv")

elif What_need.lower() == 'n':
    Show_records()

elif What_need.lower() == 'e':
    Show_records()
    with open("Guitar.csv", 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        all_rows = list(csv_reader)
    Change = int(input(
        "What line do you want to change? (Enter the line number): "))
    try:
        if Change < 0 or Change >= len(all_rows):
            print("Please enter a valid munber")
    except ValueError:
        print("Please enter a valid number")
    print(all_rows[Change])
    for index, header_name in enumerate(header, start=0):
        print(f"{index}: {header_name}")
    Change_what = int(input("What column do you wanna change?: "))
    new_value = input("Enter the new value: ")
    index = Change_what
    all_rows[Change][index] = new_value
    with open("Guitar.csv", 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar="\\")
        writer.writerows(all_rows)
    print("Done")
