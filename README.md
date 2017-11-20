
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

> - **Game** ---> API
> - **Pymongo --- Mongoengine** ----> ORM para MongoDB que facilita la creacion de Modelos y Queries.
> - Python 3.5