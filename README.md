# **HUNDIR LA FLOTA**

¡Bienvenido a la guerra en el gran azul! 

Es una versión del clásico juego de estrategia naval, con la peculiaridad de que **los barcos se pueden colocar en diagonal**. 🎉

---

## 📋 Descripción del juego

En **Hundir la Flota**, cada jugador dispone de una flota de barcos colocados estratégicamente en un tablero de 10x10. El objetivo es hundir todos los barcos del oponente antes de que él hunda los tuyos. Este proyecto incluye las siguientes características destacadas:

- Funcionalidad para jugar contra una **inteligencia artificial básica** (HAL-9000, inspirado en la famosa IA de "2001: Una odisea del espacio").
- **Barcos en orientación diagonal**, además de las orientaciones horizontal y vertical tradicionales. ✨
- Implementación en Python utilizando **Numpy** para la gestión de los tableros.
- Mensajes dinámicos y feedback durante el juego para mejorar la experiencia del usuario.

---

## 🚀 Cómo empezar

### Requisitos previos

Para ejecutar este proyecto necesitarás:
- **Python 3.8+**
- El módulo **Numpy**

### Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/JZubiaga13/Hundir-la-Flota.git
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install numpy
   ```
3. Asegúrate de ejecutar el archivo desde un entorno compatible, como **Visual Studio Code** o un terminal.

---

## 📖 Instrucciones de uso

1. Ejecuta el script `hundirflota.py`:
   ```bash
   python hundirflota.py
   ```
2. El juego te pedirá coordenadas para disparar contra los barcos del ordenador. Ingresa las coordenadas como números del 0 al 9.
3. El ordenador también disparará automáticamente contra tu tablero.
4. El juego termina cuando todos los barcos de uno de los jugadores han sido hundidos. 🚩

---

## 🛠️ Funciones principales del código

### **creartablero**
Crea un tablero vacío de tamaño 10x10 utilizando Numpy. Puedes coger y modificar el código si quieres un tablero diferente.

### **crearbarco**
Genera barcos de una longitud específica con orientación horizontal, vertical o diagonal.

### **colocarbarcos**
Coloca los barcos en el tablero asegurándose de que no haya colisiones.

### **disparar**
Determina si un disparo da en el blanco, toca un barco o simplemente cae en el agua.

### **vista_oculta**
Muestra el tablero del oponente ocultando las posiciones de los barcos no descubiertos.

### **hundirflota**
Orquesta la mecánica del juego, alternando turnos entre el jugador y la IA.

---

## 🧠 IA básica: HAL-9000

El ordenador juega como HAL-9000. Sus disparos son aleatorios, pero eso no lo hace menos competitivo. Durante el juego, HAL también reacciona a los resultados de sus disparos y anuncia cuando hunde uno de tus barcos. ¡Cuidado! 

---

## 🔥 Peculiaridades

- Los barcos pueden orientarse en diagonal, algo que no es común en los juegos tradicionales de Hundir la Flota.
- Es un proyecto educativo con comentarios en el código que explican algunos pasos. 💡
- ¡Incluye mensajes temáticos para dar un toque de humor al juego! 

---

## 🖼️ Ejemplo de juego

```
Tablero de la Maquina:
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _
_ _ _ _ _ _ _ _ _ _

Introduce la fila (0-9): 4
Introduce la columna (0-9): 5
Tocado

HAL dispara a (3, 2): AGUA
```

---

## 📌 Contribuciones

Si tienes sugerencias o quieres mejorar este proyecto, ¡serán bienvenidas! Puedes abrir un issue o enviar un pull request. 🛠️

---

## 🏆 Créditos

Este proyecto fue desarrollado durante mi **Bootcamp de Data Science** como ejercicio para practicar lógica de programación, Numpy y diseño de juegos básicos en Python. ¡Espero que lo disfrutes tanto como yo al crearlo! 😊

---

¡Gracias por jugar y que te diviertas hundiendo flotas! 🚢💥

