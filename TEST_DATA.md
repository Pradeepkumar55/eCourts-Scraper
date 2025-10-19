# 📝 Test Data - eCourts Listing Checker

Complete list of sample data you can use to test the web interface and CLI.

---

## 🎯 Quick Copy-Paste Data

### Test Case 1: Search by CNR (Most Common)

```
CNR:        ABCD1234567890123
Court ID:   101
When:       Today
State:      Andhra Pradesh
District:   Kadapa
```

**Expected Result:** ✅ Case Found - CIV 123/2024, Serial No: 15

---

### Test Case 2: Search by Case Number

```
Case Type:  CIV
Number:     123
Year:       2024
Court ID:   101
When:       Today
```

**Expected Result:** ✅ Same case as Test 1

---

### Test Case 3: Criminal Case

```
CNR:        WXYZ9876543210987
Court ID:   101
When:       Today
```

**Expected Result:** ✅ Case Found - CRLP 456/2023, Serial No: 22

---

### Test Case 4: High Court Case

```
CNR:        HCAP1111222233334
Court ID:   102
When:       Today
```

**Expected Result:** ✅ Case Found - WP 1001/2024, Serial No: 5

---

### Test Case 5: View Full Cause List

```
Court ID:   101
When:       Today
State:      Andhra Pradesh
District:   Kadapa
```

**Expected Result:** ✅ 3 cases displayed in table

---

### Test Case 6: Case Not Found

```
CNR:        NOTFOUND123456789
Court ID:   101
When:       Today
```

**Expected Result:** ⚠️ Case not found message

---

## 📋 Complete Sample Database

### Court 101 - District Court, Kadapa

#### Case 1: Civil Dispute
```
CNR:           ABCD1234567890123
Case Number:   CIV 123/2024
Case Type:     Civil
Serial No:     15
Parties:       Ram Kumar vs Shyam Singh
Advocate:      Adv. Rajesh Sharma
Purpose:       Final Arguments
Status:        Listed Today
```

#### Case 2: Criminal Petition
```
CNR:           WXYZ9876543210987
Case Number:   CRLP 456/2023
Case Type:     Criminal
Serial No:     22
Parties:       State vs Mohan Lal
Advocate:      Adv. Priya Verma
Purpose:       Hearing
Status:        Listed Today
```

#### Case 3: Civil Suit
```
CNR:           PQRS5555666677778
Case Number:   CIV 789/2024
Case Type:     Civil
Serial No:     8
Parties:       Lakshmi Devi vs Municipal Corporation
Advocate:      Adv. Suresh Kumar
Purpose:       Evidence
Status:        Listed Today
```

---

### Court 102 - High Court, Andhra Pradesh

#### Case 1: Writ Petition
```
CNR:           HCAP1111222233334
Case Number:   WP 1001/2024
Case Type:     Writ Petition
Serial No:     5
Parties:       Vijay Enterprises vs State of AP
Advocate:      Sr. Adv. Ramesh Babu
Purpose:       Final Hearing
Status:        Listed Today
```

---

## 🔍 Search Combinations

### By CNR Only
| Field | Value |
|-------|-------|
| CNR | `ABCD1234567890123` |
| Court ID | `101` |
| When | `Today` |

### By Case Details Only
| Field | Value |
|-------|-------|
| Case Type | `CIV` |
| Number | `123` |
| Year | `2024` |
| Court ID | `101` |
| When | `Today` |

### With State & District
| Field | Value |
|-------|-------|
| CNR | `ABCD1234567890123` |
| Court ID | `101` |
| When | `Today` |
| State | `Andhra Pradesh` |
| District | `Kadapa` |

### Check Tomorrow
| Field | Value |
|-------|-------|
| CNR | `WXYZ9876543210987` |
| Court ID | `101` |
| When | `Tomorrow` |

### Check Both Days
| Field | Value |
|-------|-------|
| CNR | `PQRS5555666677778` |
| Court ID | `101` |
| When | `Both Today & Tomorrow` |

---

## 📊 All Valid CNRs (Copy-Paste Ready)

```
ABCD1234567890123
WXYZ9876543210987
PQRS5555666677778
HCAP1111222233334
```

---

## 🏛️ All Valid Court IDs

```
101  (District Court - Kadapa)
102  (High Court - Andhra Pradesh)
```

---

## 📝 Case Type Examples

```
CIV    (Civil)
CRLP   (Criminal Petition)
WP     (Writ Petition)
CS     (Civil Suit)
CRL    (Criminal)
MAC    (Motor Accident Claim)
```

---

## 🎯 Testing Scenarios

### Scenario 1: Happy Path - Case Found
1. Go to home page
2. Enter CNR: `ABCD1234567890123`
3. Enter Court ID: `101`
4. Select When: `Today`
5. Click Search
6. ✅ See case details with serial number 15

### Scenario 2: Alternative Search Method
1. Go to home page
2. Leave CNR blank
3. Enter Case Type: `CIV`
4. Enter Number: `123`
5. Enter Year: `2024`
6. Enter Court ID: `101`
7. Select When: `Today`
8. Click Search
9. ✅ See same case as Scenario 1

