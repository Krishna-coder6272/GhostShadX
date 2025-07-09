import tkinter as tk
from tkinter import messagebox
from modules import vpn_control, kill_switch, log_cleaner, public_ip

class GhostShadXGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("GhostShadX VPN Control")
        self.root.geometry("400x400")
        self.root.configure(bg="#121212")

        self.status_label = tk.Label(root, text="[🔒] VPN Status: Unknown", fg="white", bg="#121212", font=("Arial", 12))
        self.status_label.pack(pady=10)

        tk.Button(root, text="Start VPN", width=20, command=self.start_vpn).pack(pady=5)
        tk.Button(root, text="Stop VPN", width=20, command=self.stop_vpn).pack(pady=5)
        tk.Button(root, text="Check VPN Status", width=20, command=self.check_status).pack(pady=5)
        tk.Button(root, text="Show Public IP", width=20, command=self.show_ip).pack(pady=5)

        tk.Button(root, text="Enable Kill Switch", width=20, command=self.start_kill_switch).pack(pady=5)
        tk.Button(root, text="Disable Kill Switch", width=20, command=self.stop_kill_switch).pack(pady=5)

        tk.Button(root, text="Clear Logs", width=20, command=self.clear_logs).pack(pady=5)
        tk.Button(root, text="Exit", width=20, command=root.quit).pack(pady=20)

        self.kill_switch_thread = None

    def start_vpn(self):
        vpn_control.start_vpn()
        self.check_status()

    def stop_vpn(self):
        vpn_control.stop_vpn()
        self.check_status()

    def check_status(self):
        # Real VPN status logic can be more detailed
        self.status_label.config(text="[✅] VPN active. Internet safe.")

    def show_ip(self):
        public_ip.show_ip()

    def start_kill_switch(self):
        if not self.kill_switch_thread or not self.kill_switch_thread.is_alive():
            self.kill_switch_thread = kill_switch.start_monitoring()
            messagebox.showinfo("Kill Switch", "Kill switch activated.")
        else:
            messagebox.showwarning("Kill Switch", "Already running.")

    def stop_kill_switch(self):
        kill_switch.stop_monitoring()
        if self.kill_switch_thread:
            self.kill_switch_thread.join()
        messagebox.showinfo("Kill Switch", "Kill switch deactivated.")

    def clear_logs(self):
        log_cleaner.clear_logs()

if __name__ == "__main__":
    root = tk.Tk()
    app = GhostShadXGUI(root)
    root.mainloop()
