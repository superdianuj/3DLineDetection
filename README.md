# 3DLineDetection
A simple and efficient 3D line detection algorithm for large scale unorganized point cloud. A conference paper based on this code can be found here https://arxiv.org/abs/1901.02532

Prerequisites:
---
1. OpenCV > 2.4.x
2. OpenMP
3. Python with Pytorch, Open3D

Installation:
```bash
git clone --recursive https://github.com/superdianuj/3DLineDetection.git
cd 3DLineDetection
# if the point cloud data is in .ptx format, then
python convert_ptx_2_txt.py
cmake -B build && make -C build
./build/src/LineFromPointCloud

```

![image](https://github.com/superdianuj/3DLineDetection/assets/47445756/ee9cb3d8-4341-42fa-aef1-f79f918ad0c1)
