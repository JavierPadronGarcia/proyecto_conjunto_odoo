# Proyecto Javier

Al instalar el módulo, se debe de instalar también el módulo de proyecto ya que dependemos de él.

Cuando se instala, deberemos entrar en la configuración del usuario y seleccionar que el usuario es administrador, además, tendremos varios grupos de usuarios más, como jefe de proyectos, analista y programador, por lo tanto quitaremos de Proyectos en la parte superior izquierda el selector de proyectos y lo dejamos en blanco para que todos los permisos funcionen correctamente

![Image of the userGroups](images/UserGroupImage.png)

Ahora sí podremos ir al módulo, una vez entramos al módulo veremos la vista tree de las empresas contratadoras.

![Empresas contratadoras menu](images/EmpresasContratadorasImage.png)

Cuando seleccionamos en nuevo nos aparecerá la vista de formulario de las empresas contratadoras con sus respectivos campos

![Empresas contratadoras form](images/EmpresasContratadorasImage2.png)

Rellenamos los campos y vemos que el campo de tipo de empresa está en gris, eso es porque es un campo calculado, este se calcula con la cantidad que se ponga en el de numero de empleados, a más número de empleados, más grande es la empresa, por lo que variará entre pequeña, mediana y gran empresa

![Empresas contratadoras form relleno](images/EmpresasContratadorasImage3.png)

También vemos que está la vista tree heredada de los proyectos que tiene la empresa, esto es debido a que tenemos un campo oneToMany asociado a los proyectos en el modelo de las empresas contratadoras, ahí se podrán agregar nuevos proyectos, probamos a agregar uno:

![Proyectos form](images/ProyectosImage1.png)

Rellenamos los datos y se agregan correctamente a la empresa contratadora correspondiente

![Proyecto nuevo creado](images/ProyectosImage2.png)

Ahora si queremos agregar una tarea vamos a poder agregarla seleccionando el proyecto que queremos y agregar la tarea desde la pestaña de tareas:

![Tareas proyecto](images/ProyectosImage3.png)

y podemos agregarlas: 

![Tareas form](images/TareasImage1.png)

agregando una tarea podremos elegir la categoría que tiene, en este caso se elige backlog. Esto está hecho mediante la carga previa de datos.

![Tareas categorías](images/TareasImage2.png)

Una vez hecho esto se ha agregado correctamente.

![Tarea agregada](images/TareasImage3.png)


Finalmente toda la estructura principal ya está explicada, las vistas de los proyectos y las tareas están heredadas además dentro de los formularios de las empresas contratadoras y los proyectos también en las pestañas de la parte superior de la pantalla desde la que podemos acceder.

![Menu odoo](images/MenuImage.png)

Ahora crearemos un reporte de una empresa contratadora, esta mostrará los datos de la empresa y los proyectos que tiene esa empresa:

En la parte superior derecha de la pantalla se ve imprimir, cuando le damos aparecerá el reporte hecho:

![Reportes](images/Reporte.png)

Vemos que está realizado el reporte con el nombre de los proyectos y el numero de tareas que tienen:

![Reportes 2](images/Reporte2.png)

Finalmente quedaría ver los permisos de los usuarios, para ello tenemos que cambiar los ajustes para poder ver los permisos que tendrían:

![Permisos jefe proyectos](images/Permisos1.png)

Si ponemos al usuario como jefe de proyectos se ejecutarán las mismas acciones explicadas en el administrador ya que tiene permisos para hacer todos los crud de los proyectos, tareas y empresas_contratadoras.



Ahora cambiamos a analista, tendremos la posibilidad de ver las empresas contratadoras y los proyectos, pero no podremos modificarlos, donde podremos hacer el crud completo será de las tareas:

De las demás vistas no podremos modificar nada, solo ver

![Permisos analistas](images/Permisos2.png)

Finalmente si entramos como programadores solo podremos ver los proyectos y las tareas, pero no podremos hacer el crud de los proyectos y no podremos agregar ni borrar tareas, solo modificarlas.

![Permisoss programadores](images/Permisos3.png)

Aquí vemos una tarea, que actualizamos la categoría de backlog a ready:

![Permisos programadores tarea sin modificar](images/Permisos4.png)

Tarea actualizada:

![Permisos programadores tarea actualizada](images/Permisos5.png)

A continuación se muestra cada una de las vistas y las demás acciones realizadas:


Modelos:

Empresas contratadoras

![Modelo empresas contratadoras](images/Model1.png)

Proyecto (heredado):

![Proyecto heredado](images/Model2.png)

Tareas (heredado):

![Tareas heredado](images/Model3.png)


Vistas:

Empresas contratadoras:

![Vistas empresas contratadoras](images/Views1.png)

Proyectos con tareas heredadas:

![Proyectos y tareas](images/Views2.png)

Acciones:

![Acciones](images/actions1.png)

Elementos de menú:

![Elementos de menú](images/menuElements.png)

Carga previa de datos:

![Carga previa](images/charge.png)