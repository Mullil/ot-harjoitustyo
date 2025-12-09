# Käyttöohje

Lataa projektin uusimman releasen lähdekoodi

## Sovelluksen käynnistäminen

Asenna sovelluksen riippuvuudet:

```bash
poetry install
```

Käynnistä sovellus:

```
poetry run invoke start
```

## Rekisteröityminen ja kirjautuminen

Sovellus käynnistyy näkymään, jossa käyttäjä voi valita kirjautumisen tai rekisteröitymisen. Rekisteröityminen onnistuu siirtymällä rekisteröitymisnäkymään ja kirjoittamalla käyttäjänimen ja salasanan sekä vahvistuksen salasanalle. Kirjautuminen onnistuu, jos käyttäjä on jo luotu, ja kirjautumissivulle annetaan syötteeksi käyttäjänimi ja tätä vastaava salasana.

## Kurssin luominen

Kirjautumisen tai rekisteröitymisen jälkeisessä näkymässä käyttäjä voi luoda kurssin painamalla add course -nappia, ja siirryttyään uuteen näkymään kirjoittamalla kurssille nimen ja opintopistemäärän. Kurssin luonnin yhteydessä kurssille voi myös lisätä tehtäviä, jotka tulee lisätä ennen kuin kurssi luodaan lopullisesti.

## Kurssin tarkastelu

Kirjautumisen jälkeisellä sivulla käyttäjän luomat kurssit listataan opintopisteineen, ja painamalla listattua kurssia voi käyttäjä siirtyä tarkastelemaan kurssin sisältöä, esim. lisättyjä tehtäviä.