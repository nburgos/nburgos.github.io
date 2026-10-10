---
layout: page
title: PhD – Atlas-based methods for image synthesis
permalink: /research-projects/phd/
---

While magnetic resonance imaging (MRI) provides high-resolution anatomical information, positron emission tomography (PET) provides functional information. Combined PET/MR scanners are expected to offer a new range of clinical applications but efforts are still necessary to mitigate some limitations of this promising technology. One of the factors limiting the use of PET/MR scanners, especially in the case of neurology studies, is the imperfect attenuation correction, leading to a strong bias of the PET activity. Exploiting the simultaneous acquisition of both modalities, I explored a new family of methods to synthesise X-ray computed tomography (CT) images from MR images. The synthetic images are generated through a multi-atlas information propagation scheme, locally matching the MRI-derived patient's morphology to a database of MR/CT image pairs, using a local image similarity measure. The proposed algorithm provides a significant improvement in PET reconstruction accuracy when compared with the current correction, allowing an unbiased analysis of the PET images. [You can try the method online.](http://cmictig.cs.ucl.ac.uk/niftyweb/program.php?p=PCT)

<figure>
<img src="{{ '/files/phd-mrac-diagram.jpg' | relative_url }}" alt="CT synthesis diagram">
<figcaption>CT synthesis diagram for a given T1-w MR image. All the MR images in the atlas database are registered to the target MR image. The CTs in the atlas database are then mapped using the same transformation to the target MR image. A local image similarity measure (LIS) between the mapped and target MR images is converted to weights (W) to reconstruct the target CT (pseudo CT).</figcaption>
</figure>

<figure>
<img src="{{ '/files/phd-mrac-results.jpg' | relative_url }}" alt="PET reconstruction results">
<figcaption>Example of CT, 18F-FDG PET and 18F-florbetapir (Aβ) PET images obtained from the real CT and the pseudo CTs for an amyloid negative (left) and an amyloid positive (right) subject.</figcaption>
</figure>

A similar image synthesis scheme was then used to better identify abnormalities in cerebral glucose metabolism measured by 18F-fluorodeoxyglucose (FDG) PET. This framework consists of creating a subject-specific healthy PET model based on the propagation of morphologically-matched PET images, and comparing the subject's PET image to the model via a Z-score. By accounting for inter-subject morphological differences, the proposed method reduces the variance of the normal population used for comparison in the Z-score, thus increasing the sensitivity.

<figure>
<img src="{{ '/files/phd-pet-model-diagram.jpg' | relative_url }}" alt="Subject-specific PET analysis framework">
<figcaption>Subject-specific PET analysis framework. The control dataset is first transported into the subject space. To generate the subject-specific Z-score parameters, the patient-specific healthy-population mean (Iμ) and standard deviation (Iσ), the set of registered PETs is locally selected and fused. Finally, the subject-specific Z-map is computed using the model parameters.</figcaption>
</figure>

To demonstrate that the applicability of the proposed CT synthesis method is not limited to PET/MR attenuation correction, I redesigned the synthesis process to derive tissue attenuation properties from MR images in the head & neck and pelvic regions to facilitate MR-based radiotherapy treatment planning.

<figure>
<img src="{{ '/files/phd-rtp-results.jpg' | relative_url }}" alt="Radiotherapy planning example">
<figcaption>Example of T2-weighted MR image, reference CT and pseudo CT in the head &amp; neck region.</figcaption>
</figure>

## Main publications

### Image synthesis for PET/MR attenuation correction

