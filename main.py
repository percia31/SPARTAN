import random, os, time

R = '\033[91m'; G = '\033[92m'; Y = '\033[93m'
C = '\033[96m'; M = '\033[95m'; END = '\033[0m'

# Algoritmo Luhn
def luhn(card):
    sum = 0
    alt = False
    for digit in reversed(card):
        if not digit.isdigit(): return False
        n = int(digit)
        if alt:
            n *= 2
            if n > 9:
                n -= 9
        sum += n
        alt = not alt
    return sum % 10 == 0

# Generar tarjeta aleatoria válida
def generar_tarjeta(bin_base):
    while True:
        tarjeta = bin_base
        while len(tarjeta) < 15:
            tarjeta += str(random.randint(0, 9))
        for i in range(10):
            temp = tarjeta + str(i)
            if luhn(temp):
                tarjeta = temp
                break
        mm = str(random.randint(1, 12)).zfill(2)
        yy = str(random.randint(24, 29))
        cvv = str(random.randint(100, 999))
        return f"{tarjeta}|{mm}/{yy}|{cvv}"

# Opción para extrapolación avanzada
def super_extrapolacion():
    print(f"\n{C}=== SUPER EXTRAPOLACIÓN LOBOJR 🐺 ==={END}")
    ultimos4 = input(f"{Y}[+] Ingresa los últimos 4 dígitos de una tarjeta real: {END}")
    bin1 = input(f"{Y}[+] Ingresa el BIN base 1 (16 dígitos reales): {END}")
    bin2 = input(f"{Y}[+] Ingresa el BIN base 2 (16 dígitos reales): {END}")

    if not (ultimos4.isdigit() and len(ultimos4) == 4 and bin1.isdigit() and bin2.isdigit()):
        print(f"{R}[!] Entrada inválida.{END}")
        return

    b1, b2 = bin1[:-4] + ultimos4, bin2[:-4] + ultimos4
    print(f"\n{G}[✓] Tarjetas extrapoladas:{END}")
    print(f"→ {b1}")
    print(f"→ {b2}")

    mid1 = bin1[6:8]
    mid2 = bin2[6:8]
    try:
        suma1 = sum([int(c) for c in mid1])
        suma2 = sum([int(c) for c in mid2])
        r1 = int((suma1 / 2) * 5)
        r2 = int((suma2 / 2) * 5)
        final = str(r1 + r2).zfill(2)
    except:
        print(f"{R}[!] Error en cálculo matemático.{END}")
        return

    super_bin1 = bin1[:8] + final + "xxxxxx"
    super_bin2 = bin2[:8] + final + "xxxxxx"

    print(f"\n{C}→ BIN extrapolado 1: {super_bin1}")
    print(f"→ BIN extrapolado 2: {super_bin2}{END}")

    if input(f"{Y}\n[?] ¿Deseas generar tarjetas con ese BIN? (s/n): {END}").lower() == 's':
        generar_desde_bin(super_bin1[:12])  # Usamos los primeros 12 numéricos

# Generar tarjetas desde BIN específico
def generar_desde_bin(bin_base):
    if 'x' in bin_base:
        print(f"{R}[!] El BIN debe ser numérico para generar tarjetas.{END}")
        return
    try:
        cantidad = int(input(f"{Y}[+] ¿Cuántas tarjetas generar? (1-5000): {END}"))
        if cantidad < 1 or cantidad > 5000:
            raise ValueError
    except:
        print(f"{R}[!] Cantidad inválida.{END}")
        return

    print(f"\n{C}[*] Generando tarjetas válidas...{END}\n")
    tarjetas = [generar_tarjeta(bin_base) for _ in range(cantidad)]
    for t in tarjetas:
        print(f"{G}[✓] {t} {END}")

    if input(f"\n{Y}[?] ¿Deseas guardar en .txt? (s/n): {END}").lower() == 's':
        with open("tarjetas_lobojr.txt", "w") as f:
            for t in tarjetas:
                f.write(t + "\n")
        print(f"{M}[✓] Guardado en tarjetas_lobojr.txt{END}")

# Menú principal
def main():
    while True:
        os.system("clear")
        print(f"{M}╔══════════════════════════════════════════╗")
        print(f"{M}║   {C}LOBOJR GENERADOR DE TARJETAS v3 🐺💳   {M}║")
        print(f"{M}╚══════════════════════════════════════════╝{END}")
        print(f"\n{Y}1. Generar tarjetas normales")
        print(f"2. Super Extrapolación")
        print(f"3. Salir{END}")

        opcion = input(f"{C}\n[?] Selecciona una opción: {END}")
        if opcion == '1':
            bin_base = input(f"{Y}[+] Ingresa el BIN (6-12 dígitos): {END}")
            if not bin_base.isdigit() or len(bin_base) < 6:
                print(f"{R}[!] BIN inválido.{END}")
                time.sleep(2)
                continue
            generar_desde_bin(bin_base)
            input(f"\n{C}[↩] Presiona ENTER para volver al menú...{END}")
        elif opcion == '2':
            super_extrapolacion()
            input(f"\n{C}[↩] Presiona ENTER para volver al menú...{END}")
        elif opcion == '3':
            print(f"{G}[✓] Hasta pronto, LOBOJR 🐺{END}")
            break
        else:
            print(f"{R}[!] Opción inválida.{END}")
            time.sleep(1)

if __name__ == "__main__":
    main()
