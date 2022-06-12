segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
horas = segundos // 3600
dia = horas // 24
a = dia % 30
b = horas % 24
segundosRestantes = segundos % 3600
c = segundosRestantes // 60
d = segundosRestantes % 60
print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")
