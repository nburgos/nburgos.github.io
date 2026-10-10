---
layout: page
title: Postdoc – Joint segmentation and image synthesis
permalink: /research-projects/postdoc-mrrtp/
---

At the end of my PhD, I received funding from the *CMIC-EPSRC platform grant* to explore a new field of research. During this 1-year postdoc at UCL, I decided to tackle the problem of automatic MR-based radiotherapy treatment planning in the pelvic region.

The aim of radiotherapy treatment planning (RTP) is to deliver an optimal dose of radiation over the target area while sparing the normal tissues. RTP first requires contouring the target and organs at risk (OARs). Once these volumes have been defined, the optimal dose distribution for treating the tumour is determined according to the attenuation properties of the different tissues. Most radiotherapy treatments are planned using an X-ray computed tomography (CT) scan of the patient. The acquisition of a CT is fast and the tissue attenuation coefficients can easily be derived from the CT intensity values in Hounsfield unit (HU). However, CT images have low soft tissue contrast, which can lead to large variations when delineating the organs, particularly when located in the brain, head &amp; neck, or pelvic regions. Magnetic resonance (MR) imaging is often preferred over CT as a structural imaging modality, mainly for its excellent soft tissue contrast. Although increasingly used in clinical practice, the role of MR in RTP is currently limited by the fact that it does not readily provide electron density information, hampering the calculation of dose distributions. My work consisted of trying to tackle the problem of RTP from MR images by developing a multi-atlas propagation framework to jointly delineate the OARs and estimate the tissue attenuation properties.

I developed an iterative multi-atlas propagation framework that combines in a single pipeline segmentation and CT synthesis, with the aim to improve both the segmentation and synthesis accuracy when compared to state-of-the art methods, and guarantee consistent results. I also proposed a new strategy to register atlas MR and CT images combining structure-guided registration and image synthesis, with the aim to build a higher quality atlas database and thus further improve the segmentation and synthesis accuracy. A diagram summarising the method and an example of results are displayed in the figures below.

<figure>
<img src="{{ '/files/postdoc-mrrtp-diagram.jpg' | relative_url }}" alt="Joint segmentation and CT synthesis diagram">
<figcaption>Joint segmentation and CT synthesis at iteration <em>t</em>. All the atlases are non-rigidly registered to the target. A local similarity measure between the mapped atlases and the target is used to jointly generate a pseudo CT and a segmented image.</figcaption>
</figure>

<figure>
<img src="{{ '/files/postdoc-mrrtp-results.jpg' | relative_url }}" alt="Segmentation and pseudo CT results">
<figcaption>The segmentations of the prostate (red), bladder (orange), rectum (green) and femur heads (blue), and the pseudo CTs were obtained from the T1-weighted and T2-weighted MR images of the patient. Note how the smoothness of the segmentations and sharpness of the pseudo CTs increase with the number of iterations.</figcaption>
</figure>

## Main publications

- **Burgos, N.**, Guerreiro, F., McClelland, J., Presles, B., Modat, M., Nill, S., Dearnaley, D., deSouza, N., Oelfke, U., Knopf, A.-C., Ourselin, S., and Cardoso, M.J.: **Iterative Framework for the Joint Segmentation and CT Synthesis of MR Images: Application to MRI-Only Radiotherapy Treatment Planning**. *Physics in Medicine and Biology*, 62(11): 4237, 2017. [doi:10.1088/1361-6560/aa66bf](https://doi.org/10.1088/1361-6560/aa66bf)
- **Burgos, N.**, Guerreiro, F., McClelland, J., Nill, S., Dearnaley, D., deSouza, N., Oelfke, U., Knopf, A.-C., Ourselin, S., and Cardoso, M.J.: **Joint Segmentation and CT Synthesis for MRI-Only Radiotherapy Treatment Planning**. In *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2016*, LNCS, 9901: 547–555, Springer, 2016. [doi:10.1007/978-3-319-46723-8_63](https://doi.org/10.1007/978-3-319-46723-8_63)
