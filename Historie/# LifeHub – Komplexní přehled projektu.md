# LifeHub – Komplexní přehled projektu

Tento dokument shrnuje dosavadní vývoj, současný stav, klíčové milníky, technické detaily a doporučení pro další kroky projektu **LifeHub – Osobní životní asistent**. Můžete jej sdílet s novými členy týmu či partnery, aby se rychle dostali do obrazu.

---

## 1. Úvod
**LifeHub** je modulární webová aplikace postavená na Django REST Framework s cílem poskytovat uživatelům jednotné prostředí pro správu různých oblastí života (uživatelé, strava, finance, domácí mazlíčci). Dokument slouží k:
- Přehledu dosavadní práce a rozhodnutí.
- Ucelení technického zázemí a endpointů.
- Navržení logického postupu dalšího vývoje.

---

## 2. Architektura a technologie

**Backend** (Django 5.1.6 + DRF)  
- **Modulární struktura**: 5 samostatných aplikací:
  - `users`: správa účtů a profilů (personal/family režimy).
  - `nutrition`: recepty, plánování jídel.
  - `finance`: evidence financí.
  - `pets`: správa domácích mazlíčků.
  - `common`: pomocné endpointy (changelog, snapshot).
- **Autentizace**: Kombinace `dj-rest-auth`/`django-allauth` + JWT (SimpleJWT).
- **Databáze**: SQLite (vývoj), doporučeno přejít na PostgreSQL v produkci.
- **Automatizace**: `.bat` skripty pro migrace a spuštění serveru; `snapshot_generator.py` pro archivaci kódu.

**Frontend** (v plánu)  
- **Technologie**: React + Material UI + Axios.
- **Layout**: hlavička, boční menu, dashboard („Zeď“).
- **Integrace**: JWT tokeny pro zabezpečené volání API.

---

## 3. Současný stav realizace

| Modul       | Stav                                     | Detail                                         |
|-------------|------------------------------------------|------------------------------------------------|
| **users**   | ✅ Hotovo (backend)                      | Registrovat, přihlásit, profil GET/PUT, JWT.   |
| **nutrition**| 🔶 Částečně (backend)                    | Model `Recipe` + GET `/recipes/`; chybí `Ingredient`, `MealPlan`. |
| **finance** | ⚪️ Skeleton                             | Prázdné `urlpatterns`, základní view.          |
| **pets**    | ⚪️ Skeleton                             | Prázdné `urlpatterns`, základní view.          |
| **common**  | ✅ Hotovo                               | `/common/changelog/`, `/common/snapshot/`.     |
| **frontend**| ⚠️ Nezahájeno                           | Projekt React dosud nevytvořen.                |

---

## 4. Klíčové milníky a časová osa

1. **Inicializace projektu** (duben 2025)
   - Vytvoření Django projektu, virtuálního prostředí.
2. **Modularizace**
   - Rozdělení do 5 aplikací, konfigurace URL.
3. **Autentizace**
   - Nasazení dj-rest-auth/allauth + SimpleJWT.
4. **Modul Strava – Recepty**
   - Implementace modelu `Recipe` a endpointu ListAPIView.
5. **Helper endpointy**
   - `changelog()` a `SnapshotView` v `common`.
6. **Automatizační nástroje**
   - `.bat` skripty a `snapshot_generator.py`.

---

## 5. Řešené problémy a přijatá řešení

| Problém                                                      | Řešení                                                                   |
|--------------------------------------------------------------|--------------------------------------------------------------------------|
| `django-admin` nebyl rozpoznán                               | Vytvoření a aktivace venv, `pip install django`.                         |
| Chybějící `urlpatterns` v apps `finance`/`pets`              | Přidání prázdných `urlpatterns = []` nebo základních routovacích vzorů.  |
| Kruhové importy                                              | Optimalizace a rozčlenění importů ve views.                              |
| Nekompatibilní migrace („no such table“, „inconsistent migrations“)| Odstranění DB + ručních migrací, nová migrace uživatele -> sites -> vše.|  
| .bat skripty nespouštěny ve správném adresáři                | Skripty kontrolují cestu, aktivují venv a spouštějí příkazy.             |
| Dynamické načtení changelogu                                 | View `changelog()` načte `CHANGELOG.md` a vrací JSON s časovou značkou.   |
| Generování snapshotu struktury                               | `generate_file_snapshot()` -> `SnapshotView` vrací seznam cest jako JSON. |

---

## 6. Zpřístupněné funkcionality

### API endpointy

| Cesta                             | Metoda  | Popis                                             |
|-----------------------------------|---------|---------------------------------------------------|
| `/api/users/register/`            | POST    | Registrace nového uživatele                       |
| `/api/users/profile/`             | GET     | Získání profilu                                   |
| `/api/users/profile/`             | PUT     | Aktualizace profilu (personal ↔ family)           |
| `/api/nutrition/recipes/`         | GET     | Výpis všech receptů                                |
| `/api/common/changelog/`          | GET     | Obsah `CHANGELOG.md` + aktuální datum/čas         |
| `/api/common/snapshot/`           | GET     | Seznam souborů projektu (relativní cesty)         |
| `/api/token/`                     | POST    | Získání JWT tokenů (access + refresh)              |
| `/api/token/refresh/`             | POST    | Obnovení access tokenu                            |

### Pomocné nástroje

- **`.bat` skripty**: Automatizace migrací a spuštění dev serveru.
- **`snapshot_generator.py`**: Generuje JSON s kontrolními součty a časy poslední úpravy pro vybrané soubory.

---

## 7. Doporučené další kroky

1. **Dokončení backendu**
   - Dokončit `nutrition`: modely `Ingredient`, `MealPlan` + CRUD.
   - Rozšířit `users` o sdílení dat v rámci rodiny.
2. **Frontend**
   - Inicializovat React + Material UI.
   - Implementovat přihlašování (JWT), výpis receptů, základní dashboard.
3. **Testování & CI/CD**
   - Jednotkové/integr. testy (pytest/django tests).
   - GitHub Actions pro lint, testy a snapshoty.
4. **Dokumentace & onboarding**
   - Udržovat `CHANGELOG.md`, `README.md` a tuto příručku.
   - Vytvořit krátkou příručku pro nové vývojáře.

---

## 8. Nejbližší akční plán

- **Dnes:** Ověřit JWT login + refresh (
POST `/api/token/`, POST `/api/token/refresh/`).
- **Týden:** Implementovat `Ingredient` a `MealPlan` + CRUD.
- **Měsíc:** Nasazení CI pipeline & základy frontendového dashboardu.

---

## 9. Kontakt & zapojení do spolupráce

- **Zdrojový kód:** Git repozitář (větve `main`, `develop`).
- **Dokumentace:** `docs/` s `README.md`, `CONTRIBUTING.md`.
- **Slack/Teams:** kanál #lifehub-dev.
- **Kde začít:** Pull request pro `Ingredient` model v `nutrition`, nebo ověření auth flow.

---

## 10. Závěr

Tímto dokumentem máte kompletní přehled o struktuře, dosavadní implementaci, technických výzvách a jasný plán pro další vývoj. Pro nové spolupracovníky je to okamžitý odrazový můstek k zapojení se do vývoje LifeHubu.

---

