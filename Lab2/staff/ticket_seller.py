"""Класс билетера"""
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime, timedelta

if TYPE_CHECKING:
    from ..tickets.order import Order
    from ..tickets.ticket import Ticket
    from ..tickets.sale import Sale
    from ..finance.payment import Payment
    from ..venues.box_office import BoxOffice
    from ..finance.budget import Budget


class TicketSeller:
    """Билетер театра"""
    
    def __init__(self, name: str, age: int, experience_years: int, salary: float):
        if not isinstance(name, str) or not name:
            raise ValueError("Имя должно быть непустой строкой")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Возраст должен быть неотрицательным целым числом")
        if not isinstance(experience_years, int) or experience_years < 0:
            raise ValueError("Опыт должен быть неотрицательным целым числом")
        if not isinstance(salary, (int, float)) or salary < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом")
        
        self.name = name
        self.age = age
        self.experience_years = experience_years
        self.salary = salary
        self.__sold_tickets_count = 0
        self.is_available = True
        self.workplace_number = 0
        self.__current_order: Optional['Order'] = None
        self.__box_office: Optional['BoxOffice'] = None
        self.__budget: Optional['Budget'] = None
        self.__available_tickets: List['Ticket'] = []
        self.__reserved_tickets: List['Ticket'] = []  # Резерв билетов
    
    def sell_ticket(self) -> None:
        """Продать билет"""
        self.__sold_tickets_count += 1
    
    def get_sold_tickets_count(self) -> int:
        """Получить количество проданных билетов"""
        return self.__sold_tickets_count
    
    def reset_sold_tickets(self) -> None:
        """Сбросить счетчик проданных билетов"""
        self.__sold_tickets_count = 0
    
    def set_workplace_number(self, number: int) -> None:
        """Установить номер рабочего места"""
        if not isinstance(number, int) or number < 0:
            raise ValueError("Номер должен быть неотрицательным целым числом")
        self.workplace_number = number
    
    def set_availability(self, available: bool) -> None:
        """Установить доступность"""
        if not isinstance(available, bool):
            raise TypeError("Доступность должна быть булевым значением")
        self.is_available = available

    def assign_to_box_office(self, box_office: 'BoxOffice') -> None:
        """Назначить кассу"""
        if box_office is None:
            raise ValueError("Касса не может быть None")
        self.__box_office = box_office
        box_office.add_seller(self.name)

    def assign_budget(self, budget: 'Budget') -> None:
        """Назначить бюджет для учета доходов"""
        if budget is None:
            raise ValueError("Бюджет не может быть None")
        self.__budget = budget

    def start_shift(self) -> None:
        """Начать смену"""
        if not self.is_available:
            raise ValueError("Продавец недоступен")
        if self.__box_office is None:
            raise ValueError("Продавец должен быть назначен на кассу")
        self.reset_sold_tickets()
        self.__current_order = None
        print(f"Смена начата для продавца {self.name} на кассе {self.workplace_number}")

    def end_shift(self) -> None:
        """Закончить смену"""
        if self.__current_order is not None:
            print(f"Предупреждение: незавершенный заказ {self.__current_order.order_number}")
        print(f"Смена закончена. Продано билетов: {self.sold_tickets_count}")
        self.set_availability(False)

    def create_order(self, customer_name: str) -> 'Order':
        """Создать новый заказ для клиента"""
        if not self.is_available:
            raise ValueError("Продавец недоступен")
        if self.__current_order is not None:
            raise ValueError("У продавца уже есть активный заказ")

        from ..tickets.order import Order
        order_number = f"ORD{self.__sold_tickets_count + 1:04d}"
        self.__current_order = Order(order_number, customer_name, datetime.now())
        return self.__current_order

    def add_ticket_to_order(self, ticket: 'Ticket') -> None:
        """Добавить билет в текущий заказ"""
        if self.__current_order is None:
            raise ValueError("Нет активного заказа")
        if ticket.is_sold:
            raise ValueError("Билет уже продан")
        if ticket.is_used:
            raise ValueError("Билет уже использован")

        self.__current_order.add_ticket(ticket.ticket_number)
        ticket_price = ticket.price
        current_total = self.__current_order.total_amount
        self.__current_order.set_total_amount(current_total + ticket_price)

    def find_available_tickets(self, performance_name: str) -> List['Ticket']:
        """Найти доступные билеты на спектакль"""
        available = []
        for ticket in self.__available_tickets:
            if (ticket.performance_name == performance_name and
                not ticket.is_sold and not ticket.is_used):
                available.append(ticket)
        return available

    def add_available_tickets(self, tickets: List['Ticket']) -> None:
        """Добавить доступные билеты в систему продавца"""
        for ticket in tickets:
            if ticket not in self.__available_tickets:
                self.__available_tickets.append(ticket)

    def process_sale(self, payment_method: str) -> 'Sale':
        """Обработать продажу текущего заказа"""
        if self.__current_order is None:
            raise ValueError("Нет активного заказа")
        if not self.__current_order.get_tickets():
            raise ValueError("Заказ пуст")

        # Создать продажу
        from ..tickets.sale import Sale
        sale_number = f"SALE{self.__sold_tickets_count + 1:04d}"
        first_ticket = self.__current_order.get_tickets()[0]
        sale = Sale(sale_number, first_ticket, self.__current_order.total_amount)
        sale.complete_sale(datetime.now(), self.name)
        sale.set_payment_method(payment_method)

        # Отметить билеты как проданные
        for ticket_num in self.__current_order.get_tickets():
            ticket = self.__find_ticket_by_number(ticket_num)
            if ticket:
                ticket.sell(datetime.now())

        # Обновить статистику
        tickets_count = len(self.__current_order.get_tickets())
        self.__sold_tickets_count += tickets_count

        # Добавить доход в кассу
        if self.__box_office:
            self.__box_office.add_revenue(self.__current_order.total_amount)

        # Добавить доход в бюджет театра
        if self.__budget:
            try:
                self.__budget.add_revenue(self.__current_order.total_amount)
                print(f"💰 Доход {self.__current_order.total_amount} руб. добавлен в бюджет")
            except Exception as e:
                print(f"⚠️ Предупреждение: не удалось добавить доход в бюджет: {e}")

        # Очистить текущий заказ
        completed_order = self.__current_order
        self.__current_order = None

        return sale

    def process_payment(self, sale: 'Sale', payment_amount: float) -> 'Payment':
        """Обработать платеж за продажу"""
        if payment_amount < sale.amount:
            raise ValueError("Недостаточная сумма оплаты")

        from ..finance.payment import Payment
        payment_number = f"PAY{sale.sale_number[4:]}"
        payment = Payment(payment_number, sale.amount, datetime.now())
        payment.set_payment_method(sale.payment_method)
        payment.set_recipient("Театр")
        payment.complete()

        return payment

    def cancel_current_order(self) -> None:
        """Отменить текущий заказ"""
        if self.__current_order:
            self.__current_order.cancel()
            self.__current_order = None

    def get_current_order(self) -> Optional['Order']:
        """Получить текущий заказ"""
        return self.__current_order

    def reserve_ticket(self, ticket: 'Ticket', customer_name: str, duration_minutes: int = 15) -> None:
        """Зарезервировать билет на время"""
        if ticket in self.__reserved_tickets:
            raise ValueError("Билет уже зарезервирован")
        if ticket.is_sold:
            raise ValueError("Билет уже продан")

        # Добавляем временную метку резервирования
        ticket._Ticket__reservation_time = datetime.now()
        ticket._Ticket__reservation_duration = duration_minutes
        ticket._Ticket__reserved_by = customer_name
        self.__reserved_tickets.append(ticket)

        print(f"🎫 Билет {ticket.ticket_number} зарезервирован для {customer_name} на {duration_minutes} минут")

    def cancel_reservation(self, ticket: 'Ticket') -> None:
        """Отменить резервирование билета"""
        if ticket in self.__reserved_tickets:
            self.__reserved_tickets.remove(ticket)
            # Очищаем поля резервирования
            if hasattr(ticket, '_Ticket__reservation_time'):
                delattr(ticket, '_Ticket__reservation_time')
            if hasattr(ticket, '_Ticket__reservation_duration'):
                delattr(ticket, '_Ticket__reservation_duration')
            if hasattr(ticket, '_Ticket__reserved_by'):
                delattr(ticket, '_Ticket__reserved_by')
            print(f"❌ Резервирование билета {ticket.ticket_number} отменено")

    def get_reserved_tickets(self) -> List['Ticket']:
        """Получить список зарезервированных билетов"""
        # Очищаем просроченные резервирования
        current_time = datetime.now()
        expired_reservations = []

        for ticket in self.__reserved_tickets:
            if hasattr(ticket, '_Ticket__reservation_time') and hasattr(ticket, '_Ticket__reservation_duration'):
                reservation_end = ticket._Ticket__reservation_time + timedelta(minutes=ticket._Ticket__reservation_duration)
                if current_time > reservation_end:
                    expired_reservations.append(ticket)

        for ticket in expired_reservations:
            self.cancel_reservation(ticket)

        return [ticket for ticket in self.__reserved_tickets if ticket not in expired_reservations]

    def apply_discount(self, order: 'Order', discount_percentage: float) -> None:
        """Применить скидку к заказу"""
        if not isinstance(discount_percentage, (int, float)) or discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Процент скидки должен быть от 0 до 100")

        discount_amount = order.total_amount * (discount_percentage / 100)
        new_total = order.total_amount - discount_amount
        order.set_total_amount(new_total)

        print(f"💸 Применена скидка {discount_percentage}%: -{discount_amount} руб. Новый итог: {new_total} руб.")

    def process_refund(self, ticket: 'Ticket', reason: str) -> None:
        """Обработать возврат билета"""
        if not ticket.is_sold:
            raise ValueError("Билет не был продан")
        if ticket.is_used:
            raise ValueError("Использованный билет нельзя вернуть")

        # Возвращаем билет в доступные
        ticket.sell(datetime.now())  # Сбрасываем статус продажи
        ticket.is_sold = False
        ticket.is_used = False
        ticket.purchase_date = None

        # Возвращаем деньги в бюджет
        refund_amount = ticket.price
        if self.__budget:
            # При возврате уменьшаем доходы бюджета
            # В реальности нужно вычесть из доходов, но для простоты добавим как отрицательный доход
            try:
                self.__budget.add_expense(refund_amount)
                print(f"💸 Возврат {refund_amount} руб. обработан через бюджет")
            except Exception as e:
                print(f"⚠️ Предупреждение: не удалось обработать возврат через бюджет: {e}")

        self.__sold_tickets_count -= 1
        print(f"🔄 Билет {ticket.ticket_number} возвращен. Причина: {reason}")

    def validate_payment(self, payment: 'Payment', order_total: float) -> bool:
        """Валидировать платеж"""
        if payment.amount != order_total:
            raise ValueError(f"Сумма платежа ({payment.amount}) не соответствует сумме заказа ({order_total})")

        if not payment.is_completed:
            raise ValueError("Платеж не завершен")

        if payment.recipient != "Театр":
            raise ValueError("Платеж должен быть адресован театру")

        return True

    def get_sales_statistics(self) -> dict:
        """Получить детальную статистику продаж"""
        total_revenue = 0
        if self.__box_office:
            total_revenue = self.__box_office.daily_revenue

        return {
            "sold_tickets": self.sold_tickets_count,
            "total_revenue": total_revenue,
            "reserved_tickets": len(self.get_reserved_tickets()),
            "available_tickets": len(self.__available_tickets),
            "workplace": self.workplace_number,
            "seller_name": self.name
        }

    def __find_ticket_by_number(self, ticket_number: str) -> Optional['Ticket']:
        """Найти билет по номеру"""
        for ticket in self.__available_tickets:
            if ticket.ticket_number == ticket_number:
                return ticket
        return None

    def generate_shift_report(self) -> str:
        """Сгенерировать отчет за смену"""
        stats = self.get_sales_statistics()
        budget_balance = "Н/Д"
        if self.__budget:
            budget_balance = f"{self.__budget.get_balance():.2f}"

        return f"""📊 Отчет за смену продавца {self.name}
🏪 Касса №{self.workplace_number}
🎫 Продано билетов: {stats['sold_tickets']}
💰 Выручка кассы: {stats['total_revenue']:.2f} руб.
💼 Баланс бюджета: {budget_balance} руб.
🎭 Доступно билетов: {stats['available_tickets']}
⏰ Зарезервировано билетов: {stats['reserved_tickets']}
📅 Время отчета: {datetime.now()}
"""

    sold_tickets_count = property(get_sold_tickets_count)

