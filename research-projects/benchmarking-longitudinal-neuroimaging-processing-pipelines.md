---
layout: page
title: Benchmarking longitudinal neuroimaging processing pipelines
permalink: /research-projects/benchmarking-longitudinal-neuroimaging-processing-pipelines/
---

When studying neurodegenerative diseases, which progress with time, imaging, biological and neuropsychological data are acquired at multiple time points, since a single time point may not sufficiently characterise the state of a patient. Longitudinal image processing methods are thus necessary to properly handle such data and extract biomarkers that are sensitive to temporal change. However, there is no clear consensus on how to do so: approaches range from treating each time point independently, to extracting biomarkers cross-sectionally before analysing them longitudinally, to performing a genuinely longitudinal processing of the images themselves. This last approach remains the least standardised and has mainly been applied to T1-weighted MRI (see figure below).

<figure class="figure-medium">
<img src="{{ '/files/longitudinal-processing.png' | relative_url }}" alt="Prototypical longitudinal processing pipeline">
<figcaption>Prototypical example of a longitudinal processing pipeline. An unbiased subject-specific template is first created using an inverse consistent registration approach and each input scan is subsequently registered to it. A cross-sectional segmentation method is then applied to the template, and the estimated parameters are used to initialise the segmentation for each time point (TP).</figcaption>
</figure>

We have initiated a new research axis on this topic within the PhD of Matthieu Joulot (started March 2024), co-supervised with Olivier Colliot. As a first step, we are conducting a systematic comparison of existing longitudinal preprocessing pipelines for T1-weighted MRI, starting by assessing their ability to produce consistent brain volume estimates from test-retest scans, i.e. when no change is expected, across multiple cohorts ([Joulot et al., SPIE Medical Imaging, 2026](https://hal.science/hal-05349492); [Joulot et al., OHBM, 2026](https://hal.science/hal-05590306)). This systematic evaluation will establish a rigorous baseline to guide the design of improved pipelines.

## Main publications

- Joulot, M., Colliot, O., and Burgos, N.: **Comparing Volumetric Consistency of Longitudinal Preprocessing: A Multi-Cohort Test-Retest Study**. In *OHBM 2026 – Annual Meeting of the Organization for Human Brain Mapping*, Bordeaux, France, 2026. <a class="pub-link" href="https://hal.science/hal-05590306" target="_blank" rel="noopener">HAL</a>
- Joulot, M., Colliot, O., and Burgos, N.: **Comparing Longitudinal Preprocessing Pipelines for Brain Volume Consistency in T1-Weighted MRI Test-Retest Scans**. In *SPIE Medical Imaging 2026: Clinical and Biomedical Imaging*, 13929:369–373, SPIE, 2026. [doi:10.1117/12.3086037](https://doi.org/10.1117/12.3086037) <a class="pub-link" href="https://hal.science/hal-05349492" target="_blank" rel="noopener">HAL</a>