# Kryptografia postkwantowa z wykorzystaniem izogenii na przykładzie protokołu CSIDH.


## Benek:

- Dosłownie malutki wstęp apropos komputerów kwantowych:
    
    - Dlaczego sa tak "niebezpieczne" dla aktualnych algorytmów szyfrowania

- podstawa matematyczna (dlaczego to dziala i jest odporne na algorytmy kwantowe)

- zalety izogenii w porownaniu z innymi postkwantowymi rozwiazaniami:
    
    - krzywe eliptyczne(postac montgomerego) - duzo rysunkow
    - ciala skonczone, homomorfizmy grup
    - supersingular isogeny


## Kamil:

- protokoly sike, csidh, sqIsign (ogolne przedstawienie) 
 
    - protokoly ustalania klucza szyfrujacego(diffie-hellmann)
    - protokol podpisu cyfrowego

- kleska protokolu sike, rowniez dotyczy to b-sidh oraz b-sike, wiec zostaje sqisign oraz csidh - czyli skupimy sie na csidh(commutative supersingular isogeny diffie hellmann)

    - sytem sike zostal zlamany w sierpniu 22 roku, uzyto do tego twierdzen z konca lat 90, na wydajnym komputerze da sie go zlamac w pare sekund (wersje z krotkim kluczem)

## Ktoś inny...

- (notebook jupyter z uproszczona implementacja protokolu csidh w pythonie) (raczej biblioteka sibc) (supersingular isogeny based cryptographic primitive) 

    - zaglebienie sie w sposob dzialania najbardziej obiecujacego protokolu wykorzystującego izogenie
    - (notebook bedzie zawieral funkcjonalnosci potrzebne do skonstruowania protokolu i bedzie umozliwial
   to wykonujacemu) moze
