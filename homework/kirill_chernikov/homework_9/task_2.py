# map | filter

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22,
                23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]


def is_high(temperature):
    return temperature > 28


high_temperature = list(filter(is_high, temperatures))

print(max(high_temperature))
print(min(high_temperature))
print(sum(high_temperature) / len(high_temperature))

# практики ради захотелось как-то map использовать + лямбда функцию.
# иного применения map для этой задачи не нашел :)

high_temperature_map = map(lambda t: t if t > 28 else None, temperatures)
high_temperature_filter = list(
    filter(lambda t: t is not None,
           high_temperature_map)
)

print(max(high_temperature_filter))
print(min(high_temperature_filter))
print(sum(high_temperature_filter) / len(high_temperature_filter))
