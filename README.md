# Ohjelmistotekniikka, harjoitustyö

Tämän harjoitustyön tarkoituksena on toteuttaa opintojen seurantajärjestelmä. Sovelluksen avulla käyttäjät voivat seurata suorittamiensa kurssien ja opintopisteiden määrää sekä seurata meneillään olevien kurssien määrää, tehtäviä ja deadlineja.

[Viikon 5 release](https://github.com/Mullil/ot-harjoitustyo/tree/viikko5)

[Viikon 6 release](https://github.com/Mullil/ot-harjoitustyo/tree/viikko6)

[Loppupalautus](https://github.com/Mullil/ot-harjoitustyo/tree/Loppupalautus)

## Käyttöohje

Asenna sovelluksen riippuvuudet komennolla:

```bash
poetry install
```

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Sovelluksen testaaminen

Testit voidaan suorittaa komennolla:

```bash
poetry run invoke start
```

Testikattavuusraportin voi tuottaa komennolla:

```bash
poetry run invoke coverage-report
```

## Pylint

Staattisen analyysin voi tehdä Pylintillä komennolla:

```bash
poetry run invoke lint
```

## Dokumentaatio

- [työaikakirjanpito](https://github.com/Mullil/ot-harjoitustyo/blob/main/dokumentaatio/tuntikirjanpito.md)

- [changelog](https://github.com/Mullil/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)

- [vaatimusmäärittely](https://github.com/Mullil/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

- [arkkitehtuuri.md](https://github.com/Mullil/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)
