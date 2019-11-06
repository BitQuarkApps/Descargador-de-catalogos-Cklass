import urllib.request
import ssl
#388
def getNumero(i):
    result = ""
    if i > 99:
        result = f"page0{i}_1.jpg"
    elif i < 10:
        result = f"page000{i}_1.jpg"
    else:
        result = f"page00{i}_1.jpg"
    return result

if __name__ == "__main__":
    Cklass_URL = "https://www.cklass.com/Catalogo/Rebajas//files/assets/common/page-html5-substrates/"
    total_imagenes = 388
    descargadas = 0
    ssl._create_default_https_context = ssl._create_unverified_context
    for i in range(1,total_imagenes+1):
        file_name = getNumero(i)
        image_url = f'{Cklass_URL}{file_name}'
        print("https://www.cklass.com/Catalogo/Rebajas//files/assets/common/page-html5-substrates/page0001_1.jpg")
        print(image_url)
        try:
            opener = urllib.request.URLopener()
            opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0')
            filename, headers = opener.retrieve(image_url, file_name)
            descargadas += 1
        except Exception as e:
            print(e)
            print(f' ---- {file_name} no se pudo descargar ----')
    print(f'Se descargaron {descargadas} de {total_imagenes}')