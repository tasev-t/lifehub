Changelog
Verze 0.1 - Datum
Založení projektu.

Vytvoření základní kostry aplikace.

Verze 0.2 - Datum
Přidání endpointu pro changelog.

Verze 0.3 - 07. dubna 2025
Přidání nové sekce do changelogu, která demonstruje dynamickou změnu.

Verze 0.4 - 08. dubna 2025
Přidáno
Nový endpoint /api/common/snapshot/ pro vrácení JSON struktury všech souborů v projektu.

Vytvořen pomocný nástroj generate_file_snapshot() ve common/views.py.

Přidání DRF view třídy SnapshotView pro správu snapshot endpointu.

common/urls.py rozšířen o cestu snapshot/.

Změněno
Hlavní urls.py aktualizován o cestu api/common/, která směruje na common.urls.

V settings.py přidána možnost SessionAuthentication vedle JWTAuthentication pro kompatibilitu s Django adminem.

Verze 0.5 - 09. dubna 2025
Přidáno
Dokumentace spolupráce a workflow:

Zaznamenány jsou podrobnosti o týmové spolupráci a koordinaci mezi vývojáři, což vedlo k rychlejšímu odstraňování chyb a implementaci nových funkcí.

Zavedení pravidelné aktualizace dokumentace a iterativního přístupu, který umožňuje neustálé vylepšování workflow.

Automatizace a CI/CD:

Integrace nástrojů pro automatizaci testování a generování snapshotů, které přispívají k transparentnosti vývoje a udržitelnosti projektu.

Optimalizace procesů:

Proces vývoje byl dále zefektivněn díky lepší komunikaci mezi členy týmu, což vedlo k zavedení podpůrných skriptů a helperů pro správu zdrojových kódů.

Změněno
Aktualizována struktura dokumentace vývoje – nyní obsahuje podrobnější přehled o vývojových fázích, řešených problémech a přijatých řešeních, což usnadňuje onboarding nových členů týmu a zajišťuje kontinuální zlepšování projektu.

