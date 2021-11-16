# Description
This repo is for solving the Programming Challenge.
The challenge has two parts:

1) Generating a file of size 2MB, containing random four type of random objects,i.e.alphabetical strings, real numbers, integers, alphanumerics.

2) A function for showing the number of each random objects. 


# Flask Services
As a backend developer, I have created two flask services for solving this challenge.


## 1. Service for generating and donwloading a text file.
This service generates a text file containing 4 types of random objects and then it downloads this file.
URL for service is given below:

	http://127.0.0.1:5000/generate_file
	

 
## 2. Map Scraping Service.
This service calculates the count of each random object in file generated using service 1. It returns a JSON object, showing count of each object in file. This json object canbe later used in the application.  
URL of service is given below:
 
 http://127.0.0.1:5000/file_stats



