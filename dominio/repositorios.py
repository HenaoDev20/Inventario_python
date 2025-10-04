from abc import ABC, abstractmethod
from dominio.producto import Producto
from dominio.cliente import Cliente
from dominio.venta import Venta

# RepositorioProducto es una interfaz que define los métodos que cualquier
# implementación concreta debe proporcionar para gestionar productos.
class RepositorioProducto(ABC):

    @abstractmethod
    def guardar(self, producto: Producto):
        "Guarda un producto en el repositorio."
        pass

    @abstractmethod
    def obtener(self,id:int)->Producto:
        "Obtiene un producto por su ID."
        pass

    @abstractmethod
    def listar(self) -> list[Producto]:
        "Lista todos los productos en el repositorio."
        pass

# RepositorioCliente es una interfaz que define los métodos que cualquier
# implementación concreta debe proporcionar para gestionar clientes.
class RepositorioCliente(ABC):

    @abstractmethod
    def guardar(self, cliente: Cliente):
        "Guarda un cliente en el repositorio."
        pass

    @abstractmethod
    def obtener(self,id:int)->Cliente:
        "Obtiene un cliente por su ID."
        pass

    @abstractmethod
    def listar(self) -> list[Cliente]:
        "Lista todos los clientes en el repositorio."
        pass
# RepositorioVenta es una interfaz que define los métodos que cualquier
# implementación concreta debe proporcionar para gestionar ventas.
class RepositorioVenta(ABC):

    @abstractmethod
    def guardar(self, venta: Venta):
        "Guarda una venta en el repositorio."
        pass

    @abstractmethod
    def obtener(self,id:int)->Venta:
        "Obtiene una venta por su ID."
        pass

    @abstractmethod
    def listar(self) -> list[Venta]:
        "Lista todas las ventas en el repositorio."
        pass