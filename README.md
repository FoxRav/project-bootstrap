# Project Bootstrap

**Suomi** · [English](README.en.md)

Project Bootstrap on uudelleenkäytettävä projektipohja ihmisen ja AI-koodausagenttien yhteiseen ohjelmistokehitykseen.

Kun aloitat uuden projektin, kloonaat tämän repon tai kopioit sen lähdetiedostot ja täytät projektin omat tiedot.

Pohja sopii sekä ensimmäistä sovellustaan rakentavalle että kokeneelle tiimille. Se antaa yhteiset työskentelysäännöt, 15 tehtäväkohtaista skilliä sekä uudelleenkäytettävät työ- ja arviointipohjat. Se ei sido sovelluskehystä tai AI-palvelua.

Versio: [BOOTSTRAP_VERSION](BOOTSTRAP_VERSION)

## Mitä Project Bootstrap tekee

Project Bootstrap määrittää:

- kuka päättää mistä
- mitä agentti saa tehdä itsenäisesti
- milloin tarvitaan lupa
- miten työ rajataan
- miten projektin konteksti säilytetään
- miten määrittelyt ja arkkitehtuuripäätökset tehdään
- miten toteutus testataan
- miten työ arvioidaan riippumattomasti
- miten tietoturvaa tarkastetaan
- miten työ luovutetaan seuraavalle tekijälle tai agentille
- miten Git-operaatiot pidetään ihmisen hallinnassa

Ilman yhteistä toimintatapaa työ voi edetä näin:

kehotus → koodi → lisää koodia → konteksti katoaa → rakenne hajautuu → regressiot

Project Bootstrapin tavoite on:

idea → täsmennys → rajattu työ → toteutus → testit → arviointi → ihmisen päätösvalta

## Pika-aloitus

```text
git clone https://github.com/FoxRav/project-bootstrap.git my-project
cd my-project
```
````

1. Kloonaa tai kopioi pohja uuden projektin hakemistoon.
2. Noudata [alustusohjetta](docs/INITIALIZE.md), myös uuden Git-historian osalta.
3. Täytä [docs/PROJECT.md](docs/PROJECT.md): tavoite, käyttäjät, rajaus ja rajoitteet.
4. Kirjaa projektin oikeat tarkistus- ja testauskomennot [docs/TESTING.md](docs/TESTING.md)-tiedostoon.
5. Määritä käytettävät ihmiset, agentit, mallit ja työkalut [docs/RUNTIME.md](docs/RUNTIME.md)-tiedostoon.
6. Pyydä agenttia aloittamaan [AGENTS.md](AGENTS.md)-tiedostosta.
7. Valitse tehtävään sopiva [skill](skills/README.md). Älä lataa kaikkia skillejä kerralla.
8. Rajaa merkittävä työ [työpohjalla](templates/WORK_ITEM_TEMPLATE.md). Pieneen ja selvään muutokseen riittää lyhyt tehtävänkuvaus.

## Työnkulku ja päätösvalta

Tyypillinen työnkulku:

idea
→ täsmennys
→ tutkimus tai prototyyppi tarvittaessa
→ määrittely
→ arkkitehtuuri / ADR tarvittaessa
→ työpaketit
→ toteutus ja testit
→ riippumaton arviointi
→ Product Owner
→ ihmisen tekemä commit ja push

Tämä ei ole pakollinen vesiputousmalli. Pienet muutokset voivat ohittaa tarpeettomat vaiheet ja testaus kulkee toteutuksen mukana.

Product Owner tarkoittaa projektin päätöksentekijää. Se voi olla myös yksin työskentelevä kehittäjä.

Agentin oletetaan:

- tutkivan nykytilan ennen muokkausta
- käyttävän vain tehtävän kannalta tarpeellista kontekstia
- pysyvän annetussa rajauksessa
- säilyttävän voimassa olevat testit ja laatukriteerit
- pyytävän luvan merkittäviin arkkitehtuuri-, turvallisuus-, data- tai rajapintamuutoksiin
- jättävän commitit ja pushit oletusarvoisesti ihmiselle

