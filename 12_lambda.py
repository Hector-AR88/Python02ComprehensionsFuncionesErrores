# Ejemplo de funcion
def increment(x):
    return x+1
result = increment(10)
print(result)

# Ejemplo de misma funcion version lambda
increment_v2 = lambda x : x+1
result = increment_v2(10)
print(result)

full_name = lambda name, last_name: f'Full name is {name.title()} {last_name.title()}'

text = full_name('hector', 'alpuche rodriguez')
print(text)