ОПИСАНИЕ КЛАССОВ ТЕАТРАЛЬНОЙ СИСТЕМЫ

СТАФФ (STAFF) - 18 классов:

Actor 7 6 → Performance, Costume, Rehearsal, Salary
Поля: name, age, experience_years, salary, __roles, is_available, contract_end_date
Методы: add_role, remove_role, get_roles, set_availability, calculate_total_earnings, join_performance, get_costume, attend_rehearsal, receive_salary

Director 7 7 → Performance, Rehearsal, Session
Поля: name, age, experience_years, salary, __directed_performances, is_available, contract_end_date, awards
Методы: add_performance, remove_performance, get_performances, add_award, set_availability, calculate_total_earnings, direct_performance, conduct_rehearsal, manage_session

CostumeDesigner 7 5 → Costume
Поля: name, age, experience_years, salary, __designed_costumes, is_available, specialization
Методы: add_costume, remove_costume, get_costumes, set_specialization, set_availability

MakeupArtist 7 5 → Actor
Поля: name, age, experience_years, salary, __makeup_styles, is_available, tools_count
Методы: add_makeup_style, remove_makeup_style, get_makeup_styles, set_tools_count, set_availability

TicketSeller 7 5 → Ticket, Order
Поля: name, age, experience_years, salary, __sold_tickets_count, is_available, workplace_number
Методы: sell_ticket, get_sold_tickets_count, reset_sold_tickets, set_workplace_number, set_availability

Administrator 7 5 → Event, Schedule
Поля: name, age, experience_years, salary, __managed_events, is_available, department
Методы: add_event, remove_event, get_events, set_department, set_availability

Manager 7 5 → Project, Team
Поля: name, age, experience_years, salary, __managed_projects, is_available, team_size
Методы: add_project, remove_project, get_projects, set_team_size, set_availability

Musician 7 5 → Performance, Instrument
Поля: name, age, experience_years, salary, __instruments, is_available, specialization
Методы: add_instrument, remove_instrument, get_instruments, set_specialization, set_availability

Choreographer 7 5 → Performance, Dance
Поля: name, age, experience_years, salary, __choreographies, is_available, dance_style
Методы: add_choreography, remove_choreography, get_choreographies, set_dance_style, set_availability

LightingTechnician 7 5 → Stage, Equipment
Поля: name, age, experience_years, salary, __lighting_equipment, is_available, equipment_count
Методы: add_equipment, remove_equipment, get_equipment, set_equipment_count, set_availability

SoundEngineer 7 5 → Stage, Equipment
Поля: name, age, experience_years, salary, __sound_equipment, is_available, equipment_count
Методы: add_equipment, remove_equipment, get_equipment, set_equipment_count, set_availability

StageManager 7 5 → Stage, Performance
Поля: name, age, experience_years, salary, __managed_stages, is_available, stage_count
Методы: add_stage, remove_stage, get_stages, set_stage_count, set_availability

PropsMaster 7 5 → Prop, Storage
Поля: name, age, experience_years, salary, __managed_props, is_available, props_count
Методы: add_prop, remove_prop, get_props, set_props_count, set_availability

SetDesigner 7 5 → Decoration, Performance
Поля: name, age, experience_years, salary, __designed_sets, is_available, style
Методы: add_set, remove_set, get_sets, set_style, set_availability

Producer 7 5 → Show, Budget
Поля: name, age, experience_years, salary, __produced_shows, is_available, budget_managed
Методы: add_show, remove_show, get_shows, set_budget_managed, set_availability

Accountant 7 4 → Budget, Invoice, Payment
Поля: name, age, experience_years, salary, __managed_accounts, certification, is_available
Методы: add_account, get_accounts, set_certification, set_availability

Audience 7 4 → Ticket, Order
Поля: name, age, email, __tickets_purchased, loyalty_points, is_member, membership_type
Методы: purchase_ticket, get_tickets_purchased, add_loyalty_points, become_member

SecurityGuard 7 5 → Area, Theater
Поля: name, age, experience_years, salary, __assigned_areas, license_number, is_available, shift
Методы: add_area, get_areas, set_license_number, set_shift, set_availability

СПЕКТАКЛИ (PERFORMANCES) - 6 классов:

Performance 7 9 → Actor, Director, Ticket, Stage, Costume
Поля: name, duration_minutes, genre, ticket_price, __actors, premiere_date, is_active, total_shows
Методы: add_actor, remove_actor, get_actors, set_premiere_date, increment_shows, set_active, assign_actor, assign_director, assign_stage, add_costume, create_ticket

Rehearsal 7 6 → Performance, Actor, Director
Поля: performance_name, date, duration_minutes, __participants, location, is_completed, notes
Методы: add_participant, remove_participant, get_participants, set_location, mark_completed, set_notes

