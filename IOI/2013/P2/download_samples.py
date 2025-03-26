import os
import requests
import time
from pathlib import Path

def download_sample(style_number, sample_number, base_url, output_dir):
    """Download a sample file for a specific style and sample number"""
    filename = f"style-{style_number}-{sample_number}.in"
    url = f"{base_url}/style-{style_number}-{sample_number}.in"
    output_path = os.path.join(output_dir, filename)
    
    try:
        print(f"Downloading {url}...")
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Successfully downloaded {filename}")
            return True
        else:
            print(f"Failed to download {filename}: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {filename}: {str(e)}")
        return False

def main():
    # Base URL for the sample files
    base_url = "https://static.dmoj.ca/data/peg/ioi1312"
    
    # Create samples directory if it doesn't exist
    samples_dir = Path("./samples")
    samples_dir.mkdir(exist_ok=True)
    
    print(f"Sample files will be saved to: {samples_dir.absolute()}")
    
    # Download samples for each style
    total_downloaded = 0
    
    # Try to download multiple samples for each style
    for style in range(1, 5):  # Styles 1-4
        print(f"\nDownloading samples for Style {style}:")
        
        # Try to download samples 0-8 for each style
        for sample in range(9):  # Samples 0-8
            success = download_sample(style, sample, base_url, samples_dir)
            if success:
                total_downloaded += 1
            
            # Add a small delay to avoid overloading the server
            time.sleep(0.5)
    
    print(f"\nDownload complete. Successfully downloaded {total_downloaded} sample files.")
    
    # Check if we have enough samples to proceed
    if total_downloaded < 4:
        print("Warning: Very few samples were downloaded. Check your internet connection or the URL.")
    else:
        print(f"You can now run analyze_samples.py to analyze the downloaded samples.")
        print("And then use classify.py to classify new images.")

if __name__ == "__main__":
    main()
