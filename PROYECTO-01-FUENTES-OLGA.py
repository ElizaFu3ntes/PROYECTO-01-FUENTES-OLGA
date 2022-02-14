#PROYECTO-01- FUENTES-OLGAELIZABETH

from unittest.util import sorted_list_difference
from lifestore_file import (lifestore_products, lifestore_sales, lifestore_searches)

"""
Informacion de LifeStore_SalesList:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""


""" 
#Indentar como login
Login
credenciales
usuario
  Elizabeth
clave
  Proyecto1
"""

def login():
  usuario_acc = False
  intentos = 0

  #Bienvenida
  mensaje_bienvenida = "Bienvenido al sistema de consultas\n\nEscribe tu usuario y clave para ingresar\n"
  print (mensaje_bienvenida)
  #Intentos para ingresar
  while not usuario_acc:
    #Para ingresar credenciales
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    intentos += 1
    #Valida credenciales
    if usuario == "Elizabeth" and clave == "Proyecto1":
      usuario_acc = True
      print("\nComencemos")
    else:
      print (f"Tienes {3 - (intentos)} intentos restantes")
      if usuario == "Elizabeth":
        print("Clave incorrecta")
        print("Intente de nuevo")
      else:
        print (f"El usuario: {usuario} no esta registrado")
        print ("Intente de nuevo")
    #Hay un intento porque sino cierra el programa aunque el 3er intento fuese con las credenciales correctas
    if intentos == 4:
      exit()

def prodcat():
  #PUNTO 1. Productos más vendidos y productos rezagados:
  #Generar un listado de los 5 productos con mayores ventas
  #y uno con los 10 productos con mayor búsquedas.
  #Por categoría, listado con los 5 productos con menores ventas
  #y uno con los 10 productos con menores búsquedas.

  ############
  #1)Obtener listas

  #Lista productos con su categoria : id_product + name + category
  idpr_category = [[producto[0], producto [1], producto[3]] for producto in lifestore_products]
  #print (idpr_category)

  #Lista id_product + refund 
  idpr_refund = [[producto[1], producto[4]] for producto in lifestore_sales]
  #print (idpr_refund)

  #Lista id_product + price
  idpr_price = [[producto[0], producto [2]] for producto in lifestore_products]
  #print (idpr_price)

  #2)Crear diccionario vacio

  #Diccionario de productos por categoria
  product_category = {}

  #Definir contenido del diccionario: category(key) id_pr(value)
  for par in idpr_category:
    id_pr = par[0]
    category = par [2]
  #revisa si la categoria ya esta como llave en el diccionario
    if category not in product_category.keys():
  #si no crea una nueva llave
      product_category[category] = []
    product_category[category].append(id_pr)
  #Muestra el diccionario que contiene a todos los productos por categoria
  #print (product_category)
  #Para mostrar en una línea la categoría y en otra la lista de productos
  for key, values in product_category.items():
    print ("Los productos de la categoria", key, "son:")
    print (values, "\n")
  ############


def califprom():
  ############
  ###lista con idproduct y score
  idprod_valuacion = [[producto[2], producto[1]] for producto in lifestore_sales]
  #print(idprod_score)

  ###Diccionario de prod vendidos por score
  valuacion_productos = {}

  for par in idprod_valuacion:
    id_pr = par[0]
    valuacion = par[1]
    if valuacion not in valuacion_productos.keys():
      valuacion_productos[valuacion] = []
    valuacion_productos[valuacion].append(id_pr)
  #print (valuacion_productos)
  print ("La calificacion promedio de cada producto es:")
  #Muestra una lista con la calificacion promedio de los productos vendidos
  for key in valuacion_productos.keys():
    print (f'P {key}: {round(sum(valuacion_productos[key])/len(valuacion_productos[key]),2)}')
  ############


def analisiscat():
  ############
  # Analisis de reviews por categoria y de ventas
  prod_reviews = {}
  for sale in lifestore_sales:
      # prod y review de venta
      prod_id = sale[1]
      review = sale[2]
      # categorizar por id
      if prod_id not in prod_reviews.keys():
          prod_reviews[prod_id] = []
      prod_reviews[prod_id].append(review)
  #print(f"Lista de reviews por cada producto vendido", prod_reviews, "\n")

  category_ids = {}
  for prod in lifestore_products:
      prod_id = prod[0]
      category = prod[3]
      if category not in category_ids.keys():
          category_ids[category] = []
      category_ids[category].append(prod_id)
  #print(category_ids)

  resultados_por_categoria = {}
  for category, prod_id_list in category_ids.items():
      reviews = []
      ganancias = 0
      ventas = 0
      for prod_id in prod_id_list:
          if prod_id not in prod_reviews.keys():
              continue
          reviews_ventas = prod_reviews[prod_id]
          precio = lifestore_products[prod_id][2]
          total_sales = len(reviews_ventas)
          g = precio * total_sales
          reviews += reviews_ventas
          ganancias += g
          ventas += total_sales

      prom_reviews = round(sum(reviews) / len(reviews),2)#valor redondeado a 2 decimales

      resultados_por_categoria[category] = {
          'review_promedio': prom_reviews,
          'ganancias': ganancias,
          'ventas_totales': ventas
      }
  #print(resultados_por_categoria)
  print ("\nResumen del análisis de ventas por categoría\n")
  for cat, dic in resultados_por_categoria.items():
      print(cat)
      for key, val in dic.items():
          print('\t', key,':', val)
  ############


def ventacalif():
  ############
  #PUNTO2. Productos por reseña en el servicio:
  # Mostrar dos listados de 5 productos cada una, un listado para
  # productos con las mejores reseñas y otro para las peores,
  # considerando los productos con devolución.

  #Produtos vendidos por score
  #Lista con id_product + id_sale + score
  score_product = [[product[1], product[2]] for product in lifestore_sales]
  #print (score_product)

  #Diccionario de prod vendidos por score
  cat_score = {}
  #Definir contenido del diccionario: score(key) id_pr(value)
  for par in score_product:
    id_pr = par[0]
    score = par[1]
  #revisa si la categoria ya esta como llave en el diccionario
    if score not in cat_score.keys():
  #si no crea una nueva llave
      cat_score[score] = []
    cat_score[score].append(id_pr)
  #Muestra el diccionario que contiene a todos los productos por score
  #print (cat_score)
  # for key in cat_score.keys():
  # Salen desordenadas las categorias
  #   print (f'Los productos vendidos con {key} de calificacion fueron \n {cat_score[key]}\n')
  print ("\nVentas por categoria\n")
  print (f'Los productos vendidos con {1} de calificacion fueron: \n {cat_score[1]}\n')
  print (f'Los productos vendidos con {2} de calificacion fueron: \n {cat_score[2]}\n')
  print (f'Los productos vendidos con {3} de calificacion fueron: \n {cat_score[3]}\n')
  print (f'Los productos vendidos con {4} de calificacion fueron: \n {cat_score[4]}\n')
  print (f'Los productos vendidos con {5} de calificacion fueron: \n {cat_score[5]}\n')
  ########### 


def ventames():
  ##########################
  # PUNTO3. Total de ingresos y ventas promedio mensuales,
  # total anual y meses con más ventas al año

  #####
  #Productos vendidos por fechas id_product + id_sale + date
  #guarda id y fecha si la venta es valida
  sale_date = [[sale[1], sale[0], sale[3]] for sale in lifestore_sales if sale[4] == 0]
  #Para ver lista creada
  #print (sale_date)

  #Diccionario de productos vendidos por mes
  cat_sale = {}

  for par in sale_date:
    id_pr = par[0]
    _, mes, _ = par[2].split('/')
  #revisa si la categoria ya esta como llave en el diccionario
    if mes not in cat_sale.keys():
  #si no crea una nueva llave
      cat_sale[mes] = []
    cat_sale[mes].append(id_pr)
  #Para ver diccionario de productos vendidos en todos los meses {mes:[id_product]}
  #print (cat_sale)
  
  #Para ver los productos vendidos por mes sin duplicados, ordenados por id
  for mes in cat_sale:
    prod_mes = set(cat_sale.get(mes))
    print ("En el mes ", (mes))
    print ("Se vendieron los productos:\n",sorted(prod_mes),"\n")

  #Relaciona ventas con precio del producto: Ingresos mensuales
  for key in cat_sale.keys():
    lista_mes = cat_sale[key]
    suma_venta = 0
    #print (lista_mes)#Muestra los productos vendidos cada mes
    for id_venta in lista_mes:
      indice = id_venta - 1
      info_venta = lifestore_sales[indice]
      id_product = info_venta[1]
      #Para obtener precio de cada producto
      precio = lifestore_products[id_product - 1][2]
      suma_venta += precio
    print (f"Los ingresos del mes {key} fueron ${suma_venta}\nVentas realizadas: {len(lista_mes)}\n")
  ### SALEN EN DESORDEN
  # FALTA SUMAR INGRESOS DE MESES PARA OBTENER TOTAL POR AÑO


def menu():
    login()
    while True:
        print('Indica la informacion que deseas consultar')
        print('1. Productos de cada categoria')
        print('2. Calificacion promedio de cada producto')
        print('3. Ventas por categoria')
        print('4. Ventas mensuales')
        print('5. Productos vendidos por calificacion')
        print('\t0. Salir')
        seleccion = input('> ')
        if seleccion == '1':
            prodcat()
        elif seleccion == '2':
            califprom()
        elif seleccion == '3':
            analisiscat()
        elif seleccion == '4':
            ventames()
        elif seleccion == '5':
            ventacalif()
        elif seleccion == '0':
            exit()
        else:
            print('Opcion invalida!')

menu()