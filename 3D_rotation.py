from Utils.image_transformer import ImageTransformer
from Utils.util import save_image
import sys
import os


def rotate_images_in_folder(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    

    # Get a list of image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Iterate through each image file
    for image_file in image_files:
        # demo 2 output
        img_path = os.path.join(folder_path, image_file)
        rot_range = 360 
        img_shape = None 

        # Instantiate the class
        it = ImageTransformer(img_path, img_shape)


    # Iterate through rotation range
        for ang in range(0, rot_range, 20):

            # NOTE: Here we can change which angle, axis, shift
            
            """ Example of rotating an image along y-axis from 0 to 360 degree 
                with a 5 pixel shift in +X direction """
            #rotated_img = it.rotate_along_axis(phi = ang, dx = 5)

            """ Example of rotating an image along yz-axis from 0 to 360 degree """
            #rotated_img = it.rotate_along_axis(phi = ang, gamma = ang)

            """ Example of rotating an image along z-axis(Normal 2D) from 0 to 360 degree """
            rotated_img = it.rotate_along_axis(theta = ang, dy = 5)


            output_file = f"y_rotated_{ang}_{image_file}"
            image_filename = os.path.splitext(os.path.basename(image_file))[0]
            out = os.path.join(output_folder, image_filename)
            os.makedirs(out, exist_ok=True)
            output_path = os.path.join(out, output_file)
            save_image(output_path.format(str(ang).zfill(3)), rotated_img)
            save_image(output_path.format(str(ang).zfill(3)), rotated_img)

            print(f"Rotated image saved: {output_path}")        


# Specify the input folder and output folder
input_folder = r"C:\Users\kaushal.i.g\Downloads\obj_nobg"
output_folder = r"C:\Users\kaushal.i.g\Downloads\aug\test9_JPG.rf.c51115e2bf67c8daacef690bdfb1a525"

# Rotate images in the input folder and save them in the output folder
rotate_images_in_folder(input_folder, output_folder)

# replace bg