import os
import numpy as np
from classify import extract_features, getR, getG, getB

def load_image_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        H, W = map(int, lines[0].split())
        
        image = []
        for i in range(1, H+1):
            row = list(map(int, lines[i].split()))
            image.append(row)
        
        return image, H, W

def analyze_style_samples(samples_dir, style_number, sample_count):
    all_features = []
    
    for i in range(sample_count):
        file_path = os.path.join(samples_dir, f"style-{style_number}-{i}.in")
        
        if not os.path.exists(file_path):
            print(f"Warning: {file_path} does not exist")
            continue
            
        image, H, W = load_image_from_file(file_path)
        features = extract_features(image, H, W)
        all_features.append(features)
        
        print(f"Style {style_number}, Sample {i}: Features extracted")
    
    if all_features:
        avg_features = np.mean(all_features, axis=0)
        std_features = np.std(all_features, axis=0)
        
        print(f"\nStyle {style_number} Average Feature Vector:")
        print(list(avg_features))
        
        print(f"\nStyle {style_number} Feature Standard Deviation:")
        print(list(std_features))
        
        print("\nFeature Analysis:")
        feature_names = [
            "Avg R", "Avg G", "Avg B", 
            "Std R", "Std G", "Std B", 
            "Brightness", "Color Variance", 
            "Normalized Unique Colors", "Edge Intensity"
        ]
        
        for i, name in enumerate(feature_names):
            print(f"{name}: {avg_features[i]:.2f} ± {std_features[i]:.2f}")
    
    return all_features

def main():
    samples_dir = "./samples"  # Update this to your actual samples directory
    
    # Check if directory exists
    if not os.path.exists(samples_dir):
        print(f"Please create a 'samples' directory at {os.path.abspath(samples_dir)}")
        print("and place the sample input files there.")
        return
    
    # Analyze samples for each style
    style1_features = analyze_style_samples(samples_dir, 1, 4)
    style2_features = analyze_style_samples(samples_dir, 2, 4)
    style3_features = analyze_style_samples(samples_dir, 3, 4)
    style4_features = analyze_style_samples(samples_dir, 4, 4)
    
    # Create style vectors (average of each style's features)
    if style1_features and style2_features and style3_features and style4_features:
        style1_vector = np.mean(style1_features, axis=0)
        style2_vector = np.mean(style2_features, axis=0)
        style3_vector = np.mean(style3_features, axis=0)
        style4_vector = np.mean(style4_features, axis=0)
        
        print("\nStyle Vectors for classify.py:")
        print(f"style1_vector = {list(style1_vector)}")
        print(f"style2_vector = {list(style2_vector)}")
        print(f"style3_vector = {list(style3_vector)}")
        print(f"style4_vector = {list(style4_vector)}")

if __name__ == "__main__":
    main()
