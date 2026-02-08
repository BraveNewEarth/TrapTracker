from PIL import Image
import os

def process_smart_icon():
    source = "Trap Tracker App.jpeg"
    
    if not os.path.exists(source):
        print(f"Error: {source} not found")
        return

    try:
        with Image.open(source) as img:
            print(f"Original: {img.size} {img.format}")
            
            # Calculate new size maintaining aspect ratio
            # Target height of ~128px is plenty for a nav bar icon (rendered at 44px height)
            # 2400/1792 = 1.339 aspect ratio
            
            target_height = 512
            aspect = img.width / img.height
            target_width = int(target_height * aspect)
            
            print(f"Resizing to: {target_width}x{target_height}")
            
            img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
            
            # Save
            img.save("app-logo.png", "PNG")
            img.save("app-logo.webp", "WEBP", quality=95)
            print("Saved app-logo.png and app-logo.webp")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    process_smart_icon()
