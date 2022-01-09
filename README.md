# WSI uczenie ze wzmocnieniem

## Autor 

Konrad Wojewódzki 300286

## Polecenie

Elon Piżmo konstruuje autonomiczne samochody do swojego najnowszego biznesu. Dysponujemy planszą NxN (domyślnie N=8) reprezentującą pole do testów  jazdy. Na planszy jako przeszkody stoją jego bezpłatni stażyści  (reprezentują dziury o ujemnej punktacji). Mamy dwa autonomiczne  samochody: Random-car, który kierunek wybiera rzucając kością (błądzi  losowo po planszy) oraz Q-uber, który uczy się przechodzić ten labirynt  (używa naszego algorytmu). Samochody zaczynają w tym samym zadanym  punkcie planszy i wygrywają, jeśli dotrą do punktu końcowego, którym  jest inny punkt planszy. Istnieje co najmniej jedna ścieżka do startu do końca. Elon oszczędzał na module do liczenia pierwiastków, dlatego samochody poruszają się przy użyciu  metryki Manhattan (góra, dół, lewo, prawo). Jeżeli samochód natrafi na  stażystę to kończy bieg i przegrywa. Analogicznie jak wejdzie na punkt  końca to wygrywa i również nie kontynuuje dalej swojej trasy. Celem agenta jest minimalizacja pokonywanej trasy. 

## Omówienie oznaczeń i uruchomienie algorytmu

#### Omówienie

![](https://i.imgur.com/58CZBWP.png)

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

![](https://i.imgur.com/riXbY7W.png)


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

Średnia ilość prób potrzebna do znalezienia ścieżki: 

Średnia ilość odwiedzonych pól po drodze do celu: 



|                 | Średnia | Minimalna | Maksymalna |
| :-------------- | :------ | --------- | :--------- |
| Próby           | 1076,14 | 5         | 5642       |
| Odwiedzone pola | 16,5    | 9         | 45         |

Algorytm próbuje porusza się w losowym kierunku do momentu aż nie trafi na "ścianę" lub nie dojdzie do punktu końcowego. Dane są z godnie z oczekiwaniami bardzo losowe. Zdarza się, że wyniki są równie dobre jak w przypadku uczenia ze wzmocnieniem, jednak jest to rzadkie zjawisko i nie jest to metoda dająca dobre wyniki. 


##### Q learning

###### Nauka

Alpha - współczynnik uczenia

Gamma - wartość oceniająca jak istotne dla algorytmu są kary i nagrody

Nauka odbywa się podczas 1000 epizodów. Średnia jest określana na podstawie 100 uruchomień algorytmu.

| Alpha | Gamma | Średnia ilość kar | Minimalna ilość kar | Maksymalna ilość kar | Średnia ilość odwiedzonych pól |
| :---- | ----- | :---------------- | ------------------- | :------------------- | ------------------------------ |
| 0.1   | 0.6   | 282,58            | 247                 | 323                  | 13,096                         |
| 0.3   | 0.6   | 221,04            | 185                 | 268                  | 11,60787209                    |
| 0.3   | 0.3   | 234,32            | 205                 | 264                  | 12,06133                       |
| 0.2   | 0.2   | 271,22            | 232                 | 319                  | 13,3289                        |
| 0.2   | 0.95  | 238,14            | 203                 | 279                  | 11,65586                       |

Zmniejszanie zarówno parametru alpha i gamma powoduje zwiększenie ilości kar oraz średnią ilość odwiedzonych pól. Gdy gamma jest dużo wyższa algorytm znajduje optymalną ścieżkę szybciej co wynika z niższej średniej ilości kroków.

###### Rozwiązanie labiryntu

Po procesie nauki nie występują żadne odchylenia od normy. Każde ze 100 uruchomień znajduje drogę do celu w 9 krokach (licząc pole startowe) i nie wjeżdża w ściany. Dla wszystkich sprawdzonych parametrów wyniki są takie same. 1000 epizodów treningowych jest wystarczające do dobrego nauczenia algorytmu.

