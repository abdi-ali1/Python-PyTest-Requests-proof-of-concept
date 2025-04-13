
# 🧪 PyTest API Test Framework – Proof of Concept

Deze Proof of Concept is een lichtgewicht testframework in Python met:

- ✅ PyTest voor het draaien van tests
- ✅ Requests voor API calls
- ✅ pytest-html voor nette HTML-rapportage
- ✅ JSON-data voor data-driven testing
- ✅ GitHub Actions voor CI/CD support

---

## 📁 Projectstructuur

```bash
Pytest-POC/
├── tests/
│   └── test_api.py            # Bevat de API-tests
│
├── data/
│   └── endpoints.json         # JSON testdata (data-driven)
│
├── reports/
│   └── report.html            # HTML testrapport (gegenereerd)
│
├── .github/
│   └── workflows/
│       └── pytest-api.yml     # CI/CD workflow (GitHub Actions)
│
├── requirements.txt           # Dependencies voor pip
├── README.md                  # Uitleg over het project

```

---

## 🔧 Installatie

Zorg dat je Python 3.x hebt geïnstalleerd. Installeer dan de dependencies:

```bash
pip install -r requirements.txt
```

## 🚀 Test uitvoeren (lokaal)
Draai de tests en genereer een HTML-rapport:

```bash
pytest tests/ --html=reports/report.html --self-contained-html
```
📂 Open daarna reports/report.html in je browser.

## 📥 Data-driven testing
Testdata staat in data/endpoints.json. Voorbeeld:

```json
[
  {
    "endpoint": "https://jsonplaceholder.typicode.com/posts/1",
    "expected_user_id": 1
  }
]

```

Elke testiteratie valideert:

* ✅ Status code = 200
* ✅ Content-Type is JSON
* ✅ userId veld is correct


## 🧪 CI/CD met GitHub Actions
Deze workflow draait automatisch bij elke push of pull request naar main.

📄 .github/workflows/pytest-api.yml:
```yaml
name: 🔍 Run PyTest API Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt
      - run: pytest tests/ --html=reports/report.html --self-contained-html
      - uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: reports/report.html
```
👀 Na elke run kun je het rapport downloaden via Artifacts in GitHub Actions.


## 🧑‍💻 Auteur
Naam: Abdi Ali