import requests
import time

def read_file_and_count(filename, url):
    """Liest die Datei zeilenweise und sendet jede Zeile an den Server."""
    total_words = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            response = requests.post(url, data=line)
            total_words += int(response.text)
    return total_words

# Startzeit erfassen
start_time = time.time()

# Datei analysieren
url = "http://127.0.0.1:5000/count_words"
filename = "test.txt"
word_count = read_file_and_count(filename, url)

# Endzeit erfassen
end_time = time.time()

# Ergebnis ausgeben
print(f"Anzahl der Wörter: {word_count}")
print(f"Ausführungsdauer: {end_time - start_time:.6f} Sekunden")
