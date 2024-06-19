from datetime import datetime

# Тема проекта: приложение «Касса кинотеатра».
# Спроектировать ПО, предназначенное для автоматизации деятельности кассы
# кинотеатра. Функции, которые должны быть реализованы в приложении:
# добавление, удаление, редактирование и просмотр информации о сеансах,
# наличии билетов и свободных мест.

class Afisha:
    def __init__(self, sessions=[]):
        self.sessions: list(Session) = sessions

    def view_sessions(self):
        for session in self.sessions:
            print(session.to_string())


    def view_movie_sessions(self, movie_to_search):
        listik = []
        for session in self.sessions:
            if session.movie == movie_to_search:
                listik.append(session)
        return listik

    def add_session(self, name, time, capacity):
        max = 0
        for session in self.sessions:
            if session.id > max:
                max = session.id
        self.sessions.append(Session(time, name, max + 1, capacity))
        print("Session added")

    def find_movie_session(self, id):
        for session in self.sessions:
            if session.id == id:
                return session

    def remove_movie_session(self, id):
        for session in self.sessions:
            if session.id == id:
                self.sessions.remove(session)
                print('Session has been removed')

class Movie:
    def __init__(self, name, duration, genre, rate):
        self.name: str = name
        self.duration : int = duration
        self.genre : str = genre
        self.rate : float = rate

    def to_string(self):
        return f"{self.name} [duration={self.duration}, genre={self.genre}, rate = {self.rate}]"

class Session:
    def __init__(self, time, movie, id, capacity):
        self.time: datetime=time
        self.movie: Movie = movie
        self.id: int = id
        self.capacity : int = capacity

    def edit_session(self, new_movie, new_time):
        self.movie = new_movie
        self.time = new_time
        print("Session has been updated")

    def to_string(self):
        return f"Session[time={self.time}, movie={self.movie.to_string()}, id={self.id}, capacity = {self.capacity}]"

class Ticket_sales:
    def __init__(self, afisha):
        self.afisha = afisha
    def buy_ticket(self, movie, count_of_tickets):
        movie_sessions = self.afisha.view_movie_sessions(movie)
        if movie_sessions[0].capacity < count_of_tickets:
            print("Not enought tickets")
            return
        movie_sessions[0].capacity -= count_of_tickets
        print("The ticket has been bought")

class Cinema:
    def __init__(self, name, address):
        self.name : str = name
        self.address : str = address
        self.afisha = Afisha()
        self.ticket_sales = Ticket_sales(self.afisha)

spider_man = Movie('Spider man', 120, 'Action', 5.6)
harry_Potter = Movie('Harry Potter', 140, 'Fantasy', 8.9)
gladiator = Movie ('Gladiator', 100, 'Action', 9.5)

cinema = Cinema('Pobeda','Gorki, 20')
cinema.afisha.add_session(harry_Potter,  datetime(2024, 6, 22, 23, 50, 00), 50)
cinema.afisha.add_session(spider_man,  datetime(2024, 6, 24, 12, 00, 00), 25)
cinema.afisha.add_session(gladiator,  datetime(2024, 6, 25, 17, 30, 00), 40)

cinema.afisha.view_sessions()
cinema.ticket_sales.buy_ticket(harry_Potter, 5)
cinema.afisha.view_sessions()
cinema.ticket_sales.buy_ticket(harry_Potter, 46)

cinema.afisha.find_movie_session(1).edit_session(spider_man, datetime(2024, 8, 29,20,
                                                                      50, 00))
cinema.afisha.view_sessions()