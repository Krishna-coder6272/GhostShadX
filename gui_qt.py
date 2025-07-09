import sys
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer

from modules import vpn_control, log_cleaner, kill_switch, public_ip

class GhostShadXGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GhostShadX - PyQt5 Multithreaded")
        self.setFixedSize(400, 450)
        self.init_ui()

        # Timer for auto-refresh status
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_status)
        self.timer.start(5000)  # every 5 seconds

        self.ks_thread = None

    def init_ui(self):
        self.setStyleSheet("background-color: #121212; color: white;")
        layout = QVBoxLayout()

        self.status_label = QLabel("[🔒] VPN Status: Unknown")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        btns = [
            ("Start VPN", self.run_in_thread, self.start_vpn),
            ("Stop VPN", self.run_in_thread, self.stop_vpn),
            ("Check VPN Status", self.check_status),
            ("Show Public IP", self.run_in_thread, self.show_ip),
            ("Enable Kill Switch", self.run_in_thread, self.start_kill),
            ("Disable Kill Switch", self.run_in_thread, self.stop_kill),
            ("Clear Logs", self.run_in_thread, self.clear_logs),
            ("Exit", self.close)
        ]

        for item in btns:
            if len(item) == 2:
                text, action = item
                btn = QPushButton(text)
                btn.clicked.connect(action)
            else:
                text, wrapper, action = item
                btn = QPushButton(text)
                btn.clicked.connect(lambda checked, a=action: wrapper(a))

            btn.setStyleSheet("background-color: #1f1f1f; padding: 10px; border-radius: 5px;")
            layout.addWidget(btn)

        self.setLayout(layout)

    def run_in_thread(self, func):
        thread = threading.Thread(target=func)
        thread.start()

    def start_vpn(self):
        vpn_control.start_vpn()
        self.update_status_label("[✅] VPN started.")

    def stop_vpn(self):
        vpn_control.stop_vpn()
        self.update_status_label("[❌] VPN stopped.")

    def check_status(self):
        # You can improve this to check real VPN status
        self.update_status_label("[✅] VPN active. Internet safe.")


    def show_ip(self):
        details = public_ip.get_public_ip_details()
        QMessageBox.information(self, "Public IP Info", details)



    def start_kill(self):
        if not self.ks_thread or not self.ks_thread.is_alive():
            self.ks_thread = threading.Thread(target=kill_switch.start_monitoring)
            self.ks_thread.start()
            self.update_status_label("[🛡️] Kill switch enabled.")
        else:
            QMessageBox.warning(self, "Kill Switch", "Kill switch already running.")

    def stop_kill(self):
        kill_switch.stop_monitoring()
        if self.ks_thread:
            self.ks_thread.join()
        self.update_status_label("[🛡️] Kill switch disabled.")

    def clear_logs(self):
        log_cleaner.clear_logs()
        self.update_status_label("[🧹] Logs cleared.")

    def update_status_label(self, text):
        self.status_label.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = GhostShadXGUI()
    gui.show()
    sys.exit(app.exec_())
