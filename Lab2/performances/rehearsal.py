"""Класс репетиции"""
from typing import List, Optional
from datetime import datetime


class Rehearsal:
    """Репетиция спектакля"""
    
    def __init__(self, performance_name: str, date: datetime, duration_minutes: int):
        if not isinstance(performance_name, str) or not performance_name:
            raise ValueError("Название спектакля должно быть непустой строкой")
        if not isinstance(date, datetime):
            raise ValueError("Дата должна быть объектом datetime")
        if not isinstance(duration_minutes, int) or duration_minutes <= 0:
            raise ValueError("Длительность должна быть положительным целым числом")
        
        self.performance_name = performance_name
        self.date = date
        self.duration_minutes = duration_minutes
        self.__participants: List[str] = []
        self.location = ""
        self.is_completed = False
        self.notes = ""
    
    def add_participant(self, participant: str) -> None:
        """Добавить участника"""
        if not isinstance(participant, str):
            raise TypeError("Участник должен быть строкой")
        if participant not in self.__participants:
            self.__participants.append(participant)
    
    def remove_participant(self, participant: str) -> None:
        """Удалить участника"""
        if participant in self.__participants:
            self.__participants.remove(participant)
    
    def get_participants(self) -> List[str]:
        """Получить список участников"""
        return self.__participants.copy()
    
    def set_location(self, location: str) -> None:
        """Установить место"""
        if not isinstance(location, str):
            raise TypeError("Место должно быть строкой")
        self.location = location
    
    def mark_completed(self) -> None:
        """Отметить как завершенную"""
        self.is_completed = True
    
    def set_notes(self, notes: str) -> None:
        """Установить заметки"""
        if not isinstance(notes, str):
            raise TypeError("Заметки должны быть строкой")
        self.notes = notes
    
    participants = property(get_participants)

