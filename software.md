---
layout: page
title: Software
permalink: /software/
---

## Clinica

[Clinica](https://www.clinica.run) is an open source software platform for clinical neuroscience research studies developed by the [Aramis Lab](https://www.aramislab.fr). It provides a standardised file organisation; complex processing pipelines involving the combination of several image analysis software packages; feature extraction and analysis approaches based on statistics and machine learning.

More precisely, Clinica integrates a comprehensive set of processing tools for the main neuroimaging modalities: currently MRI (anatomical and diffusion) and PET. For each modality, Clinica allows the easy extraction of various types of features (regional measures, parametric maps, surfaces, curves, networks). Such features are then subsequently used as input of machine learning, deep learning, statistical modelling, morphometry or network analysis methods. Processing pipelines are based on combinations of freely available tools developed by the community. It provides an integrated data management specification to store raw and processing data. Clinica is written in Python and uses the Nipype system for pipelining. It combines widely-used software packages for neuroimaging data analysis (SPM, Freesurfer, FSL, MRtrix, etc.), machine learning (Scikit-learn), deep learning (PyTorch) and the BIDS standard for data organization. Overall, Clinica should help to: i) easily share data and results; ii) make research more reproducible; iii) spend less time on data management and processing.

I contribute to the management of the project and of the developers.

**References:**

