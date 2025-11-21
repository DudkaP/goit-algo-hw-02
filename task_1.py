import queue
import time
import random

request_queue = queue.Queue()

request_id = 1

def generate_request():
    global request_id
    new_request = f"Заявка #{request_id}"
    request_queue.put(new_request)
    print(f"[+] Додано: {new_request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        req = request_queue.get()
        print(f"[✔] Обробляю: {req}")
        time.sleep(0.5)
    else:
        print("[!] Черга порожня, нічого обробляти")

def main():
    print("Система обробки заявок запущена.\nНатисніть Ctrl+C, щоб завершити.\n")

    try:
        while True:
            if random.random() < 0.7:
                generate_request()

            process_request()

            time.sleep(0.7)

    except KeyboardInterrupt:
        print("\nПрограма завершена користувачем.")

main()
