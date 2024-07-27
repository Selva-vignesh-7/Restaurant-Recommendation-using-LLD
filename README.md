# Restaurnt-Recommendation-System

**Installation Guide for Required Dependencies**
This README file provides detailed instructions on how to install the necessary dependencies for the system to function properly. Please follow the steps below to ensure a successful installation.

Dependencies
The following dependencies are required for the system:

pymongo:

To install pymongo, run the following command in your terminal or command prompt:

Copy code
pip install pymongo

Homebrew:

Homebrew is a package manager for macOS that facilitates the installation of various software packages. To install Homebrew, follow the instructions provided on the official website: https://brew.sh/#install

MongoDB:

MongoDB is a NoSQL database that the system relies on. To install MongoDB on macOS, adhere to the guidelines furnished in the official MongoDB documentation: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/

Gensim:

To install Gensim, run the following command in your terminal or command prompt:

Copy code
pip install gensim
NLTK:

To install NLTK (Natural Language Toolkit), use the following command:

Copy code
pip install nltk
Downloading NLTK Data
After installing NLTK, you need to download the required data. In Python, import the library and execute the following commands:

python
Copy code
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
Make sure to run these commands in your Python environment to download the necessary NLTK data.



part 1: https://www.youtube.com/watch?v=vvCvQPOVBn0

part 2: https://www.youtube.com/watch?v=hNy0HZj0Ecc&t=435s

** there will be multiple errors popping during the installing requirements and running the model, make sure to install python version that is equal or lower than v9.12. and using online resources like stack overflow you can easily clear the exceptions .  
and the driver.py file need to be edited as per your directory path. thats all enjoy this repository .
