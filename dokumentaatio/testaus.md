# Testausdokumentti

Ohjelmaa on testattu yksikkötestein unittest-kirjastolla ja manuaalisesti.

## Yksikkötestaus

Sovelluslogiikasta vastaavia luokkia CourseService, TaskService ja UserService testataan näitä vastaavilla testiluokilla. Nämä testit käyttävät testitietokantaa, joka tulee määritellä .env.test tiedostoon muuuttujalle DB.


## Testikattavuus

Sovelluksen testikattavuus on käyttöliittymää lukuunottamatta 74 %. Testaamatta jäi kokonaan TaskService-luokka.

## Järjestelmätestaus

Sovelluksen konfiguraatiota on testattu manuaalisesti siten, että start-invoke luo tietokannan, jos sitä ei ole olemassa, ja test-invoke luo testitietokannan, jos sitä ei ole olemassa. Repositorion juuressa oleviin .env ja .env.test tiedostoihin asettamalla DB muuttujan arvon saa määritettyä tietokantatiedoston nimen.

Kaikki määrittelydokumentissa mainitut toiminnallisuudet on käyty manuaalisesti läpi. Kirjautuessa ja rekisteröityessä virheelliset syötteet on käyty läpi, ja testattu, että tyhjää käyttäjänimeä lukuunottamatta nämä palauttavat järkevät virheilmoitukset. Lisäksi kurssille ei voi antaa opintopistemäärää, joka ei ole kokonaisluku.

## Sovellukseen jääneet laatuongelmat

Sovellus ei salasanaa ja opintopistemäärää lukuunottamatta estä tyhjien merkkijonojen syöttämistä esimerkiksi kurssin nimeksi tai käyttäjänimeksi. Lisäksi deadlineksi voi asettaa minkä tahansa merkkijonon.