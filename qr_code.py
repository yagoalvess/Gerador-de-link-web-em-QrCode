# Bibliotecas importadas
import qrcode
import webbrowser


def redirecionar_qrcode(link):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Salvar o QR code como um arquivo de imagem
    qr_img.save("qrcode.png")

    # Abrir o link no navegador padrão
    webbrowser.open(link)


# Exemplo de uso:
link = "https://www.example.com"
redirecionar_qrcode(link)
