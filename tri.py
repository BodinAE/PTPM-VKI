import math
import re
import logging
import sys

# Шаблон строки лога (аналог template в Serilog)
# Содержит: время, уровень (до 7 символов для выравнивания), имя логгера и сообщение
log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Базовая настройка корневого логгера
logging.basicConfig(
    level=logging.DEBUG, # Минимальный уровень логирования (аналог MinimumLevel.Debug)
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),          # Настройка логирования в консоль
        logging.FileHandler("logs/file_txt.log", encoding="utf-8") # Настройка логирования в файл
    ]
)

logging.info("Логгер успешно сконфигурирован")
logging.info("Приложение запущено")

def triForDraw(astr, bstr, cstr):
    inputs = [astr, bstr, cstr]
    pattern = re.compile(r'^[1-9](?:\.\d)?$')
    triType = "не треугольник"
    triCoord = [(-2, -2), (-2, -2), (-2, -2)]
    validInput = True
    for str in inputs:
        validInput *= bool(re.match(pattern, str))
    if validInput:
        a = float(astr)
        b = float(bstr)
        c = float(cstr)
        isTri = a < b + c
        isTri *= b < a + c
        isTri *= c < a + b
        if isTri:
            triTypeScore = (a == b) + (a == c) + (b == c)
            match triTypeScore:
                case 0:
                    triType = "Разносторонний"
                case 1:
                    triType = "Равнобедренный"
                case 2:
                    raise ArithmeticError
                    #IMPOSSIBLE!!!!!
                case 3:
                    triType = "Равносторонний"
            triCoord[0] = (0, 0)
            triCoord[1] = (int(a), 0)
            cx = int(((b**2) + (c**2) - (a**2))/(2 * c))
            cy = int(math.sqrt((b**2) - (cx**2)))
            triCoord[2] = (cx, cy)
        else:
            triCoord = [(-1, -1), (-1, -1), (-1, -1)]
    return triType, triCoord

print(triForDraw("1","1","2"))