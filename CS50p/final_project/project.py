import tkinter as tk
import ttkbootstrap as ttk
import re



def main():
    followers_set1 = process_txtwidget_input(text1)
    following_set1 = process_txtwidget_input(text2)

    create_file(followers_set1, "followers.txt")
    create_file(following_set1, "following.txt")

    followers_set2, following_set2 = count_followers_n_following("followers.txt", "following.txt")
    not_following_back, not_followed_back = analyze_followers(followers_set2, following_set2)

    final_output_label(not_following_back, not_followed_back, len(followers_set2), len(following_set2))



def process_txtwidget_input(text_widget):
    set1 = set()
    k = 1
    while True:
        start_index = f"{k}.0"
        end_index = f"{k}.end"
        line = text_widget.get(start_index, end_index).strip()
        if line:
            set1.add(line)
        else:
            break
        k += 1
    return set1



def create_file(set, filename):
    with open(filename, "w") as file:
        for line in set:
            try:
                file.write(f"{line}\n")
            except UnicodeEncodeError:
                line = line.replace("\u202f", "")
                file.write(f"{line}\n")



def count_followers_n_following(followers_file, following_file):
    followers_set2 = set()
    with open(followers_file, "r") as file:
        for line in file:
            if not re.match(r"^(?:\d{1,2}) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?:\d{4}), (?:\d{1,2}:\d{1,2})$", line.strip()):
                followers_set2.add(line.strip())

    following_set2 = set()
    with open(following_file, "r") as file:
        for line in file:
            if not re.match(r"^(?:\d{1,2}) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?:\d{4}), (?:\d{1,2}:\d{1,2})$", line.strip()):
                following_set2.add(line.strip())

    return followers_set2, following_set2



def analyze_followers(followers_set2, following_set2):
    not_following_back = sorted(following_set2 - followers_set2)
    not_followed_back = sorted(followers_set2 - following_set2)
    return not_following_back, not_followed_back



def final_output_label(not_following_back, not_followed_back, total_followers, total_following):
    label21_str.set(f"• Users I don't follow back:\n " + "\n  ".join(not_followed_back))
    label22_str.set(f"• Users not following me back:\n " + "\n  ".join(not_following_back))
    final_label_var.set(f"Followers: {total_followers}     Following: {total_following}")



# window
window = ttk.Window(themename="cyborg")
window.title("CS50P final Project | Kevin | kevgon8 ")
window.geometry("2050x800")

# title
label1 = ttk.Label(master=window, text="Instagram Followers Analyzer", font="Calibri 30 bold")
label1.pack()

# input field and button
input_frame = tk.Frame(master=window)
text1 = tk.Text(master=input_frame)
text2 = tk.Text(master=input_frame)
text1.pack(side="left", padx=13)
text2.pack(side="right", padx=13)
input_frame.pack(pady=32)

button = ttk.Button(master=window, text="Analyze", command=main)
button.pack()

# output field
output_frame = tk.Frame(master=window, borderwidth=10, relief=tk.SOLID)
label21_str = tk.StringVar()
label21 = ttk.Label(master=output_frame, textvariable=label21_str, font="Courier 10 bold")
label22_str = tk.StringVar()
label22 = ttk.Label(master=output_frame, textvariable=label22_str, font="Courier 10 bold")
label21.pack(side="left", padx=13)
label22.pack(side="right", padx=13)
output_frame.pack(pady=27)

final_label_var = tk.StringVar()
final_label = ttk.Label(master=window, textvariable=final_label_var, font="Helvetica 13 bold")
final_label.pack()

# run
window.mainloop()
