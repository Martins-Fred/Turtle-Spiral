# 🐢 Turtle Spiral

A simple Python project that uses the built-in `turtle` module to draw a colorful spiral pattern on a black background.

## ✨ Features

* 🎨 Uses multiple colors
* 🌀 Creates a colorful spiral pattern
* 🐢 Built with Python's `turtle` module
* ⚡ Uses maximum turtle drawing speed
* 🖥️ Opens the drawing in a graphical window

## 📋 Requirements

You need:

* Python 3.x
* The built-in `turtle` module

No additional packages are required.

## 🚀 How to Run

1. Make sure Python is installed.
2. Save the code as `turtle_spiral.py`.
3. Open a terminal in the project directory.
4. Run:

```bash
python turtle_spiral.py
```

A window will open and the turtle will draw the spiral.

## 🧩 How It Works

The program:

1. Creates a Turtle graphics window with a black background.
2. Creates a turtle pen.
3. Cycles through six different colors.
4. Moves forward by an increasingly larger distance.
5. Turns right by `59` degrees after each movement.
6. Repeats this process 250 times to create the spiral.

```python
for i in range(250):
    pen.color(colors[i % 6])
    pen.forward(i * 2)
    pen.right(59)
```

## 🎨 Colors Used

The spiral cycles through:

* Purple
* Blue
* Green
* Yellow
* Orange
* Red

## 📸 Result

Running the program produces a colorful geometric spiral similar to:

**🌈 🌀 Colorful Turtle Spiral 🌀 🌈**

## 📁 Project Structure

```text
turtle-spiral/
│
├── turtle_spiral.py
└── README.md
```

## 🛠️ Customization

You can experiment with the values to create different patterns.

For example:

* Change `range(250)` to control the number of lines.
* Change `i * 2` to change how quickly the spiral grows.
* Change `59` to change the turning angle.
* Add or remove colors from the `colors` list.
* Change `screen.bgcolor()` to use a different background.

## 📄 License

This project is free to use and modify for learning and personal projects.

