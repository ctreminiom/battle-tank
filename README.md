Proyecto #1 - Servicios Web
===================


Este repositorio contiene un servicios web cuyo objetivo es orquestar las partidas del juego conocido como Battle Tanks.  **Battle Tanks**  esta subdividido en el modelo de desarrollo de software por capas. Esto significa que este repositorio es la mitad del proyecto #1. 

----------

Requerimientos
-------------

Este desarrollo esta implementado con el modelo MVW. Se utiliza el microframework de python llamado  **Flask**. Sin embargo, se utiliza una extension de Flask llamado Flask-RESTful. Se utiliza MongoDB como gestor de bases de datos y se extiende gracias a un ORM

> **Paquetes utilizados:**

> - **Flask --- Flask-Restful** ---> API
> - **Pymongo --- Mongoengine** ----> ORM para MongoDB que facilita la creacion de Modelos y Queries.
> - Python 3.5

#### <i class="icon-file"></i> Funcionamiento

Este API se comunica con el front-end para crear la partida de juego, los jugadores y los movimientos. Primeramente el front-end le envia un  **POST** al server indicandole que se va a crear una partida de juego, posteriormente se crean los dos juegadores, cada jugador tiene un **UUID** unico que lo identifica. Cuando el primer jugador es creado, este jugador envia un **POST** al server para que le indique sobre el primer movimiento (el movimiento de los jugadores de realizan utilizando las coordenadas **X** y **Y**), el server guarda el movimiento actual del jugador, valida el movimiento en el mismo turno del segundo jugador. Dependiendo de las coordenadas suministradas por el server, se procesa y se envia la nueva coordenada al jugador #1. Este mismo procedimiento se realiza con el segundo jugador al mismo tiempo.

Cuando un jugador colisiona con una bala, el cliente realiza un **PUT** al server indicandole que el jugador con dicho **ID** perdio puntos de vida. En el server se valida si la vida del jugador colisionado es igual a 0. Si la vida es 0, se termina la sesion de juego que se actualiza el campo **Winner** de la sesion.  


![enter image description here](https://lh3.googleusercontent.com/-aeDQSFCFr6o/WhJhJ6wKLQI/AAAAAAAAjB0/JlUjiQhfy4IXVmUOma60OU7dbuNuqiEQACLcBGAs/s0/Screenshot+at+2017-11-19+22-55-50.png "Code")



#### <i class="icon-folder-open"></i>Modelos

Para este proyecto, se crearon 3 modelos, el modelo **Game**, **Player** y **Movement**. 

> - **Game** ---> Este modelo es donde se almacenan los jugadores que van a jugar la partida, este modelo tiene un documento embebido llamado player, se crean dos jugadores con sus respectivas caracteristicas.
> 
> 
![Game Model](https://lh3.googleusercontent.com/-yCLvhARsvsI/WhJlb8W-TII/AAAAAAAAjCE/FxnQNOhDFTUS5MNbSOb5WnIgDeFLQKLHQCLcBGAs/s0/Screenshot+at+2017-11-19+23-15-52.png "Game Model")

> - **Player** ----> Este modelo es el documento embebido que existe en el modelo **Game**
> 
> ![enter image description here](https://lh3.googleusercontent.com/-JlJhFTnJY7M/WhJmGCYSyhI/AAAAAAAAjCU/39tsYVi0Va4eXwE_exNdhiwT1PBT02VHACLcBGAs/s0/Screenshot+at+2017-11-19+23-19-34.png)
> - **Movement** ----> Este modelo contiene los movimiento que se realizan los jugadores que estan en la sesion de juego. Dicho modelo tiene una relacion con el player y con la sesion.
> 
> ![enter image description here](https://lh3.googleusercontent.com/-_cORekrhGnY/WhJmqFwXkWI/AAAAAAAAjCk/YYD6YXRRd_QeqILk8-XNEqlRIFdX1F5SwCLcBGAs/s0/Screenshot+at+2017-11-19+23-22-33.png)


#### <i class="icon-pencil"></i> Instalacion

> **Paso #1** --> git clone https://github.com/ctreminiom/battle-tank.git

> **Paso #2** --> virtualenv env

> **Paso #3** --> source env/bin/activate

> **Paso #4** --> pip3 install -r requirements.txt

> **Paso #5** --> cd code/

> **Paso #6** --> vim **db.py** (cambiar la variables de entorno)

> **Paso #7 ** --> **python3 run.py**