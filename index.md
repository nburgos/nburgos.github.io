---
layout: default
---
<div class="about">
  <div class="about-photo">
    <img src="{{ site.author.photo | relative_url }}" alt="Portrait of Ninon Burgos" width="220" height="283">
  </div>
  <div class="about-text">
    <h1 style="margin-top:0">About me</h1>
    <p>I am a CNRS research director at the <a href="https://parisbraininstitute.org/" target="_blank" rel="noopener">Paris Brain Institute</a>, co-head of the <a href="https://www.aramislab.fr" target="_blank" rel="noopener">ARAMIS Lab</a> and a fellow of <a href="https://prairie-institute.fr/" target="_blank" rel="noopener">PR[AI]RIE</a>, the PaRis Artificial Intelligence Research InstitutE. I completed my PhD in 2016 at University College London in the <a href="https://www.ucl.ac.uk/medical-image-computing/" target="_blank" rel="noopener">Centre for Medical Image Computing</a> under the supervision of Sébastien Ourselin and obtained my Habilitation (ability to supervise research, HDR) from Sorbonne Université in 2022. In 2019, I received the <a href="https://www.ercim.eu/news/468-2019-ercim-cor-baayen-young-researcher-award-for-ninon-burgos-and-andras-gilyen" target="_blank" rel="noopener">ERCIM Cor Baayen Young Researcher Award</a>.</p>
    <p>My research focuses on the processing and analysis of medical images, on the use of images to guide diagnosis, and on the application of these methods to the clinic. In particular, I have contributed to: i) anomaly detection using both traditional image processing techniques and deep generative models, ii) the translation of machine learning approaches for quality control and computer-aided diagnosis into clinical practice, iii) reproducible medical image processing and computer-aided diagnosis with machine learning, and iv) the development of open-source software. These efforts aim to enhance the reliability and scalability of research in clinical neuroscience and support practical advancements in medical imaging.</p>
    <a class="cv-button" href="{{ site.author.cv | relative_url }}">Download my CV (PDF)</a>
  </div>
</div>

{% include latest-pubs.html %}
