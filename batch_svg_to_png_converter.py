import tkinter as tk
from tkinter import filedialog, messagebox, Listbox, END
import os
import cairosvg

def select_svg_files():
    files = filedialog.askopenfilenames(
        title="Select SVG files", 
        filetypes=(("SVG Files", "*.svg"), ("All Files", "*.*"))
    )
    if files:
        svg_files_list.delete(0, END)  # Clear previous selections
        for file in files:
            svg_files_list.insert(END, file)  # Display selected files in the listbox

def select_destination_folder():
    folder = filedialog.askdirectory(title="Select Destination Folder")
    destination_folder.set(folder)

def convert_svgs_to_png():
    svgs = svg_files_list.get(0, END)
    dest_folder = destination_folder.get()

    if not svgs or not dest_folder:
        messagebox.showerror("Error", "Please select SVG files and a destination folder.")
        return

    for svg in svgs:
        try:
            base_name = os.path.basename(svg)
            png_name = os.path.splitext(base_name)[0] + ".png"
            dest_path = os.path.join(dest_folder, png_name)

            # Convert SVG to PNG with 300 DPI using CairoSVG
            cairosvg.svg2png(url=svg, write_to=dest_path, dpi=300)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert {svg}: {e}")
            return

    messagebox.showinfo("Success", f"Converted {len(svgs)} files successfully.")

# Set up the main window
root = tk.Tk()
root.title("SVG to PNG Converter")

svg_files_list = Listbox(root, selectmode=tk.MULTIPLE, width=60)
svg_files_list.grid(row=0, column=1, padx=10, pady=10)

destination_folder = tk.StringVar()

# Create and place widgets
tk.Button(root, text="Select SVG Files", command=select_svg_files).grid(row=0, column=0, padx=10, pady=10)
tk.Button(root, text="Select Destination Folder", command=select_destination_folder).grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Convert to PNG", command=convert_svgs_to_png).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
