# WSI uczenie ze wzmocnieniem

## Autor 

Konrad Wojewódzki 300286

## Polecenie

Elon Piżmo konstruuje autonomiczne samochody do swojego najnowszego biznesu. Dysponujemy planszą NxN (domyślnie N=8) reprezentującą pole do testów  jazdy. Na planszy jako przeszkody stoją jego bezpłatni stażyści  (reprezentują dziury o ujemnej punktacji). Mamy dwa autonomiczne  samochody: Random-car, który kierunek wybiera rzucając kością (błądzi  losowo po planszy) oraz Q-uber, który uczy się przechodzić ten labirynt  (używa naszego algorytmu). Samochody zaczynają w tym samym zadanym  punkcie planszy i wygrywają, jeśli dotrą do punktu końcowego, którym  jest inny punkt planszy. Istnieje co najmniej jedna ścieżka do startu do końca. Elon oszczędzał na module do liczenia pierwiastków, dlatego samochody poruszają się przy użyciu  metryki Manhattan (góra, dół, lewo, prawo). Jeżeli samochód natrafi na  stażystę to kończy bieg i przegrywa. Analogicznie jak wejdzie na punkt  końca to wygrywa i również nie kontynuuje dalej swojej trasy. Celem agenta jest minimalizacja pokonywanej trasy. 

## Omówienie oznaczeń i uruchomienie algorytmu

#### Omówienie

![labirynt](D:\programming\Python\reinforced-learning\graphics\labirynt.png)

<span style="color:red">Czerwony</span> - Zajęte pole, wjechanie na nie powoduje kolizję

<span style="color:green">Zielony</span> - Pole startowe

<span style="color:blue">Niebieski</span> - Pole końcowe, dotarcie na nie powoduje zakończenie algorytmu

<span style="color:black">Biały</span> - Wolne pole

Wyjechanie poza obszar również jest traktowane jako kolizja.

#### Uruchamianie

Algorytm jest uruchamiany przez komendę `python main.py "start" "finish" "load_maze"`

* start - pozycja startowa (Dla tego problemu zakres 0-63)
* finish - pozycja do której dążymy (Dla tego problemu zakres 0-63)
* load_maze - zmienna informująca czy program ma wczytać gotowy labirynt czy wygenerować nowy(0 oznacza wygenerowanie, a każda inna wartość wczytanie)

## Opis problemu i testy

#### Opis problemu

![labirynt_do_rozwiąznia](D:\programming\Python\reinforced-learning\graphics\labirynt_do_rozwiąznia.png)

Celem programu jest pokonanie powyższego labiryntu w jak najkrótszym czasie. W tym celu zostały użyte dwa algorytmy. Jeden porusza się losowo dopóki nie znajdzie ścieżki między punktami, gdy wjedzie na zabronione pole lub wyjedzie poza zakres algorytm resetuje się i próbuje znowu od punktu początkowego. Drugi algorytm wykorzystuje uczenie ze wzmocnieniem. Na początku przechodzi labirynt i zapamiętuje optymalną ścieżkę. Następnie przechodzi labirynt i zapisuje ścieżkę którą się poruszał.

#### Przyjęty system kar i nagród

##### Kary

* Wyjechanie za obszar = -10
* Wjechanie na pole zabronione = -10
* Ruch na pole dozwolone = -1 

##### Nagrody

* Dojechanie do celu = 10

#### Testy

##### Losowe poruszanie

Średnia ilość prób potrzebna do znalezienia ścieżki: 1076,14

Średnia ilość odwiedzonych pól po drodze do celu: 16,5

@TODO dodać wnioski

##### Q learning

###### Nauka

Średnia ilość kroków : 13,0961413 

Średnia ilość kar: 282,58

@TODO dopisać wszystko

###### Rozwiązanie labiryntu

Średnia liczba kroków: 9

Średnia liczba kar: 0