---
layout: default
---
<div class="about">
  <div class="about-photo">
    <img src="{{ site.author.photo | relative_url }}" alt="Portrait of Ninon Burgos" width="220" height="283">
  </div>
  <div class="about-text">
    <h1 style="margin-top:0">About me</h1>
    <p>I am a CNRS research director at the <a href="https://parisbraininstitute.org/" target="_blank" rel="noopener">Paris Brain Institute</a>, co-head of the <a href="https://www.aramislab.fr" target="_blank" rel="noopener">ARAMIS Lab</a> and a fellow of the Paris Artificial Intelligence Research Institute (<a href="https://prairie-institute.fr/" target="_blank" rel="noopener">PRAIRIE</a>). I completed my PhD in 2016 at University College London in the <a href="https://www.ucl.ac.uk/medical-image-computing/" target="_blank" rel="noopener">Centre for Medical Image Computing</a> and obtained my Habilitation (HDR) from Sorbonne Université in 2022. In 2019, I received the <a href="https://www.ercim.eu/news/468-2019-ercim-cor-baayen-young-researcher-award-for-ninon-burgos-and-andras-gilyen" target="_blank" rel="noopener">ERCIM Cor Baayen Young Researcher Award</a>. I am associate editor-in-chief of the journal <a href="https://www.sciencedirect.com/journal/pattern-recognition" target="_blank" rel="noopener"><em>Pattern Recognition</em></a>, I was general co-chair of <a href="https://2024.midl.io/" target="_blank" rel="noopener">MIDL 2024</a> and I am programme co-chair of <a href="https://2027.ipmi-conf.org/" target="_blank" rel="noopener">IPMI 2027</a>.</p>
    <p>My research focuses on the processing and analysis of medical images, on the use of images to guide diagnosis, and on the application of these methods to the clinic. In particular, I have contributed to: i) anomaly detection using deep generative models and traditional image processing techniques, ii) the translation of machine learning approaches for quality control and computer-aided diagnosis into clinical practice through hospital data warehouses, iii) reproducible medical image analysis pipelines and the rigorous benchmarking of machine learning methods, and iv) the development of open-source software.</p>
    <a class="cv-button" href="{{ site.author.cv | relative_url }}">Download my CV (PDF)</a>
  </div>
</div>

<h2 id="contact">Contact</h2>
<p>The best way to reach me is by email: <a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a>.</p>
<p class="contact-note"><em>Note: Due to the large number of inquiries and commitments, I may unfortunately not be able to respond to all emails.</em></p>
<p>If you are interested in joining the team, please apply by filling in <a href="https://docs.google.com/forms/d/1QyaYN6KkqNF0QLKU6NGX2CtBQAFV3pIbTvIWvoAWoOY/viewform" target="_blank" rel="noopener">this form</a>.</p>

{% include latest-pubs.html %}
