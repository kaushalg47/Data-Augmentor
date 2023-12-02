# Data-Augmentor
 Applying various types of augmentations to derive a slightly disturbed image from the original image will help any model to improve its Detection and classification accuracy. Three types of augmentations were performed on the current images for the dataset. All the generated images were packed into a folder with its products name. Each image of the product were converted to 300 images with augmentations.
## Perspective Transformation along X and Y axis:
This step involves performing a perspective rotation of a 2D image in 3D plane along the given axis. Length/2 will serve as the radius of rotation. From the 2D image a perspective projection matrix is derived. 2D perspective matrix is converted to 3D and then, with the help of Rotation matrices the image is rotated over X and Y axis with an interval of 20 Degrees in the limit of 360 degrees.
(credits: @eborboihuc)
## Basic disturbance:  
Augments such as Noise, Blur, saturation, Warmth, Brightness, Dullness are performed.  For these operations only CV2 (OpenCV-python) library was utilized. The following number of augments were performed.
## Background augmentation:
This step consists of changing the background of the image so that this dataset helps in detection of the object with any kind of background. This involves two steps:

Step 1: Extracting the product image without the background. rembg module as well as remove.bg API was used in performing the extraction of product image without the background
Step 2: A dataset consisting of random blurred images was chosen as background images. The product image was overlayed on Each of the background image at its center and then cropped to cut out only the part were product is present. 

## Author
kaushal G / @kaushalg47
