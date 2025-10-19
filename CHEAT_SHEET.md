# 📝 eCourts Listing Checker - CHEAT SHEET

## 🎯 COPY-PASTE READY DATA

### Test 1: Basic Search ✅
```
CNR:        ABCD1234567890123
Court ID:   101
When:       Today
```
**Result:** CIV 123/2024, Serial No: 15

---

### Test 2: By Case Number ✅
```
Case Type:  CIV
Number:     123
Year:       2024
Court ID:   101
When:       Today
```
**Result:** Same as Test 1

---

### Test 3: Criminal Case ✅
```
CNR:        WXYZ9876543210987
Court ID:   101
When:       Today
```
**Result:** CRLP 456/2023, Serial No: 22

---

### Test 4: High Court ✅
```
CNR:        HCAP1111222233334
Court ID:   102
When:       Today
```
**Result:** WP 1001/2024, Serial No: 5

---

### Test 5: Cause List ✅
```
Court ID:   101
When:       Today
```
**Result:** 3 cases in table

---

## 📋 ALL CNRs (One-Click Copy)

```
ABCD1234567890123
WXYZ9876543210987
PQRS5555666677778
HCAP1111222233334
```

---

## 🏛️ Court IDs

```
101  (District Court - 3 cases)
102  (High Court - 1 case)
```

---

## 🚀 Quick Start Commands

### Web Interface:
```bash
START_WEB.bat
```
Then open: http://localhost:5000

### CLI:
```bash
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
```

---

## 💡 Pro Tips

1. Click any value in SAMPLE_DATA.html to copy
2. Use FILL_FORM_GUIDE.txt for step-by-step
3. Check TEST_DATA.md for complete details
4. All data works in both web and CLI

---

**That's all you need! 🎉**
