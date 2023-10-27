from pathlib import Path
from PIL import Image, ImageDraw

def convert_to_circle(input_image_path, output_image_path):
    # Open the image
    with Image.open(input_image_path) as img:
        # Create a mask and draw a white circle on it
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        width, height = img.size
        draw.ellipse((0, 0, width, height), fill=255)
        
        # Apply the mask to the image
        img.putalpha(mask)

        # Save the image
        img.save(output_image_path)

# Specify the input and output file paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
input_image_path = current_dir / "assets" / "profile.jpeg"  # Replace with your actual file path
output_image_path = current_dir / "assets" / "circle_profile_pic.png"  # Replace with your desired output file path

# Call the function to convert the image
convert_to_circle(input_image_path, output_image_path)
