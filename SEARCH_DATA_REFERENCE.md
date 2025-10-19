# Search Data Reference - eCourts Listing Checker

## 🔍 What Data to Search

This guide shows you exactly what values to enter when searching for cases.

---

## 📋 Quick Search Reference

### **Court 101 - District Court, Kadapa**

#### Case 1: Civil Case
```
CNR Number:     ABCD1234567890123
Court ID:       101
When to Check:  Today
State:          (Optional) Andhra Pradesh
District:       (Optional) Kadapa

Expected Result:
- Case No:      CIV 123/2024
- Serial No:    15
- Type:         Civil
- Parties:      Ram Kumar vs Shyam Singh
- Advocate:     Adv. Rajesh Sharma
- Purpose:      Final Arguments
```

#### Case 2: Criminal Case
```
CNR Number:     WXYZ9876543210987
Court ID:       101
When to Check:  Today
State:          (Optional) Andhra Pradesh
District:       (Optional) Kadapa

Expected Result:
- Case No:      CRLP 456/2023
- Serial No:    22
- Type:         Criminal
- Parties:      State vs Mohan Lal
- Advocate:     Adv. Priya Verma
- Purpose:      Hearing
```

#### Case 3: Another Civil Case
```
CNR Number:     PQRS5555666677778
Court ID:       101
When to Check:  Today
State:          (Optional) Andhra Pradesh
District:       (Optional) Kadapa

Expected Result:
- Case No:      CIV 789/2024
- Serial No:    8
- Type:         Civil
- Parties:      Lakshmi Devi vs Municipal Corporation
- Advocate:     Adv. Suresh Kumar
- Purpose:      Evidence
```

---

### **Court 102 - High Court, Andhra Pradesh**

#### Case 4: Writ Petition
```
CNR Number:     HCAP1111222233334
Court ID:       102
When to Check:  Today
State:          (Optional) Andhra Pradesh
District:       (Optional) Kadapa

Expected Result:
- Case No:      WP 1001/2024
- Serial No:    5
- Type:         Writ Petition
- Parties:      Vijay Enterprises vs State of AP
- Advocate:     Sr. Adv. Ramesh Babu
- Purpose:      Final Hearing
```

---

## 🎯 Alternative: Search by Case Details

Instead of CNR, you can search using Case Type, Number, and Year:

### Example 1: Search for CIV 123/2024
```
Case Type:      CIV
Case Number:    123
Year:           2024
Court ID:       101
When to Check:  Today
```

### Example 2: Search for CRLP 456/2023
```
Case Type:      CRLP
Case Number:    456
Year:           2023
Court ID:       101
When to Check:  Today
```

### Example 3: Search for WP 1001/2024
```
Case Type:      WP
Case Number:    1001
Year:           2024
Court ID:       102
When to Check:  Today
```

---

## 📅 When to Check Options

You can select:
- **Today** - Check today's cause list only
- **Tomorrow** - Check tomorrow's cause list only
- **Both Today & Tomorrow** - Check both dates

---

## 🏛️ Available Court IDs

| Court ID | Court Name | Cases Available |
|----------|------------|-----------------|
| 101 | District Court, Kadapa | 3 cases |
| 102 | High Court, Andhra Pradesh | 1 case |

---

## 📊 Complete Data Table

| CNR | Case No | Court ID | Type | Serial No | Parties | Advocate | Purpose |
|-----|---------|----------|------|-----------|---------|----------|---------|
| ABCD1234567890123 | CIV 123/2024 | 101 | Civil | 15 | Ram Kumar vs Shyam Singh | Adv. Rajesh Sharma | Final Arguments |
| WXYZ9876543210987 | CRLP 456/2023 | 101 | Criminal | 22 | State vs Mohan Lal | Adv. Priya Verma | Hearing |
| PQRS5555666677778 | CIV 789/2024 | 101 | Civil | 8 | Lakshmi Devi vs Municipal Corporation | Adv. Suresh Kumar | Evidence |
| HCAP1111222233334 | WP 1001/2024 | 102 | Writ Petition | 5 | Vijay Enterprises vs State of AP | Sr. Adv. Ramesh Babu | Final Hearing |

---

## 💡 Copy-Paste Ready Values

### For Quick Testing

**Test 1 - Basic Search:**
```
CNR: ABCD1234567890123
Court ID: 101
When: Today
```

**Test 2 - Criminal Case:**
```
CNR: WXYZ9876543210987
Court ID: 101
When: Today
```

**Test 3 - High Court:**
```
CNR: HCAP1111222233334
Court ID: 102
When: Today
```

**Test 4 - View Full Cause List:**
```
Court ID: 101
When: Today
(Leave CNR blank to see all cases)
```

---

## 🌐 Web Form Fields Explained

### Required Fields:
1. **CNR Number** OR **Case Type + Number + Year**
   - Choose one method, not both
   
2. **Court ID** (Required)
   - Must enter: 101 or 102

3. **When to Check** (Required)
   - Select from dropdown: Today, Tomorrow, or Both

### Optional Fields:
- **State**: Andhra Pradesh (pre-filled in mock data)
- **District**: Kadapa (pre-filled in mock data)

---

## 🎨 Interactive Data Browser

For the easiest experience, open **`SAMPLE_DATA.html`** in your browser:
- Click any value to copy it instantly
- No typing needed
- Color-coded for easy identification
- All test cases in one place

---

## 📝 Example Search Scenarios

### Scenario 1: "I want to check if my civil case is listed today"
```
1. Open web app: http://localhost:5000
2. Enter CNR: ABCD1234567890123
3. Enter Court ID: 101
4. Select When: Today
5. Click Search
6. Result: CIV 123/2024, Serial No: 15
```

### Scenario 2: "Show me all cases in District Court today"
```
1. Go to "Cause List" page
2. Enter Court ID: 101
3. Select When: Today
4. Click "Get Cause List"
5. Result: 3 cases displayed
```

### Scenario 3: "Check if case is listed today or tomorrow"
```
1. Enter CNR: WXYZ9876543210987
2. Enter Court ID: 101
3. Select When: Both Today & Tomorrow
4. Click Search
5. Result: Shows listings for both dates
```

---

## ⚠️ Important Notes

1. **CNR Format**: 
   - Must be exact: `ABCD1234567890123`
   - Case-sensitive in some systems
   - No spaces or special characters

2. **Court ID**:
   - Only 101 and 102 have data
   - Other IDs will return "No cases found"

3. **Date Availability**:
   - Mock data only available for Today and Tomorrow
   - Other dates will return empty results

4. **Case Type Codes**:
   - CIV = Civil
   - CRLP = Criminal Petition
   - WP = Writ Petition

---

## 🔗 Related Files

- **`SAMPLE_DATA.html`** - Interactive click-to-copy interface
- **`CHEAT_SHEET.md`** - Quick reference guide
- **`DATA_TABLE.txt`** - Formatted table view
- **`FILL_FORM_GUIDE.txt`** - Step-by-step form filling
- **`TEST_DATA.md`** - Complete test data documentation

---

## ✅ Quick Test Checklist

Try these searches to verify everything works:

- [ ] Search by CNR: ABCD1234567890123
- [ ] Search by Case Details: CIV 123/2024
- [ ] View full cause list for Court 101
- [ ] Check "Both Today & Tomorrow"
- [ ] Try High Court case: HCAP1111222233334
- [ ] Test with invalid CNR (should show "not found")

---

**Pro Tip**: Use `SAMPLE_DATA.html` for the fastest testing experience! Just click to copy any value. 🚀
