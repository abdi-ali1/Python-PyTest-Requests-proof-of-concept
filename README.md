# ⚙️ PyTest API Test Framework – Proof of Concept

Deze PoC toont een simpele en uitbreidbare testopzet in Python met:

- ✅ PyTest voor testuitvoering
- ✅ Requests voor API-calls
- ✅ PyTest-HTML voor rapportage
- ✅ JSON-data als input (data-driven)

---

## 🏗️ Structuur

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