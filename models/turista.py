class Turista:
    def __init__(self, id_turista, nombre, documento, email, telefono): #constructores
        self._id_turista = id_turista #GUARDAR DATOS  
        self._nombre = nombre
        self._documento = documento
        self._email = email
        self._telefono = telefono

    def get_id(self):  #EL GET ES PARA VER LOS DATOS
        return self._id_turista

    def get_nombre(self):
        return self._nombre

    def set_email(self, nuevo_email): 
        self._email = nuevo_email # EL SET ES PARA PODER CAMBIAR DATOS

    def mostrar_info(self):
        return f"Turista: {self._nombre} - Email: {self._email}"
    

# ===== PRUEBA =====
t1 = Turista(1, "David", "123", "david@mail.com", "300")

print(t1.get_nombre())
print(t1.mostrar_info())

t1.set_email("nuevo@mail.com")
print(t1.mostrar_info())