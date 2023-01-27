# Etl_Marketing

In this project, we use a GCP cloud function built with the FLASK framework to execute an ETL process. The cloud function is triggered by a cloud Scheduler and the result is saved in a GCP bucket.

## Starting 🚀

To get the project on your local machine, please clone the repository named **Pipeline_cloudFunction**. Note that you must have permission from the organization.

### Prerequisites 📋

This project must be run directly on a GCP cloud function with **Python 3.10** or, with some modifications, it can also be run on a virtual machine. The following dependencies must be installed in the cloud function or virtual environment, as listed in the `requirements.txt` file:


```
pip install -r requeriments.txt
```
In the cloud function, simply upload the file and DEPLOY, the dependencies will be installed automatically.

## Overview
This code is used to classify and merge data from a website's goals, read from a file and fix any problems with the data. The output is saved in a CSV file.

## Dependencies
This code depends on the following modules:

- Params
- Read_trans
- Merge_data
- Clasify_df

## Function: run()
The `run()` function is the main function of the code. It contains the following steps:

1. The function calls the `params()` function from the `Params` module to read the parameters needed for the code.
2. The function uses the `read_trans()` function from the `Read_trans` module to read the file containing the website's goals, and the `read_transf()` function to transform the goals.
3. The function uses the `read_clasify()` function from the `Clasify_df` module to classify the data in the file into different lists: `filecls_2_m1`, `filecls_2_m2`, and `list_goalname`.
4. The function uses the `clean()` function from the `Clasify_df` module to clean the lists obtained in the previous step.
5. The function uses the `merge()` function from the `Merge_data` module to merge the data in the lists and the file obtained in step 2.
6. The function saves the resulting dataframe to a CSV file in the specified location.

### Note
The commented out lines of code in the `run()` function are related to the `Fix_Goals` class from the `Fix_Goals` module, which is used to extract and fix any problems with the goals data. This functionality is not currently being used in the code, but it's kept in the script for future reference or development.

## Usage
To use this code, simply run the `run()` function in the script.

## Running the Tests ⚙️

The cloud function is designed to handle small amounts of data. If the data volume increases in the future, a more scalable solution must be implemented using another Google Cloud service. However, this is only necessary for processing more than 50 GB of data. For now, the cloud function, being designed with OOP, is relatively very stable and scalable.

### Analyze end-to-end tests🔩

If the whole process is executed correctly, the cloud function response will show the message **the extract GOALS SSS started** and the following



## Built With  🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [FLASK](https://flask.palletsprojects.com/en/2.2.x/) - Freamwork API

## Versioning 📌

For all available versions, see the [tags en este repositorio](https://github.com/frealexandro/Etl_goals_marketing).

## Autors ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)





