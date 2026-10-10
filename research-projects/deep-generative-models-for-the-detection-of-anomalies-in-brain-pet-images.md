---
layout: page
title: Deep generative models for the detection of anomalies in brain PET images
permalink: /research-projects/deep-generative-models-for-the-detection-of-anomalies-in-brain-pet-images/
---

Neuroimaging offers an unmatched description of the brain's structure and physiology, which explains its crucial role in the understanding, diagnosis, and treatment of neurological disorders. However, identifying subtle pathological changes simply by looking at images of the brain can be a difficult task. For this reason, images are often transported to a standard space where they can be visually or quantitatively compared to images of normal controls. The main limitation of this approach is its lack of sensitivity due to variabilities between subjects in non-pathological areas.

During my postdoc, I proposed an approach to mitigate this limitation that consists of generating a healthy-looking image specific to the patient under investigation. When compared to the real image of the patient, the pseudo-healthy model can be used to detect the areas of the image that show abnormalities. More details on [this page]({{'/research-projects/postdoc-abnormalitymaps/' | relative_url}}). The image synthesis approach used to generate the pseudo-healthy models is based on a registration and fusion algorithm. However, deep generative models have demonstrated their ability to detect anomalies in medical images.

With the aim to detect subtler anomalies, and in a more computationally efficient manner, we are developing an approach relying on variational autoencoders (VAEs). During the training phase, only images of healthy subjects are used so that the network can learn the distribution of healthy images. During the application phase, the image of a patient is fed to the VAE, which only knows how to reconstruct healthy images. As a result, the reconstructed image would be a pseudo-healthy representation of the input image. Comparing the input image and its pseudo-healthy reconstruction highlights the areas of the brain presenting anomalies.

<figure>
<img src="{{ '/files/anomaly-detection-ae.png' | relative_url }}" alt="Anomaly detection framework using autoencoders">
<figcaption>Anomaly detection framework using autoencoders</figcaption>
</figure>

## Main publications

- Hassanaly, R., Brianceau, C., Solal, M., Colliot, O., and Burgos, N.: **Evaluation of Pseudo-Healthy Image Reconstruction for Anomaly Detection with Deep Generative Models: Application to Brain FDG PET**. *Machine Learning for Biomedical Imaging*, 2(Special Issue for Generative Models): 611–656, 2024. [doi:10.59275/j.melba.2024-b87a](https://doi.org/10.59275/j.melba.2024-b87a) Available on [HAL](https://hal.science/hal-04315738)
- Solal, M., Hassanaly, R., and Burgos, N.: **Leveraging Healthy Population Variability in Deep Learning Unsupervised Anomaly Detection in Brain FDG PET**. In *SPIE Medical Imaging 2024: Image Processing*, 12926:359–365, SPIE, 2024. [doi:10.1117/12.2691683](https://doi.org/10.1117/12.2691683) Available on [HAL](https://hal.science/hal-04291561)
- Hassanaly, R., Bottani, S., Sauty, B., Colliot, O., and Burgos, N.: **Simulation Based Evaluation Framework for Deep Learning Unsupervised Anomaly Detection on Brain FDG-PET**. In *SPIE Medical Imaging 2023: Image Processing*, 12464:524–531, SPIE, 2023. [doi:10.1117/12.2653893](https://doi.org/10.1117/12.2653893) Available on [HAL](https://hal.science/hal-03835015)
- Hassanaly, R., Brianceau, C., Colliot, O., and Burgos, N.: **Unsupervised Anomaly Detection in 3D Brain FDG PET: A Benchmark of 17 VAE-based Approaches**. In *Deep Generative Models Workshop @ MICCAI 2023*, 2023. Available on [HAL](https://hal.science/hal-04185304)
