"""Класс спектакля"""
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from staff.actor import Actor
    from staff.director import Director
    from tickets.ticket import Ticket
    from venues.stage import Stage
    from costumes.costume import Costume


class Performance:
    """Спектакль театра"""
    
    def __init__(self, name: str, duration_minutes: int, genre: str, ticket_price: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Название должно быть непустой строкой")
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Длительность должна быть положительным целым числом")
        if not isinstance(genre, str) or not genre:
            raise ValueError("Жанр должен быть непустой строкой")
        if not isinstance(ticket_price, (int, float)) or ticket_price < 0:
            raise ValueError("Цена билета должна быть неотрицательным числом")
        
        self.name = name
        self.duration_minutes = duration_minutes
        self.genre = genre
        self.ticket_price = ticket_price
        self.__actors: List[str] = []
        self.premiere_date: Optional[datetime] = None
        self.is_active = True
        self.total_shows = 0
    
    def add_actor(self, actor_name: str) -> None:
        """Добавить актера"""
        if not isinstance(actor_name, str):
            raise TypeError("Имя актера должно быть строкой")
        if actor_name not in self.__actors:
            self.__actors.append(actor_name)
    
    def remove_actor(self, actor_name: str) -> None:
        """Удалить актера"""
        if actor_name in self.__actors:
            self.__actors.remove(actor_name)
    
    def get_actors(self) -> List[str]:
        """Получить список актеров"""
        return self.__actors.copy()
    
    def set_premiere_date(self, date: datetime) -> None:
        """Установить дату премьеры"""
        if not isinstance(date, datetime):
            raise TypeError("Дата должна быть объектом datetime")
        self.premiere_date = date
    
    def increment_shows(self) -> None:
        """Увеличить счетчик показов"""
        self.total_shows += 1
    
    def set_active(self, active: bool) -> None:
        """Установить активность"""
        if not isinstance(active, bool):
            raise TypeError("Активность должна быть булевым значением")
        self.is_active = active
    
    def assign_actor(self, actor: 'Actor') -> None:
        """Назначить актера (ассоциация с Actor)"""
        if actor.name not in self.__actors:
            self.__actors.append(actor.name)
    
    def assign_director(self, director: 'Director') -> None:
        """Назначить режиссера (ассоциация с Director)"""
        if director is None:
            raise ValueError("Режиссер не может быть None")
        if not director.is_available:
            raise ValueError("Режиссер недоступен")
        # Режиссер назначается на спектакль
        if director.name not in [p for p in director.get_performances()]:
            director.add_performance(self.name)
    
    def assign_stage(self, stage: 'Stage') -> None:
        """Назначить сцену (ассоциация с Stage)"""
        if stage is None:
            raise ValueError("Сцена не может быть None")
        if not stage.is_available:
            raise ValueError("Сцена недоступна")
        # Сцена назначается для спектакля
    
    def add_costume(self, costume: 'Costume') -> None:
        """Добавить костюм (ассоциация с Costume)"""
        if costume is None:
            raise ValueError("Костюм не может быть None")
        # Костюм добавляется к спектаклю
    
    def create_ticket(self, ticket: 'Ticket') -> None:
        """Создать билет (ассоциация с Ticket)"""
        if ticket is None:
            raise ValueError("Билет не может быть None")
        if ticket.price != self.ticket_price:
            raise ValueError("Цена билета не соответствует цене спектакля")
        # Билет создается для спектакля
    
    actors = property(get_actors)

