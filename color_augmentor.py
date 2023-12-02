import cv2
import os
import numpy as np


folder_path = r"" #Objects folder
output_folder_path = r"" #Output folder 


image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]


for image_file in image_files:
    input_image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(input_image_path)
    
    
    augmented_images = []
    
    # Brightness adjustment
    brightened_image = cv2.convertScaleAbs(image, alpha=0.8, beta=0)
    augmented_images.append(brightened_image)
    
    
    # Noise addition
    noise = np.random.normal(scale=20, size=image.shape).astype(np.uint8)
    noisy_image = cv2.add(image, noise)
    augmented_images.append(noisy_image)
    
    
    # Blur
    blurred_image = cv2.blur(image, (5,5))
    augmented_images.append(blurred_image)
    
    
    #Saturation adjustment
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_image[:, :, 1] = cv2.multiply(hsv_image[:, :, 1], saturation_factor) #add saturation factor here
    saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    augmented_images.append(saturated_image)
    
    
    
    # Save augmented images
    for i, augmented_image in enumerate(augmented_images):
        image_filename = os.path.splitext(os.path.basename(image_file))[0]
        out = os.path.join(output_folder_path, image_filename)
        output_image_path = os.path.join(out, f'augmented_image_{i}.jpg')
        cv2.imwrite(output_image_path, augmented_image)