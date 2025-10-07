import csv
def carica_da_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf8') as file:
            file.readline()
            lista = list()

            for line in file:
                parti = line.strip().split(',')
                lista.append(parti)

            return lista
    except FileNotFoundError:
        print('il tuo file non esiste')
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):

    for f in biblioteca:
        titolo_libro = f[0]
        if titolo == titolo_libro:
            return None

    nuovo_libro = [titolo, autore, anno, pagine, sezione]
    biblioteca.append(nuovo_libro)
    try:
        with open(file_path, 'a', encoding='utf8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(nuovo_libro)

            return nuovo_libro
    except OSError:
        print('il tuo file non esiste')
        return None

def cerca_libro(biblioteca, titolo):
    for f in biblioteca:
        titolo_libro = f[0]
        if titolo == titolo_libro:
            return f'{f[0]}, {f[1]}, {f[2]}, {f[3]}, {f[4]}'
    return None

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    libri_sezione = []
    for libro in biblioteca:
        if int(libro[4]) == sezione:
            libri_sezione.append(libro[0])

    if len(libri_sezione) == 0:
        return None

    libri_sezione.sort()
    return libri_sezione

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo: {libro[0]} {libro[1]} {libro[2]}")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato:", risultato)
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")

if __name__ == "__main__":
    main()
