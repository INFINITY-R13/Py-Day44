import tkinter as tk

# Create the main application window
app = tk.Tk()
app.title("Python GUI Version")
app.geometry("600x800") # Set window size

# --- First Box (like the .first div) ---
# The outer frame handles the border
first_frame_border = tk.Frame(app, bg="gray")

# The inner frame handles the padding and background color
first_frame_padding = tk.Frame(first_frame_border, bg="aqua", width=200, height=200, padx=20, pady=20)
first_frame_padding.pack(padx=10, pady=10) # This simulates the border width

# Add the text label inside
p_text = "Lorem, ipsum dolor sit amet consectetur adipisicing elit..."
label = tk.Label(first_frame_padding, text=p_text, bg="aqua", wraplength=200, justify="left")
label.pack()

# Place the first box on the window
first_frame_border.place(x=0, y=0)


# --- Second Box (like the .second div) ---
# Use a Frame for the box and configure its border
second_box = tk.Frame(app, bg="aquamarine", width=200, height=200,
                      borderwidth=10, relief="solid") # Note: Tkinter border width is uniform

# Place it using the margin-left value
# Total width of first div = 200 (width) + 40 (padding) + 20 (border) = 260
# It appears on the next "line" because divs are block elements.
# So we calculate y-position based on the first box's height.
second_box.place(x=260, y=260) # x simulates margin-left, y places it below


# --- Third Box (like the .third div) ---
third_box = tk.Frame(app, bg="teal", width=200, height=200,
                     borderwidth=10, relief="solid", highlightbackground="gray", highlightthickness=10)

# Place it below the second box
third_box.place(x=40, y=520) # x simulates margin-left, y places it below


# Start the application's main loop
app.mainloop()