Merkittävä työ arvioidaan riippumattomasti ennen hyväksyntää.

Tarkastus-ZIP on tarvittaessa tehtävä luovutuspaketti, ei normaali pakollinen työvaihe.

Tarkat rajat löytyvät [toimintaperiaatteista](PROJECT_BOOTSTRAP.md).

## Repon rakenne

| Sijainti                                                                       | Tarkoitus                                              |
| ------------------------------------------------------------------------------ | ------------------------------------------------------ |
| [AGENTS.md](AGENTS.md)                                                         | Agentin aloituspiste, navigointi ja päätösvallan rajat |
| [PROJECT_BOOTSTRAP.md](PROJECT_BOOTSTRAP.md)                                   | Yleiset toimintaperiaatteet                            |
| [docs/PROJECT.md](docs/PROJECT.md)                                             | Projektin omat tiedot ja tietokartta                   |
| [docs/INITIALIZE.md](docs/INITIALIZE.md)                                       | Projektin alustusohje                                  |
| [docs/RUNTIME.md](docs/RUNTIME.md)                                             | Ihmiset, agentit, mallit ja työkalut                   |
| [docs/TESTING.md](docs/TESTING.md)                                             | Projektin tarkistus- ja testauskomennot                |
| [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md)                                 | Skillien lähteet ja alkuperä                           |
| [skills/README.md](skills/README.md)                                           | Skillien valinta ja käyttö                             |
| [templates/WORK_ITEM_TEMPLATE.md](templates/WORK_ITEM_TEMPLATE.md)             | Työpaketin pohja                                       |
| [templates/ADR_TEMPLATE.md](templates/ADR_TEMPLATE.md)                         | Arkkitehtuuripäätöksen pohja                           |
| [templates/REVIEW_TEMPLATE.md](templates/REVIEW_TEMPLATE.md)                   | Arvioinnin pohja                                       |
| [templates/PROJECT_CONTEXT_TEMPLATE.md](templates/PROJECT_CONTEXT_TEMPLATE.md) | Projektikontekstin pohja                               |
| [scripts/bootstrap.py](scripts/bootstrap.py)                                   | Projektipohjan tarkistus ja valinnainen paketointi     |
| [tests/test_bootstrap.py](tests/test_bootstrap.py)                             | Bootstrap-työkalun regressiotestit                     |

## Skillit

Skill on uudelleenkäytettävä toimintaresepti tietynlaiseen tehtävään.

Project Bootstrap sisältää 15 yleiskäyttöistä skilliä:

`grill-with-docs` · `grill-me` · `domain-modeling` · `research` · `prototype` · `to-spec` ·
`architecture-review` · `to-tickets` · `implement` · `tdd` · `diagnose-bug` · `code-review` ·
`security-review` · `release-readiness` · `handoff`

Skillit eivät anna lupaa ohittaa projektin päätösvaltaa tai muita sääntöjä.

Skill voidaan lukea suoraan tiedostopolun kautta ilman erillistä asennusta. Runtime-kohtainen automaattinen skillien löytäminen määritellään tarvittaessa [runtime-ohjeessa](docs/RUNTIME.md#skill-discovery).

Projektikohtaiset skillit versioidaan projektin mukana.

Katso [skills/README.md](skills/README.md).

## Projektipohjan tarkistus

Aja repon juuresta Python 3.10+:lla:

```text
python scripts/bootstrap.py check
python -m unittest discover -s tests -v
```

Nämä komennot tarkistavat Project Bootstrap -pohjan. Varsinaisessa sovellusprojektissa määritä projektin omat tarkistukset [docs/TESTING.md](docs/TESTING.md)-tiedostoon.

Normaali työ ei vaadi ZIP-pakettia.

Katso [komennot ja valinnainen paketointi](docs/TESTING.md).

## Lisenssi

Tämä projekti on julkaistu [MIT-lisenssillä](LICENSE).

Skillien lähteet ja taustat: [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md).

---

**Suomi** · [English](README.en.md)
