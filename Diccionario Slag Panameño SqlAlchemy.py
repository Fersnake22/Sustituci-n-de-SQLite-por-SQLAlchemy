from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///Diccionario Slag Panameño.db')
 

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class diccionario(Base):
	__tablename__= "Diccionario"

	id = Column(Integer, primary_key=True, autoincrement=True)
	palabra = Column(String, nullable=False)
	significado= Column(String, nullable=False)

	def __repr__(self):
		return f'{self.id}, {self.palabra}, {self.significado}'

	def __init__(self,id, palabra, significado):
		self.palabra=palabra
		self.significado=significado

class Ejemplo:

	def __init__(self):
		self.filas = session.query(diccionario).all()
		self.opcion_usuario = input("""
1) Agregar palabra
2) Editar palabra existente
3) Eliminar palabra existente
4) Ver listado de palabras
5) Buscar significado de palabras
0) salir	
			""") 

	def opcion_1(self):
		if self.opcion_usuario =='1':
			palabra=input("Ingrese la palabra: ")
			significado=input("Ingrese el significado: ")
			nueva_palabra= diccionario(id,palabra,significado)
			session.add(nueva_palabra)
			session.commit()
			print("La palabra ha sido agregada exitosamente")

	def opcion_2(self):
		if self.opcion_usuario=='2':
			palabra_buscar=input("Ingrese la pabalbra que quiere editar: ")
			nuevo_significado= input("\nIngrese el nuevo significado: ")
			session.query(diccionario).filter(diccionario.palabra==palabra_buscar).update(
				{diccionario.significado: nuevo_significado})
			session.commit()
			print("\nPalabra editada exitosamente")

	def opcion_3(self):
		if self.opcion_usuario == '3':
			palabra_eliminar= input("Ingresa la palabra a eliminar: ")
			session.query(diccionario).filter(diccionario.palabra==palabra_eliminar).delete()
			session.commit()
			print("\nLa palabra ha sido borrada exitosamente")

	def opcion_4(self):
		if self.opcion_usuario == '4':
			print("\nTodas las palabras\n")
			u=session.query(diccionario).order_by(asc(diccionario.id)).all()
			if len(u)>0:
				for count, i in enumerate(u):
					print(f'{i.palabra}')
				print()
			else:
				print("No hay palabras\n")

	def opcion_5(self):
		if self.opcion_usuario== '5':
			saber_significado = input("Escriba al palabra de la cual quiere saber el siginificado: ")
			x=session.query(diccionario).filter(diccionario.palabra==saber_significado).first()
			print()
			print(x.significado)

	def opcion_0(self):
		if self.opcion_usuario == '0':
			print("\nHasta la vista")
			exit()



while True:

	tarea= Ejemplo()
	tarea.opcion_1()
	tarea.opcion_2()
	tarea.opcion_3()
	tarea.opcion_4()
	tarea.opcion_5()
	tarea.opcion_0()