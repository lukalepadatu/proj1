# Formula: Fahrenheit = Celsius * 9 / 5 + 32

# input: temp_celsius
# output : temp_fahr

temp_celsius =float(input("Enter temperature in Celsius: "))
if type(temp_celsius) != int:
temp_celsius = int (temp_celsius)
temp_fahr = temp_celsius * 9 / 5 + 32 
print(f"Temperature in Fahrenheit: {tempfahr}")

# float contain int