- [GitHub](https://github.com/aramis-lab/clinica) / [Documentation](https://www.clinica.run/doc/)
- Routier, A., Burgos, N., Díaz, M., Bacci, M., Bottani, S., El-Rifai, O., Fontanella, S., Gori, P., Guillon, J., Guyot, A., Hassanaly, R., Jacquemont, T., Lu, P., Marcoux, A., Moreau, T., Samper-González, J., Teichmann, M., Thibeau-Sutre, E., Vaillant, G., Wen, J., Wild, A., Habert, M.-O., Durrleman, S., and Colliot, O.: **Clinica: An Open Source Software Platform for Reproducible Clinical Neuroscience Studies**, *Frontiers in Neuroinformatics*, 15: 39, 2021. [doi:10.3389/fninf.2021.689675](https://doi.org/10.3389/fninf.2021.689675) Available on [HAL](https://hal.science/hal-02308126)
- OHBM [2018](https://hal.science/hal-01760658), [2019](https://hal.science/hal-02132147), [2020](https://hal.science/hal-02549242), [2022](https://hal.science/hal-03728243)
- Samper-González, J., Burgos, N., Bottani, S., Fontanella, S., Lu, P., Marcoux, A., Routier, A., Guillon, J., Bacci, M., Wen, J., Bertrand, A., Bertin, H., Habert, M.-O., Durrleman, S., Evgeniou, T., and Colliot, O.: **Reproducible Evaluation of Classification Methods in Alzheimer's Disease: Framework and Application to MRI and PET Data**. *NeuroImage*, 183: 504–521, 2018. [doi:10.1016/j.neuroimage.2018.08.042](https://doi.org/10.1016/j.neuroimage.2018.08.042) Available on [HAL](https://hal.science/hal-01858384)
- Wen, J., Thibeau-Sutre, E., Diaz-Melo, M., Samper-González, J., Routier, A., Bottani, S., Dormont, D., Durrleman, S., Burgos, N., and Colliot, O.: **Convolutional Neural Networks for Classification of Alzheimer's Disease: Overview and Reproducible Evaluation**. *Medical Image Analysis*, 63: 101694, 2020. [doi:10.1016/j.media.2020.101694](https://doi.org/10.1016/j.media.2020.101694) Available on [HAL](https://hal.science/hal-02562504)
- Wen, J., Samper-González, J., Bottani, S., Routier, A., Burgos, N., Jacquemont, T., Fontanella, S., Durrleman, S., Epelbaum, S., Bertrand, A., and Colliot, O.: **Reproducible Evaluation of Diffusion MRI Features for Automatic Classification of Patients with Alzheimer's Disease**. *Neuroinformatics*, 19: 57–78, 2021. [doi:10.1007/s12021-020-09469-5](https://doi.org/10.1007/s12021-020-09469-5) Available on [HAL](https://hal.science/hal-02566361)
- Marcoux, A., Burgos, N., Bertrand, A., Teichmann, M., Routier, A., Wen, J., Samper-Gonzalez, J., Bottani, S., Durrleman, S., Habert, M.-O., and Colliot, O.: **An Automated Pipeline for the Analysis of PET Data on the Cortical Surface**. *Frontiers in Neuroinformatics*, 12, 2018. [doi:10.3389/fninf.2018.00094](https://doi.org/10.3389/fninf.2018.00094)

## ClinicaDL

As deep learning faces a reproducibility crisis and studies on deep learning applied to neuroimaging are contaminated by methodological flaws, there is an urgent need to provide a safe environment for deep learning users to help them avoid common pitfalls that will bias and discredit their results. Several tools have been proposed to help deep learning users design their framework for neuroimaging data sets.

ClinicaDL has been developed to bring answers to three common issues encountered by deep learning users who are not always familiar with neuroimaging data: (1) the format and preprocessing of neuroimaging data sets, (2) the contamination of the evaluation procedure by data leakage and (3) a lack of reproducibility. The combination of ClinicaDL and its companion project Clinica allows performing an end-to-end neuroimaging analysis, from the download of raw data sets to the interpretation of trained networks, including neuroimaging preprocessing, quality check, label definition, architecture search, and network training and evaluation.

I contribute to the management of the project and of the developers.

**References:**

- [GitHub](https://github.com/aramis-lab/clinicadl) / [Documentation](https://clinicadl.readthedocs.io/)
- Tutorial [Deep learning classification from brain MRI: Application to Alzheimer's disease](https://aramislab.paris.inria.fr/clinicadl/tuto)
- Thibeau-Sutre, E., Diaz, M., Hassanaly, R., Routier, A., Dormont, D., Colliot, O., and Burgos, N.: **ClinicaDL: An Open-Source Deep Learning Software for Reproducible Neuroimaging Processing**. *Computer Methods and Programs in Biomedicine*, 220: 106818, 2022. [doi:10.1016/j.cmpb.2022.106818](https://doi.org/10.1016/j.cmpb.2022.106818) Available on [HAL](https://hal.science/hal-03351976)

## AD-ML / AD-DL

AD-ML and AD-DL are frameworks for the reproducible evaluation of machine learning and deep learning classification experiments using neuroimaging for the computer-aided diagnosis of Alzheimer's disease (AD) that rely on [Clinica](https://www.clinica.run).

**References AD-ML:**

- [GitHub](https://github.com/aramis-lab/ad-ml)
- Samper-González, J., Burgos, N., Bottani, S., Fontanella, S., Lu, P., Marcoux, A., Routier, A., Guillon, J., Bacci, M., Wen, J., Bertrand, A., Bertin, H., Habert, M.-O., Durrleman, S., Evgeniou, T., and Colliot, O.: **Reproducible Evaluation of Classification Methods in Alzheimer's Disease: Framework and Application to MRI and PET Data**. *NeuroImage*, 183: 504–521, 2018. [doi:10.1016/j.neuroimage.2018.08.042](https://doi.org/10.1016/j.neuroimage.2018.08.042) Available on [HAL](https://hal.science/hal-01858384)
- Wen, J., Samper-González, J., Bottani, S., Routier, A., Burgos, N., Jacquemont, T., Fontanella, S., Durrleman, S., Epelbaum, S., Bertrand, A., and Colliot, O.: **Reproducible Evaluation of Diffusion MRI Features for Automatic Classification of Patients with Alzheimer's Disease**. *Neuroinformatics*, 19: 57–78, 2021. [doi:10.1007/s12021-020-09469-5](https://doi.org/10.1007/s12021-020-09469-5) Available on [HAL](https://hal.science/hal-02566361)

**References AD-DL:**

- [GitHub](https://github.com/aramis-lab/ad-dl)
- Wen, J., Thibeau-Sutre, E., Diaz-Melo, M., Samper-González, J., Routier, A., Bottani, S., Dormont, D., Durrleman, S., Burgos, N., and Colliot, O.: **Convolutional Neural Networks for Classification of Alzheimer's Disease: Overview and Reproducible Evaluation**. *Medical Image Analysis*, 63: 101694, 2020. [doi:10.1016/j.media.2020.101694](https://doi.org/10.1016/j.media.2020.101694) Available on [HAL](https://hal.science/hal-02562504)

## NiftyWeb

[NiftyWeb](http://niftyweb.cs.ucl.ac.uk/index.php) is a web service tool developed at UCL that provides an entry point to cutting edge medical image analysis algorithms. NiftyWeb has a friendly interface and allows anyone to test or use the algorithms with minimal effort and with their optimal configurations. The website currently runs on a distributed network, where different nodes are responsible for specific algorithms.

I contributed to the creation of the [pCT web service tool](http://niftyweb.cs.ucl.ac.uk/program.php?p=PCT), which enables the fully automated synthesis of CT images from MRI data. This tool has already been used more than 4000 times.

**References:**

- Prados Carrasco, F., Cardoso, M.J., Burgos, N., Wheeler-Kingshott, C.A.M., and Ourselin, S.: **NiftyWeb: Web Based Platform for Image Processing on the Cloud**. In *Proceedings of the 24th Scientific Meeting and Exhibition of the International Society for Magnetic Resonance in Medicine (ISMRM)*, 2016. Available on [HAL](https://hal.science/hal-01827198v1).

## NiftySeg

[NiftySeg](http://niftyseg.sourceforge.net) is an open source image segmentation and parcellation software developed by the [Translational Imaging Group](http://cmictig.cs.ucl.ac.uk/) (UCL) with 6000+ downloads from 43 countries. I contributed to the creation of novel algorithms for image synthesis based on a multi-atlas propagation and fusion technique. My contribution mainly focused on the fusion part of the approach, where the propagated atlases are combined locally by computing for each voxel a local similarity measure between each deformed atlas and the target subject.
