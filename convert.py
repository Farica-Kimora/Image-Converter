from PIL import Image
import os

# Set the current and output directory paths
current_dir = os.getcwd()  # Get the current working directory
current_dir_images = os.path.join(current_dir, '')  # Specify the 'images' subdirectory

# Set the correct current directory
os.chdir(current_dir_images)

# Print the current directory for confirmation
print("Current Directory:", current_dir_images)

# Specify the output directory
output_dir = os.path.join(current_dir, 'output')  # Output directory in the original 'FaricaKimora-main\FaricaKimora-main' directory

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Get a list of all files in the current directory
all_files = os.listdir(current_dir_images)

# Filter the list to include only .png files
png_files = [file for file in all_files if file.lower().endswith('.png')]

# Loop through each .png file and copy it to the output directory
for png_file in png_files:
    # Construct the full paths for input and output files
    input_path = os.path.join(current_dir_images, png_file)
    output_path = os.path.join(output_dir, os.path.splitext(png_file)[0] + '.jpg')

    # Open the image and save it in the output directory
    try:
        im = Image.open(input_path)
        
        # Check if the image has an alpha channel (transparency)
        if im.mode == 'RGBA':
            # Convert to RGB before saving as JPEG
            im = im.convert('RGB')

        # Save the image in the output directory
        im.save(output_path)
        print(f"Successfully copied {png_file} to {output_path}")
    except Exception as e:
        print(f"Error copying {png_file}: {e}")