- **Burgos, N.**, Cardoso, M.J., Thielemans, K., Modat, M., Pedemonte, S., Dickson, J., Barnes, A., Ahmed, R., Mahoney, C.J., Schott, J.M., Duncan, J.S., Atkinson, D., Arridge, S.R., Hutton, B.F., and Ourselin, S.: **Attenuation Correction Synthesis for Hybrid PET-MR Scanners: Application to Brain Studies**. *IEEE Transactions on Medical Imaging*, 33(12): 2332–2341, 2014. [doi:10.1109/TMI.2014.2340135](https://doi.org/10.1109/TMI.2014.2340135)
- **Burgos, N.**, Cardoso, M.J., Thielemans, K., Modat, M., Dickson, J., Schott, J.M., Atkinson, D., Arridge, S.R., Hutton, B.F., and Ourselin, S.: **Multi-Contrast Attenuation Map Synthesis for PET/MR Scanners: Assessment on FDG and Florbetapir PET Tracers**. *European Journal of Nuclear Medicine and Molecular Imaging*, 42(9): 1447–1458, 2015. [doi:10.1007/s00259-015-3082-x](https://doi.org/10.1007/s00259-015-3082-x)
- **Burgos, N.**, Cardoso, M.J., Modat, M., Pedemonte, S., Dickson, J., Barnes, A., Duncan, J.S., Arridge, S.R., Hutton, B.F., and Ourselin, S.: **Attenuation Correction Synthesis for Hybrid PET-MR Scanners**. In *Medical Image Computing and Computer-Assisted Intervention – MICCAI 2013*, LNCS, 8149: 147–154, Springer, 2013. [doi:10.1007/978-3-642-40811-3_19](https://doi.org/10.1007/978-3-642-40811-3_19)
- Ladefoged, C.N., et al.: **A Multi-Centre Evaluation of Eleven Clinically Feasible Brain PET/MRI Attenuation Correction Techniques Using a Large Cohort of Patients**. *NeuroImage*, 147: 346–359, 2017. [doi:10.1016/j.neuroimage.2016.12.010](https://doi.org/10.1016/j.neuroimage.2016.12.010)
- Sekine, T., **Burgos, N.**, Warnock, G., Huellner, M., Buck, A., Voert, E.E.G.W. ter, Cardoso, M.J., Hutton, B.F., Ourselin, S., Veit-Haibach, P., and Delso, G.: **Multi Atlas-Based Attenuation Correction for Brain FDG-PET Imaging Using a TOF-PET/MR Scanner: Comparison with Clinical Single Atlas- and CT-Based Attenuation Correction**. *Journal of Nuclear Medicine*, 57(8): 1258–1264, 2016. [doi:10.2967/jnumed.115.169045](https://doi.org/10.2967/jnumed.115.169045)
- Lane, C.A., et al.: **Study Protocol: Insight 46 – a Neuroscience Sub-Study of the MRC National Survey of Health and Development**. *BMC Neurology*, 17: 75, 2017. [doi:10.1186/s12883-017-0846-x](https://doi.org/10.1186/s12883-017-0846-x)

### Image synthesis for the analysis of PET data

- **Burgos, N.**, Cardoso, M.J., Mendelson, A.F., Schott, J.M., Atkinson, D., Arridge, S.R., Hutton, B.F., and Ourselin, S.: **Subject-Specific Models for the Analysis of Pathological FDG PET Data**. In *Medical Image Computing and Computer-Assisted Intervention — MICCAI 2015*, LNCS, 9350: 651–658, Springer, 2015. [doi:10.1007/978-3-319-24571-3_78](https://doi.org/10.1007/978-3-319-24571-3_78)

### Image synthesis for MR-based radiotherapy treatment planning

- **Burgos, N.**, Cardoso, M.J., Guerreiro, F., Veiga, C., Modat, M., McClelland, J., Knopf, A.-C., Punwani, S., Atkinson, D., Arridge, S.R., Hutton, B.F., and Ourselin, S.: **Robust CT Synthesis for Radiotherapy Planning: Application to the Head & Neck Region**. In *Medical Image Computing and Computer-Assisted Intervention — MICCAI 2015*, LNCS, 9350: 476–484, Springer, 2015. [doi:10.1007/978-3-319-24571-3_57](https://doi.org/10.1007/978-3-319-24571-3_57)
