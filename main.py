import qrcode
from qrcode.constants import ERROR_CORRECT_M

def generate_qr_code(url: str,output_path: str):

    # COnfigure QR code
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True) # fit to content

    img = qr.make_image(fill_color="black", back_color="white") # Generate code image

    # Save to file
    img.save(output_path)
    print(f"QR code saved to: {output_path}")

def main():
    print("==================QR Code Generator===================")
    url = input("Enter the URL to create a QR code: ").strip()
    if not url:
        print("No URL found, exiting.")
        return

    out = input("Output file name (default: qrcode.png): ").strip()
    if not out:
        out = "qrcode.png"

    generate_qr_code(url=url,
                     output_path=out)

if __name__ == "__main__":
    main()