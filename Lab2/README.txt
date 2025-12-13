Accountant 6 5 -> Budget, Expense, Revenue, Salary
Actor 7 9 -> Performance, Costume, Rehearsal, Salary
Address 5 4 -> Theater
Administrator 6 5 -> StationNetwork, StationManager, Meteorologist
Audience 6 4 ->
Auditorium 5 5 -> Theater, Performance
BoxOffice 5 7 -> Ticket, Sale
Budget 4 6 -> Expense, Revenue
Calendar 1 5 -> Schedule
Choreographer 6 6 ->
Costume 5 5 -> Actor, Performance, CostumeRental
CostumeDesigner 5 5 -> Costume
CostumeRental 6 5 -> Costume, Actor
Decoration 7 5 -> Performance
Director 5 9 -> Performance, Rehearsal, Session
DressingRoom 5 5 -> Theater, Actor
Expense 5 3 -> Budget
Invoice 5 4 -> Payment
LightingTechnician 6 5 ->
MakeupArtist 6 5 ->
Manager 6 5 -> Budget, Expense, Revenue
Musician 6 5 ->
Order 6 6 -> Ticket, Payment
Payment 5 4 -> Invoice
Performance 8 11 -> Actor, Director, Stage, Ticket, Costume
Premiere 7 5 -> Performance
Producer 6 5 -> Performance, Budget
Prop 5 5 -> PropsMaster, Performance
PropStorage 5 6 -> Prop
PropsMaster 6 5 -> Prop
Refund 5 3 -> Ticket
Rehearsal 6 6 -> Performance, Actor, Director
Revenue 5 3 -> Budget
Review 6 4 -> Performance
Salary 5 6 -> Accountant
Sale 5 3 -> Ticket, Payment
Schedule 3 5 -> Performance
Seat 6 5 -> Ticket
SecurityGuard 7 5 ->
Session 6 5 -> Director, Rehearsal
SetDesigner 6 5 ->
Show 6 5 -> Performance
SoundEngineer 6 5 ->
Stage 6 5 -> Theater, Performance
StageManager 6 5 -> Performance, Rehearsal
Theater 5 5 -> Address, Auditorium, Stage, DressingRoom
Ticket 7 4 -> Performance, Seat, Order, Sale
TicketSeller 7 5 -> Ticket, Sale
Tour 5 7 -> Performance
Wardrobe 5 6 -> Costume, Actor

Exceptions(12):
ActorNotAvailableException 0 0 ->
DirectorNotAvailableException 0 0 ->
InsufficientFundsException 0 0 ->
InvalidActorDataException 0 0 ->
InvalidLicenseException 0 0 ->
InvalidPerformanceDataException 0 0 ->
InvalidScheduleException 0 0 ->
InvalidTicketDataException 0 0 ->
PerformanceNotFoundException 0 0 ->
TheaterException 1 0 ->
TicketSoldOutException 0 0 ->
VenueOverloadException 0 0 ->

Поля: 279
Поведения: 261
Исключения: 12