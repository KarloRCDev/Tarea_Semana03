import cv2
from pathlib import Path

current_directory = Path(__file__).resolve().parent
path = f"{current_directory}/Imagenes/img1.jpg"
path2 = f"{current_directory}/Imagenes/img2.jpg"
path3 = f"{current_directory}/Imagenes/result.jpg"
# Carga las imágenes
img1 = cv2.imread(path)
img2 = cv2.imread(path2)

# Redimensiona las imágenes para que tengan las mismas dimensiones
img1 = cv2.resize(img1, (500, 500))
img2 = cv2.resize(img2, (500, 500))

# Realiza la operación lógica "AND" para superponer las imágenes
result = cv2.bitwise_and(img2, img1)
cv2.imshow("Imagen1", img1)
cv2.imshow("Imagen2", img2)
# Muestra y guarda la imagen resultante
cv2.imshow("Result", result)
cv2.imwrite(path3, result)
cv2.waitKey(0)
cv2.destroyAllWindows()