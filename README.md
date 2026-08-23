# Anomaly detection applied to a small MVTec data set

This is a short project to explore anomaly detection for images by using the "bottle" dataset from MVTec.

# Motivation

Anomaly detection is a useful branch of study in machine learning and statistics with practical use in industry, disaster response, policies, science, among others. The project serves me as an extension of outlier detection for unstructured data, in this case images. 

# Results

Two classification methods, described in the "Approach" section, were used to identify bottles that contained contamination or broken pieces. The overall results and pictures of the error heatmaps are shown below. 

| Method | Combined AUROC | Contamination | Broken (large/small) |
| ------- | --------- | ----------- | ----------- |
| Autoencoder |	0.82 | 0.72 | 0.85 / 0.89 |
| PatchCore | 0.998	| 0.995 | 1.0 / 1.0 |


**Error heatmaps for autoencoder model:**

![Good bottles](.\results\autoencoder_error_heatmap_good.png "Autoencoder heatmap for good bottles")

![Contaminated bottles](.\results\autoencoder_error_heatmap_contamination.png "Autoencoder heatmap for contaminated bottles")

**Error heatmaps for PatchCore model:**

![Good vs contaminated bottle](.\results\patchcore_error_heatmap.png "PatchCore model heatmap")

# Approach

The project is composed of three parts: 1. Short data exploration of the "Bottles" data set; 2. Construction and test of a convolutional autoencoder; 3. PatchCore-like model inspired by the work of [Roth et al.](https://arxiv.org/abs/2106.08265).

The first model uses an autoencoder with a few convolutional layers fitted only on the bottles labeled as "good". Once trained, the model was used to reconstruct test images from the other defect and contamination categories and then the root mean squared error (RMSE) was computed. The hypothesis is that the defective/contaminated images would have higher RMSEs driven by higher reconstruction errors around the anomaly area.

As a baseline model, the performance based on the ROC AUC score was somewhat good, but the model struggled with the contaminated bottles. It failed to identify structure in the images and confounded the ring formed by the light around the bottle as an anomaly.

The PatchCore model was built by using transfer learning from ResNet50. I froze the middle layers to keep the mid-level feature maps, structure, and shape patterns of images and used this pre-trained model as a feature extractor only for the "good" training sample. Each spatial location of the feauture map can be considered a "patch", which can be collected in a "memory bank". At test time, the patch-level features from each image were extracted to find their nearest neighbor in the memory bank. A patch whose nearest neighbor is far away in feature space has no good match among anything seen during training and this becomes the anomaly signal.

All the results are contained in the notebook cv-anomaly-detection.ipynb. 

# Notes/Lessons learned

* Modelling for a few epochs in the first attempt underfitted the data and could not create a good reconstruction of the images. For future projects a more programmatic approach like cross-validation or hyperparameter tuning would be better.

* A big portion of the project was bug fixing. Slight syntax differences between packages and models led to errors during the testing time.

# Credits/References

* Roth et al. (2022), Towards Total Recall in Industrial Anomaly Detection. arXiv: https://arxiv.org/abs/2106.08265

* Bergmann et al. (2021), The MVTec Anomaly Detection Dataset: A Comprehensive Real-World Dataset for Unsupervised Anomaly Detection. https://www.mvtec.com/research-teaching/datasets/mvtec-ad