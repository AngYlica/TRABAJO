# Solicitar al usuario el valor del dólar en pesos mexicanos (MX)
valor_dolar_en_mx = float(input("Ingresa el valor del dólar: "))

# Solicitar al usuario la cantidad de pesos mexicanos a convertir
pesos_mx = float(input("Ingresa la cantidad de pesos mexicanos (MX) que deseas convertir: "))

# Calcular la conversión de pesos mexicanos a dólares
dolares_usd = pesos_mx / valor_dolar_en_mx

# Mostrar el resultado de la conversión
print(f"La conversión de {pesos_mx} pesos mexicanos (MX) a dólares (USD) es: {dolares_usd} USD")
