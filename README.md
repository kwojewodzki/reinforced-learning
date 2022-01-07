# WSI uczenie ze wzmocnieniem

## Autor 

Konrad Wojewódzki 300286

## Polecenie

Elon Piżmo konstruuje autonomiczne samochody do swojego najnowszego biznesu. Dysponujemy planszą NxN (domyślnie N=8) reprezentującą pole do testów  jazdy. Na planszy jako przeszkody stoją jego bezpłatni stażyści  (reprezentują dziury o ujemnej punktacji). Mamy dwa autonomiczne  samochody: Random-car, który kierunek wybiera rzucając kością (błądzi  losowo po planszy) oraz Q-uber, który uczy się przechodzić ten labirynt  (używa naszego algorytmu). Samochody zaczynają w tym samym zadanym  punkcie planszy i wygrywają, jeśli dotrą do punktu końcowego, którym  jest inny punkt planszy. Istnieje co najmniej jedna ścieżka do startu do końca. Elon oszczędzał na module do liczenia pierwiastków, dlatego samochody poruszają się przy użyciu  metryki Manhattan (góra, dół, lewo, prawo). Jeżeli samochód natrafi na  stażystę to kończy bieg i przegrywa. Analogicznie jak wejdzie na punkt  końca to wygrywa i również nie kontynuuje dalej swojej trasy. Celem  agenta jest minimalizacja pokonywanej trasy. 

## Omówienie oznaczeń i uruchomienie algorytmu

![labirynt](D:\programming\Python\reinforced-learning\graphics\labirynt.png)

<span style="color:red">Czerwony</span> - Zajęte pole, wjechanie na nie powoduje kolizję

<span style="color:green">Zielony</span> - Pole startowe

<span style="color:blue">Niebieski</span> - Pole końcowe, dotarcie na nie powoduje zakończenie algorytmu

<span style="color:black">Biały</span> - Wolne pole