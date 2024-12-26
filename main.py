import customtkinter as ctk

ctk.set_appearance_mode("Light") 
ctk.set_default_color_theme("green")  

class DecimalConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Decimal Number Converter")
        self.geometry("400x400")

        self.label = ctk.CTkLabel(self, text="Enter a decimal number:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.on_enter_pressed)

        self.convert_button = ctk.CTkButton(self, text="Convert", command=self.convert)
        self.convert_button.pack(pady=20)

        self.binary_result_label = ctk.CTkLabel(self, text="")
        self.binary_result_label.pack(pady=5)

        self.hexadecimal_result_label = ctk.CTkLabel(self, text="")
        self.hexadecimal_result_label.pack(pady=5)

        self.octal_result_label = ctk.CTkLabel(self, text="")
        self.octal_result_label.pack(pady=5)

        self.decimal_result_label = ctk.CTkLabel(self, text="")
        self.decimal_result_label.pack(pady=5)

    def decimal_to_binary(self, n):
        return bin(n)[2:] 

    def decimal_to_hexadecimal(self, n):
        return hex(n)[2:].upper() 

    def decimal_to_octal(self, n):
        return oct(n)[2:]  

    def convert(self):
        try:
            decimal_number = int(self.entry.get())

            binary_number = self.decimal_to_binary(decimal_number)
            hexadecimal_number = self.decimal_to_hexadecimal(decimal_number)
            octal_number = self.decimal_to_octal(decimal_number)
            
            self.binary_result_label.configure(text=f"Binary representation: {binary_number}")
            self.hexadecimal_result_label.configure(text=f"Hexadecimal representation: {hexadecimal_number}")
            self.octal_result_label.configure(text=f"Octal representation: {octal_number}")
            self.decimal_result_label.configure(text=f"Decimal representation: {decimal_number}")
        except ValueError:
            self.binary_result_label.configure(text="")
            self.hexadecimal_result_label.configure(text="")
            self.octal_result_label.configure(text="")
            self.decimal_result_label.configure(text="Please enter a valid integer.")

    def on_enter_pressed(self, event):
        self.convert()

if __name__ == "__main__":
    app = DecimalConverterApp()
    app.mainloop()
