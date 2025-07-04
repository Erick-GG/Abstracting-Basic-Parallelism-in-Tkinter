import time
from tkinter import Tk
from gui import BankGUI

class BankLogic:
    def __init__(self, instance_number, shared_balance, lock):
        self.instance_number = instance_number
        self.balance = shared_balance
        self.lock = lock
        self.gui = None

    def setup_window(self, window):
        self.gui = BankGUI(window, self.instance_number, self.withdraw, self.deposit)
        self.update_display()

    def withdraw(self):
        amount = 50  # Monto fijo de retiro
        with self.lock:
            print(f"[Usuario {self.instance_number}] {time.time():.2f} Intentando retirar {amount}...")
            time.sleep(2)  # Simulamos tiempo de proceso
            if self.balance.value >= amount:
                prev_balance = self.balance.value
                self.balance.value = prev_balance - amount
                print(f"[Usuario {self.instance_number}] {time.time():.2f} Retiro exitoso. Balance anterior: {prev_balance}, nuevo balance: {self.balance.value}")
                self.update_display()
                return True
            else:
                print(f"[Usuario {self.instance_number}] {time.time():.2f} Fondos insuficientes. Balance actual: {self.balance.value}")
                return False

    def deposit(self):
        amount = 50  # Monto fijo de depósito
        with self.lock:
            print(f"[Usuario {self.instance_number}] {time.time():.2f} Depositando {amount}...")
            time.sleep(2)  # Simulamos tiempo de proceso
            prev_balance = self.balance.value
            self.balance.value = prev_balance + amount
            print(f"[Usuario {self.instance_number}] {time.time():.2f} Depósito exitoso. Balance anterior: {prev_balance}, nuevo balance: {self.balance.value}")
            self.update_display()

    def update_display(self):
        if self.gui:
            self.gui.update_balance_display(self.balance.value)
        self.schedule_next_update()

    def schedule_next_update(self):
        if self.gui:
            self.gui.window.after(100, self.update_display)

def run_bank_app(instance_number, shared_balance, lock):
    root = Tk()
    bank = BankLogic(instance_number, shared_balance, lock)
    bank.setup_window(root)
    root.mainloop()

