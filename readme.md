# 1. Executive Summary
“What is not measured cannot be improved” once said by Lord Kelvin. Describes the fundamental believe of this project. Families throw away health fruits and vegetables daily. [Missouri Dept. of Natural Resources](https://dnr.mo.gov/waste-recycling/reduce-reuse-recycle/what-to-do-with-specific/food) estimates that 30-40% of all food goes uneaten within the United States. On top of that food prices since 2019 have increased more than 25% per [US Dept. of Agriculture](https://www.ers.usda.gov/data-products/ag-and-food-statistics-charting-the-essentials/food-prices-and-spending/?topicId=1afac93a-444e-4e05-99f3-53217721a8be). This increasing in cost and high waste creates an opportunity for a database software to track food bought within the household. This project helps to enable others to track fruits and vegetables. 

# The problem being fixed.
This program will provide an interface to track food entering into a household. Their will be an added element of artificial intelligence to understand how to integrate it into a data pipeline. 

## High-level Benefits and objectives
Allow for photos of fruits and vegetables to be processed by a AI framework. This framework will make a predicted guess and ask for user feedback to be used for further training. As time progress and more data is collected the program will reduce the toil of entering the food items and allow for a easier to use tracking system.  

### Functional Requirements
* Cross Platform 
* Easy To Use
* Able To Correct Entries
* Able to enter pictures into the program

### Non-Functional Requirements
* Whole AI Pipeline must run within One Minute.
* Must be able to run on a light weight compute device (Raspberry Pi 4 will be the benchmark.)

## Intended audience and key stakeholders
### Stakeholders
| Name           | Role    |
| --------       | ------- |
| Bobby Houston  | Lead    |
| Deepti Manglik | Reviewer|
# 2. Introduction

## 2.1 Background information on the problem or need.
In recent years AI tools have been created within the programming space to act as a black box for image classification as such this project will treat the training of the model as a black box and use example code from the [tensorflow](https://www.tensorflow.org/tutorials/images/classification) website.

Along side that databases have been critical into IT for many years. Some notable databases include database 2 (DB2), Oracle, SQL, and PostgreSQL. As such this project will also focus on the deployment and creation of one of these databases. The 1st attempt focused on MySQL however, setting up the database would require a external API between that and the program. Due to later on requirements this was dropped in favor of sqlite3. This allowed for different programming designs to take place.

Programming designs explored with microservices and tightly coupled codes. Tightly coupling makes the other parts of the code heavily depend on other code functions but allows for faster processing normally. Where microservices allows for faster deployment and is common in cloud platforms at the cost of more resources consumed. 

PaaS was lastly explored with a part of the application being ran in a container service. Containers goal is to stop the well it works on my machine problem. This is preformed by running the code inside the OS instead of creating a new virtual machine. This deployment method has become largely popular in cloud computing with the start up time of new services often less than a minute. 

## 2.2 Project Objectives for the creator.
High level understanding when to use containers, different coding patterns, when to use a database, and how to deploy an AI pipeline. 

## 2.3 Architectural Decisions

#### Architectural Decision 1
**Programming Language**

**Description**:
Python, C++, and Java are the top languages in this space.\ 
**Pro/Cons**:
| Issue                                   | Winner          |
| --------                                | -------         |
| Cross Platform                          | Python & Java   |
| Popularity                              | Python          |
| Security                                | Java            |
| Speed                                   | c++             |

**Conclusion**:\
Python

#### Architectural Decision 2
**Container Software**

**Description**:
Docker and Podman where the two different container based platforms looked at.\
**Pro/Cons**:
| Issue                                   | Winner    |
| --------                                | -------   |
| Runs on Raspberry Pi, Mac OS and Windows| Docker    |
| Popularity                              | Docker    |
| Security                                | Podman    |

**Conclusion**:\
Docker
#### Architectural Decision 3
**AI Framework**

**Description**:
PyTorch and Tensorflow were the two major frameworks looked into.\
**Pro/Cons**:
| Issue                                   | Winner         |
| --------                                | -------        |
| Data Visualization                      | Tensorflow     |
| Ease of Use                             | PyTorch        |
| Written in Python                       | Tensorflow     |

**Conclusion**:\
Tensorflow

#### Architectural Decision 4
**Database Used**

**Description**:
MySQL or python's native support for sqlite3 module.\
**Pro/Cons**:
| Issue                                   | Winner         |
| --------                                | -------        |
| Ease of Use                             | sqlite3        |
| Industry Standard                       | MySQL          |
| Mobile                                  | sqlite3        |

**Conclusion**:\
sqlite3

#### Architectural Decision 5
**Interface**

**Description**:
Tkinter can create a GUI. While Flask allows for API web development.\
**Pro/Cons**:
| Issue                                   | Winner         |
| --------                                | -------        |
| User Ease of Use.                       | Flask          |
| Industry Standard                       | Flask          |
| Development time                        | Tkinter          |

**Conclusion**:\
tkinter

# 3. Objectives and Goals

## Specific objectives the solution aims to achieve.
* Provide a easy user interface.
* Make best effort to guess fruit.
* Provide best effort to give a date to use by.

## Success criteria and measurable goals.
* User can enter a new fruit or vegetable with in 30-45 seconds.
* AI component makes a guess and tracks accuracy.
* Database provides use by date allowing for users to track when to use fruit by.

# 4. Solution Overview

## Dataflow of user interface.
![Diagram 1](highlevel_goal.png "User Flow")

## Key components and architecture.
![Diagram 2](scrit_flow.png "Script Flow")

## How the solution addresses the problem.
This solution creates a tracking method to help users find food that needs to be consumed that week.

# 5. Technical Requirements

## Hardware Tested On:
* M1 Macbook Air
* Windows 11 AMD CPU & GPU
* Windows 11 Intel CPU & Nvidia GPU
* Raspberry PI 4

## Software Needed
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/)

## Python Modules used
* [tensorflow](https://www.tensorflow.org)
* [matplotlib](https://matplotlib.org/)
* [numpy](https://numpy.org/)
* [pillow](https://python-pillow.org/)
* [pandas](https://pandas.pydata.org/)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

# 6. Deployment Plan

## Tools to Install
1. [Install Visual Studio Code](https://code.visualstudio.com/download)
2. [Install GitHub](https://desktop.github.com/download/)
3. [Install Python](https://www.python.org/downloads/)
4. [Install Docker](https://docs.docker.com/engine/install/)

## Visual Studio Code Extensions
1. Code Spell Checker
2. Dev Containers
3. Docker
4. Github Copilot
6. IntelliCode
7. Jupyter
8. Prettier
9. Python
10. WSL

## How to quickly install python modules
1. Open code directory in VScode
2. On Windows/Linux press control+shift+p on mac press command+shift+p
3. Click on venv environment, this will create a virtual python environment
4. Click on requirements.txt, this will use that file to gather all the modules outline in technical requirements.
5. Find the file called main.py and click run

## How to use the program 
1. Upload allows you to load a jpg picture into the AI model
2. If it guesses the correct fruit/vegetable once the user clicks yes it will change the correct fruit
3. Then you can call the storage method.
4. Then submit will load it into the database.
5. On close it will ask the user to save the database to csv and open excel. 

## Docker Deploy
1. The code comes with a docker file. 
2. Once the user right clicks on the docker file with the correct extensions they can deploy the docker container.
3. It will then fetch the image in test and guess what the file is. 

# 7. Sources Used

## Data Used
https://www.kaggle.com/datasets/kritikseth/fruit-and-vegetable-image-recognition/data



