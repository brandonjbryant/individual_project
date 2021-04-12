# _What Makes Red Wine "Good"?_

![](https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)




- This project uses a various classification models to predict drivers in red wine quality rankiings.
- In this README I will :
    * Explain what the project is and goals I attempted to reach. 
    * Explain how to reproduce my work. 
    * Contain notes from project planning.

## Goals
- This project aims to classify the quality of red wine using various parameters or features. This will be a approached as classification problem and will try to use various classification models to find the best accuracy score.

## Project Planning
- Trello Board Link:
  - https://trello.com/b/NJcVVZvd/individual-project-board

**Deliverables:**
1. README.md file containing overall project information, how to reproduce work, and notes from project planning.
2. Jupyter Notebook Report detailing the pipeline process.
3. Python modules that automate the data acquistion, preparation, and exploration process.

## Key Findings 
* Alcohol was the most significant feature in regards to higher quality red wine rankings.
*  The higher the percentage of sulphates, the higher the quality of wine. 
* The higher the levels of volitile acidity, sulfur dioxide, and chlorides, the lower the quality of the wine.
* Random Forest was my best performing classification model overall.

## Conclusion
- For this individual project, I aimed to analyze which psychochemical are more related with higher quality wine.
- Although I ran out of time and was unable to see how my model performs on unseen data, I am confident that the Random Forest model would be sufficient in correctly in predicting on test data.

- I was able to utilize new methods in order to explore my data as well as model it. If I had more time, I would evaluate my best models performance on unseen data, as well as enhance my exploratory phase. This project would also benefit from access to more features in the data such as  other wine types ,grapes, prices, etc, that I did not have access to in this particular data set.

## Reccomendations based on my findings 
- Alcohol is the most important feature to decide quality of the wine. It appears that that the higher the alcohol percentage, the higher the quality of wine. 

- Sulphates were also a good citeria in searching for good wine. The higher the percentage of sulphates, the higher the quality of wine. 

- I would reccomend choosing wines with lower volitile acidity, sulfur dioxide, and chlorides as the higher those levels were, the more likely the quality of the wine will decrease.

- With more time I hope to expand on my exploration and be able to offer more reccomendations based on those findings. I thank you for taking the time to analyze my research.



## Setup this project
* Dependencies
    1. python
    2. pandas
    3. scipy
    4. sklearn
    5. numpy
    6. matplotlib.pyplot
    7. seaborn
* Steps to recreate
    1. Clone this repository
    3. Open `individual_project_final_draft.ipynb` and run the cells


## Data Dictionary 

#### Target
Name | Description | Type
:---: | :---: | :---:
quality | Wine quality ranking(score between 0 and 10) | int

#### Features
Name | Description | Type
:---: | :---: | :---:
fixed acidity  |  Most acids involved with wine or fixed or nonvolatile | float
volatile acidity  |  The amount of acetic acid in wine | float
residual sugar | The amount of sugar remaining after fermentation stops| float
chlorides | The amount of salt in the wine | float
free sulfur dioxide | The free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion | float
density | The density of water is close to that of water depending on the percent alcohol and sugar content  | float
pH | Describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic) | float
sulphates | A wine additive which can contribute to sulfur dioxide gas (S02) levels | float
alcohol | The percent alcohol content of the wine| float
