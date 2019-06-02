Instituto Tecnológico de Costa Rica  <br /> 
Área Académica de Ingeniería en Computadores <br /> 
Arquitectura de Computadores 1 <br /> 

# Simulación y análisis de un procesador ARM

Mediante el desarrollo de este proyecto, el estudiante aplicará los conceptos de arquitectura de computadores en la exploración de espacio de diseño.

El programa debe ser capaz de usar compilar y correr 5 pruebas de los benchmarks SPEC o PARSEC sobre el modelo
GEM5 TimingSimpleCPU (figura 3) por al menos 2 OOO OOO de instrucciones.

Basado en un fundamento teórico debe variar los siguientes parámetros del sistema:
* Tamaño de caché
* Ancho línea de caché
* Asociatividad
* Tipo de branch predictor

# Instrucciones de uso

Una vez descargado y antes de compilar gem5 (http://www.gem5.org/Introduction), ingrese al directorio gem5, copie el directorio src a su directorio de descarga de gem5 permitiendole sobreescribir los archivos que ahí se encuentran. Entonces comile gem5 commo indica la documentación oficial.

Cuando haya realizado la compilación puede copiar el resto de archivos dentro del directorio gem5 permitiendo reemplazar los que sea necesario.

# Benchmarks

Para ejecutar los benchmarks se debe acceder en la carpeta de gem5:
```
cd gem5
```

Luego ejecutar el archivo de benchmarks automátizados
```
python benchmarks.py
```
# Visualizar resultados
Para crear graficas de los resultados se debe acceder en la carpeta de python:
```
cd python
```
Se debe instalar Matplotlib
```
sudo apt-get install python3-matplotlib
```

Finalmente ejecutar el archivo de graficacion
```
python3 plot.py
```