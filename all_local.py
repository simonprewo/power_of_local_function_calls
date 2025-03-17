import time

def read_file_line_by_line(filename):
    """Liest eine Datei zeilenweise und gibt die Gesamtanzahl der Wörter zurück."""
    total_words = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            total_words += count_words(line)
    return total_words


def count_words(line):
    """Zählt die Anzahl der Wörter in einer Zeile."""
    return len(line.split())

# Startzeit erfassen
start_time = time.time()

# Beispielaufruf
filename = "test.txt"
word_count = read_file_line_by_line(filename)

# Endzeit erfassen
end_time = time.time()

# Ergebnis ausgeben
print(f"Anzahl der Wörter: {word_count}")
print(f"Ausführungsdauer: {end_time - start_time:.6f} Sekunden")