import dateparser
from datetime import datetime

class Book:
    def __init__(self, title, author):
        self.title = title  # Título del libro
        self.author = author  # Autor del libro

class Member:
    def __init__(self, name):
        self.name = name  # Nombre del miembro

class Loan:
    def __init__(self, book, member, return_date):
        self.book = book  # Libro prestado
        self.member = member  # Miembro que toma el préstamo
        self.loan_date = datetime.now()  # Fecha del préstamo
        self.return_date = return_date  # Fecha límite de devolución
        self.returned = False  # Estado de devolución
        self.late_returns = 0  # Contador de retrasos

    def process_return(self):
        today = datetime.now()  # Fecha actual
        self.returned = True  # Marca el libro como devuelto
        if today > self.return_date:
            late_days = (today - self.return_date).days  # Días de retraso
            self.late_returns += 1  # Incrementa el contador de retrasos
            if self.late_returns == 1:
                print(f"El libro '{self.book.title}' fue devuelto con {late_days} días de retraso.")
                print("Advertencia: Si se repite el retraso, se aplicará una sanción.")
            else:
                print(f"El libro '{self.book.title}' fue devuelto tarde nuevamente. Se aplicará una sanción.")
        else:
            print(f"El libro '{self.book.title}' fue devuelto a tiempo. No hay sanción.")

class Library:
    def __init__(self):
        self.loans = []  # Lista de préstamos

    def issue_loan(self, book, member):
        return_date_input = input(f"Introduce la fecha límite para devolver '{book.title}' (en cualquier formato reconocible): ")
        return_date = dateparser.parse(return_date_input)  # Interpreta la fecha
        if return_date is None:
            print("Formato de fecha no reconocido. Intenta de nuevo.")
            return

        new_loan = Loan(book, member, return_date)  # Crea un nuevo préstamo
        self.loans.append(new_loan)  # Añade el préstamo a la lista
        print(f"El libro '{book.title}' fue prestado a {member.name}. Fecha límite de devolución: {return_date}.")

    def return_loan(self, book, member):
        for loan in self.loans:
            if loan.book == book and loan.member == member and not loan.returned:
                loan.process_return()  # Procesa la devolución
                return
        print(f"No se encontró un préstamo activo para '{book.title}' a nombre de {member.name}.")

# Ejemplo de uso interactivo

library = Library()  # Instancia de la biblioteca

books = []
num_books = int(input("¿Cuántos libros quieres agregar? "))
for _ in range(num_books):
    title = input("Título del libro: ")
    author = input("Autor del libro: ")
    books.append(Book(title, author))  # Añade libros a la lista

members = []
num_members = int(input("¿Cuántos usuarios quieres agregar? "))
for _ in range(num_members):
    name = input("Nombre del usuario: ")
    members.append(Member(name))  # Añade usuarios a la lista

active = True
while active:
    print("\nMenú de opciones:")
    print("1. Realizar préstamo")
    print("2. Devolver libro")
    print("3. Salir")
    option = input("Selecciona una opción: ")

    if option == "1":
        print("\nLibros disponibles:")
        for i, book in enumerate(books):
            print(f"{i + 1}. {book.title} por {book.author}")
        book_choice = int(input("Selecciona el número del libro a prestar: ")) - 1
        
        print("\nUsuarios registrados:")
        for i, member in enumerate(members):
            print(f"{i + 1}. {member.name}")
        member_choice = int(input("Selecciona el número del usuario: ")) - 1

        library.issue_loan(books[book_choice], members[member_choice])  # Realiza el préstamo

    elif option == "2":
        print("\nLibros prestados actualmente:")
        for i, loan in enumerate(library.loans):
            if not loan.returned:
                print(f"{i + 1}. '{loan.book.title}' por {loan.book.author} (Prestado a {loan.member.name})")
        loan_choice = int(input("Selecciona el número del libro a devolver: ")) - 1

        library.return_loan(library.loans[loan_choice].book, library.loans[loan_choice].member)  # Realiza la devolución

    elif option == "3":
        print("Saliendo del sistema. ¡Hasta luego!")
        active = False  # Finaliza el bucle

    else:
        print("Opción no válida. Inténtalo de nuevo.")
