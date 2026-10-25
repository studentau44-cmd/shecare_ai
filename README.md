# SheCare AI 🌸 (SurvivorCare AI)
### Secure, Offline-First Care & Safety Application with Nearby Help & Safe Shelters

> **Application Name:** SheCare AI / SurvivorCare AI  
> **Repository Subpath:** `/Shecare_AI/`  
> **Live Deployed Site:** `https://manahilx.github.io/Shecare_AI/`  
> **Target Audience:** Rape and sexual assault survivors, particularly women experiencing family abuse, domestic coercion, isolation, denial of medical care, or deprivation of sustenance.  
> **Tech Stack:** Offline-First HTML5 / CSS3 / Vanilla Modern JavaScript (ES2022) / Web Crypto API (PBKDF2 SHA-256) / PWA Service Worker / Python 3 Standard Library Backend (Zero External Dependencies) / Google Maps Platform & Leaflet/OpenStreetMap Fallback.

---

## 🌟 1. Feature Overview: Nearby Help & Safe Places

The **Nearby Help & Safe Places** feature enables survivors of rape, sexual assault, and gender-based violence to quickly and safely locate nearby medical facilities, emergency departments, women's shelters, crisis-support organizations, legal aid, and counseling services.

### Core Capabilities:
- **Filterable Service Categories:**
  - 🏥 **Hospitals & Emergency Departments:** 24/7 casualty care, obstetrics & gynecology, and acute injury management.
  - 🏡 **Women's Shelters & Safe Accommodation:** Verified government shelters (*Dar-ul-Aman*, *Sakhi One Stop Centres*) and accredited non-profit refuges.
  - ⚖️ **Survivor Support & SARC:** Specialized Sexual Assault Referral Centres, One-Stop Crisis Centres, and forensic medico-legal examination units.
  - 🧠 **Counselling & Mental Health:** Trauma-informed psychological first aid and non-judgmental crisis counseling.
  - 📜 **Legal Aid & NGOs:** Rights advocacy, police accompaniment, and court protection orders.
- **Dual-Engine Mapping Architecture:**
  - **Official Google Maps Platform Integration:** Utilizes Google Maps JavaScript API and Places API (New) when an API key is configured.
  - **Zero-API-Key Offline Fallback Mode:** When no Google API key is provided, the application runs seamlessly using **Leaflet + OpenStreetMap** interactive mapping alongside curated, non-stigmatizing Google Maps search links.
- **Strict Location Privacy & Consent:**
  - Browser geolocation is **100% OPTIONAL**.
  - A trauma-informed consent modal explains why location is requested before any prompt is displayed.
  - Survivors can choose manual city/area entry (e.g., *Lahore*, *Karachi*, *Islamabad*, *Delhi*, *Mumbai*, etc.) at any time.
  - Zero server telemetry: Coordinates remain strictly in device memory and can be cleared instantly with the **"Clear Location"** button.
  - Never automatically contacts police or transmits location to third parties.
- **Safe Shelters & Confidentiality Protections:**
  - Protects resident safety by keeping physical shelter addresses strictly confidential (*"Exact address confidential for resident safety. Contact 24/7 helpline for intake and secure transfer."*).
  - Clear separation between general hospital emergency care and verified specialist survivor shelters.
- **Emergency & Medical Guidance:**
  - Prominent emergency guidance banner indicating regional lifelines: **112** (India), **1099 / 1043 / 15** (Pakistan), **911** (US/Canada), **999** (UK).
  - Transparent telephone dialer notice: Explains that opening a dialer prepares a call on the device but does **not** automatically place or complete it.
- **Strict Exclusion:**
  - In strict compliance with guidelines, **no language translator or translation feature** is included.

---

## 🏗️ 2. Architecture & File Structure

