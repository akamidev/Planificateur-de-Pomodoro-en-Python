import tkinter as tk
import time
from plyer import notification

# Paramètres de temps par défaut
WORK_TIME = 25 * 60  # 25 minutes
BREAK_TIME = 5 * 60  # 5 minutes

# Fonction pour démarrer le minuteur
def start_timer(duration, message):
    while duration:
        mins, secs = divmod(duration, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        root.update()
        time.sleep(1)
        duration -= 1
    notification.notify(
        title="Pomodoro Timer",
        message=message,
        timeout=5
    )

# Fonction pour la session de travail
def start_work():
    label.config(text="Session de Travail")
    start_timer(WORK_TIME, "Pause bien méritée !")

# Fonction pour la pause
def start_break():
    label.config(text="Pause !")
    start_timer(BREAK_TIME, "Retour au travail !")

# Interface graphique avec Tkinter
root = tk.Tk()
root.title("Planificateur de Pomodoro")

label = tk.Label(root, font=("Arial", 30), text="25:00")
label.pack()

work_button = tk.Button(root, text="Démarrer Session", command=start_work)
work_button.pack()

break_button = tk.Button(root, text="Démarrer Pause", command=start_break)
break_button.pack()

root.mainloop()