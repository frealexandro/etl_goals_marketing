# Etl_Marketing

_En este proyecto encontramos una cloud function en gcp utilizando el framework de FLASK que mediante el llamado de un un cloud Scheduler ejecuta un ETL que deja el resultado en un bucket de GCP _

## Comenzando 🚀

_Para obtener el proyecto en tu maquina local porfavor clone el repositorio con el nombre de **Pipeline_cloudFunction**, Recuerda que debes tener permiso de la organizacion_

### Pre-requisitos 📋

_Este proyecto se debe ejecutar directaente en una cloud function de GCP con lenguaje de **Python 3.10** o si se desea tambien se puede ejecutar directamente en tu maquina virtual con algunas modificaciones .Debes instalar las siguientes dependencias en la cloud function o en  entorno vrtual contenidas en el archivo requeriments.txt_

```
pip install -r requeriments.txt
```
_En la cloud function solo es necesario cargar el archivo, una vez esta haga el DEPLOY de esta se instalaran automaticamente las dependencias_


### Instalación 🔧


1.se debe crear una cloud function en GCP con un trigger de HTTP request alli se deben cargar todos los archivos que se encuentran dentro de el repositorio y se
deben establecer las diferentes rutas de donde se extraeran los archivos y las ruta donde se dejara el resultado de el ETL estas rutas estan establecidas el archivo de 
**params.py** alli ademas tambien se encuentran la informacion complementaria para extraer los distintos datos


```
'gs://jobs_goal_completions/{file}.csv'

```

2.debes establecer la ruta en la que va a terminar la data en GCP contenida en un bucket en cloud storage ,esta tambien puede ser modificada en el arhivo **params.py**

```
'gs://jobs_goal_completions/result_goal_completions/'

```

## Ejecutando las pruebas ⚙️


_La cloud function se encuentra en su maximo funcionamiento es un ETL diseñado para pequeñas cantidades de data, En caso de que sea mas gigante a futuros se debe iplementar una solucion mas escalable con otro servicio de google cloud pero nos referimos tal vez mas de 50 gb de procesamiento , por ahora la cloud fuction al estar diseñada con POO es relativamente muy estable y escalable_

### Analice las pruebas end-to-end 🔩


_Si todo el proceso se ejecuta correctamente, te saldran en el response de la cloud function este mensaje **the extract GOALS SSS started**y en los logs de GCP apareceran estos mensajes_

```
params is SSS ok
read and transf is SSS ok
clasify is SSS ok
clean is SSS ok
merge is SSS ok

```

### estilo de codificación ⌨️

_Este programa se modularizo en su totalidad mediante programcion orientada a objetos y tambien se intento codificar bajo el regimen del **pep 8**_



## Construido con 🛠️

* [PEP-8](https://peps.python.org/pep-0008/#id8)- Guia de Parametrizacion
* [PANDAS](https://pandas.pydata.org/) - Libreria manipulacion data
* [FLASK](https://flask.palletsprojects.com/en/2.2.x/) - Freamwork API

## Versionado 📌

Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/di-contactica/Pipeline_cloudFunction).

## Autores ✒️


* **Santiago Novoa** - *Trabajo Inicial - Documentacion * - [Frealexandro](https://github.com/frealexandro)

* También puedes mirar la lista de todos los [contribuyentes](https://github.com/orgs/di-contactica/people) quíenes han participado en este proyecto. 


## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢

