import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image


def embed_alpha(base_path: str, alpha_path: str, out_path: str, resize_mode: str):
    base = Image.open(base_path).convert("RGBA")
    alpha_img = Image.open(alpha_path)

    if resize_mode == "Fit (resize alpha to base)":
        alpha_img = alpha_img.resize(base.size, Image.Resampling.LANCZOS)
    elif resize_mode == "Require same size":
        if alpha_img.size != base.size:
            raise ValueError(f"Size mismatch:\nBase: {base.size}\nAlpha: {alpha_img.size}")
    else:
        raise ValueError("Unknown size handling option")

    # Split base channels
    r, g, b, _ = base.split()

    # Flip green channel (G -> 255 - G)
    g = g.point(lambda x: 255 - x)

    # Use brightness of alpha image as alpha channel
    alpha = alpha_img.convert("L")  # grayscale 0..255

    out = Image.merge("RGBA", (r, g, b, alpha))
    out.save(out_path)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Embed Image into Alpha Channel (Flip Green)")
        self.minsize(820, 310)

        # Slightly nicer scaling on some Windows DPI setups
        try:
            self.tk.call("tk", "scaling", 1.15)
        except Exception:
            pass

        self.base_path = tk.StringVar()
        self.alpha_path = tk.StringVar()
        self.out_path = tk.StringVar()
        self.resize_mode = tk.StringVar(value="Fit (resize alpha to base)")

        root = ttk.Frame(self, padding=14)
        root.grid(row=0, column=0, sticky="nsew")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Make entry column stretch
        root.columnconfigure(0, weight=0)  # labels
        root.columnconfigure(1, weight=1)  # entries
        root.columnconfigure(2, weight=0)  # buttons

        def add_row(r, label, var, btn_text, btn_cmd):
            ttk.Label(root, text=label).grid(row=r, column=0, sticky="w", padx=(0, 10), pady=6)
            entry = ttk.Entry(root, textvariable=var)
            entry.grid(row=r, column=1, sticky="ew", pady=6)
            ttk.Button(root, text=btn_text, command=btn_cmd).grid(row=r, column=2, sticky="e", pady=6)

        add_row(0, "Base RGB image (keeps RGB, flips GREEN):", self.base_path, "Browse…", self.pick_base)
        add_row(1, "Alpha image (brightness → alpha):", self.alpha_path, "Browse…", self.pick_alpha)
        add_row(2, "Output PNG:", self.out_path, "Save as…", self.pick_out)

        ttk.Label(root, text="Size handling:").grid(row=3, column=0, sticky="w", padx=(0, 10), pady=(10, 6))
        mode = ttk.Combobox(
            root,
            textvariable=self.resize_mode,
            state="readonly",
            values=["Fit (resize alpha to base)", "Require same size"],
        )
        mode.grid(row=3, column=1, sticky="w", pady=(10, 6))
        mode.current(0)

        btns = ttk.Frame(root)
        btns.grid(row=4, column=0, columnspan=3, sticky="e", pady=(18, 6))
        ttk.Button(btns, text="Embed Alpha", command=self.run).grid(row=0, column=0, padx=(0, 10))
        ttk.Button(btns, text="Quit", command=self.destroy).grid(row=0, column=1)

        ttk.Label(
            root,
            text="Tip: Output should be PNG (JPEG doesn’t support alpha). Green channel is inverted before embedding alpha.",
            foreground="#555",
        ).grid(row=5, column=0, columnspan=3, sticky="w", pady=(10, 0))

    def pick_base(self):
        path = filedialog.askopenfilename(
            title="Select base image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.tga *.bmp *.tif *.tiff"), ("All files", "*.*")]
        )
        if path:
            self.base_path.set(path)
            self.suggest_out()

    def pick_alpha(self):
        path = filedialog.askopenfilename(
            title="Select alpha image",
            filetypes=[("Images", "*.png *.jpg *.jpeg *.tga *.bmp *.tif *.tiff"), ("All files", "*.*")]
        )
        if path:
            self.alpha_path.set(path)
            self.suggest_out()

    def pick_out(self):
        path = filedialog.asksaveasfilename(
            title="Save output as",
            defaultextension=".png",
            filetypes=[("PNG", "*.png")]
        )
        if path:
            if not path.lower().endswith(".png"):
                path += ".png"
            self.out_path.set(path)

    def suggest_out(self):
        base = self.base_path.get()
        if base and not self.out_path.get():
            folder = os.path.dirname(base)
            name, _ = os.path.splitext(os.path.basename(base))
            self.out_path.set(os.path.join(folder, f"{name}_alpha.png"))

    def run(self):
        base = self.base_path.get().strip()
        alpha = self.alpha_path.get().strip()
        out = self.out_path.get().strip()

        if not base or not alpha or not out:
            messagebox.showerror("Missing input", "Please choose base image, alpha image, and output file.")
            return

        try:
            embed_alpha(base, alpha, out, self.resize_mode.get())
        except Exception as e:
            messagebox.showerror("Failed", str(e))
            return

        messagebox.showinfo("Done", f"Saved:\n{out}")


if __name__ == "__main__":
    App().mainloop()
