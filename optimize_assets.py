import os
import shutil
from PIL import Image

# Asset Mapping: old_name -> new_base_name
# Note: Case sensitive on Mac/Linux
ASSET_MAP = {
    "IMG_2679.PNG": "screenshot-dashboard",
    "IMG_2680.PNG": "screenshot-projects",
    "IMG_2681.PNG": "screenshot-pest-library",
    "IMG_2682.PNG": "screenshot-settings",
    "IMG_2683.PNG": "screenshot-trap-photo",
    "IMG_2684.PNG": "screenshot-trap-details",
    "IMG_2685.PNG": "screenshot-map",
    "MAINIMAGE.jpg": "hero-poster",
    "icon1-watchOS-Default-1088x1088_1x.png": "app-icon"
}

def process_assets():
    print("Starting asset processing...")
    
    # Store dimensions for HTML generation
    dimensions = {}
    
    for old_name, new_base in ASSET_MAP.items():
        if not os.path.exists(old_name):
            print(f"Skipping {old_name}: File not found")
            continue
            
        print(f"Processing {old_name} -> {new_base}...")
        
        try:
            with Image.open(old_name) as img:
                # Store dimensions
                dimensions[new_base] = img.size
                
                # Determine output format based on source
                src_format = img.format
                if src_format == "JPEG":
                    ext = ".jpg"
                else:
                    ext = ".png"
                
                # 1. Create normalized original (lowercase)
                new_orig_name = f"{new_base}{ext}"
                img.save(new_orig_name)
                print(f"  Saved {new_orig_name}")
                
                # 2. Create WebP version
                new_webp_name = f"{new_base}.webp"
                img.save(new_webp_name, "WEBP", quality=85)
                print(f"  Saved {new_webp_name}")
                
        except Exception as e:
            print(f"Error processing {old_name}: {e}")

    # Print dimensions for easy reference
    print("\n--- IMAGE DIMENSIONS ---")
    for name, size in dimensions.items():
        print(f"{name}: width={size[0]} height={size[1]}")

if __name__ == "__main__":
    process_assets()
