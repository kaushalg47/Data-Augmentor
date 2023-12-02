
from rembg import remove 
from PIL import Image 
import os
import numpy as np
import cv2
  

  
folder_path = r"" #object images folder
output_path = r"" #output folder
  
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

for image_file in image_files[64:]: 
    print("processing "+image_file)
    input_path = os.path.join(folder_path, image_file)
    input = Image.open(input_path) 
      
    # Removing the background from the given Image 
    output = remove(input) 
    np_image = np.array(output)
    bgr_image = cv2.cvtColor(np_image, cv2.COLOR_RGBA2BGR)
    


    #accesing random image dataset
    folder_path = r"" #random image dataset
    
    image_files = os.listdir(folder_path)
    count = 0
    
    for file_name in image_files:
        if file_name.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            file_path = os.path.join(folder_path, file_name)
            background = cv2.imread(file_path)

            #Overlay the image
    
            overlay_image = bgr_image
            overlay_image = cv2.resize(overlay_image, (1000, 1000))
            h, w = overlay_image.shape[:2]
            shapes = np.zeros_like(background, np.uint8)
            start_x = (background.shape[1] - overlay_image.shape[1]) // 2
            start_y = (background.shape[0] - overlay_image.shape[0]) // 2
            end_x = start_x + overlay_image.shape[1]
            end_y = start_y + overlay_image.shape[0]
            
            shapes[start_y:end_y, start_x:end_x] = overlay_image
            mask = shapes.astype(bool)
            alpha = 1 
            bg_img = background.copy()

            
            bg_img[mask] = cv2.addWeighted(bg_img, 1 - alpha, shapes,
                                          alpha, 0)[mask]
            
            # Optional
            cv2.putText(bg_img, f'Alpha: {round(alpha,1)}', (50, 200),
                        cv2.FONT_HERSHEY_PLAIN, 8, (200, 200, 200), 7)
            
            # resize 
            bg_img = cv2.resize(bg_img, (630,630))
            crop_width = 500  # width of the cropped region
            crop_height = 500  # height of the cropped region
            
            image_height, image_width = bg_img.shape[:2]
            start_x = (image_width - crop_width) // 2
            start_y = (image_height - crop_height) // 2
            end_x = start_x + crop_width
            end_y = start_y + crop_height
    
            # Crop out the center region
            crop = bg_img[start_y:end_y, start_x:end_x]
            image_filename = os.path.splitext(os.path.basename(image_file))[0]
            out_path = os.path.join(output_path, image_filename)
            out_pat = os.path.join(out_path, file_name)
            cv2.imwrite(out_pat, crop)
            