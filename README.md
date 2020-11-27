# Soccer-Tinyface
A celebrity tiny-face dataset to facilitate low-resolution face-recognition research.

# Dataset
![Alex Morgan](https://github.com/xiyichen/soccer-tinyface/blob/main/img.jpg?raw=true)
<p align="center">
  Gallery and query faces for Alex Morgan
</p>
We build this dataset based on the 50 soccer players who were nominated for Ballon d'Or 2019. All query faces are collected from 88 soccer videos of 1280x720 pixels resolution on YouTube. Most of the videos are clipped from soccer game recordings shot by camcorders with long-range lenses and a few others are from documentaries or personal interviews of the soccer players. The videos are downloaded by Python Pafy library and are processed frame by frame by OpenCV. A HOG based face detector in Python Face Recognition library is used to detect low-resolution faces in each frame of the videos. All detected faces for each identity are manually reviewed to find at least 4 frames with their faces at different angles. The faces are all clear enough to be human recognizable but below 60x60 pixels. The 4 faces with lowest resolutions for each individual are then selected, making the size of the query set 200. The average resolution of the query faces are 40x42 pixels. In addition, we collect 2 nearly front view gallery faces for each identity from Google Images.

# Preliminary Face-identification Experiment
We use a template-based deep heterogeneous feature fusion network proposed by Bodla et al. [1] to detect faces and get their corresponding feature maps. In order to increase the difficulty of face identification, the Celebrities in Frontal-Profile in the Wild (CFPW) dataset [2] with a total of 500 celebrities is used to expand our gallery set. 7 soccer players appear in both of the datasets, and we decide to select the gallery faces for these identities from the CFPW dataset. Consequently, the size of the expanded gallery set is 543. We normalize and average the 2 gallery faces, and choose the 4 query faces with the lowest resolutions for each identity to perform face-identification. The rank accuracy results are as follows:
| Rank 1 | Rank 5 | Rank 10 |
| :---: | :---: | :---: |
| 0.380 | 0.595 | 0.680 |

# References
<a id="1">[1]</a> N. Bodla, J. Zheng, H. Xu, J. Chen, C. Castillo and R. Chellappa, "Deep Heterogeneous Feature Fusion for Template-Based Face Recognition," 2017 IEEE Winter Conference on Applications of Computer Vision (WACV), Santa Rosa, CA, 2017, pp. 586-595, doi: 10.1109/WACV.2017.71.

<a id="2">[2]</a> S. Sengupta, J.C. Cheng, C.D. Castillo, V.M. Patel, R. Chellappa and D.W. Jacobs, "Frontal to Profile Face Verification in the Wild," 2016 IEEE Winter conference on Applications of Computer Vision (WACV), 2016.
