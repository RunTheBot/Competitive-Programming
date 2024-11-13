import cv2
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry.polygon import LinearRing
from scipy.interpolate import splprep, splev
import svgwrite


def threshold_image(image, threshold_value=200):
    """Apply a binary threshold to the image. Anything below the threshold becomes black (0),
    anything above the threshold becomes white (255)."""
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

def find_edges_and_contours(image_path):
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image: values below 200 become black, above 200 become white
    binary_image = threshold_image(gray, 0)

    # Use GaussianBlur to reduce noise and improve edge detection
    blurred = cv2.GaussianBlur(binary_image, (5, 5), 0)
    
    # Perform Canny edge detection on the binary image
    edges = cv2.Canny(blurred, 100, 200)

    # Find contours from the edges
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours, image.shape

def contours_to_polygon(contours):
    # Get the largest contour which is the main shape of the image
    max_contour = max(contours, key=cv2.contourArea)

    # Convert the contour into a polygon (Shapely)
    points = [tuple(point[0]) for point in max_contour]
    polygon = Polygon(points)

    return polygon

def offset_polygon(polygon, offset_distance):
    # Create an offset of the polygon to generate the cutline
    offset_polygon = polygon.buffer(offset_distance)

    return offset_polygon

def smooth_polygon(polygon, smoothing_factor=0.05):
    """
    Smooth the polygon using spline interpolation on its exterior ring.
    The smoothing_factor controls the degree of smoothing (lower is more detailed, higher is smoother).
    """
    # Extract the exterior coordinates of the polygon
    ring = LinearRing(polygon.exterior.coords)
    x, y = ring.xy

    # Use B-spline interpolation to smooth the polygon
    tck, u = splprep([x, y], s=smoothing_factor)
    unew = np.linspace(0, 1, len(x) * 5)  # Increase the number of points for smoothing
    smoothed_coords = splev(unew, tck)

    # Create a new polygon from the smoothed coordinates
    smoothed_polygon = Polygon(zip(smoothed_coords[0], smoothed_coords[1]))

    return smoothed_polygon

def polygon_to_svg(polygon, image_size, output_svg_path):
    # Create an SVG drawing
    dwg = svgwrite.Drawing(output_svg_path, profile='tiny', size=image_size)

    # Extract the points from the polygon and scale/translate them if needed
    if polygon.is_empty:
        print("Polygon is empty.")
        return

    exterior_coords = list(polygon.exterior.coords)

    # Create a path for the exterior of the polygon with smooth corners
    path = dwg.path(d='M {} {}'.format(exterior_coords[0][0], exterior_coords[0][1]), fill='none', stroke='black', stroke_width=1)

    for coord in exterior_coords[1:]:
        path.push('L {} {}'.format(coord[0], coord[1]))

    path.push('Z')  # Close the path
    dwg.add(path)

    # Save the SVG file
    dwg.save()

def process_image_for_cutline(image_path, offset_distance, output_svg_path, smoothing_factor=0.05):
    # Step 1: Detect edges and contours
    contours, image_size = find_edges_and_contours(image_path)
    
    # Step 2: Convert contours to a polygon
    polygon = contours_to_polygon(contours)

    # Step 3: Offset the polygon to create a cutline
    offset_polygon_path = offset_polygon(polygon, offset_distance)

    # Step 4: Smooth the polygon
    smoothed_polygon = smooth_polygon(offset_polygon_path, smoothing_factor)

    # Step 5: Convert the polygon into SVG and save
    polygon_to_svg(smoothed_polygon, image_size, output_svg_path)

if __name__ == "__main__":
    # Path to your image
    image_path = 'papermc.png'

    # Offset distance (positive for outside, negative for inside)
    offset_distance = 10  # Adjust according to your requirement

    # Output path for the SVG cutline
    output_svg_path = 'cutline_output.svg'

    # Smoothing factor for corner smoothness (lower values keep more detail, higher values smooth more)
    smoothing_factor = 0.5  # Adjust this to control smoothness

    # Process the image to generate a vector path cutline
    process_image_for_cutline(image_path, offset_distance, output_svg_path, smoothing_factor)

    print(f"SVG cutline saved at {output_svg_path}")
