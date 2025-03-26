from ImageProcessor import ImageProcessor

imp = ImageProcessor()
arr = imp.load("non_existing_file.png")

print(arr)

arr = imp.load("./empty_file.png")

print(arr)

arr = imp.load("./Background.jpg")

print(arr)

imp.display(arr)

arr = imp.load("./42AI.png")

print(arr)

imp.display(arr)
