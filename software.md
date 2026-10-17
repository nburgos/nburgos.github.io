---
layout: page
title: Software
permalink: /software/
---

<details class="software-group" open>
<summary class="software-heading"><span class="software-title">Clinica</span></summary>

<p class="software-links">
  <a class="pub-link" href="https://github.com/aramis-lab/clinica" target="_blank" rel="noopener">GitHub</a>
  <a class="pub-link" href="https://aramislab.paris.inria.fr/clinica/docs/public/latest/" target="_blank" rel="noopener">Documentation</a>
</p>

[Clinica](https://www.clinica.run) is an open source software platform for neuroimaging studies. It aims to make neuroimaging research easier and more reproducible, enabling researchers to spend less time on data management and processing, perform reproducible evaluations of their methods, and easily share data and results within their institution and with external collaborators.

The core of Clinica is a set of automatic pipelines for the processing and analysis of multimodal neuroimaging data, currently T1-weighted, FLAIR and diffusion MRI, and PET data, as well as tools for statistics and machine learning. Clinica relies on the Brain Imaging Data Structure (BIDS) for the organisation of raw datasets, and provides converters of several public neuroimaging datasets to BIDS, including ADNI, AIBL, OASIS and NIFD. Processing pipelines are built by combining widely used, freely available tools developed by the neuroimaging community (SPM, FreeSurfer, FSL, MRtrix, etc.), and processed data, such as tissue probability maps, cortical thickness maps or regional averages, follow the ClinicA Processed Structure (CAPS) format, which shares the same philosophy as BIDS. This consistent organisation of raw and processed files facilitates the execution of single pipelines or sequences of pipelines, as well as the integration of processed data into statistical or machine learning frameworks.

I lead the development of the project and manage the developers.

**References:**

- Routier, A., Burgos, N., Díaz, M., Bacci, M., Bottani, S., El-Rifai, O., Fontanella, S., Gori, P., Guillon, J., Guyot, A., Hassanaly, R., Jacquemont, T., Lu, P., Marcoux, A., Moreau, T., Samper-González, J., Teichmann, M., Thibeau-Sutre, E., Vaillant, G., Wen, J., Wild, A., Habert, M.-O., Durrleman, S., and Colliot, O.: **Clinica: An Open Source Software Platform for Reproducible Clinical Neuroscience Studies**, *Frontiers in Neuroinformatics*, 15: 39, 2021. [doi:10.3389/fninf.2021.689675](https://doi.org/10.3389/fninf.2021.689675) <a class="pub-link" href="https://hal.science/hal-02308126" target="_blank" rel="noopener">HAL</a>
- Marcoux, A., Burgos, N., Bertrand, A., Teichmann, M., Routier, A., Wen, J., Samper-Gonzalez, J., Bottani, S., Durrleman, S., Habert, M.-O., and Colliot, O.: **An Automated Pipeline for the Analysis of PET Data on the Cortical Surface**. *Frontiers in Neuroinformatics*, 12, 2018. [doi:10.3389/fninf.2018.00094](https://doi.org/10.3389/fninf.2018.00094)
- OHBM [2018](https://hal.science/hal-01760658), [2019](https://hal.science/hal-02132147), [2020](https://hal.science/hal-02549242), [2022](https://hal.science/hal-03728243), [2023](https://hal.science/hal-04278898), [2026a](https://hal.science/hal-05641657), [2026b](https://hal.science/hal-05641717)

</details>

<details class="software-group" open>
<summary class="software-heading"><span class="software-title">ClinicaDL</span></summary>

<p class="software-links">
  <a class="pub-link" href="https://github.com/aramis-lab/clinicadl" target="_blank" rel="noopener">GitHub</a>
  <a class="pub-link" href="https://clinicadl.readthedocs.io/" target="_blank" rel="noopener">Documentation</a>
  <a class="pub-link" href="https://aramislab.paris.inria.fr/clinicadl/tuto" target="_blank" rel="noopener">Tutorial</a>
</p>

[ClinicaDL](https://clinicadl.readthedocs.io) is an open source software platform that aims to enhance the reproducibility and rigour of research on deep learning applied to neuroimaging. Neuroimaging data have specific characteristics: they are three-dimensional, carry physical information such as voxel spacing, and are often longitudinal, which limits the direct use of standard deep learning frameworks. General-purpose medical imaging frameworks such as MONAI address some of these constraints, but lack integration with neuroimaging-specific data standards and preprocessing pipelines. ClinicaDL fills this gap by natively integrating with the brain imaging data structure (BIDS) and neuroimaging preprocessing pipelines, so it can be used with a large variety of neuroimaging datasets.

Its main features include data preparation, model training, inference and prediction, and interpretation algorithms, supporting classification, regression, reconstruction, segmentation and generative tasks. Training outputs follow a dedicated structure, the Model Analysis and Processing Structure (MAPS), which stores checkpoints, logs, evaluation results and all elements required to reproduce an experiment, such as user-defined variables and the Python environment, thereby guarding against data leakage and ensuring reproducibility and fair comparison between models. The combination of ClinicaDL and its companion project Clinica allows an end-to-end neuroimaging analysis, from the download of raw datasets to the interpretation of trained networks, including preprocessing, quality check, label definition, architecture search, and network training and evaluation.

I lead the development of the project and manage the developers.

**References:**

- Thibeau-Sutre, E., Diaz, M., Hassanaly, R., Routier, A., Dormont, D., Colliot, O., and Burgos, N.: **ClinicaDL: An Open-Source Deep Learning Software for Reproducible Neuroimaging Processing**. *Computer Methods and Programs in Biomedicine*, 220: 106818, 2022. [doi:10.1016/j.cmpb.2022.106818](https://doi.org/10.1016/j.cmpb.2022.106818) <a class="pub-link" href="https://hal.science/hal-03351976" target="_blank" rel="noopener">HAL</a>
- [OHBM 2022](https://hal.science/hal-04279014), [SPIE Medical Imaging 2024](https://hal.science/hal-04419141), [OHBM 2026](https://hal.science/hal-05587597)

</details>

<details class="software-group" open>
<summary class="software-heading"><span class="software-title">AD-ML / AD-DL</span></summary>

<p class="software-links">
  <a class="pub-link" href="https://github.com/aramis-lab/ad-ml" target="_blank" rel="noopener">GitHub (AD-ML)</a>
  <a class="pub-link" href="https://github.com/aramis-lab/ad-dl" target="_blank" rel="noopener">GitHub (AD-DL)</a>
</p>

AD-ML and AD-DL are frameworks for the reproducible evaluation of machine learning and deep learning classification experiments using neuroimaging for the computer-aided diagnosis of Alzheimer's disease (AD) that rely on [Clinica](https://www.clinica.run).

**References AD-ML:**

- Samper-González, J., Burgos, N., Bottani, S., Fontanella, S., Lu, P., Marcoux, A., Routier, A., Guillon, J., Bacci, M., Wen, J., Bertrand, A., Bertin, H., Habert, M.-O., Durrleman, S., Evgeniou, T., and Colliot, O.: **Reproducible Evaluation of Classification Methods in Alzheimer's Disease: Framework and Application to MRI and PET Data**. *NeuroImage*, 183: 504–521, 2018. [doi:10.1016/j.neuroimage.2018.08.042](https://doi.org/10.1016/j.neuroimage.2018.08.042) <a class="pub-link" href="https://hal.science/hal-01858384" target="_blank" rel="noopener">HAL</a>
- Wen, J., Samper-González, J., Bottani, S., Routier, A., Burgos, N., Jacquemont, T., Fontanella, S., Durrleman, S., Epelbaum, S., Bertrand, A., and Colliot, O.: **Reproducible Evaluation of Diffusion MRI Features for Automatic Classification of Patients with Alzheimer's Disease**. *Neuroinformatics*, 19: 57–78, 2021. [doi:10.1007/s12021-020-09469-5](https://doi.org/10.1007/s12021-020-09469-5) <a class="pub-link" href="https://hal.science/hal-02566361" target="_blank" rel="noopener">HAL</a>

**References AD-DL:**

- Wen, J., Thibeau-Sutre, E., Diaz-Melo, M., Samper-González, J., Routier, A., Bottani, S., Dormont, D., Durrleman, S., Burgos, N., and Colliot, O.: **Convolutional Neural Networks for Classification of Alzheimer's Disease: Overview and Reproducible Evaluation**. *Medical Image Analysis*, 63: 101694, 2020. [doi:10.1016/j.media.2020.101694](https://doi.org/10.1016/j.media.2020.101694) <a class="pub-link" href="https://hal.science/hal-02562504" target="_blank" rel="noopener">HAL</a>

</details>

<details class="software-group" open>
<summary class="software-heading"><span class="software-title">NiftyWeb</span></summary>

<p class="software-links">
  <a class="pub-link" href="http://niftyweb.cs.ucl.ac.uk/index.php" target="_blank" rel="noopener">NiftyWeb</a>
  <a class="pub-link" href="http://niftyweb.cs.ucl.ac.uk/program.php?p=PCT" target="_blank" rel="noopener">pCT tool</a>
</p>

[NiftyWeb](http://niftyweb.cs.ucl.ac.uk/index.php) is a web service tool developed at UCL that provides an entry point to cutting edge medical image analysis algorithms. NiftyWeb has a friendly interface and allows anyone to test or use the algorithms with minimal effort and with their optimal configurations. The website currently runs on a distributed network, where different nodes are responsible for specific algorithms.

I contributed to the creation of the [pCT web service tool](http://niftyweb.cs.ucl.ac.uk/program.php?p=PCT), which enables the fully automated synthesis of CT images from MRI data. This tool has already been used more than 5500 times.

**References:**

- Prados Carrasco, F., Cardoso, M.J., Burgos, N., Wheeler-Kingshott, C.A.M., and Ourselin, S.: **NiftyWeb: Web Based Platform for Image Processing on the Cloud**. In *Proceedings of the 24th Scientific Meeting and Exhibition of the International Society for Magnetic Resonance in Medicine (ISMRM)*, 2016. <a class="pub-link" href="https://hal.science/hal-01827198" target="_blank" rel="noopener">HAL</a>

</details>

<details class="software-group" open>
<summary class="software-heading"><span class="software-title">NiftySeg</span></summary>

<p class="software-links">
  <a class="pub-link" href="https://github.com/KCL-BMEIS/NiftySeg" target="_blank" rel="noopener">GitHub</a>
</p>

[NiftySeg](https://github.com/KCL-BMEIS/NiftySeg) is an open source image segmentation and parcellation software. I contributed to the creation of novel algorithms for image synthesis based on a multi-atlas propagation and fusion technique. My contribution mainly focused on the fusion part of the approach, where the propagated atlases are combined locally by computing for each voxel a local similarity measure between each deformed atlas and the target subject.

</details>
