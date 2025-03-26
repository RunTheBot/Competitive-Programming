import math
from collections import defaultdict

input = __import__('sys').stdin.readline

def getR(RGB):
    return (RGB >> 16) & 0xFF

def getG(RGB):
    return (RGB >> 8) & 0xFF

def getB(RGB):
    return RGB & 0xFF

def mean(values):
    return sum(values) / len(values) if values else 0

def std_dev(values):
    if not values:
        return 0
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    return math.sqrt(variance)

def histogram(values, bins=8, min_val=0, max_val=256):
    bin_width = (max_val - min_val) / bins
    hist = [0] * bins
    
    for v in values:
        bin_idx = min(bins - 1, int((v - min_val) / bin_width))
        hist[bin_idx] += 1
    
    total = sum(hist)
    return [h / total for h in hist] if total > 0 else [0] * bins

# No numpy :sob:
def extract_features(image, height, width, decimate=1):
    # Extract R, G, B arrays
    R = []
    G = []
    B = []
    r_2d = []
    g_2d = []
    b_2d = []
    
    for i in range(0, height, decimate):
        r_row = []
        g_row = []
        b_row = []
        for j in range(0, width, decimate):
            pixel = image[i][j]
            r = getR(pixel)
            g = getG(pixel)
            b = getB(pixel)
            R.append(r)
            G.append(g)
            B.append(b)
            r_row.append(r)
            g_row.append(g)
            b_row.append(b)
        r_2d.append(r_row)
        g_2d.append(g_row)
        b_2d.append(b_row)
    
    # New decimated dimensions
    dec_height = len(r_2d)
    dec_width = len(r_2d[0]) if dec_height > 0 else 0
    
    # Calculate average RGB
    avg_r = mean(R)
    avg_g = mean(G)
    avg_b = mean(B)
    
    # Calculate standard deviation of RGB
    std_r = std_dev(R)
    std_g = std_dev(G)
    std_b = std_dev(B)
    
    # Calculate brightness
    brightness = mean([r + g + b for r, g, b in zip(R, G, B)]) / 3
    
    # Calculate color variance
    color_variance = mean([max(r, g, b) - min(r, g, b) for r, g, b in zip(R, G, B)])
    
    # Calculate number of unique colors
    unique_colors = set()
    for i in range(dec_height):
        for j in range(dec_width):
            unique_colors.add((r_2d[i][j], g_2d[i][j], b_2d[i][j]))
    normalized_unique_colors = len(unique_colors) / (dec_height * dec_width)
    
    # Calculate edge intensity
    edge_intensity = 0
    for i in range(1, dec_height):
        for j in range(1, dec_width):
            edge_r = abs(r_2d[i][j] - r_2d[i-1][j]) + abs(r_2d[i][j] - r_2d[i][j-1])
            edge_g = abs(g_2d[i][j] - g_2d[i-1][j]) + abs(g_2d[i][j] - g_2d[i][j-1])
            edge_b = abs(b_2d[i][j] - b_2d[i-1][j]) + abs(b_2d[i][j] - b_2d[i][j-1])
            edge_intensity += (edge_r + edge_g + edge_b)
    edge_intensity /= (dec_height * dec_width)
    
    # Calculate color histogram features
    r_bins = histogram(R, 8, 0, 256)
    g_bins = histogram(G, 8, 0, 256)
    b_bins = histogram(B, 8, 0, 256)
    
    # Create feature vector
    features = [
        avg_r, avg_g, avg_b,
        std_r, std_g, std_b,
        brightness, color_variance,
        normalized_unique_colors, edge_intensity
    ]
    features.extend(r_bins)
    features.extend(g_bins)
    features.extend(b_bins)
    
    return features

