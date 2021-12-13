import sqlite3
from sqlite3 import Error


def sql_connection():
    # Método para establecer la conexión
    try:
        con = sqlite3.connect('tienda.db')
        return con
    except Error:
        print(Error)


def sql_table(con):
    # Metodo que  crea un objeto cursor para ejecutar la sentencia de create table
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE clientes(id integer PRIMARY KEY AUTOINCREMENT, nombre text, precio REAL , cantidad INTEGER)")
    con.commit()  # guarda todos los cambios que hacemos


con = sql_connection()  # Establecemos conexión/Creamos base de datos
#sql_table(con)


def sql_insert(con, name, price, quantity):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO clientes(nombre, precio, cantidad) VALUES(?, ?, ?)', (name, price, quantity))
    # usamos el signo de interrogación (?) Como argumento para cada valor
    con.commit()


sql_insert(con, 'pan', 0.5, 20)#Ejecutamos el insert con nuestros datos
sql_insert(con, 'leche', 1, 10)#Ejecutamos el insert con nuestros datos
sql_insert(con, 'vino', 10, 5)#Ejecutamos el insert con nuestros datos


def tuple_to_dict(mytuple):
    mydict = dict()
    mydict['id'] = mytuple[0]
    mydict['nombre'] = mytuple[1]
    mydict['precio'] = mytuple[2]
    mydict['cantidad'] = mytuple[3]
    return mydict

def sql_select_nombre(con,valor):
    cursorObj = con.cursor()
    query = "SELECT * FROM clientes WHERE nombre = '"+str(valor)+"'"
    cursorObj.execute(query)
    row = cursorObj.fetchone()
    return tuple_to_dict(row)

print('SELECT leche')
print(sql_select_nombre(con, 'leche'))

def sql_update(con, nombre, precio, cantidad):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE clientes SET precio = ?, cantidad = ? where nombre = ?', (precio, cantidad, nombre))
    con.commit()

print('UPDATE pan')
#sql_update(con, 'pan', price=1.5, quantity=5)
sql_update(con, 'pan', 1.5, 5)
print(sql_select_nombre(con, 'pan'))

def sql_delete(con, nombre):
    cursorObj = con.cursor()
    query = "DELETE * FROM clientes WHERE nombre = '" + str(nombre) + "'"
    cursorObj.execute(query)
    con.commit()

con.close()
