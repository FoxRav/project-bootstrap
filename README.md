# Project Bootstrap

A reusable foundation for people and AI coding agents to build software together.

[Suomi](#suomi) · [English](#english) · [Repository map / Rakenne](#repository-map--rakenne)

Clone or copy it when starting a project, then fill in that project's own context.
You get shared working rules, 15 task recipes and reusable work/review templates.
For solo builders and teams; no application framework or AI subscription is required.
Version: [BOOTSTRAP_VERSION](BOOTSTRAP_VERSION).

## Suomi

Project Bootstrap on valmis projektipohja, joka antaa ihmiselle ja AI-koodausagenteille
yhteiset työskentelysäännöt. Kun aloitat uuden projektin, kloonaat tämän repon tai kopioit
sen lähdetiedostot ja täytät projektin omat tiedot.

Pohja sopii sekä ensimmäistä sovellustaan rakentavalle että kokeneelle tiimille.
Se kertoo, kuka päättää mistä, mitä agentti saa tehdä itsenäisesti, milloin tarvitaan
lupa, miten työ pilkotaan ja testataan sekä miten arvioidaan, onko työ valmis.
Skillit auttavat valitsemaan tehtävään sopivan toimintatavan. Projektin tiedot pysyvät
tiedostoissa seuraavaa työskentelykertaa varten.

Ilman yhteistä toimintatapaa työ voi edetä näin:
kehotus → koodi → lisää koodia → konteksti katoaa → rakenne hajautuu → regressiot.
Pohjan tavoite on: idea → täsmennys → rajattu työ → toteutus → testit → arviointi →
ihmisen päätösvalta.

### Pika-aloitus

```text
git clone https://github.com/FoxRav/project-bootstrap.git my-project
cd my-project
```

1. Kloonaa tai kopioi pohja uuden projektin hakemistoon. Noudata
   [alustusohjetta](docs/INITIALIZE.md), myös uuden Git-historian osalta.
2. Täytä [docs/PROJECT.md](docs/PROJECT.md): tavoite, käyttäjät, rajaus ja rajoitteet.
3. Kirjaa oman projektin oikeat testauskomennot [docs/TESTING.md](docs/TESTING.md)-tiedostoon.
4. Valitse käytettävät ihmiset ja työkalut [runtime-ohjeeseen](docs/RUNTIME.md).
5. Pyydä agenttia aloittamaan [AGENTS.md](AGENTS.md)-tiedostosta. Valitse tarvittava
   [skill](skills/README.md), älä lataa kaikkia kerralla.
6. Rajaa ensimmäinen työ [työpohjalla](templates/WORK_ITEM_TEMPLATE.md) ja aloita.
   Pieneen, selkeään muutokseen riittää lyhyt tehtävänkuvaus.

### Työn kulku ja päätösvalta

Idea → täsmennys → tutkimus/kokeilu tarvittaessa → määrittely → arkkitehtuuri/ADR
tarvittaessa → työpaketit → toteutus ja testit → riippumaton arviointi → Product Owner
→ ihmisen tekemä commit/push.

Tämä ei ole pakollinen vesiputousmalli. Pienet muutokset ohittavat tarpeettomat vaiheet;
testaus kulkee toteutuksen mukana. Product Owner tarkoittaa projektin päätöksentekijää
ja voi olla yksin työskentelevä kehittäjä. Agentti tutkii nykytilan ennen muokkausta,
käyttää vain tarpeellista kontekstia eikä laajenna tehtävää tai heikennä testejä salaa.
Merkittävä työ arvioidaan riippumattomasti. Commitit ja pushit tekee oletusarvoisesti
ihminen. Tarkastus-ZIP on tarvittaessa tehtävä luovutuspaketti, ei normaali työvaihe.
Tarkat rajat ovat [toimintaperiaatteissa](PROJECT_BOOTSTRAP.md).

Ohjeiden ja skillien varsinainen ylläpitokieli on englanti. Alla oleva yhteinen
rakennekartta kertoo, missä säännöt, projektin tiedot ja toimintareseptit sijaitsevat.

## English

Project Bootstrap is a reusable foundation for human + AI software development.
Clone or copy it at the beginning of a project and replace the project context with
your own goals, constraints and commands. It works for solo builders and teams, from
small utilities to larger services.

It gives coding agents a consistent operating model for authority, scope, project
knowledge, specifications, implementation, tests, review, evidence, security and
handoff. Skills provide focused task recipes; human approval remains explicit.
The repository supplies a working process, not an application stack.

### Quick Start

```text
git clone https://github.com/FoxRav/project-bootstrap.git my-project
cd my-project
```

1. Clone or copy the foundation into a new project directory. Follow
   [initialization](docs/INITIALIZE.md), including the new-project Git-history guidance.
2. Fill in [docs/PROJECT.md](docs/PROJECT.md): purpose, users, scope and constraints.
3. Put your project's real validation commands in [docs/TESTING.md](docs/TESTING.md).
4. Set your people and tools in the [runtime adapter](docs/RUNTIME.md).
5. Start the agent at [AGENTS.md](AGENTS.md); select only the relevant
   [skill](skills/README.md) and context.
6. Define the first bounded task with the [work template](templates/WORK_ITEM_TEMPLATE.md)
   and begin. A short task description is enough for a small, obvious change.

### Workflow and control

Idea → clarify/grill → research/prototype when needed → specification → architecture/ADR
when needed → work items → implementation and tests → independent review → Product Owner
→ manual commit/push.

This is not a mandatory waterfall. Skip unnecessary stages for small changes and test
throughout implementation. The Product Owner is the project's decision maker, which
may be the solo developer. Agents inspect before editing, load only relevant context,
stay within scope and preserve valid tests. Non-trivial work gets independent review.
Commits and pushes remain manual by default. Review ZIPs are optional handoff artifacts.
See the [canonical policy](PROJECT_BOOTSTRAP.md) for authority and approval boundaries.

## Repository map / Rakenne

| Location | Purpose / tarkoitus |
| --- | --- |
| [AGENTS.md](AGENTS.md) | Agent entry and navigation / agentin aloituspiste |
| [PROJECT_BOOTSTRAP.md](PROJECT_BOOTSTRAP.md) | Universal policy / yhteiset toimintaperiaatteet |
| [docs/PROJECT.md](docs/PROJECT.md) | Actual project facts and knowledge map / projektin omat tiedot |
| [docs/INITIALIZE.md](docs/INITIALIZE.md) | Setup; `docs/` also holds testing and runtime guidance / alustus ja käytännön ohjeet |
| [skills/README.md](skills/README.md) | Reusable task recipes / tehtäväkohtaiset toimintareseptit |
| [templates/WORK_ITEM_TEMPLATE.md](templates/WORK_ITEM_TEMPLATE.md) | Work, [ADR](templates/ADR_TEMPLATE.md) and [review](templates/REVIEW_TEMPLATE.md) forms / työ-, päätös- ja arviointipohjat |
| [scripts/bootstrap.py](scripts/bootstrap.py) | Canonical-template validation and optional packaging / pohjan tarkistustyökalu |
| [tests/test_bootstrap.py](tests/test_bootstrap.py) | Tool regression tests / työkalun regressiotestit |

### Skills / Skillit

A skill is a reusable procedure for one class of work. / Skill on toimintaresepti
tietynlaiseen tehtävään. [Choose by task / Valitse tehtävän mukaan](skills/README.md):

`grill-with-docs` · `grill-me` · `domain-modeling` · `research` · `prototype` · `to-spec` ·
`architecture-review` · `to-tickets` · `implement` · `tdd` · `diagnose-bug` · `code-review` ·
`security-review` · `release-readiness` · `handoff`.

Recipes do not grant approval. Explicit file-path loading works without installation;
native tool discovery needs its own [runtime adapter](docs/RUNTIME.md#skill-discovery).
Resepti ei anna lupaa ohittaa sääntöjä. Skillin voi lukea tiedostopolun kautta ilman asennusta.
Project-specific recipes belong with their project. / Projektin omat skillit versioidaan sen mukana.

## Validate the foundation / Tarkista pohja

From the repository root, with Python 3.10+ and its standard library:
aja repon juuresta Python 3.10+:lla, ilman lisäpaketteja:

```text
python scripts/bootstrap.py check
python -m unittest discover -s tests -v
```

These checks maintain this foundation; replace/adapt them when building your product.
Nämä tarkistavat projektipohjan. Määritä sovelluksellesi omat tarkistukset alustuksessa.
No ZIP is needed. / ZIP-pakettia ei tarvita.
[Commands and optional packaging / Komennot ja valinnainen paketointi](docs/TESTING.md).

## License / Lisenssi

PUBLICATION BLOCKER: LICENSE decision required. The Product Owner has not yet selected
a license. / Julkaisu odottaa Product Ownerin lisenssivalintaa. Lisenssiä ei ole vielä annettu.

Skill design provenance / Skillien lähteet: [docs/SKILL_SOURCES.md](docs/SKILL_SOURCES.md).
