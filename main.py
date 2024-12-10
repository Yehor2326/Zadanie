import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter
import matplotlib.pyplot as plt

def generate_and_process():
    try:
        # Získanie hodnoty z textového poľa
        num_values = int(entry.get())
        if num_values <= 0:
            raise ValueError("Číslo musí byť kladné")
    except ValueError:
        messagebox.showerror("Chyba", "Zadajte kladné celé číslo.")
        return
    
    # Generovanie náhodných hodnôt
    random_values = [random.randint(-110, 5) for _ in range(num_values)]
    
    # Zoradenie hodnôt
    sorted_values = sorted(random_values)
    
    # Počítanie výskytu každej hodnoty
    occurrences = Counter(sorted_values)

    # Vykreslenie grafu pred triedením
    plt.figure(figsize=(8, 4))
    plt.bar(range(len(random_values)), random_values, color='blue', alpha=0.7)
    plt.title("Graf hodnôt pred triedením")
    plt.xlabel("Index")
    plt.ylabel("Hodnota")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    
    # Zobrazenie výsledkov
    results = (
        f"Generované hodnoty (pred triedením): {random_values}\n"
        f"Zoradené hodnoty: {sorted_values}\n"
        f"Počty výskytov: {dict(occurrences)}"
    )
    messagebox.showinfo("Výsledky", results)

# Vytvorenie hlavného okna
root = tk.Tk()
root.title("Programovacie techniky")
root.geometry("1100x300")

# Zobrazenie textu
title_label = tk.Label(root, text="Programovacie techniky", font=("Arial", 16))
title_label.pack(pady=10)

author_label = tk.Label(root, text="Yehor Vovchenko", font=("Arial", 12))
author_label.pack(pady=5)

task_label = tk.Label(root, text="24. Vygenerujte pole 20 náhodných hodnôt celých čísel od 5 do -110, zoradiť od najmenšieho čísla po najväčšie, vypísať koľko krát sa opakuje každá hodnota, vykresliť graf hodnôt pred triedením.")
task_label.pack(pady=5)

# Vstupné pole pre počet hodnôt (Voliteľný parameter)
entry_label = tk.Label(root, text="Zadajte počet hodnôt (predvolene 20):", font=("Arial", 12))
entry_label.pack(pady=5)

entry = tk.Entry(root, font=("Arial", 12))
entry.insert(0, "20")  # Nastavenie predvolenej hodnoty
entry.pack(pady=5)

# Tlačidlo na spustenie programu
start_button = tk.Button(root, text="Spustiť program", font=("Arial", 12), command=generate_and_process)
start_button.pack(pady=20)

# Spustenie aplikácie
root.mainloop()

