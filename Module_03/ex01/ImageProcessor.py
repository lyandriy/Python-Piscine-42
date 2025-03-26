import matplotlib.pyplot as plt 
import matplotlib.image as img

class ImageProcessor:
    def __init__(self):
        pass

    def load(self, path):
        try:
            Image = img.imread(path)
            size = Image.shape
            print(f"Loading image of dimensions {size[0]} x {size[2]}")
            return (Image)
        except Exception as e:
            print(f"Exception: {e.__class__.__name__} -- strerror: {e.args}")

    def display(self, array):
        try:
            plt.imshow(array)
            plt.axis("off")
            plt.show()
        except Exception as e:
            print(f"Exception: {e.__class__.__name__} -- strerror: {e.args}")