# Data Collection Pipeline

This project aims to scrape data from CEX website. The scraped data is stored as a json file and the image data is downloaded locally. The project is encased in a docker container to make it more portal. With actions being created so that a docker image can be created from the requirments.

## Milestone 1:

- Create github repository 

## Milestone 2:

- Select website to scrape

- CEX was chosen as it contained data that could be analysed to perform business analysis and was of interest to the programmer

## Milestone 3:

- Prototpye finding the individual page for each entry

- Use selenium and BeautifulSoup to scrape CEX website. Though ultimatley only selenium was used for scraping. With methods being created to bypass cookies and perform scraping tasks

## Milestone 4:

- Retrive data from details page

- Stored the retrieved data in a dictonary which was later exported out in a json file. With the image data being downloaded locally in the same directory as the code itself. The image was given a unique id generated using the current ID and the image index in the dictionary

## Milestone 5:

- Unit tests were written so that the url could be checked to ensure that it has not changed and also the number of items gathered from the website were as expected

## Milestone 6:

- Refractored the code, setup headless mode, created a docker image and a docker container

- Used pylint, PEP8 style guide, Google python style guide to clean up the code and write docstrings. Ensured that the program was running in headless mode using '--headless'. Finally using docker to create an image with the requirments and creating a container. Pushing the image to docker hub for future reference

## Milestone 7:

- Setup a CI/CD pipeline for Docker image

- Setup CI/CD using github action and secrets. With the action creating a docker class and pushing it to Docker hub when pulling or pushing to repo