import py5


def setup():
    py5.size(500, 500)  # Tamaño del lienzo
    py5.background(30)  # Fondo oscuro


def draw():
    py5.fill(255, 0, 0)  # Color de relleno rojo
    py5.ellipse(py5.mouse_x, py5.mouse_y, 50, 50)
    # Dibuja círculos en la posición del mouse


py5.run_sketch()