Premiere 7 5 → Performance, Venue, Ticket
Поля: performance_name, date, venue_name, tickets_sold, is_successful, reviews_count, rating
Методы: sell_ticket, get_tickets_sold, mark_successful, add_review, set_rating

Tour 7 7 → Performance, City, Venue
Поля: name, start_date, end_date, __cities, __performances, total_revenue, is_completed
Методы: add_city, remove_city, get_cities, add_performance, get_performances, add_revenue, mark_completed

Show 7 5 → Performance, Venue, Ticket
Поля: performance_name, date, venue_name, tickets_sold, tickets_available, is_cancelled, start_time
Методы: sell_ticket, set_tickets_available, cancel, set_start_time, get_occupancy_rate

Review 7 5 → Performance, Audience
Поля: performance_name, reviewer_name, rating, comment, review_date, is_published, is_verified
Методы: publish, verify, set_review_date, is_positive

МЕСТА (VENUES) - 7 классов:

Theater 7 4 → Stage, DressingRoom, Address
Поля: name, address, capacity, __stages, __dressing_rooms, founded_year, is_active
Методы: add_stage, get_stages, add_dressing_room, get_dressing_rooms, set_founded_year

Stage 7 6 → Performance, Equipment
Поля: name, width, depth, height, __equipment, is_available, current_performance
Методы: add_equipment, get_equipment, set_availability, set_current_performance, calculate_area

DressingRoom 7 5 → Actor, MakeupArtist
Поля: number, capacity, __occupants, has_mirror, has_lighting, is_available
Методы: add_occupant, remove_occupant, get_occupants, set_availability, is_full

Wardrobe 7 5 → Costume
Поля: name, capacity, __costumes, temperature, humidity, is_climate_controlled
Методы: add_costume, remove_costume, get_costumes, set_temperature, set_humidity, is_full

Auditorium 7 5 → Seat, Section
Поля: name, capacity, __sections, has_balcony, has_orchestra, acoustics_rating
Методы: add_section, get_sections, set_has_balcony, set_acoustics_rating, calculate_occupancy

BoxOffice 7 6 → TicketSeller, Ticket, Sale
Поля: number, location, __sellers, daily_revenue, tickets_sold_today, is_open
Методы: add_seller, get_sellers, add_revenue, sell_ticket, open, close, reset_daily_stats

Address 6 4 → Theater, Venue
Поля: street, city, country, building_number, postal_code, district
Методы: set_building_number, set_postal_code, set_district, get_full_address

БИЛЕТЫ (TICKETS) - 5 классов:

Ticket 7 4 → Performance, Seat, Order
Поля: ticket_number, performance_name, price, seat_number, purchase_date, is_sold, is_used, section
Методы: sell, use, set_section, is_valid

Order 7 6 → Ticket, Customer, Payment
Поля: order_number, customer_name, order_date, __tickets, total_amount, is_paid, is_cancelled
Методы: add_ticket, remove_ticket, get_tickets, set_total_amount, pay, cancel

Sale 7 3 → Ticket, TicketSeller, Payment
Поля: sale_number, ticket_number, amount, sale_date, seller_name, payment_method
Методы: complete_sale, set_payment_method, is_completed

Refund 7 3 → Ticket, Order
Поля: refund_number, ticket_number, amount, refund_date, reason, is_processed
Методы: process_refund, set_reason, is_valid

Seat 6 4 → Ticket, Auditorium
Поля: seat_number, row, section, is_occupied, price_multiplier, view_quality
Методы: occupy, release, set_price_multiplier, set_view_quality, calculate_price

КОСТЮМЫ (COSTUMES) - 3 класса:

Costume 7 5 → Actor, Performance, Wardrobe
Поля: name, size, material, __performances, condition, is_available, actor_name
Методы: add_performance, get_performances, set_condition, assign_to_actor, release

Decoration 7 5 → Performance, Stage
Поля: name, width, height, depth, __performances, material, is_portable, storage_location
Методы: add_performance, get_performances, set_material, calculate_volume, set_storage_location

CostumeRental 7 5 → Costume, Actor
Поля: costume_name, actor_name, start_date, end_date, rental_fee, is_returned, damage_fee
Методы: set_end_date, set_rental_fee, return_costume, add_damage_fee, calculate_total_fee

РЕКВИЗИТ (PROPS) - 2 класса:

Prop 7 5 → Performance, Storage
Поля: name, prop_type, weight, __performances, condition, is_available, storage_location
Методы: add_performance, get_performances, set_condition, set_storage_location, release

