from models.reserva import Reserva

class ReservaHotel(Reserva):
    def _init_(self, id_reserva, turista, sucursal, fecha_reserva, hotel, fecha_entrada, fecha_salida):
        super()._init_(id_reserva, turista, sucursal, fecha_reserva)
        self._hotel = hotel
        self._fecha_entrada = fecha_entrada
        self._fecha_salida = fecha_salida
        hotel.reservar_plaza()

    def cancelar(self):
        super().cancelar()
        self._hotel.liberar_plaza()

    def get_hotel(self):
        return self._hotel
from models.reserva import Reserva

class ReservaVuelo(Reserva):
    def _init_(self, id_reserva, turista, sucursal, fecha_reserva, vuelo):
        super()._init_(id_reserva, turista, sucursal, fecha_reserva)
        self._vuelo = vuelo
        vuelo.reservar_plaza(turista)

    def cancelar(self):
        super().cancelar()
        self._vuelo.liberar_plaza(self._turista)

    def get_vuelo(self):
        return self._vuelo