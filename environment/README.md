# Métodos Computacionales 2S2023

## Setup

En la materia vamos a estar programando en Python, para lo que vamos a necesitar instalar algunas herramientas y paquetes. Una opción conveniente es instalar [Anaconda](https://www.anaconda.com/download) (especialmente su versión minimal [Miniconda](https://docs.conda.io/en/latest/miniconda.html)), un administrador de paquetes que incluye Python y todas las librerías necesarias en un sólo instalador. Otra opción es simplemente instalar Python 3 de la página oficial [acá](https://www.python.org/downloads/) y manejarse con [pip](https://pypi.org/project/pip/). Una tercera opción es trabajar en [Google Collab](https://colab.research.google.com/), en cuyo caso no hace falta configurar nada.

### Instrucciones para Anaconda

Habiendo instalado Anaconda o Miniconda, el próximo paso es clonar este repositorio o descargarse el archivo `environment.yml` que incluye una lista de todos los paquetes a instalar. Corriendo el siguiente comando desde la Conda prompt/terminal,

```
conda env create -f environment.yml
```

se crea el entorno de desarrollo y se instalan todos los paquetes necesarios. Despues, es necesario activarlo mediante

```
conda activate metodos
```

y registrar el entorno para poder ser utilizado en Jupyter

```
python -m ipykernel install --user --name metodos
```

Por último, ejecutando Jupyter Lab (o Jupyter Notebook) ya está todo disponible para trabajar

```
jupyter lab
```

### Instrucciones para Pip

Habiendo instalado Python 3, podemos usar `pip` y `venv` para configurar el mismo entorno. Primero creamos el entorno mediante el siguiente comando (lo crea en el working directory)

```bash
python -m venv metodos
```

Después es necesario activarlo para instalarle los paquetes necesarios. El comando para activar el entorno en OSX/Ubuntu es

```bash
source metodos/bin/activate
```

Si están en Windows, ver [acá](https://docs.python.org/3/library/venv.html#creating-virtual-environments).

Ahora, para instalar los paquetes a utilizar, descargar el archivo `requirements.txt` de este repositorio y correr

```bash
python -m pip install -r requirements.txt
```

y para registrar el entorno para poder ser utilizado en Jupyter

```bash
python -m ipykernel install --user --name metodos
```

Por último, ejecutando Jupyter Lab (o Jupyter Notebook) ya está todo disponible para trabajar

```bash
jupyter lab
```