def classify_image(features):
    # Precalculated style vectors
    style1_vector = [156.28869159904986, 143.84964191380493, 139.0742674997212, 77.32441580957948, 77.24762341906425, 79.99896449543267, 146.40420033752534, 37.522636099393345, 0.11002451270741079, 31.061392260019257, 0.12898775377594487, 0.08354349345541462, 0.07013483873839388, 0.046632303750325926, 0.05258470889521442, 0.17479979148777158, 0.16726240712145107, 0.2760547027754836, 0.1427664059913411, 0.0985452402029184, 0.10994366261901112, 0.046708062073757314, 0.06062272890619619, 0.15985288959361266, 0.18772519430761478, 0.19383581630554847, 0.18370865998538258, 0.10904304073936906, 0.07821320588515895, 0.03288363088707672, 0.0694991411619793, 0.17693789582520764, 0.10861976663203826, 0.24109465888378748]
    style2_vector = [95.22998804075209, 91.9766596265078, 55.245337652840945, 54.78839091339409, 57.249812793788045, 52.41643451150377, 80.81732844003362, 42.48390354516841, 0.268390742782282, 62.453184724968686, 0.09375198652033485, 0.2558034479434448, 0.23137678720914903, 0.17775684595610045, 0.09983343080548415, 0.05442838128666535, 0.04532202343286533, 0.0417270968459561, 0.11242522196954716, 0.276128498450992, 0.2255209242963549, 0.16619136024322723, 0.081724770367807, 0.044033980208951294, 0.043321699212312964, 0.050653545250807466, 0.4302129849713269, 0.31994330062289894, 0.10477794945949509, 0.03187482911475842, 0.021712568139872126, 0.033728136823544926, 0.04517151291938567, 0.012578717948717948]
    style3_vector = [110.65583442721368, 100.24190518931658, 86.17103576677508, 58.081058344118546, 55.97307120067656, 51.10048030073915, 99.02292512776845, 27.16829928865191, 0.4531338492705357, 197.3015040065744, 0.1247657419246857, 0.15004984030970414, 0.15790853732583765, 0.1694428564533169, 0.16007235971800396, 0.11531981412960719, 0.07239995351173817, 0.05004089662710633, 0.16313631595173989, 0.17432557313592129, 0.16130222065309158, 0.1721059271954194, 0.14046260926804127, 0.0911704503998641, 0.05860596941094051, 0.03889093398498199, 0.2031460810581968, 0.22815770807163177, 0.17905946155442728, 0.1528808822676564, 0.1076211482319134, 0.06119749146611132, 0.039071132421417853, 0.028866094928645232]
    style4_vector = [183.6546294571317, 135.0949213059441, 55.594299310519716, 41.09990296858506, 63.15343236810274, 49.128822383097614, 124.78128335786519, 140.28779233691245, 0.15385755889412026, 16.24364411528854, 0.030513038583252192, 0.09416057083739046, 0.0394797803067186, 0.03885252599457504, 0.04481336995109053, 0.12196290589907838, 0.22117343622171112, 0.4090443722061836, 0.12633959000597667, 0.08807587013528201, 0.08351634034076308, 0.1042594600227867, 0.11946045425155191, 0.31989067013427996, 0.05663289798326539, 0.10182471712609424, 0.601953475678473, 0.12098379534941565, 0.023924160094223518, 0.026573582477113104, 0.07389153022744258, 0.08923883147599558, 0.03390314769975787, 0.029531476997578694]
    
    min_length = min(len(features), len(style1_vector))
    features = features[:min_length]
    style1_vector = style1_vector[:min_length]
    style2_vector = style2_vector[:min_length]
    style3_vector = style3_vector[:min_length]
    style4_vector = style4_vector[:min_length]
    
    dist1 = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, style1_vector)))
    dist2 = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, style2_vector)))
    dist3 = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, style3_vector)))
    dist4 = math.sqrt(sum((a - b) ** 2 for a, b in zip(features, style4_vector)))
    
    distances = [dist1, dist2, dist3, dist4]
    
    # Apply style-specific heuristics
    if features[8] < 0.1 and features[6] > 100 and features[7] > 80:
        distances[0] *= 0.7  # Style 1: geometric shapes, high contrast, limited palette

    if 90 < features[0] < 100 and 90 < features[1] < 100 and 50 < features[2] < 60:
        distances[1] *= 0.7  # Style 2: impressionist landscapes, natural colors

    if features[7] > 90 and features[8] > 0.4 and features[9] > 15:
        distances[2] *= 0.7  # Style 3: expressionist action paintings, high variance

    # Adjusted heuristic for Style 4:
    # For the provided style 4 vector, average red > 110, green > 90, blue < 40 and low edge intensity (<20)
    if features[0] > 110 and features[1] > 90 and features[2] < 40 and features[9] < 20:
        distances[3] *= 0.7  # Style 4: color field paintings, low blue average and low edge intensity
    
    return distances.index(min(distances)) + 1

# num_tests = 1
num_tests = int(input())
for _ in range(num_tests):
    H, W = map(int, input().split())
    
    image = []
    
    for i in range(H):
        row = list(map(int, input().split()))
        image.append(row)
    
    # Determine decimation factor based on image size
    # For large images, use a higher decimation factor
    decimate = 1
    if H > 400 or W > 400:
        decimate = 2
    
    features = extract_features(image, H, W, decimate)
    # print(features)
    style = classify_image(features)
    
    print(style)
