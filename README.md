# Py-Day44
# Py-Day44: CSS Box Model in Python Tkinter

This project demonstrates how to replicate the CSS Box Model using Python's built-in GUI library, Tkinter. It takes a simple HTML file styled with CSS and recreates its visual layout as a desktop application.

## Objective

The goal is to understand how CSS properties like `height`, `width`, `padding`, `border`, and `margin` translate to the layout and widget options available in Tkinter.

## Files

  * `index.html`: The source HTML file containing three `div` elements styled to showcase the box model.
  * `main.py`: The Python script that uses Tkinter to build a GUI that mimics the `index.html` page.

## Visual Breakdown

### 1\. HTML & CSS Version (`index.html`)

The webpage consists of three stacked `div` elements, each with distinct styling:

  * **First Div (`.first`)**:

      * `background-color`: aqua
      * `padding`: 20px
      * `border`: 10px solid gray
      * Contains placeholder text.

  * **Second Div (`.second`)**:

      * `background-color`: aquamarine
      * `border`: 20px (top/bottom) and 10px (left/right) solid gray border
      * `margin-left`: 260px

  * **Third Div (`.third`)**:

      * `background-color`: teal
      * `border`: 10px solid gray
      * `margin-left`: 40px

### 2\. Python Tkinter Version (`main.py`)

The Python script recreates this layout using `tk.Frame` widgets and the `.place()` geometry manager to control positioning precisely.

  * **First Box**:

      * A clever workaround is used to simulate padding and border separately.
      * An outer `tk.Frame` is colored gray to act as the border.
      * An inner `tk.Frame` is colored aqua and uses `padx` and `pady` options to create the 20px internal padding. The `pack()` method on this inner frame is given padding to simulate the border thickness.

  * **Second Box**:

      * A single `tk.Frame` is used with a background color of aquamarine.
      * The border is created using the `borderwidth` and `relief="solid"` options.
      * **Note**: Tkinter's `borderwidth` is uniform on all sides, so it cannot perfectly replicate the different vertical and horizontal border widths from the CSS.
      * The `margin-left` is simulated by setting the `x` coordinate in the `.place(x=260, ...)` method.

  * **Third Box**:

      * Another `tk.Frame` with a teal background.
      * The border is simulated using `highlightbackground="gray"` and `highlightthickness=10`.
      * The `margin-left` is again handled by setting the `x` coordinate: `.place(x=40, ...)`.

## How to Run

1.  Ensure you have Python installed. Tkinter is included in most standard installations.
2.  Run the script from your terminal:
    ```sh
    python main.py
    ```