### Scenario 3: View Full Cause List
1. Click "Cause List" in navigation
2. Enter Court ID: `101`
3. Select When: `Today`
4. Click Get Cause List
5. ✅ See table with 3 cases

### Scenario 4: High Court Case
1. Go to home page
2. Enter CNR: `HCAP1111222233334`
3. Enter Court ID: `102`
4. Select When: `Today`
5. Click Search
6. ✅ See High Court case details

### Scenario 5: Case Not Found
1. Go to home page
2. Enter CNR: `INVALID123456789`
3. Enter Court ID: `101`
4. Select When: `Today`
5. Click Search
6. ⚠️ See "Case Not Found" message

### Scenario 6: Missing Required Field
1. Go to home page
2. Enter CNR: `ABCD1234567890123`
3. Leave Court ID blank
4. Click Search
5. ⚠️ See validation error

---

## 🌐 API Testing Data

### cURL Command 1: Search by CNR
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "cnr": "ABCD1234567890123",
    "when": "today",
    "court_id": "101"
  }'
```

### cURL Command 2: Search by Case Number
```bash
curl -X POST http://localhost:5000/api/search \
  -H "Content-Type: application/json" \
  -d '{
    "case_type": "CIV",
    "number": "123",
    "year": "2024",
    "when": "today",
    "court_id": "101"
  }'
```

### cURL Command 3: Health Check
```bash
curl http://localhost:5000/api/health
```

---

## 💻 CLI Testing Data

### Command 1: Search by CNR
```bash
python -m src.cli --cnr ABCD1234567890123 --when today --court-id 101 --offline
```

### Command 2: Search by Case Number
```bash
python -m src.cli --case-type CIV --number 123 --year 2024 --when today --court-id 101 --offline
```

### Command 3: Get Cause List
```bash
python -m src.cli --causelist --court-id 101 --when today --offline
```

### Command 4: Check Tomorrow
```bash
python -m src.cli --cnr WXYZ9876543210987 --when tomorrow --court-id 101 --offline
```

### Command 5: Check Both Days
```bash
python -m src.cli --cnr PQRS5555666677778 --when both --court-id 101 --offline
```

---

## 📱 Mobile Testing Tips

Test these on your phone/tablet:

1. **Portrait Mode:**
   - CNR: `ABCD1234567890123`
   - Court ID: `101`
   - When: `Today`

2. **Landscape Mode:**
   - View cause list for Court 101
   - Check table scrolls horizontally

3. **Touch Interactions:**
   - Tap form fields
   - Use dropdown menus
   - Click buttons

---

## 🎨 Visual Testing Checklist

- [ ] Search form displays correctly
- [ ] Sample cases card shows all CNRs
- [ ] Results page shows green success box
- [ ] Case details table is readable
- [ ] Serial number badge is visible
- [ ] Navigation links work
- [ ] Cause list table scrolls on mobile
- [ ] About page displays correctly
- [ ] Flash messages appear and disappear
- [ ] Buttons have hover effects

---

## 🔧 Edge Cases to Test

### Empty/Invalid Inputs
```
CNR:        (leave blank)
Court ID:   (leave blank)
Result:     Validation error
```

### Special Characters
```
CNR:        ABC@#$%123
Court ID:   101
Result:     Case not found
```

### Very Long Input
```
CNR:        ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890
Court ID:   101
Result:     Case not found
```

### Wrong Court ID
```
CNR:        ABCD1234567890123
Court ID:   999
Result:     Empty cause list
```

---

## 📊 Expected Results Summary

| Test | CNR | Court | Result |
|------|-----|-------|--------|
| 1 | `ABCD1234567890123` | 101 | ✅ Found (Serial 15) |
| 2 | `WXYZ9876543210987` | 101 | ✅ Found (Serial 22) |
| 3 | `PQRS5555666677778` | 101 | ✅ Found (Serial 8) |
| 4 | `HCAP1111222233334` | 102 | ✅ Found (Serial 5) |
| 5 | `INVALID123` | 101 | ⚠️ Not Found |
| 6 | (blank) | 101 | ❌ Validation Error |

---

## 🎯 Quick Test Checklist

Copy this for your testing session:

```
✅ Test 1: Search by CNR (ABCD1234567890123, Court 101)
✅ Test 2: Search by Case Number (CIV 123/2024, Court 101)
✅ Test 3: View Cause List (Court 101)
✅ Test 4: High Court Case (HCAP1111222233334, Court 102)
✅ Test 5: Case Not Found (INVALID123, Court 101)
✅ Test 6: Tomorrow's Listing (WXYZ9876543210987, Tomorrow)
✅ Test 7: Both Days (PQRS5555666677778, Both)
✅ Test 8: API Health Check
✅ Test 9: Mobile Responsive View
✅ Test 10: Navigation Between Pages
```

---

## 💡 Pro Tips

1. **Use Copy-Paste:** Copy CNRs directly from this file
2. **Test Systematically:** Go through each scenario
3. **Check Outputs:** Look in `outputs/` folder for saved results
4. **Try Mobile:** Test on different screen sizes
5. **Use Browser DevTools:** Check console for errors

---

**Happy Testing! 🎉**

All data above works in both the web interface and CLI!
