# Wzorzec projektowy Memento

## Opis
Memento (Pamiątka) jest behawioralnym wzorcem projektowym, pozwalającym na zapisywanie stanu obiektu i przywracanie go w przyszłości. 
Najczęstszym przykładem zastosowania wzorca jest przycisk 'undo' i 'redo' w niemalże każdym programie desktopowym.

Wzorzec Pamiątka składa się z klas:

 * Originator z metodami zapisującymi i przeywracającymi stan objektu,
 * Snapshot zawierającej metody umożliwiające obiektowi odpowiednio zapisanie swojego stanu do pamiątki albo pobranie zapisanego stanu obiektu, dla którego została stworzona pamiątka,
 * Caretaker, która odpowiada za przechowywanie stworzonych pamiątek.

Jedną z wad Pamiątki jest to, że ich używanie może być kosztowne pod kątem wykorzystania pamięci, jeżeli zachowujemy długą historię zmian i zasobożerne objekty.

## Zastosowanie wzorca w projekcie
Opisywany wzorzec projektowy zaimplementowałem w niewielkim programie graficznym, wyświetlającym położenie gracza(kropki) na planszy 2D.
Sterowanie odbywa się przy pomocy strzałek na klawiaturze, zapisywanie położenia przez 's' i przywracanie 'r'. Można zapamiętać dowolną liczbę położeń

### Konfiguracja
##### Zainstaluj Pythona 3 i bibliotekę Pygame
```
# pip3 install pygame
```

##### Uruchomienie
```bash
# python3 main.py
```