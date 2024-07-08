<a name="readme-top"></a>



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/awcereh/Ozon-Detection">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Ozon Level Detection</h3>

  <p align="center">
    A final project for the Computational Physics Capita Selecta course.
    <br />
    <a href="https://github.com/awcereh/Ozon-Detection">View Demo</a>
    ·
    <a href="https://www.datascienceportfol.io/rosyids_">Report Bug</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]

This repository solves the Vehicle Routing Problem using OpenStreetMap and the Google OR-Tools library. The VRP is a classic optimization problem where a fleet of vehicles is tasked with visiting several locations to minimize the total distance and time traveled. The data used includes data from Alfamart and Indomaret stores across South Jakarta, which I grouped to contain only 2 coordinates per subdistrict.

The VRP is a classic optimization problem where a number of vehicles are tasked with visiting several locations to minimize travel costs.
Analyzing the Ozone Level detection dataset using Fast Fourier Transform, performing visualization and data reduction (PCA), and creating prediction models

This dataset contains:
   1. **nama_tempat:** contains the name of the place, either Alfamart or Indomaret
   2. **rating_tempat:** the rating of the place based on Google Maps
   3. **user_ratings_total:** the total number of users who rated the place
   4. **latitude & longitude:** the coordinates of the Alfamart or Indomaret location
   5. **alamat_tempat:** the address of the place
   6. **place_ID:** the ID of each store
   7. **store:** distinguishes whether the place is an Alfamart or Indomaret
   8. **nama_kelurahan:** the name of the subdistrict where the store is located
   9. **nama_kecamatan:** the name of the district where the store is located
   10. **nama_kota** the name of the city where the store is located

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With


This project was completed using Excel and Python: with the libraries OpenStreetMap, Google OR-Tools, geopy, pandas, as well as Matplotlib and Folium for data visualization.

* [![Python][Python.org]][Python-url]
* [![Excel][Excel.com]][Excel-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Installation

_If you want to run the code for learning purposes or to change the parameters, please follow the steps below:_

1. Download Zip, or
2. Clone the repo
   ```sh
   git clone https://github.com/awcereh/route-optimization-engine.git
   ```
3. Run in your code editor (Recommended: VS Code).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

The purpose of the project Analyzing the Ozone Level detection dataset using Fast Fourier Transform, performing visualization and data reduction (PCA), and creating prediction models

### Fast Fourier Transform
[![FFT][FFT-url]
The Fourier coefficients were obtained from the FFT computation of daily wind speed measurements from 1998 to 2004.

The first Matplotlib graph shows the Fourier coefficient graph for each WSR wind speed along with the largest Fourier coefficient value.
The second graph shows the Fourier coefficient graph for the highest peak wind speed (𝑊𝑆𝑅𝑃𝐾):
(WSR PK) measured each day from 1998 to 2004, with a maximum Fourier coefficient of 
MAX 𝑋𝐾
WSRPK =10566.420707964606
MAX XK WSRPK =10566.420707964606.
The third graph shows the Fourier coefficient graph for the average wind speed (𝑊𝑆𝑅𝐴𝑉)
(WSR AV) measured each day from 1998 to 2004, with a maximum Fourier coefficient of 
MAX 𝑋𝐾 WSRAV = 5862.8862831858405
MAX XK WSRAV =5862.8862831858405.

### Principal Component Analysis
[![PCA][PCA-url]
According to the reference, the cumulative variance in PCA provides an indication of how much the features (columns) summarize variation in the data. A higher cumulative variance indicates that more data is explained by those features.

Between the two features, WSR and Temperature, the feature that better reduces the data from many dimensions is identified. For the feature DSW, data is reduced from 26 dimensions to 2 dimensions with a variance of 71.73%, while for the Temperature feature, data is reduced from 27 dimensions to 2 dimensions with a variance of 96.43%.

### Modelling Data
[![Modelling][Modelling-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] FFT
- [x] Principal Component Analysis (PCA)
- [x] modelling Data

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Muhammad Rosyid Suseno - [@rosyids_](https://instagram.com/rosyids_) - muhammadrosyid1229@gmail.com

Project Link: [https://github.com/awcereh/Ozon-Detection](https://github.com/awcereh/Ozon-Detection)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/mrosyids/
[product-screenshot]: images/screenshot.png
[Python.org]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Excel.com]: https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white
[Excel-url]: https://www.microsoft.com/id-id/microsoft-365/excel

[FFT-url]: images/fft.png
[PCA-url]: images/pca.png
[Modelling-url]: images/modelling.jpg

