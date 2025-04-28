from PyQt5.QtBluetooth import QBluetoothDeviceDiscoveryAgent, QBluetoothDeviceInfo
from PyQt5.QtCore import QCoreApplication, QTimer

class BluetoothScanner:
    def __init__(self):
        self.app = QCoreApplication([])  # PyQt benötigt eine Event-Schleife
        self.agent = QBluetoothDeviceDiscoveryAgent()
        self.agent.deviceDiscovered.connect(self.device_discovered)
        self.agent.finished.connect(self.scan_finished)
        self.device_found = False
        self.device_mac = None  # Variable für die MAC-Adresse

    def start_scan(self):
        print("Starte Bluetooth-Scan...")
        self.agent.start()

    def device_discovered(self, device: QBluetoothDeviceInfo):
        # Wenn das Gerät Cybershoes2 gefunden wurde, stoppe den Scan
        if device.name() == "Cybershoes2":
            self.device_mac = device.address().toString()  # Speichere die MAC-Adresse
            print(f"Gefundenes Gerät: {device.name()}, Adresse: {self.device_mac}")
            self.agent.stop()  # Beende den Scan, da das gewünschte Gerät gefunden wurde
            self.device_found = True

    def scan_finished(self):
        if not self.device_found:
            print("Cybershoes2 wurde nicht gefunden.")
        else:
            print("Scan abgeschlossen und Cybershoes2 gefunden.")
        self.app.quit()  # Beende die Anwendung nach Abschluss des Scans

if __name__ == "__main__":
    scanner = BluetoothScanner()
    scanner.start_scan()

    # Sicherstellen, dass der Scan richtig ausgeführt wird
    while not scanner.device_found:  # Solange der Scan nicht beendet ist
        scanner.app.processEvents()  # Event-Schleife fortsetzen, damit der Scan weiterläuft

    # Nach dem erfolgreichen Scan können wir die Event-Schleife nun beenden
    print("Scan abgeschlossen.")
