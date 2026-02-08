import os
from PIL import Image

def process_icon():
    source = "Trap Tracker App.jpeg"
    base_name = "app-logo" # New text name to be clean
    
    if not os.path.exists(source):
        print(f"Error: {source} not found")
        return

    try:
        with Image.open(source) as img:
            print(f"Original size: {img.size}")
            
            # Resize to standard icon size (512x512 is standard for web apps)
            # keeping it high quality
            img = img.resize((512, 512), Image.Resampling.LANCZOS)
            
            # Save as PNG
            png_name = f"{base_name}.png"
            img.save(png_name, "PNG")
            print(f"Saved {png_name}")
            
            # Save as WebP
            webp_name = f"{base_name}.webp"
            img.save(webp_name, "WEBP", quality=90)
            print(f"Saved {webp_name}")
            
    except Exception as e:
        print(f"Error processing icon: {e}")

if __name__ == "__main__":
    process_icon()
