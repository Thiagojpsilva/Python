# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
print(locale.getlocale())

print(calendar.calendar(2024, w=2, l=1, c=3, m=3))

# print(calendar.month(2024, 1))

# Pegar qual dia da semana começou o mes, e ultimo dia do mes monthrange:

# fev_primeiro_dia, fev_ultimo_ida = calendar.monthrange(2024, 2)
# print(calendar.day_name[fev_primeiro_dia])
# print(calendar.day_name[calendar.weekday(2022, 12, fev_ultimo_ida)])

# pegar nome do dias da semana:
# print(list(enumerate(calendar.day_name)))

# retorna o mes mostrando os  dias do mes em cada semana.
# print(calendar.monthcalendar(2024, 2))

# for week in calendar.monthcalendar(2024, 2):
#     for day in week:
#         if day == 0:
#             continue
#         print(day)


# Apresentar o mes corrente e o dia atual destacado.
# import calendar
# from datetime import datetime
# def display_calendar(year, month):
#     # Get the current day
#     current_day = datetime.now().day

#     # Generate the calendar for the specified year and month
#     cal = calendar.monthcalendar(year, month)

#     # Iterate through the calendar and mark the current day
#     for week in cal:
#         for i, day in enumerate(week):
#             if day != 0:
#                 if day == current_day:
#                     week[i] = f"[{day:2d}]"
#                 else:
#                     week[i] = f" {day:2d}"

#     # Display the modified calendar
#     print(calendar.month_name[month], year)
#     print("Mo Tu We Th Fr Sa Su")
#     for week in cal:
#         print(" ".join(map(str, week)))


# # Specify the year and month you want to display
# year_to_display = 2024
# month_to_display = 1  # January

# # Display the calendar with the current day marked
# display_calendar(year_to_display, month_to_display)
