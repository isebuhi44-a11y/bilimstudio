
def menyunu_goster():
    """Kalkulyatorun menyusunu ekrana çıxarır."""
    print("""
+======================================+
|          RIYAZI KALKULYATOR          |
+======================================+
|  1. Toplama                 (+)      |
|  2. Cixma                   (-)      |
|  3. Vurma                   (*)      |
|  4. Bolme                   (/)      |
|  5. Tam bolme               (//)     |
|  6. Qaliq                   (%)      |
|  7. Quvvet                  (**)     |
+======================================+
|  0. Proqramdan cixis                 |
+======================================+
""")


def eded_daxil_et(mesaj):
    """İstifadəçidən düzgün ədəd daxil edilməsini tələb edir."""
    while True:
        daxil_edilen = input(mesaj).strip().replace(",", ".")

        try:
            if not daxil_edilen:
                raise ValueError

            try:
                eded = int(daxil_edilen)
            except ValueError:
                eded = float(daxil_edilen)

            if isinstance(eded, float):
                if eded != eded or eded in (float("inf"), float("-inf")):
                    raise ValueError

            return eded

        except ValueError:
            print("Xeta: Zehmet olmasa duzgun eded daxil edin.")


def hesabla(a, emeliyyat, b):
    """Verilmiş riyazi əməliyyatı yerinə yetirir."""
    if emeliyyat == "+":
        return a + b
    elif emeliyyat == "-":
        return a - b
    elif emeliyyat == "*":
        return a * b
    elif emeliyyat == "/":
        return a / b
    elif emeliyyat == "//":
        return a // b
    elif emeliyyat == "%":
        return a % b
    elif emeliyyat == "**":
        return a ** b
    else:
        raise ValueError("Naməlum riyazi əməliyyat!")


def neticeni_goster(neticə):
    """Hesablamanın nəticəsini səliqəli şəkildə göstərir."""
    if isinstance(neticə, float):
        if neticə == neticə and neticə not in (
            float("inf"), float("-inf")
        ):
            if neticə.is_integer():
                print(f"Nəticə: {int(neticə)}")
                return

            print(f"Nəticə: {neticə:.10g}")
            return

    print(f"Nəticə: {neticə}")


def esas_proqram():
    """Kalkulyatorun əsas idarəetmə dövrü."""
    while True:
        menyunu_goster()
        secim = input("Emeliyyati secin (0-7): ").strip()

        if secim == "0":
            print("\nKalkulyatordan istifade etdiyiniz ucun tesekkurler!")
            print("Proqram dayandirildi.")
            break

        emeliyyatlar = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/",
            "5": "//",
            "6": "%",
            "7": "**"
        }

        if secim not in emeliyyatlar:
            print("Xeta: Yanlis secim! 0-7 arasinda secim edin.")
            continue

        a = eded_daxil_et("Birinci ededi daxil edin: ")
        b = eded_daxil_et("Ikinci ededi daxil edin: ")
        emeliyyat = emeliyyatlar[secim]

        try:
            netice = hesabla(a, emeliyyat, b)
            neticeni_goster(netice)

        except ZeroDivisionError:
            if emeliyyat in ("/", "//", "%"):
                print("Xeta: Sifira bolmek mumkun deyil!")
            else:
                print("Xeta: Sifir menfi quvvete yukseldile bilmez!")

        except OverflowError:
            print("Xeta: Hesablamanin neticesi cox boyukdur!")

        except (ValueError, TypeError):
            print("Xeta: Bu ededlerle emeliyyati yerine yetirmek olmur.")

        print("-" * 40)


if __name__ == "__main__":
    try:
        esas_proqram()
    except (KeyboardInterrupt, EOFError):
        print("\nProqram dayandirildi.")

def menyunu_goster():
    """Kalkulyatorun menyusunu ekrana çıxarır."""
    print("""
+======================================+
|          RIYAZI KALKULYATOR          |
+======================================+
|  1. Toplama                 (+)      |
|  2. Cixma                   (-)      |
|  3. Vurma                   (*)      |
|  4. Bolme                   (/)      |
|  5. Tam bolme               (//)     |
|  6. Qaliq                   (%)      |
|  7. Quvvet                  (**)     |
+======================================+
|  0. Proqramdan cixis                 |
+======================================+
""")


def eded_daxil_et(mesaj):
    """İstifadəçidən düzgün ədəd daxil edilməsini tələb edir."""
    while True:
        daxil_edilen = input(mesaj).strip().replace(",", ".")

        try:
            if not daxil_edilen:
                raise ValueError

            try:
                eded = int(daxil_edilen)
            except ValueError:
                eded = float(daxil_edilen)

            if isinstance(eded, float):
                if eded != eded or eded in (float("inf"), float("-inf")):
                    raise ValueError

            return eded

        except ValueError:
            print("Xeta: Zehmet olmasa duzgun eded daxil edin.")


def hesabla(a, emeliyyat, b):
    """Verilmiş riyazi əməliyyatı yerinə yetirir."""
    if emeliyyat == "+":
        return a + b
    elif emeliyyat == "-":
        return a - b
    elif emeliyyat == "*":
        return a * b
    elif emeliyyat == "/":
        return a / b
    elif emeliyyat == "//":
        return a // b
    elif emeliyyat == "%":
        return a % b
    elif emeliyyat == "**":
        return a ** b
    else:
        raise ValueError("Naməlum riyazi əməliyyat!")


def neticeni_goster(neticə):
    """Hesablamanın nəticəsini səliqəli şəkildə göstərir."""
    if isinstance(neticə, float):
        if neticə == neticə and neticə not in (
            float("inf"), float("-inf")
        ):
            if neticə.is_integer():
                print(f"Nəticə: {int(neticə)}")
                return

            print(f"Nəticə: {neticə:.10g}")
            return

    print(f"Nəticə: {neticə}")


def esas_proqram():
    """Kalkulyatorun əsas idarəetmə dövrü."""
    while True:
        menyunu_goster()
        secim = input("Emeliyyati secin (0-7): ").strip()

        if secim == "0":
            print("\nKalkulyatordan istifade etdiyiniz ucun tesekkurler!")
            print("Proqram dayandirildi.")
            break

        emeliyyatlar = {
            "1": "+",
            "2": "-",
            "3": "*",
            "4": "/",
            "5": "//",
            "6": "%",
            "7": "**"
        }

        if secim not in emeliyyatlar:
            print("Xeta: Yanlis secim! 0-7 arasinda secim edin.")
            continue

        a = eded_daxil_et("Birinci ededi daxil edin: ")
        b = eded_daxil_et("Ikinci ededi daxil edin: ")
        emeliyyat = emeliyyatlar[secim]

        try:
            netice = hesabla(a, emeliyyat, b)
            neticeni_goster(netice)

        except ZeroDivisionError:
            if emeliyyat in ("/", "//", "%"):
                print("Xeta: Sifira bolmek mumkun deyil!")
            else:
                print("Xeta: Sifir menfi quvvete yukseldile bilmez!")

        except OverflowError:
            print("Xeta: Hesablamanin neticesi cox boyukdur!")

        except (ValueError, TypeError):
            print("Xeta: Bu ededlerle emeliyyati yerine yetirmek olmur.")

        print("-" * 40)


if __name__ == "__main__":
    try:
        esas_proqram()
    except (KeyboardInterrupt, EOFError):
        print("\nProqram dayandirildi.")
