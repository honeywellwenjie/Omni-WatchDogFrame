# platform/fakeHardware_watchdog.py

class FakeHardwareWatchdog:
    def __init__(self, path=None):
        print("[FAKE] init fake watchdog")

    def kick(self):
        print("[FAKE] kick fake watchdog")
        return True

    def sett(self, timeout):
        print(f"[FAKE] set fake timeout {timeout}")
        return True

    def close(self):
        print("[FAKE] close fake watchdog")
        return True

