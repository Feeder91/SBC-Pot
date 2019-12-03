import spidev
from time import sleep


class ADCSensor:
    def __init__(self):
        self.detectar_agua = 0
        self.humedad_agua_int = 1
        self.humedad_agua_ext = 2

    @staticmethod
    def read(self, channel):
        spi = spidev.SpiDev()
        spi.open(1, 0)
        rawData = spi.xfer([1, (8 + channel) << 4, 0])
        process_data = ((rawData[1] & 3) << 8) + rawData[2]
        return process_data

    def read_detectar_agua(self):
        water_detector_value = self.read(self.detectar_agua)
        sleep(0.5)
        return water_detector_value

    def read_detectar_humedad_int(self):
        humidity_detector_value = self.read(self, self.humedad_agua_int)
        sleep(0.5)
        return humidity_detector_value

    def read_detectar_humedad_ext(self):
        humidity_detector_value = self.read(self, self.humedad_agua_ext)
        sleep(0.5)
        return humidity_detector_value
