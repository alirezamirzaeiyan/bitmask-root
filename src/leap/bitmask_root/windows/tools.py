import _winreg as reg
import os
import subprocess


class Tools:
    def __init__(self):
        pass

    @staticmethod
    def windows_has_tap_device():
        adapter_key = 'SYSTEM\CurrentControlSet\Control\Class' \
                      '\{4D36E972-E325-11CE-BFC1-08002BE10318}'
        with reg.OpenKey(reg.HKEY_LOCAL_MACHINE, adapter_key) as adapters:
            try:
                for i in xrange(10000):
                    key_name = reg.EnumKey(adapters, i)
                    with reg.OpenKey(adapters, key_name) as adapter:
                        try:
                            component_id = reg.QueryValueEx(adapter, 'ComponentId')[0]
                            if component_id.startswith("tap0901"):
                                return True
                        except WindowsError:
                            pass
            except WindowsError:
                pass
        return False

    @staticmethod
    def is_ovpn_installed():
        try:
            cmd = subprocess.Popen('openvpn')
            return bool(cmd.communicate())
        except OSError:
            return False
