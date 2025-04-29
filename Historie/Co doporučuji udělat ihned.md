Výborně! 🎯 Abychom mohli postupovat systematicky a efektivně, navrhuji následující konkrétní kroky, které budeme realizovat postupně:

## 🚀 **Akční plán na nejbližší období:**

### 1. 🟢 **Dokončení správy uživatelů (backend):**

- [ ] **Ověřit JWT workflow**:
  - [ ] Registrace uživatele
  - [ ] Přihlášení a získání tokenu (access, refresh)
  - [ ] Endpoint pro aktualizaci profilu

- [ ] **Implementovat rodinný profil**:
  - [ ] Přidat možnost přepnutí mezi osobním a rodinným režimem
  - [ ] Implementovat jednoduché sdílení obsahu/dat mezi členy rodiny

### 2. 🟢 **Rozšíření modulu Strava (backend):**

- [ ] **Přidání modelů a jejich endpointů**:
  - [ ] `Ingredient` – model a CRUD API
  - [ ] `MealPlan` – model, vazby na recepty a ingredience, CRUD API

- [ ] **Optional:** Generátor nákupních seznamů z jídelníčků (lze i později)

### 3. 🟢 **Zahájení práce na frontendové aplikaci (React + Material UI):**

- [ ] Vytvořit nový projekt React:
  - [ ] Instalace React, React Router, Axios, Material UI
  - [ ] Nastavení struktury souborů (modulární dle backendu)

- [ ] Implementovat autentizaci:
  - [ ] Přihlašovací formulář (JWT autentizace, ukládání tokenů)
  - [ ] Zabezpečení API requestů přes Axios

- [ ] Základní UI komponenty:
  - [ ] Hlavička s navigací, boční menu
  - [ ] Dashboard (zeď), zatím jen základní zobrazení (postupně doplňovat data)

- [ ] První propojení s backendem:
  - [ ] Výpis receptů ze stávajícího endpointu

### 4. 🟢 **Zavedení testů a CI/CD:**

- [ ] Základní jednotkové testy Django backendu
- [ ] Nastavení GitHub Actions pro automatizaci testování

### 5. 🟢 **Dokumentace a snapshoty:**

- [ ] Aktualizovat dokumentaci a changelog po každém větším kroku
- [ ] Automaticky generovat a uchovávat snapshoty projektu (již vytvořený skript)

---

## 🛠️ **Nejbližší kroky, které provedeme ihned:**

Abychom neztratili čas, pojďme rovnou začít s prvním bodem „**Dokončení správy uživatelů**“:

### ✅ **1. Ověření kompletního JWT workflow**

Už máš hotové:

- Registrace nového uživatele (`/api/users/register/`)
- Endpointy na profil (`/api/users/profile/`)

**👉 Akce, kterou potřebujeme nyní provést:**

1. Zkontroluj funkčnost registrace a přihlášení.
2. Ověř správnou manipulaci s JWT tokeny:
   - Získání nového access tokenu při přihlášení.
   - Refreshování tokenů.

### 📋 **Potřebné API endpointy:**

- Přihlášení a získání tokenu:
  ```http
  POST /api/token/
  {
    "username": "...",
    "password": "..."
  }
  ```
- Obnovení tokenu:
  ```http
  POST /api/token/refresh/
  {
    "refresh": "..."
  }
  ```

Pokud endpointy pro získávání a obnovování tokenů zatím nemáš implementované, dej mi vědět – připravím ti přesný postup, jak je rychle integrovat pomocí SimpleJWT.

---

## 🔎 **Co od tebe potřebuji nyní:**

- Potvrzení, zda máš aktuálně funkční endpointy pro získání a refreshování JWT tokenů.
- Pokud ne, připravím ti přesné instrukce, jak je přidat.

Jakmile budeme mít ověřeno toto workflow, můžeme okamžitě přejít na implementaci rodinného profilu a rozšiřování modulu Strava.

Potvrď mi prosím tento postup, nebo mi dej vědět, jestli mám cokoli upravit či doplnit. 🚀