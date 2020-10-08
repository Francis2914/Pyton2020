@@ -1,4 +1,4 @@
 
#OPCION 1
importar  sqlite3
conn  =  sqlite3 . conectar ( "agendatelefonica.db" )
cursor  =  conn . cursor ()
@@ -93,21 +93,21 @@ def menu ():
  c  =  int ( input ( "Digite su opcion:" ))
  si  c  ==  1 :
    mientras es  cierto :
      nombre  =  input ( " nombre :" )
      nombre  =  input ( " Nombre :" )
      apellido  =  input ( "Nombre del Apellido:" )
      numero  =  input ( "Numero del contacto:" )
      insertar ()
      insertar ()  
      print ( "desea agregar otro?" )
      imprimir ( "1- si" )
      imprimir ( "2- no" )
      si =  int ( input ( "digite una opcion:" ))
      si  si  ==  2 : 
      si  si  ==  2 :
        rotura
  si  c  ==  2 :
    listar ()
    t  =  input ( "volver al menú:" )
  si  c  ==  3 :
    d  =  input ( "Digite ID que desea ver:" )
    d  =  int ( input ( "Digite ID que desea ver:" ) )
    listarID ()
    t  =  input ( "volver al menú:" )
  si  c  ==  4 :
@@ -135,21 +135,20 @@ def menu ():
    si  m  ==  3 :
      listar ()
      num  =  input ( "numero a modificar:" )
      d  =  int ( "ID del campo a modificar:" )
      d  =  int ( input ( "ID del campo a modificar:" ) )
      modificarnumero ()
      t  =  input ( "volver al menú:" )
  si  c  ==  6 :
    print ( "1- Buscar nombre" )
    print ( "2- Buscar numero" )
    b  =  int ( input ( "Digite una opcion:" ))
    si  b  ==  1 :
    si  b  ==  1   :
      nombre  =  input ( "buscar nombre:" )
      buscarnombre ()
      t  =  input ( "volver al menú:" )
    si  b  == 2 :
      numero  =  input ( "buscar numero:" )
      buscartelefono ()
      t  =  input ( "volver al menú:" )
  si  c  ==  7  :
  si  c  ==  7 :
    rotura
conn . cerrar () 