PropStorage 7 5 → Prop
Поля: name, capacity, __props, temperature, humidity, is_climate_controlled
Методы: add_prop, remove_prop, get_props, set_temperature, set_humidity, is_full

ФИНАНСЫ (FINANCE) - 7 классов:

Budget 7 5 → Expense, Revenue, Accountant
Поля: year, total_amount, __expenses, __revenues, allocated_amount, remaining_amount
Методы: add_expense, add_revenue, get_total_expenses, get_total_revenues, allocate, get_balance

Salary 7 5 → Employee, Accountant
Поля: employee_name, base_salary, payment_date, bonuses, deductions, is_paid, tax_rate
Методы: add_bonus, add_deduction, calculate_gross_salary, calculate_net_salary, pay, set_tax_rate

Expense 7 3 → Budget, Accountant
Поля: description, amount, expense_date, category, is_approved, approved_by
Методы: set_category, approve, is_valid

Revenue 7 3 → Budget, Accountant
Поля: description, amount, revenue_date, source, is_recorded, recorded_by
Методы: set_source, record, is_valid

Payment 7 4 → Invoice, Order, Accountant
Поля: payment_number, amount, payment_date, payment_method, is_completed, recipient
Методы: set_payment_method, set_recipient, complete, is_valid

Invoice 7 4 → Client, Payment, Accountant
Поля: invoice_number, amount, issue_date, due_date, is_paid, client_name
Методы: set_due_date, set_client_name, pay, is_overdue

Accountant 7 4 → Budget, Invoice, Payment
Поля: name, age, experience_years, salary, __managed_accounts, certification, is_available
Методы: add_account, get_accounts, set_certification, set_availability

РАСПИСАНИЕ (SCHEDULE) - 3 класса:

Schedule 7 5 → Performance, Event, Calendar
Поля: month, year, __events, __performances, is_published, last_updated
Методы: add_event, get_events, add_performance, get_performances, publish

Calendar 7 5 → Schedule, Holiday
Поля: year, __holidays, __special_dates, season_start, season_end
Методы: add_holiday, get_holidays, add_special_date, get_special_dates, set_season

Session 7 5 → Performance, Venue, Director
Поля: performance_name, start_time, venue_name, end_time, tickets_sold, is_sold_out, director_name
Методы: set_end_time, sell_ticket, check_sold_out, set_director_name, get_duration_minutes

ИСКЛЮЧЕНИЯ (EXCEPTIONS) - 12 классов:

TheaterException 1 1 → Базовое исключение
Поля: message
Методы: __init__

InsufficientFundsException 0 0 → Наследуется от TheaterException

InvalidActorDataException 0 0 → Наследуется от TheaterException

PerformanceNotFoundException 0 0 → Наследуется от TheaterException

InvalidPerformanceDataException 0 0 → Наследуется от TheaterException

InvalidTicketDataException 0 0 → Наследуется от TheaterException

TicketSoldOutException 0 0 → Наследуется от TheaterException

VenueOverloadException 0 0 → Наследуется от TheaterException

ActorNotAvailableException 0 0 → Наследуется от TheaterException

DirectorNotAvailableException 0 0 → Наследуется от TheaterException

InvalidLicenseException 0 0 → Наследуется от TheaterException

InvalidScheduleException 0 0 → Наследуется от TheaterException

АССОЦИАЦИИ (30 примеров):

1. Actor → Performance (join_performance)
2. Actor → Costume (get_costume)
3. Actor → Rehearsal (attend_rehearsal)
4. Actor → Salary (receive_salary)
5. Performance → Actor (assign_actor)
6. Performance → Director (assign_director)
7. Performance → Stage (assign_stage)
8. Performance → Costume (add_costume)
9. Performance → Ticket (create_ticket)
10. Director → Performance (direct_performance)
11. Director → Rehearsal (conduct_rehearsal)
12. Director → Session (manage_session)
13. Costume → Actor (assign_to_actor)
14. Costume → Performance (add_performance)
15. Ticket → Performance (performance_name)
16. Ticket → Seat (seat_number)
17. Order → Ticket (add_ticket)
18. Order → Customer (customer_name)
19. Sale → Ticket (ticket_number)
20. Sale → TicketSeller (seller_name)
21. Budget → Expense (add_expense)
22. Budget → Revenue (add_revenue)
23. Salary → Employee (employee_name)
24. Invoice → Client (client_name)
25. Payment → Invoice (payment_number)
26. Rehearsal → Performance (performance_name)
27. Rehearsal → Actor (add_participant)
28. Show → Performance (performance_name)
29. Show → Venue (venue_name)
30. Theater → Stage (add_stage)

ИТОГО:
Классы: 50
Поля: 275
Методы: 259
Ассоциации: 30
Исключения: 12

