# Prática Machine Learning - CUNEF

## Antonio Bartolomé Redondo y Daniel Buendía Ureña

### Definición del problema:
Somos una aseguradora que opera en el mercado europeo y tiene pensado llevar a cabo un proceso de internacionalización a través de la adquisición de una aseguradora canadiense como filial. El consejo de administración, con el objetivo de evaluar esta operación, ha solicitado al departamento de Data Science que realice un estudio y una posterior modelización de los accidentes acaecidos en el país entre 1999 y 2014 con el objetivo de determinar su grado de mortalidad. 

Para ello, el equipo de Data Science va a utilizar los datos recogidos en la base de datos contiene los datos de colisiones de accidentes de tráfico en Canadá de 1999 a 2014, proporcionados por Transport Canada. Este conjunto de datos ofrece diversas características, como la hora del día, si hubo o no víctimas mortales, el sexo del conductor, etc. Los códigos de las diferentes categorías se detallarán a continuación en el diccionario de datos. 

### Scripts 

Los scripts utilizados para el planteamiento y resolución del problema son los siguientes:

* **00_EDA:** En él se lleva a cabo la extracción de los datos originales, así como un análisis exploratorio del mismo, de outliers y valores nulos.  


* **01_Preprocesamiento_dataset** Se le realizarán al dataset de test diferentes tranformaciones, hasta agruparlo a nivel de accidente.
 
 
* **02_Modelado:** Se realizarán multiples pruebas, tanto de estimación con diferentes algoritmos de ML como la optimización de hiperparámetros del modelo estimado con mejor performance y un análisis de explicabilidad del modelo final. 

### Enlaces a github

Antonio Bartolomé Redondo: https://github.com/abartolomeredon/MachineLearning.git

Daniel Buendía Ureña: https://github.com/danibuendia16/practicas_masterdatascience.git