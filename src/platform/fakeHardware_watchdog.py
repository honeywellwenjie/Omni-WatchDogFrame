# platform/fakeHardware_watchdog.py

class FakeHardwareWatchdog:
    def __init__(self, path=None):
        print("[FAKE] init watchdog")

    def kick(self):
        print("[FAKE] kick watchdog")

    def sett(self, timeout):
        print(f"[FAKE] set timeout {timeout}")

    def close(self):
        print("[FAKE] close watchdog")

