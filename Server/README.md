#  Estructura de Base de Datos mysql

Fullaxis  ┐ <br />
&emsp;&emsp;&emsp;&emsp;├ Users ┐<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;├ ID_user (int)<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;├ Name (str)<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;├ Password (str)<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;├ Proyect (str)<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;├ Enable (bol)<br />
&emsp;&emsp;&emsp;&emsp;│&emsp;&emsp;&emsp;└ DatelastAccess (timestamp)<br />
&emsp;&emsp;&emsp;&emsp;└ B2_key ┐<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;├ ID_key (int)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;├ ID_key_user (int)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;├ KeyName (str)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;├ KeyPassword (str)<br />
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&ensp;└ Enable (bol)<br />
