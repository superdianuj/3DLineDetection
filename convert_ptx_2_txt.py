import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d

def read_ptx_file(file_path):
    with open(file_path, 'r') as file:
        num_columns = int(file.readline().strip())
        num_rows = int(file.readline().strip())
        for _ in range(12):
            file.readline()
        
        points = []
        colors = []
        for line in file:
            parts = line.strip().split()
            if len(parts) == 7:
                x, y, z, intensity, r, g, b = map(float, parts)
                points.append([x, y, z])
                colors.append([r / 255.0, g / 255.0, b / 255.0])  # Normalize RGB values to [0, 1]
    
    return np.array(points), np.array(colors)

def write_txt_file(points, colors, output_file_path):
    with open(output_file_path, 'w') as file:
        for point, color in zip(points, colors):
            x, y, z = point
            r, g, b = color
            file.write(f"{x} {y} {z} {r} {g} {b}\n")

# Example usage
points, colors = read_ptx_file('office1/office1/scan0.ptx')
write_txt_file(points, colors, 'output.txt')