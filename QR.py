import tkinter as tk
from tkinter import messagebox
import qrcode

def generar_qr():
    # Obtener el texto desde la entrada de texto
    texto = entrada_texto.get()

    if texto:
        # Crear un objeto QRCode
        codigo_qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Agregar datos al código QR
        codigo_qr.add_data(texto)
        codigo_qr.make(fit=True)

        # Crear una imagen QR
        imagen_qr = codigo_qr.make_image(fill_color="black", back_color="white")

        # Mostrar la imagen en la interfaz
        imagen_qr.show()
    else:
        messagebox.showerror("Error", "Por favor, ingrese un texto.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Código QR")
ventana.geometry("700x350")

# Crear una etiqueta y entrada de texto
etiqueta = tk.Label(ventana, text="Ingrese la dirección para la que desea el código:")
etiqueta.pack(pady=10)

entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=10)

# Crear un botón para generar el código QR
boton_generar = tk.Button(ventana, text="Generar QR", command=generar_qr)
boton_generar.pack(pady=20)

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
