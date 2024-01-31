<<<<<<< HEAD
# Autotest-Selenium

<p align="center">
  <img src=".images/bees_for_git.png" alt="Telegram Admin Bot Logo">
</p>

## About
This project is a set of automated tests to verify the functionality of web elements on Tensor and VLSI pages. The tests are implemented in Python using the requests library to download the VLSI installer to the project folder and the pytest framework to organize and run autotests. The Selenium library is used to interact with the elements on the pages.
## Install and Run
**1. Create and activate a virtual environment:**
   
    python3 -m venv env  # Linux  macOS
    python -m venv venv  # Windows


    source env/bin/activate  # Linux  macOS
    source venv/Scripts/activate  # Windows
   
**2. Install dependencies from a file requirements.txt:**

    python3 -m pip install --upgrade pip 
    pip install -r requirements.txt

**3. To run all autotests, run the following command:**
   
    pytest
   

## Test Description
**The sites that autotests interact with are located at the following URLs:**
- VLSI: https://sbis.ru 
- Tensor: https://tensor.ru 

**Within the framework of the project, 3 scenarios are being tested, each scenario and its steps are described below:**

_**The first scenario:**_

- Go to https://sbis.ru to the "Contacts" section
- Find the Tensor banner and click on it
- Go to https://tensor.ru/
- Check that there is a block "Strength in people
- Go to the "Details" section in this section and make sure that it opens https://tensor.ru/about 
- Find the Work section and check that all photos of the chronology have the same height and width

_**The second scenario:**_

- Go to https://sbis.ru / to the "Contacts" section 
- Check that your region has been determined (in our example, the Yaroslavl region) and there is a list of partners
- Change the region to Kamchatka Territory
- Check that the selected region has been substituted, the list of partners has changed, the url and title contain information about the selected region

_**The third scenario:**_

- Go to https://sbis.ru/ 
- In Footer, find and go to "Download VLSI"
- Download VLSI Plugin for your windows web installer to the folder with this test
- Make sure that the plugin has been downloaded 
- Compare the size of the downloaded file in megabytes. It must match the one specified on the site (in the example 3.64 MB).

---
This test works great and performs all its functions.
=======
"# Autotest-Selenium" 
>>>>>>> origin/main
