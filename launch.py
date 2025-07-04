from multiprocessing import Process, Value, Lock
from app import run_bank_app

if __name__ == "__main__":
    # Crear el balance compartido y el lock
    initial_balance = 500
    balance = Value('i', initial_balance)
    lock = Lock()

    # Crear y ejecutar los procesos
    p1 = Process(target=run_bank_app, args=(1, balance, lock))
    p2 = Process(target=run_bank_app, args=(2, balance, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
