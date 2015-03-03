import imghdr

IMG_PATH = None

def get_ext(path):
    """retourne une description de type de l'image"""
    if os.path.exists(path):
        return imghdr.what(path)
    else:
        print("fichier n'existe pas")

def main():
    img_ext = get_ext(IMG_PATH)
    print("l'image:[{}], et type est :[{}]".format(IMG_PATH,img_ext))
