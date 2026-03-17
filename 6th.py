def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temperatures = [0, 20, 37, 100]
for temp in temperatures:
    print(f"{temp}°C = {celsius_to_fahrenheit(temp):.1f}°F")
 
  