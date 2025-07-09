from modules import vpn_control, kill_switch, log_cleaner, public_ip
import threading

def main():
    kill_switch_thread = None

    while True:
        print("""
--- GhostShadX Main Menu ---
1. Start VPN
2. Stop VPN
3. Check VPN Status
4. Check Public IP
5. Clear System Logs
6. Start Kill Switch Monitor
7. Stop Kill Switch Monitor
0. Exit
""")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("[!] Please enter a valid number.")
            continue

        if choice == 1:
            vpn_control.start_vpn()
        elif choice == 2:
            vpn_control.stop_vpn()
        elif choice == 3:
            vpn_control.check_status()
        elif choice == 4:
            public_ip.show_ip()
        elif choice == 5:
            log_cleaner.clear_logs()
        elif choice == 6:
            if kill_switch_thread is None or not kill_switch_thread.is_alive():
                kill_switch_thread = kill_switch.start_monitoring()
            else:
                print("[!] Kill Switch already running.")
        elif choice == 7:
            if kill_switch_thread and kill_switch_thread.is_alive():
                kill_switch.stop_monitoring()
                kill_switch_thread.join()
            else:
                print("[!] Kill Switch not running.")
        elif choice == 0:
            print("Exiting GhostShadX. Goodbye!")
            if kill_switch_thread and kill_switch_thread.is_alive():
                kill_switch.stop_monitoring()
                kill_switch_thread.join()
            break
        else:
            print("[!] Invalid choice. Try again.")

if __name__ == "__main__":
    main()
