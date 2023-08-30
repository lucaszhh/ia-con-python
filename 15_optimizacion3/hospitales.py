import random

class Espacio():

    def __init__(self, altura, ancho, num_hospitales):
        """Crea un nuevo espacio de estado con las dimensiones dadas."""
        self.altura = altura
        self.ancho = ancho
        self.num_hospitales = num_hospitales
        self.casas = set()
        self.hospitales = set()

    def agregar_casa(self, fila, col):
        """Agrega una casa en una ubicación particular en el espacio de estado."""
        self.casas.add((fila, col))

    def espacios_disponibles(self):
        """Devuelve todas las celdas que no están siendo utilizadas actualmente por una casa o un hospital."""

        # Considera todas las celdas posibles
        candidatos = set(
            (fila, col)
            for fila in range(self.altura)
            for col in range(self.ancho)
        )

        # Elimina todas las casas y hospitales
        for casa in self.casas:
            candidatos.remove(casa)
        for hospital in self.hospitales:
            candidatos.remove(hospital)
        return candidatos

    def hill_climb(self, maximo=None, prefijo_imagen=None, log=False):
        """Realiza una búsqueda de hill_climb para encontrar una solución."""
        cuenta = 0

        # Comienza inicializando hospitales al azar
        self.hospitales = set()
        for i in range(self.num_hospitales):
            self.hospitales.add(random.choice(list(self.espacios_disponibles())))
        if log:
            print("Estado inicial: costo", self.obtener_costo(self.hospitales))
        if prefijo_imagen:
            self.generar_imagen(f"{prefijo_imagen}{str(cuenta).zfill(3)}.png")

        # Continúa hasta alcanzar el número máximo de iteraciones
        while maximo is None or cuenta < maximo:
            cuenta += 1
            mejores_vecinos = []
            mejor_costo_vecino = None

            # Considera todos los hospitales para mover
            for hospital in self.hospitales:

                # Considera todos los vecinos para ese hospital
                for reemplazo in self.obtener_vecinos(*hospital):  #hospital = (fila, columna) --> *hospital : fila, columna
                    # Genera un conjunto vecino de hospitales
                    vecino = self.hospitales.copy()
                    vecino.remove(hospital)
                    vecino.add(reemplazo)

                    # Verifica si el vecino es el mejor hasta ahora
                    costo = self.obtener_costo(vecino)
                    if mejor_costo_vecino is None or costo < mejor_costo_vecino:
                        mejor_costo_vecino = costo
                        mejores_vecinos = [vecino]
                    elif mejor_costo_vecino == costo:
                        mejores_vecinos.append(vecino)

            # Ninguno de los vecinos es mejor que el estado actual
            if mejor_costo_vecino >= self.obtener_costo(self.hospitales):
                return self.hospitales

            # Mover al vecino de mayor valor
            else:
                if log:
                    print(f"Encontrado vecino mejor: costo {mejor_costo_vecino}")
                self.hospitales = random.choice(mejores_vecinos)

            # Generar imagen
            if prefijo_imagen:
                self.generar_imagen(f"{prefijo_imagen}{str(cuenta).zfill(3)}.png")

    def reinicio_aleatorio(self, maximo, prefijo_imagen=None, log=False):
        """Repite la búsqueda de hill_climb varias veces."""
        mejores_hospitales = None
        mejor_costo = None

        # Repite la búsqueda de hill_climb un número fijo de veces
        for i in range(maximo):
            hospitales = self.hill_climb()
            costo = self.obtener_costo(hospitales)
            if mejor_costo is None or costo < mejor_costo:
                mejor_costo = costo
                mejores_hospitales = hospitales
                if log:
                    print(f"{i}: Encontrado nuevo mejor estado: costo {costo}")
            else:
                if log:
                    print(f"{i}: Encontrado estado: costo {costo}")

            if prefijo_imagen:
                self.generar_imagen(f"{prefijo_imagen}{str(i).zfill(3)}.png")

        return mejores_hospitales

    def obtener_costo(self, hospitales):
        """Calcula la suma de las distancias desde las casas al hospital más cercano."""
        costo = 0
        for casa in self.casas:
            costo += min(
                abs(casa[0] - hospital[0]) + abs(casa[1] - hospital[1])
                for hospital in hospitales
            )
        return costo

    def obtener_vecinos(self, fila, col):
        """Devuelve vecinos que aún no contienen una casa ni un hospital."""
        candidatos = [
            (fila - 1, col),
            (fila + 1, col),
            (fila, col - 1),
            (fila, col + 1)
        ]
        vecinos = []
        for f, c in candidatos:
            if (f, c) in self.casas or (f, c) in self.hospitales:
                continue
            if 0 <= f < self.altura and 0 <= c < self.ancho:
                vecinos.append((f, c))
        return vecinos

    def generar_imagen(self, nombre_archivo):
        """Genera una imagen con todas las casas y hospitales."""
        from PIL import Image, ImageDraw, ImageFont
        tamano_celda = 100
        borde_celda = 2
        tamano_costo = 40
        relleno = 10

        # Crea un lienzo en blanco
        img = Image.new(
            "RGBA",
            (self.ancho * tamano_celda,
             self.altura * tamano_celda + tamano_costo + relleno * 2),
            "white"
        )
        casa = Image.open("assets/images/Casa.png").resize(
            (tamano_celda, tamano_celda)
        )
        hospital = Image.open("assets/images/Hospital.png").resize(
            (tamano_celda, tamano_celda)
        )
        fuente = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 30)
        draw = ImageDraw.Draw(img)

        for i in range(self.altura):
            for j in range(self.ancho):

                # Dibujar celda
                rectangulo = [
                    (j * tamano_celda + borde_celda,
                     i * tamano_celda + borde_celda),
                    ((j + 1) * tamano_celda - borde_celda,
                     (i + 1) * tamano_celda - borde_celda)
                ]
                draw.rectangle(rectangulo, fill="black")

                if (i, j) in self.casas:
                    img.paste(casa, rectangulo[0], casa)
                if (i, j) in self.hospitales:
                    img.paste(hospital, rectangulo[0], hospital)

        # Agregar costo
        draw.rectangle(
            (0, self.altura * tamano_celda, self.ancho * tamano_celda,
             self.altura * tamano_celda + tamano_costo + relleno * 2),
            "black"
        )
        draw.text(
            (relleno, self.altura * tamano_celda + relleno),
            f"Costo: {self.obtener_costo(self.hospitales)}",
            fill="white",
            font=fuente
        )

        img.save(nombre_archivo)


# Crea un nuevo espacio y agrega casas al azar
espacio = Espacio(altura=10, ancho=20, num_hospitales=3)
for i in range(15):
    espacio.agregar_casa(random.randrange(espacio.altura), random.randrange(espacio.ancho))

# Utiliza la búsqueda local para determinar la ubicación de los hospitales
hospitales = espacio.hill_climb(prefijo_imagen="hospitales", log=True)