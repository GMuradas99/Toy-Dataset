import os

from tqdm import tqdm

from functions import *

NUMBER_INSTANCES = 10
OUTPUT_DIRECTORY = 'toy_dataset/'

# Parameters 
radious_param = (20, 100)
thickness_param = (1, 5)

# Creating the output directory
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# Generating the images
for i in tqdm(range(NUMBER_INSTANCES)):
    radious = np.random.randint(radious_param[0], radious_param[1])
    thickness = np.random.randint(thickness_param[0], thickness_param[1])
    angle = uniformallyDistributedInclination()

    inclination = getInclination(radious, angle, color=(255,255,255), backcolor=(0,0,0), padding=0.1, thickness=thickness)
    image = np.full((224, 224, 3), (0,0,0), dtype=np.uint8)
    image = randomlyInsert(image, inclination)

    cv2.imwrite(OUTPUT_DIRECTORY + str(i) + '_' + str(angle) + '.png', image)