```
SheCare AI/
├── index.html               # Responsive single-page application with self-contained styling,
│                            # mobile layout, Nearby Help views, and interactive modals
├── manifest.json            # PWA manifest (discreet name: "Daily Notes", theme: #C96F55)
├── sw.js                    # PWA Service Worker (v2.2 safe MIME caching & offline precache)
├── server.py                # Python 3 standard library server with security headers & APIs
├── run_app.bat              # One-click Windows runner (starts server and opens browser)
├── .gitignore               # Protects runtime sessions and personal data from git commits
├── README.md                # Comprehensive documentation, API setup, sources & verification
├── css/
│   └── styles.css           # Light-peach to dark-peach ombre theme, accessible contrast,
│                            # neutral camouflage overrides, and responsive mobile rules
├── js/
│   ├── app.js               # Application coordinator, view router, quick-exit handler,
│                            # water tracking (max 12), and modal management
│   ├── auth.js              # Client-side Web Crypto PBKDF2 hashing, dynamic password strength,
│                            # inactivity auto-lock, and truthful device recognition
│   ├── db.js                # Offline storage engine (LocalStorage abstraction, strict 12-glass
│                            # water clamping, purge & export, camouflage notes storage)
│   ├── mental_health.js     # Trauma-informed offline companion, 5-4-3-2-1 grounding, box breathing
│   ├── physical_health.js   # Symptom & injury logger, red flag warnings, sustenance guidance
│   ├── period_tracker.js    # Timezone-safe menstrual cycle tracking with boundary math
│   ├── pregnancy_sti.js     # 72-Hour HIV PEP live countdown, pregnancy test calculator,
│                            # and comprehensive STI educational knowledgebase
│   ├── sos.js               # Trusted contact management, SMS/tel dispatch, truthful status
│   ├── safety_plan.js       # Safety plan builder, go-bag checklist, verified directory
│   └── nearby_help.js       # Nearby Help & Safe Places engine (Google Maps + Leaflet fallback,
│                            # verified directory for Pakistan & India, Haversine distance math)
├── data/                    # Local server JSON storage (sessions, users, SOS gateway logs)
└── tests/
    └── test_suite.py        # Automated test suite (15 tests covering backend, crypto, water limits,
                             # cycle math, verified directory, camouflage, SVGs, and disclaimers)
```

---

## 🗺️ 3. Google Maps Platform Setup & API Configuration

SheCare AI supports Google Maps JavaScript API and Places API with rigorous client-side security restrictions.

