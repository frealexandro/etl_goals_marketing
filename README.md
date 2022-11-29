# Etl_Marketing

_In this project we find a cloud function in gcp using the FLASK framework that by calling a cloud Scheduler executes an ETL that leaves the result in a GCP bucket _

## Starting 🚀

_To get the project on your local machine please clone the repository with the name of **Pipeline_cloudFunction**, remember that you must have permission from the organization_

### Pre requirements 📋

_This project must be run directly in a GCP cloud function with **Python 3.10** language or if desired it can also be run directly in your virtual machine with some modifications. You must install the following dependencies in the cloud function or environment vrtual contained in the file requirements.txt_

```
pip install -r requeriments.txt
```
_In the cloud function it is only necessary to load the file, once it is done DEPLOY it, the dependencies will be installed automatically_


###installation 🔧


1.a cloud function must be created in GCP with a trigger of HTTP request there all the files found within the repository must be uploaded and
They must establish the different paths from which the files will be extracted and the paths where the result of the ETL will be left. These paths are established in the output file.
**params.py** there are also complementary information to extract the different data


```
'gs://jobs_goal_completions/{file}.csv'

```

2.You must establish the route in which the data will end up in GCP contained in a bucket in cloud storage, this can also be modified in the file **params.py**

```
'gs://jobs_goal_completions/result_goal_completions/'

```

## running the tests ⚙️


_The cloud function is at its maximum performance, it is an ETL designed for small amounts of data. In the event that it is more gigantic in the future, a more scalable solution must be implemented with another google cloud service, but we are referring to perhaps more than 50 gb of processing, for now the cloud function, being designed with OOP, is relatively very stable and scalable_

###Analyze end-to-end tests🔩


_If the whole process is executed correctly, the cloud function response will show this message **the extract GOALS SSS started** and these messages will appear in the GCP logs_

```
params is SSS ok
read and transf is SSS ok
clasify is SSS ok
clean is SSS ok
merge is SSS ok

```

### coding style ⌨️

_This program was completely modularized through object-oriented programming and also attempted to be codified under the **pep 8** regime._



## Construido con 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [FLASK](https://flask.palletsprojects.com/en/2.2.x/) - Freamwork API

## Versionado 📌

For all available versions, see the [tags en este repositorio](https://github.com/frealexandro/Etl_goals_marketing).

## Autores ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)




## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢

