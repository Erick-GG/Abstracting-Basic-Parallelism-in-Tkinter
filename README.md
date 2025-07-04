# Abstracting-Basic-Parallelism-in-Tkinter
Basic example and concepts for abstracting and showing parallelism in Tkinter applications.

# Tkinter Parallelism Abstracted

## Descripción

Este proyecto demuestra cómo manejar y abstraer conceptos básicos de paralelismo en aplicaciones Tkinter en Python, utilizando procesos para simular múltiples usuarios interactuando con una cuenta bancaria compartida. La aplicación permite realizar depósitos y retiros de forma concurrente, mostrando cómo sincronizar accesos a recursos compartidos para evitar condiciones de carrera.

## ¿Qué incluye este proyecto?

- **`launch.py`**: Código principal que inicia múltiples procesos de la app bancaria.
- **`app.py`**: Contiene la lógica del banco y las funciones relevantes.
- **`gui.py`**: Interfaz gráfica de usuario (GUI) para cada instancia, con botones para depósito y retiro, y visualización del saldo.

## Cómo funciona

- Se crean dos procesos que ejecutan la misma lógica de una cuenta bancaria, compartiendo un saldo inicial.
- La sincronización entre procesos se realiza usando `Value` y `Lock` de `multiprocessing` para evitar conflictos al acceder y modificar el saldo.
- Cada proceso corre una instancia de la interfaz gráfica, permitiendo a dos usuarios interactuar simultáneamente con la misma cuenta.

## Requisitos

- Python 3.13
- Tkinter (normalmente incluido en la instalación estándar de Python)

## Instalación

No requiere instalaciones especiales más allá de tener Python instalado.

## Uso

1. Ejecuta el archivo `launch.py` para iniciar la simulación:

```bash
python launch.py
```

2. Aparecerán dos ventanas, cada una representando un usuario diferente.
3. Puedes realizar depósitos y retiros desde cada interfaz, y verás cómo se actualiza el saldo en ambas ventanas en tiempo real, asegurando la correcta gestión del paralelismo.

## Estructura del código

- `launch.py`: inicia los procesos y comparte el saldo
- `app.py`: maneja la lógica operacional de un banco (retiro/deposito/balance)
- `gui.py`: define la interfaz gráfica para cada usuario

## Notas y sugerencias

- La sincronización en este ejemplo es básica; para aplicaciones más complejas, considera usar mecanismos avanzados o bibliotecas especializadas.
- La interfaz gráfica fue generada con Tkinter Designer y puede modificarse para adaptarse a diferentes estilos y funcionalidades.
- La implementación actual es un ejemplo simple para entender conceptos de paralelismo y acceso concurrente en Python de una manera visual.

## Contribución

Si deseas mejorar este proyecto o agregar nuevas funcionalidades, ¡siéntete libre de hacer un fork y enviar tus cambios!

## Licencia

Este proyecto es solo con fines educativos y de demostración.

