# Curso de Introducción a la Programación en Python

<font size=4>
    
Curso de formación interna, CIEMAT. <br/>
Madrid, Junio de 2020

Antonio Delgado Peris
</font>

https://github.com/andelpe/curso-intro-python/


## Sobre este curso

Este es un curso preparado para impartirse como formación Interna del Centro de Investigaciones Energéticas Medioambientales y Tecnológicas (CIEMAT). Sin embargo, sus contenidos son totalmente genéricos, así que puede ser usado por cualquier interesado en el lenguaje Python.

- Nota: el curso asume que se utiliza Python 3.

Este curso está basado en _Notebooks Jupyter_ (_Jupyterlab_), así que puede seguirse a través de un navegador, en una instalación local (previa descarga), o en una plataforma en la nube. Se dan más detalles [abajo](#seguir_curso).

Para lanzar este curso en la plataforma en la nube _Binder_: 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/andelpe/curso-intro-python/master?urlpath=lab)


### Objetivos generales del curso

Proporcionar los fundamentos de la programación en Python, lenguaje de alto nivel, moderno, potente, y versátil, muy usado tanto en entornos académicos como científicos, por su sintaxis clara, su capacidad de integración con otros lenguajes, y el gran número de librerías de las que dispone. 

El curso cubrirá los elementos básicos para la creación de un programa en Python, incluyendo las estructuras y operadores fundamentales, los tipos de datos, las funciones, la orientación a objetos, y los módulos. 

### Contenidos 
Los temas en los que está estructurado el curso son los siguientes:

1.	Introducción y Generalidades
2.	Sentencias, objetos, tipos y variables
3.	Iterables y bucles (I): Secuencias
4.	Iterables y bucles (II): Diccionarios
5.	Entrada y Salida
6.	Funciones y módulos
7.	Clases y objetos
8.	Otros recursos _(avanzados)_
9.	El ecosistema Python: librería estándar y otros paquetes populares

### Ejercicios

Aunque el curso incluye numeroso código ejecutable (y editable), a modo de ejemplos, también se proponen ejercicios, para los cuales no se incluyen aquí las soluciones. 

El motivo para esto, es que considero que enfrentarse a un desarrollo (aunque sea corto) desde cero es la mejor manera de aprender.

Lógicamente, los participantes en el curso del CIEMAT tendrán acceso a mis soluciones... después de haber probado las suyas propias.


## <a name="seguir_curso"></a>Como seguir este curso

Este curso está basado en _notebooks Jupyter_, que integran comentarios con código ejecutable. 
Este formato cobra sentido cuando se ejecutan los _notebooks_ en una plataforma Jupyter (accedida, siempre, usando un
navegador web).

La plataforma Jupyter usada puede ser una instalación local, o bien un servicio de la nube.

Aunque en el _notebook_ del Tema 1 comentamos algunos detalles, existe información extensa sobre 
el uso de Jupyterlab aquí: https://jupyterlab.readthedocs.io/


### Instalación en el equipo local

Si es posible, una instalación de Jupyterlab local es seguramente más cómoda: 
no se depende de la red, y los cambios permanecen en el equipo propio.

- Requisitos previos: además de Python 3, para unos pocos ejemplos/ejercicios se requiere instalar `matplotlib` y `pytest`.

- En primer lugar, debemos descargar el repositorio completo del curso de GitHub, y descomprimirlo en el directorio que nos interese.

- También necesitamos instalar Jupyterlab. Existen varias opciones, que se pueden consultar aquí: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html

- Una vez instalado, Jupyter puede lanzarse con, por ejemplo: `jupyter lab`.

  - **NOTA:** es muy recomendable lanzar jupyter desde el directorio raíz del curso, para que ese sea el directorio de trabajo inicial, y todas las rutas sean correctas.


- El comando anterior debería abrir un interfaz Jupyterlab en nuestro navegador (podemos elegir cuál con la opción `--browser`). Si no se ha abierto, podremos acceder al interfaz Jupyterlab usando la dirección correcta en el navegador. _Por defecto_, es: http://localhost:8888/lab

Existen muchos más detalles en: https://jupyterlab.readthedocs.io/


### Usar un servicio en la nube.
Al principio de este mismo _README_ se incluye un link para lanzar este repositorio en la plataforma _Binder_, y 
esta es la opción _online_ recomendada. Sin embargo, algunas otras soluciones son posibles.

- **Binder**

  - Pinchar en el icono _Binder_ al principio de este documento, para lanzar el repositorio en Binder (no requiere crear una cuenta de usuario).
  
  - El interfaz que ofrece Binder es idéntico al de una instalación Jupyterlab local, y todos los archivos del repositorio, así como Matplotlib y pytest, estarán disponibles.
  
  - Los ficheros modificados se guardan automáticamente cada cierto tiempo en el espacio Binder, pero si queréis conservar vuestro trabajo después de cerrada la sesión, debéis descargarlos a vuestro ordenador:
      - Guardar como notebook (`.ipynb` file): _File > Download_
      - O bien como script (`.py`): _File > Export Notebook as > Executable Script_
      - NOTA: Podéis seleccionar varios notebooks y descargarlos todos a la vez.
      
      
  - NOTA: Una sesión inactiva durante varios minutos será **automáticamente cerrada**.
  
- **Google Colab**:

  - Requiere utilizar una cuenta de Google. Presenta un interfaz propio, inspirado en de Jupyterlab, pero diferente a él.
  
  - El método seguramente más fácil es descargar el repositorio completo de GitHub y subirlo al Google Drive del usuario. A partir de ahí, todas los cambios quedarán almacenadas en nuestro Drive.
  
  - Si nunca se ha Colab con Drive, hay que conectarlos. 
  
    - Para ello hay que ir a la carpeta donde hemos guardado el repositorio, y hacer click con el botón derecho del ratón _en el fondo_ (no en un archivo), y elegir _More_, en el menú que aparece, y luego _Colaboratory_.
  
  - Una vez conectados, hacer click en un notebook, lo abrirá.
  
  - Adicionalmente, para muchos ejemplos y ejercicios se requieren archivos auxiliares, contenidos en el repositorio.
  
    - Para que funcionen, una vez abierto el notebook, se debe montar Drive.
    - Primero, hay que pinchar un icono de una carpeta, a la izquierda del todo.
    - Después pinchar en _Mount Drive_, en el menú que aparece.
    - Entonces, seguir las instrucciones y aceptar la petición de autorización.
    - Finalmente, hay que cambiar el directorio de trabajo al del repositorio en Drive.
      - Para ello, refrescar el árbol de carpetas (izquierda), buscar el directorio del repositorio (bajo _drive_), pinchar con el botón derecho y elegir _Copy path_. 
      - Ir a una celda y ejecutar: `%cd "<path-copiado>"` Nota: Las comillas son importantes!
  
Existen más opciones: _CoCalc_, o _Azure notebooks_.



