class Plato:
    """
    Representa un plato del menú del restaurante.
    """
    def __init__(self, nombre, precio, descripcion):
        """
        Inicializa un nuevo objeto Plato.

        Args:
            nombre (str): El nombre del plato.
            precio (float): El precio del plato.
            descripcion (str): Una breve descripción del plato.
        """
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        """
        Retorna una representación legible del objeto Plato.
        """
        return f"{self.nombre} (${self.precio:.2f}) - {self.descripcion}"

class Pedido:
    """
    Representa un pedido realizado por un cliente.
    """
    def __init__(self, id_pedido, cliente):
        """
        Inicializa un nuevo objeto Pedido.

        Args:
            id_pedido (str): Un identificador único para el pedido.
            cliente (Cliente): El objeto Cliente que realiza el pedido.
        """
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.items = {}  # Diccionario para almacenar {Plato: cantidad}
        self.total = 0.0
        self.estado = "Pendiente" # Estados posibles: "Pendiente", "Preparando", "Listo", "Entregado", "Cancelado"

    def agregar_item(self, plato, cantidad):
        """
        Agrega un plato al pedido.

        Args:
            plato (Plato): El objeto Plato a agregar.
            cantidad (int): La cantidad de ese plato.
        """
        if cantidad > 0:
            self.items[plato] = self.items.get(plato, 0) + cantidad
            self.calcular_total()
            print(f"'{cantidad}x {plato.nombre}' agregado al pedido {self.id_pedido}.")
        else:
            print("La cantidad debe ser mayor que cero.")

    def remover_item(self, plato, cantidad):
        """
        Remueve una cantidad específica de un plato del pedido.

        Args:
            plato (Plato): El objeto Plato a remover.
            cantidad (int): La cantidad a remover.
        """
        if plato in self.items:
            if self.items[plato] <= cantidad:
                del self.items[plato]
                print(f"'{plato.nombre}' removido completamente del pedido {self.id_pedido}.")
            else:
                self.items[plato] -= cantidad
                print(f"'{cantidad}x {plato.nombre}' removido del pedido {self.id_pedido}.")
            self.calcular_total()
        else:
            print(f"'{plato.nombre}' no está en el pedido {self.id_pedido}.")

    def calcular_total(self):
        """
        Calcula el precio total del pedido.
        """
        self.total = sum(plato.precio * cantidad for plato, cantidad in self.items.items())

    def actualizar_estado(self, nuevo_estado):
        """
        Actualiza el estado del pedido.

        Args:
            nuevo_estado (str): El nuevo estado del pedido.
        """
        estados_validos = ["Pendiente", "Preparando", "Listo", "Entregado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
            print(f"Estado del pedido {self.id_pedido} actualizado a: {self.estado}.")
        else:
            print(f"Error: Estado '{nuevo_estado}' no válido.")

    def __str__(self):
        """
        Retorna una representación legible del objeto Pedido.
        """
        items_str = "\n".join([f"  - {cant}x {plato.nombre} (${plato.precio:.2f} c/u)" for plato, cant in self.items.items()])
        return (f"Pedido ID: {self.id_pedido}\n"
                f"Cliente: {self.cliente.nombre}\n"
                f"Estado: {self.estado}\n"
                f"Items:\n{items_str}\n"
                f"Total: ${self.total:.2f}")

class Cliente:
    """
    Representa un cliente del restaurante.
    """
    def __init__(self, nombre, telefono):
        """
        Inicializa un nuevo objeto Cliente.

        Args:
            nombre (str): El nombre del cliente.
            telefono (str): El número de teléfono del cliente.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.pedidos = [] # Lista para almacenar los objetos Pedido del cliente

    def __str__(self):
        """
        Retorna una representación legible del objeto Cliente.
        """
        return f"Cliente: {self.nombre} (Tel: {self.telefono})"

class Restaurante:
    """
    Gestiona el menú, los clientes y los pedidos del restaurante.
    """
    def __init__(self, nombre):
        """
        Inicializa un nuevo objeto Restaurante.

        Args:
            nombre (str): El nombre del restaurante.
        """
        self.nombre = nombre
        self.menu = {}  # Diccionario para almacenar platos, usando nombre como clave
        self.clientes = {} # Diccionario para almacenar clientes, usando teléfono como clave
        self.pedidos = {} # Diccionario para almacenar pedidos, usando id_pedido como clave
        self._next_pedido_id = 1 # Contador interno para generar IDs de pedidos

    def agregar_plato_menu(self, plato):
        """
        Agrega un plato al menú del restaurante.

        Args:
            plato (Plato): El objeto Plato a agregar.
        """
        if plato.nombre in self.menu:
            print(f"Error: El plato '{plato.nombre}' ya existe en el menú.")
        else:
            self.menu[plato.nombre] = plato
            print(f"Plato '{plato.nombre}' agregado al menú.")

    def registrar_cliente(self, cliente):
        """
        Registra un cliente en el restaurante.

        Args:
            cliente (Cliente): El objeto Cliente a registrar.
        """
        if cliente.telefono in self.clientes:
            print(f"Error: El cliente con teléfono {cliente.telefono} ya está registrado.")
        else:
            self.clientes[cliente.telefono] = cliente
            print(f"Cliente '{cliente.nombre}' registrado.")

    def crear_pedido(self, telefono_cliente):
        """
        Crea un nuevo pedido para un cliente.

        Args:
            telefono_cliente (str): El número de teléfono del cliente que realiza el pedido.

        Returns:
            Pedido or None: El objeto Pedido creado, o None si el cliente no existe.
        """
        cliente = self.clientes.get(telefono_cliente)
        if not cliente:
            print(f"Error: Cliente con teléfono {telefono_cliente} no encontrado.")
            return None

        pedido_id = f"PED-{self._next_pedido_id:04d}"
        self._next_pedido_id += 1
        nuevo_pedido = Pedido(pedido_id, cliente)
        self.pedidos[pedido_id] = nuevo_pedido
        cliente.pedidos.append(nuevo_pedido)
        print(f"Pedido {pedido_id} creado para {cliente.nombre}.")
        return nuevo_pedido

    def mostrar_menu(self):
        """
        Muestra todos los platos disponibles en el menú.
        """
        print("\n--- Menú del Restaurante ---")
        if self.menu:
            for plato_nombre, plato in self.menu.items():
                print(plato)
        else:
            print("El menú está vacío.")

    def mostrar_pedidos_activos(self):
        """
        Muestra todos los pedidos que no están en estado 'Entregado' o 'Cancelado'.
        """
        print("\n--- Pedidos Activos ---")
        activos = [p for p in self.pedidos.values() if p.estado not in ["Entregado", "Cancelado"]]
        if activos:
            for pedido in activos:
                print(f"\n{pedido}")
                print("-" * 20)
        else:
            print("No hay pedidos activos en este momento.")

# --- Ejemplo de Uso del Sistema de Pedidos de Restaurante ---
if __name__ == "__main__":
    mi_restaurante = Restaurante("La Cuchara de Oro")

    # Crear objetos Plato y agregarlos al menú
    pizza = Plato("Pizza Pepperoni", 12.50, "Deliciosa pizza con pepperoni y queso mozzarella.")
    pasta = Plato("Pasta Carbonara", 10.00, "Clásica pasta con huevo, tocino y queso parmesano.")
    ensalada = Plato("Ensalada César", 8.00, "Lechuga romana, crutones, queso parmesano y aderezo César.")
    refresco = Plato("Refresco Coca-Cola", 2.00, "Bebida refrescante.")

    mi_restaurante.agregar_plato_menu(pizza)
    mi_restaurante.agregar_plato_menu(pasta)
    mi_restaurante.agregar_plato_menu(ensalada)
    mi_restaurante.agregar_plato_menu(refresco)
    print("-" * 30)

    mi_restaurante.mostrar_menu()
    print("-" * 30)

    # Crear objetos Cliente y registrarlos
    cliente1 = Cliente("Sofía Fernández", "555-1234")
    cliente2 = Cliente("Diego López", "555-5678")

    mi_restaurante.registrar_cliente(cliente1)
    mi_restaurante.registrar_cliente(cliente2)
    print("-" * 30)

    # Crear pedidos
    pedido1 = mi_restaurante.crear_pedido("555-1234") # Pedido de Sofía
    if pedido1:
        pedido1.agregar_item(pizza, 1)
        pedido1.agregar_item(refresco, 2)
        pedido1.agregar_item(ensalada, 1)
    print("-" * 30)

    pedido2 = mi_restaurante.crear_pedido("555-5678") # Pedido de Diego
    if pedido2:
        pedido2.agregar_item(pasta, 2)
        pedido2.agregar_item(refresco, 1)
    print("-" * 30)

    # Mostrar pedidos activos
    mi_restaurante.mostrar_pedidos_activos()
    print("-" * 30)

    # Actualizar estado de un pedido
    if pedido1:
        pedido1.actualizar_estado("Preparando")
        pedido1.actualizar_estado("Listo")
    print("-" * 30)

    # Mostrar pedidos activos después de actualización
    mi_restaurante.mostrar_pedidos_activos()
    print("-" * 30)

    # Remover un item de un pedido
    if pedido1:
        pedido1.remover_item(refresco, 1)
    print("-" * 30)

    # Mostrar el pedido actualizado
    if pedido1:
        print(f"\n{pedido1}")
    print("-" * 30)

    # Finalizar un pedido
    if pedido1:
        pedido1.actualizar_estado("Entregado")
    print("-" * 30)

    # Mostrar pedidos activos (pedido1 ya no debería aparecer)
    mi_restaurante.mostrar_pedidos_activos()