import cv2
import math
import numpy as np

def getInclination(radious: int, angle: float, color = 255, backcolor = 0, padding = 0.05, thickness = 1):
    """
    Generate an image with a line inclined at a given angle.

    Parameters:
    - radious (int): The radius of the circle on which the line is inclined.
    - angle (float): The angle at which the line is inclined, in degrees.
    - color (int or float or tuple, optional): The color of the line. Defaults to 255 (white).
    - backcolor (int or float or tuple, optional): The background color of the image. Defaults to 0 (black).
    - padding (float, optional): The padding around the circle. Defaults to 0.05 (5% of the radius).
    - thickness (int, optional): The thickness of the line. Defaults to 1.

    Returns:
    - img (numpy.ndarray): The generated image with the inclined line.
    """
    # Creating the image
    height = int(radious + radious*padding*2)
    width = int((radious + radious*padding)*2)
    if type(color) == int or type(color) == float:
        img = np.full((height, width), backcolor, dtype=np.uint8)
    else: 
        img = np.full((height, width, len(color)), backcolor, dtype=np.uint8)
    
    # Segments initial and final points
    initialPoint = (radious+int(radious*padding), radious+int(radious*padding))
    angle_rad = math.radians(angle)
    x = initialPoint[0] - radious * math.cos(angle_rad)
    y = initialPoint[1] - radious * math.sin(angle_rad)
    finalPoint = (int(round(x, 0)), int(round(y, 0)))

    # Drawing the line
    img = cv2.line(img, initialPoint, finalPoint, color, thickness)

    return img

def randomlyInsert(image, inclination):
    """
    Randomly insert the inclination image in the input image.

    Parameters:
    - image (numpy.ndarray): The input image.
    - inclination (numpy.ndarray): The image to insert.

    Returns:
    - img (numpy.ndarray): The input image with the inclination image inserted.
    """
    # Generating random coordinates
    x = np.random.randint(0, image.shape[1] - inclination.shape[1])
    y = np.random.randint(0, image.shape[0] - inclination.shape[0])

    # Inserting the inclination image
    img = image.copy()
    img[y:y+inclination.shape[0], x:x+inclination.shape[1]] = inclination

    return img

def uniformallyDistributedInclination(loc: int = 90, scale: int = 20):
    """
    Generate a random inclination angle uniformly distributed between 0 and 180 degrees.

    Parameters:
    loc (int): The mean of the normal distribution used to generate the random angle. Default is 90.
    scale (int): The standard deviation of the normal distribution used to generate the random angle. Default is 20.

    Returns:
    float: A random inclination angle between 0 and 180 degrees.
    """
    random_float = np.random.normal(loc=loc, scale=scale)
    
    # Truncating the angle to be between 0 and 180 degrees
    random_float = max(0, min(random_float, 180))

    return random_float