### Step 1: Create a Google Cloud Project
1. Log in to the [Google Cloud Console](https://console.cloud.google.com/).
2. Click **Select a project** > **New Project** and name it `SheCare-AI-Maps`.
3. Link an active billing account (Google Cloud provides $200 free monthly credit for Maps Platform, covering tens of thousands of map loads).

### Step 2: Enable the Required APIs
Navigate to **APIs & Services** > **Library** and enable:
1. **Maps JavaScript API** (Required for interactive map rendering, custom markers, and InfoWindows).
2. **Places API (New)** / **Places API** (Required for nearby places searches).
3. **Geocoding API** (Optional: allows address-to-coordinate lookups).

### Step 3: Create and Restrict Your API Key
Browser keys are exposed in client-side network requests. **You MUST apply restrictions:**
1. Navigate to **APIs & Services** > **Credentials**.
2. Click **Create Credentials** > **API Key**.
3. Under **Application restrictions**, select **HTTP referrers (web sites)**.
4. Add the allowed website URLs:
   - `https://manahilx.github.io/*` (Your live GitHub Pages deployment)
   - `http://localhost:*` (Local development)
   - `http://127.0.0.1:*` (Local development)
5. Under **API restrictions**, select **Restrict key**, then check:
   - `Maps JavaScript API`
   - `Places API` (or `Places API (New)`)
6. Click **Save**.

### Step 4: Configure the Key in SheCare AI
1. In the app, navigate to **Nearby Help & Safe Places**.
2. Click **⚙️ Google Maps Key** in the top control bar.
3. Paste your restricted API key into the field.
4. Optionally check *"Save key in local browser storage on this device"* if using a private trusted computer, or leave unchecked for session-only storage.
5. Click **Save & Initialize Map**. The live Google Map will initialize immediately.

---

## 🔒 4. Zero-API-Key Offline Fallback Mode

If no Google Maps API key is configured or if network access is restricted:
- **Interactive OpenStreetMap Map:** The application automatically initializes an interactive map using **Leaflet.js** and OpenStreetMap tiles.
- **Full Verified Directory:** All verified specialist shelters, hospitals, SARCs, and NGOs are plotted as interactive markers with complete address, availability, and phone details.
- **Accurate Distance Calculation:** Distances are computed mathematically using the **Haversine formula** ($R = 6371\text{ km}$) without needing any cloud API.
- **Safe External Google Maps Links:** Every card includes clean, direct links to Google Maps:
  - *Directions:* `https://www.google.com/maps/dir/?api=1&destination=lat,lng`
  - *Clean Search:* Formatted with safe, non-stigmatizing terms (e.g. `hospital emergency room Lahore`) that protect survivor search history.

---

## 🇵🇰 5. Verified Resources: Pakistan & India Directories

Every directory record has been verified against official government portals and accredited civil society organizations (Verified: **October 2026**). Fictional shelters and manufactured phone numbers are strictly prohibited.

### 🇵🇰 Pakistan Directory Entries
| Facility Name | Category | City | Phone | Address & Verification Source |
|---|---|---|---|---|
| **Dar-ul-Aman Lahore** | Safe Shelters | Lahore | `1043` / `042-99201389` | *Confidential address for resident safety.* Punjab Social Welfare Dept / PCSW. |
| **Mayo Hospital ER & Medico-Legal** | Hospitals & ER | Lahore | `042-99211129` | Hospital Rd, Anarkali. 24/7 casualty & forensic exams. King Edward Medical Univ. |
| **Jinnah Hospital Trauma ER** | Hospitals & ER | Lahore | `042-99231400` | Faisal Town, Lahore. 24/7 trauma & PEP availability. Punjab Health Dept. |
| **Violence Against Women Centre (VAWC)** | Survivor SARC | Multan | `061-9330381` / `1043` | Mati Tal Rd, Multan. Unified police, forensic, legal & shelter center. PCSW. |
| **Nishtar Hospital Emergency** | Hospitals & ER | Multan | `061-9200238` | Nishtar Rd, Multan. 24/7 casualty & medico-legal services. Punjab Health Dept. |
| **Benazir Bhutto Hospital (BBH) ER** | Hospitals & ER | Rawalpindi | `051-9290301` | Murree Rd, Rawalpindi. 24/7 casualty & forensic exam. Rawalpindi Medical Univ. |
| **Dar-ul-Aman Rawalpindi** | Safe Shelters | Rawalpindi | `1043` / `051-9290145` | *Confidential address.* Punjab Social Welfare Dept. |
| **PIMS Hospital Emergency** | Hospitals & ER | Islamabad | `051-9261170` | Sector G-8/3, Islamabad. Federal apex hospital. Ministry of National Health Services. |
| **Shaheed Benazir Bhutto Crisis Centre** | Survivor SARC | Islamabad | `1099` / `051-9257471` | Sector H-8/1, Islamabad. Crisis shelter & legal aid. Ministry of Human Rights. |
| **Rozan Trauma Counseling NGO** | Counselling | Islamabad | `0800-22444` / `0304-111-1741` | Mon–Sat 10AM–6PM. Specialist trauma psychology. Rozan Registered NGO. |
| **Panah Shelter Home for Women** | Safe Shelters | Karachi | `021-35380963` | *Confidential address.* Panah Trust / Registered Charity (panah.org.pk). |
| **JPMC Emergency & Medico-Legal** | Hospitals & ER | Karachi | `021-99201300` | Rafiqui Sarwar Shaheed Rd. 24/7 female MLO officers on duty. Sindh Health Dept. |
| **Civil Hospital Karachi (Ruth Pfau)** | Hospitals & ER | Karachi | `021-99215740` | Mission Rd, Karachi. 24/7 casualty & forensic services. Dow Univ of Health Sciences. |
| **Lady Reading Hospital (LRH) ER** | Hospitals & ER | Peshawar | `091-9211430` | Soekarno Rd, Peshawar. Apex tertiary emergency trauma center. KP Health Dept. |

### 🇮🇳 India Directory Entries
| Facility Name | Category | City | Phone | Address & Verification Source |
|---|---|---|---|---|
| **Sakhi One Stop Centre (OSC) Central Delhi** | Survivor SARC | Delhi | `181` / `011-23317004` | 24/7 medical, legal, police & 5-day safe shelter. MWCD Sakhi Scheme. |
| **AIIMS New Delhi Emergency** | Hospitals & ER | Delhi | `011-26588500` | Sri Aurobindo Marg, Ansari Nagar. Apex emergency & forensic medicine. MOHFW. |
| **Safdarjung Hospital Crisis Unit** | Hospitals & ER | Delhi | `011-26165060` | Ring Road, New Delhi. Dedicated sexual assault crisis care. Central Govt Health Scheme. |
| **Jagori Women's Counseling Centre** | Counselling | Delhi | `011-26691219` | Malviya Nagar, New Delhi. Feminist trauma counseling & legal advocacy. Jagori NGO. |
| **Special Cell for Women & Children** | Survivor SARC | Mumbai | `103` / `022-22620111` | Police HQ, Crawford Market. Social work crisis intervention. TISS & Mumbai Police. |
| **KEM Hospital Emergency** | Hospitals & ER | Mumbai | `022-24107000` | Parel, Mumbai. 24/7 emergency casualty & forensic exams. BMC Public Health Dept. |
| **Urja Trust Safe Shelter** | Safe Shelters | Mumbai | `022-24141108` | *Confidential address in Dadar.* Shelter for young women survivors. Urja Trust NGO. |
| **Sakhi One Stop Centre Bengaluru** | Survivor SARC | Bengaluru | `181` / `080-25591325` | Bowring Hospital Campus, Tasker Town. Integrated crisis care. Karnataka DWCD. |
| **Victoria Hospital Emergency** | Hospitals & ER | Bengaluru | `080-26701150` | Fort Road, Bengaluru. 24/7 casualty & forensic medico-legal center. BMCRI. |
| **Bharosa Support Centre** | Survivor SARC | Hyderabad | `100` / `040-27852355` | HACA Bhavan, Saifabad. Integrated medical, legal & shelter aid. Hyderabad Police. |

---

## 🔒 6. Location Privacy & Informed Consent Architecture

1. **Permission Required Before Geolocation:** Browser geolocation is never invoked on page load. Tapping **"📍 Near Me"** opens `#modalLocationConsent` with clear explanations.
2. **Zero Cloud Transmission:** Geographic coordinates are processed entirely inside the survivor's browser. They are never sent to external logging servers or third parties.
3. **No Automatic Reporting:** SheCare AI strictly refrains from automatically reporting incidents or contacting police or relatives.
4. **Instant Location Purge:** Clicking **"Clear Location"** immediately zeroes coordinates in memory and returns the map to manual area mode.
5. **Non-Stigmatizing External Queries:** External search URLs use safe, neutral query terms (`hospital emergency room [city]`) to prevent sexual violence queries from appearing in Google search history or ISP router logs.

---

## 🧪 7. Automated Test Suite Results

The automated test suite in `tests/test_suite.py` verifies all requirements:
```bash
python tests/test_suite.py
```

### Test Results:
```
...............
----------------------------------------------------------------------
Ran 15 tests in 0.131s

OK
```

### Verified Test Cases:
1. `test_pbkdf2_sha256_cryptographic_security`: 100,000-iteration PBKDF2 hashing equivalence.
2. `test_water_tracker_strict_limit_of_12`: Daily tracking limit of 12 glasses strictly enforced; decrement cannot go below 0.
3. `test_period_tracker_utc_date_math`: Leap year, month, and year boundary arithmetic without timezone drift.
4. `test_haversine_distance_calculation`: Haversine formula distance accuracy against real coordinates.
5. `test_verified_specialist_directory_integrity`: Authoritative Pakistan & India shelters, hospitals, and SARCs present.
6. `test_shelter_address_confidentiality_protection`: Sensitive shelter addresses marked with confidential safety badges.
7. `test_location_privacy_and_consent_mechanics`: Geolocation optional, consent modal, and clear location functionality.
8. `test_non_stigmatizing_search_queries`: External Google search links sanitized against stigmatizing words.
9. `test_google_maps_platform_and_fallback_modes`: Key setup modal, HTTP referrer security instructions, and OpenStreetMap fallback.
10. `test_emergency_and_dialer_transparency`: Honest dialer notice and non-diagnostic disclaimers.
11. `test_camouflage_and_discreet_mode_for_nearby_places`: Quick Exit and Discreet Mode camouflage for nearby places.
12. `test_github_pages_static_paths_compatibility`: Relative paths for `/Shecare_AI/` subpath deployment.
13. `test_strict_exclusion_of_language_translator`: Zero translation dropdowns or translation libraries.
14. `test_svg_icon_dimensions`: SVGs strictly constrained to 24px width and height.
15. `test_server_endpoint_handlers`: Security headers (`nosniff`, `DENY`), health check, and SOS dispatch gateway.

---

## 🚀 8. Deployment on GitHub Pages

1. Push the repository files (`index.html`, `manifest.json`, `sw.js`, `README.md`, `css/styles.css`, `js/` folder) to your repository `manahilx/Shecare_AI`.
2. Go to your GitHub repository **Settings** > **Pages**.
3. Under **Build and deployment**, select **Deploy from a branch** > branch: `main` / `root`.
4. Your site is live at: `https://manahilx.github.io/Shecare_AI/`
5. On mobile, add SheCare AI to your Home Screen for full offline PWA access.
