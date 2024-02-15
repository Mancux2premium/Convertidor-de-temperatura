temperatura =int(input("Ingrese la temperatura en Celsius y el programa le mostrara su valor en diferentes escalas:"))


celcius = temperatura
fahrenheit = (temperatura*1.8) +32
kelvin = temperatura + 273.15
rankine = ((temperatura + 273.15 ) *9) / 5 

print("La temperatura en celcius es:",celcius,"(ºC)", "\n" "La temperatura en fahrenheit  es:", fahrenheit,"(ºF)" "\n" "La temperatura en Kelvin es:",kelvin,"(K)" "\n" "La temperatura en Rankine  es:", rankine*9,"(ºR)")