# Prática Machine Learning - CUNEF
## Productivización del modelo de análisis de siniestralidad

Antonio Bartolomé Redondo y Daniel Buendía Ureña

### Enlaces a github

Antonio Bartolomé Redondo: https://github.com/abartolomeredon/MachineLearning.git

Daniel Buendía Ureña: https://github.com/danibuendia16/practicas_masterdatascience.git

### Estructura de la API
La API se estructura en varios archivos:
- dockerfile: en él se define la imagen del contenedor Docker y se especifican los comandos que nos permiten crear el entorno de ejecución de la aplicación.
- requirements: se establecen las librerías necesarias para el funcionamiento de la app, así como las versiones de cada una de ellas que se utilizan.
- app: desarrolla y define el funcionamiento de la aplicación, desde la validación de las llamadas a la API hasta las estructuras de predicción, así como el output final. 
- model: contiene el modelo generado en la práctica de análisis de siniestralidad
- request: se han almacenado, parte de las consultas realizadas, para poder ser replicadas

### DETALLE DOCKER
La imagen, basada en continuumio/anaconda3, se puede descargar a través del siguiente comando: docker pull abarrad/api_traffic_collision


### USUARIOS
Debido a que el planteamiento previo a realizar el modelo condujo a agrupar el dataset de referencia a nivel de accidente, la API se ha construido considerando esto, por lo que no todas las variables coinciden completamente con las del dataset original.
Por ello, se detalla a continuación, una breve explicación sobre las variables contempladas en la API y su naturaleza:
 
C_MNTH: mes en el que se produjo el accidente. Variable categórica.
C_WDAY: día de la semana en el que se produjo el accidente. Variable categórica.
C_HOUR: franja horaria en la que se produjo el accidente. Variable categórica.
C_VEHS: Número de vehículos involucrados en el accidente. Variable numérica
C_CONF: configuración detallada del accidente.
C_RCFG: detalle lugar del accidente. Variable categórica. 
C_WTHR: detalle climatología en el momento del accidente. Variable categórica.
C_RSUR: detalle situación de la carretera en el momento del accidente. Variable categórica.
C_RALN: detalle de la configuración de la carretera donde se produjo el accidente. Variable categórica.
C_TRAF: detalle señales de tráfico cercanas al lugar donde se produjo el accidente. Variable categórica.
V_TYPE_1: número de vehículos estándar implicados en el accidente. Variable numérica.
V_TYPE_5: número de furgonetas implicadas en el accidente. Variable numérica.
V_TYPE_6: número de otros camiones y furgonetas implicados en el accidente. Variable numérica.
V_TYPE_7: número de camiones pesados implicados en el accidente. Variable numérica.
V_TYPE_8: número de tractores de carretera implicados en el accidente. Variable numérica.
V_TYPE_9: número de autobuses escolares estándar implicados en el accidente. Variable numérica.
V_TYPE_10: número de autobuses escolares pequeños implicados en el accidente. Variable numérica.
V_TYPE_11: número de autobuses de línea implicados en el accidente. Variable numérica.
V_TYPE_14: número de motocicletas implicados en el accidente. Variable numérica.
V_TYPE_16: número de todoterrenos implicados en el accidente. Variable numérica.
V_TYPE_17: número de bicicletas implicados en el accidente. Variable numérica.
V_TYPE_18: número de autocaravanas implicados en el accidente. Variable numérica.
V_TYPE_19: número de vehículos de granja implicados en el accidente. Variable numérica.
V_TYPE_20: número de vehículos de construcción implicados en el accidente. Variable numérica.
V_TYPE_21: número de camiones de bomberos implicados en el accidente. Variable numérica.
V_TYPE_22: número de quitanieves implicados en el accidente. Variable numérica.
V_TYPE_23: número de coches aparcados implicados en el accidente. Variable numérica.
V_TYPE_24: número de vehículos perteneciente a otra categoría implicados en el accidente. Variable numérica.
P_SEX_F: Número de mujeres implicadas en el accidente. Variable numérica.
P_SEX_M: Número de hombres implicadas en el accidente. Variable numérica.
P_SAFE: Porcentaje de personas implicadas en el accidente que utilizaban al menos un dispositivo de seguridad. Variable numérica(porcentaje).
P_AGE: Edad media de las personas involucradas en el accidente. Variable numérica.
A_VAGE: Antigüedad media de los vehículos involucrados en el accidente. Variable numérica.

#### DICCIONARIO DE DATOS

![Diccionario de datos parte 1]('diccionario-de-datos/data-dict_part_1.PNG')
![Diccionario de datos parte 1]('diccionario-de-datos/data-dict_part_2.PNG')
![Diccionario de datos parte 1]('diccionario-de-datos/data-dict_part_3.PNG')
![Diccionario de datos parte 1]('diccionario-de-datos/data-dict_part_4.PNG')
![Diccionario de datos parte 1]('diccionario-de-datos/data-dict_part_5.PNG')
 