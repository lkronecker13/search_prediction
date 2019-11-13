# Search analysis and prediction project

This project was developed as a test for Coveo.

## Project structure

### Notebooks

In the root folder of the project you will find two notebooks prepended with a number:

```
1. EDA
2. Modeling
```

This files are to be opened in order so that the flow in which the project was developed can be followed. 
The answer to the first question is at the end of the first notebook, the remaining three answers are in notebook 2. You will find links to access these answers quickly at the top of each notebook.

### Data

The folder data contains the following paths:

```
original: Contains the original data as was received. The contents of this folder should never be modified so we always have a backup.
flattened: Contains the data that resulted from the preprocessing.
enhanced: Contains enhanced data that resulted from feature engineering in the EDA step.
```

### Results

In the paths models/ and model_weigths/ we find the details of the models trained in the notebooks. In order to understand them better one should open the second notebook.

### Tools

The file tools.py contains some functions that are shared among the notebooks. I moved them here to free some space in the notebooks.

## Project setup

In order to successfully run the project make sure that Anaconda (https://www.anaconda.com/downloads) is installed in your system since it is used as an 
environment/package manager. 

Once conda is installed in your system navigate to the project's root in your terminal (where the file searches-env.yml) and run the
following command:

```conda env create -f searches-env.yml```

This will create an environment that will be used to run the project. Once all the packages are installed run the command:

```jupyter notebook```

Once the web interface opens you will have access to the following notebooks:

```
1. EDA
2. Modeling
```

Open them in order so you can start looking at the project. Feel free to follow along by just reading or executing the code
in the notebook. Some of the code blocks will take a while to finish executing since the data files are kinda big.


With all this said I think you should be able to successfully run the project!



