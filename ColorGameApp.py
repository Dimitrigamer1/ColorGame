import random
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Color")

credit_label = ctk.CTkLabel(
    app,
    text="Created by Dim!",
    font=("times", 15),
)
credit_label.place(x=480, y=470)

ctk.CTkLabel(
    app, text="🎨Color Game",
    font=("Comic Sans MS", 30, "bold"),
).pack(pady=15)

seconds = {"Easy": 45, "Normal": 30, "Hard": 15}
best = 0

def change_df(value):
    time_lbl.configure(text=f"Time:⏱ {seconds[value]}")

difficulty = ctk.CTkSegmentedButton(
    app,
    values=list(seconds),
    font=("Comic Sans MS", 15, "bold"),
    command=change_df,
)

difficulty.pack(pady=15)
difficulty.set("Normal")

time_left = (seconds)[difficulty.get()]

colors = ["red", "blue", "green", "pink", "yellow", "orange", "white", "purple", "brown"]
score = 0

def next_word():
    random.shuffle(colors)
    word_lbl.configure(text=colors[0].upper(), text_color=colors[1])


def start():
    global score, time_left

    score = 0
    time_left = seconds[difficulty.get()]

    score_lbl.configure(text="Score: 0")
    time_lbl.configure(text=f"Time:⏱ {seconds[difficulty.get()]}")

    start_btn.configure(state="disabled")

    difficulty.configure(state="disabled")

    word_entry.configure(state="normal")
    word_entry.delete(0, "end")
    word_entry.focus()

    next_word()
    time_lbl.after(1000, countdown)


def check(event):
    global word_lbl, word_entry, score, score_lbl

    if word_entry.get().lower() == word_lbl.cget("text_color"):
        score += 1
        score_lbl.configure(text=f"Score: {score}")
        word_entry.delete(0, "end")
        next_word()
        flash()



def countdown():
    global time_left

    if time_left > 0:
        time_left -= 1
        time_lbl.configure(text=f"Time:⏱ {time_left}")
        time_lbl.after(1000, countdown)
    elif time_left == 0:
        end_game()


def end_game():
    global score, best

    word_entry.delete(0, "end")
    word_entry.configure(state="disabled")
    difficulty.configure(state="normal")
    start_btn.configure(state="normal", command=start)
    word_lbl.configure(text="STOP NOW", text_color="gray")
    time_lbl.configure(text=f"Time:⏱ {seconds[difficulty.get()]}")

    if score < 0:
        best_lbl.configure(text=f"Best score: {score}")
    elif score > best:
        best = score
        best_lbl.configure(text=f"Best score: {best}")
    elif score == best or score < best:
        best_lbl.configure(text=f"Best score: {best}")

def flash():
    word_lbl.configure(fg_color="#166534")
    word_lbl.after(100, lambda: word_lbl.configure(fg_color="#1a1a1a"))

    if button.get() == "Light":
        word_lbl.after(100, lambda: word_lbl.configure(fg_color="#CCCCCC"))
    else:
        word_lbl.after(100, lambda: word_lbl.configure(fg_color="#1a1a1a"))

score_lbl = ctk.CTkLabel(
    app,
    text="Score: 0",
    font=("Arial", 16),
    text_color="gold",
)
score_lbl.pack(pady=10)

time_lbl = ctk.CTkLabel(
    app,
    text=f"Time:⏱ {seconds[difficulty.get()]}",
    font=("Arial", 16),
)
time_lbl.pack(pady=10)

word_lbl = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 45, "bold"),
    fg_color="#1a1a1a", corner_radius=15,
    width=360, height=110
)
word_lbl.pack(pady=10)

word_entry = ctk.CTkEntry(
    app,
    placeholder_text="Color in English",
    state="disabled",
    font=("Arial", 15),
    width=250, height=30,
    justify="center",
)
word_entry.pack(pady=10)
word_entry.bind("<KeyRelease>", check)

start_btn = ctk.CTkButton(
    app,
    text="Start",
    command=start,
    corner_radius=100,
)
start_btn.pack(pady=10)

best_lbl = ctk.CTkLabel(
    app, text="Best Score: ",
    font=("Arial", 20, "bold"),
)

best_lbl.place(x=10, y=10)

app.bind("<Return>", lambda event: start_btn.invoke())

def change_bg(value):
    ctk.set_appearance_mode(value)

    if button.get() == "Light":
        word_lbl.configure(fg_color="#CCCCCC")
    else:
        word_lbl.configure(fg_color="#1a1a1a")


button = ctk.CTkSegmentedButton(
    app,
    values=["Dark", "Light"],
    command=change_bg,
)
button.place(x=500, y=10)
button.set("Dark")

app.geometry("600x500")
app.mainloop()