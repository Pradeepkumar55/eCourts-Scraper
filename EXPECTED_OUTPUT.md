# Expected Output Guide - eCourts Listing Checker

## ✅ What You Should See When Searching

This guide shows you what the correct output looks like for each search.

---

## 🔍 Search Example 1: Civil Case

### Input:
```
CNR Number:     ABCD1234567890123
Court ID:       101
When to Check:  Today
```

### Expected Output:

```
✅ Case Found! Your case is listed on the following date(s):

📅 2025-10-19
Court: District Court - Kadapa
Serial No: 15

Case Details:
┌─────────────────┬──────────────────────────────────────┐
│ CNR             │ ABCD1234567890123                    │
│ Case Number     │ CIV 123/2024                         │
│ Case Type       │ Civil                                │
│ Parties         │ Ram Kumar vs Shyam Singh             │
│ Advocate        │ Adv. Rajesh Sharma                   │
│ Purpose         │ Final Arguments                      │
│ Document        │ 📄 View PDF                          │
└─────────────────┴──────────────────────────────────────┘
```

---

## 🔍 Search Example 2: Criminal Case

### Input:
```
CNR Number:     WXYZ9876543210987
Court ID:       101
When to Check:  Today
```

### Expected Output:

```
✅ Case Found! Your case is listed on the following date(s):

📅 2025-10-19
Court: District Court - Kadapa
Serial No: 22

Case Details:
┌─────────────────┬──────────────────────────────────────┐
│ CNR             │ WXYZ9876543210987                    │
│ Case Number     │ CRLP 456/2023                        │
│ Case Type       │ Criminal                             │
│ Parties         │ State vs Mohan Lal                   │
│ Advocate        │ Adv. Priya Verma                     │
│ Purpose         │ Hearing                              │
│ Document        │ 📄 View PDF                          │
└─────────────────┴──────────────────────────────────────┘
```

---

## 🔍 Search Example 3: High Court Case

### Input:
```
CNR Number:     HCAP1111222233334
Court ID:       102
When to Check:  Today
```

### Expected Output:

```
✅ Case Found! Your case is listed on the following date(s):

📅 2025-10-19
Court: High Court - Andhra Pradesh
Serial No: 5

Case Details:
┌─────────────────┬──────────────────────────────────────┐
│ CNR             │ HCAP1111222233334                    │
│ Case Number     │ WP 1001/2024                         │
│ Case Type       │ Writ Petition                        │
│ Parties         │ Vijay Enterprises vs State of AP     │
│ Advocate        │ Sr. Adv. Ramesh Babu                 │
│ Purpose         │ Final Hearing                        │
│ Document        │ 📄 View PDF                          │
└─────────────────┴──────────────────────────────────────┘
```

---

## 📋 Full Cause List Output

### Input:
```
Court ID:       101
When to Check:  Today
(Leave CNR blank)
```

### Expected Output:

```
📋 Cause List for Court 101
Date: 2025-10-19
Court: District Court - Kadapa

Total Cases: 3

┌────────┬──────────────────┬──────────────┬─────────────────────────────────┬──────────────────────┐
│ Serial │ Case Number      │ Case Type    │ Parties                         │ Purpose              │
├────────┼──────────────────┼──────────────┼─────────────────────────────────┼──────────────────────┤
│   8    │ CIV 789/2024     │ Civil        │ Lakshmi Devi vs Municipal Corp  │ Evidence             │
│  15    │ CIV 123/2024     │ Civil        │ Ram Kumar vs Shyam Singh        │ Final Arguments      │
│  22    │ CRLP 456/2023    │ Criminal     │ State vs Mohan Lal              │ Hearing              │
└────────┴──────────────────┴──────────────┴─────────────────────────────────┴──────────────────────┘
```

---

## ❌ Case Not Found Output

### Input:
```
CNR Number:     INVALID123456789
Court ID:       101
When to Check:  Today
```

### Expected Output:

```
⚠️ Case Not Found

Your case is not listed on the requested date(s). Please check:
• The CNR or case details are correct
• The court ID is correct
• Try checking for a different date
```

---

## 🎨 Web Interface Display

The web interface shows the same information but with:

### Visual Elements:
- ✅ **Green border** around found cases
- ✅ **Green badge** showing Serial Number
- ✅ **Formatted table** with all case details
- ✅ **Date header** with calendar icon
- ✅ **Court name** displayed prominently
- ✅ **Clickable PDF link** (if available)

### Layout:
```
┌─────────────────────────────────────────────────────────┐
│  📊 Search Results                                      │
├─────────────────────────────────────────────────────────┤
│  Query Details:                                         │
│  CNR: ABCD1234567890123  Court ID: 101  When: Today    │
├─────────────────────────────────────────────────────────┤
│  ✅ Case Found! Your case is listed on the following   │
│     date(s):                                            │
│                                                         │
│  ┌───────────────────────────────────────────────────┐ │
│  │ 📅 2025-10-19              Serial No: 15          │ │
│  │ Court: District Court - Kadapa                    │ │
│  │                                                   │ │
│  │ Case Details:                                     │ │
│  │ ┌─────────────────┬─────────────────────────────┐ │ │
│  │ │ CNR             │ ABCD1234567890123           │ │ │
│  │ │ Case Number     │ CIV 123/2024                │ │ │
│  │ │ Case Type       │ Civil                       │ │ │
│  │ │ Parties         │ Ram Kumar vs Shyam Singh    │ │ │
│  │ │ Advocate        │ Adv. Rajesh Sharma          │ │ │
│  │ │ Purpose         │ Final Arguments             │ │ │
│  │ │ Document        │ 📄 View PDF                 │ │ │
│  │ └─────────────────┴─────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────┘ │
│                                                         │
│  [🔍 New Search]  [📋 View Full Cause List]            │
└─────────────────────────────────────────────────────────┘
```

---

## 📱 Mobile Display

On mobile devices, the layout adapts:
- Single column layout
- Stacked information
- Touch-friendly buttons
- Responsive tables

---

## 🎯 Key Information Displayed

For each case found, you will see:

1. **Date** - When the case is listed (📅 2025-10-19)
2. **Court Name** - Which court (District Court - Kadapa)
3. **Serial Number** - Your position in the list (15)
4. **CNR** - Case Number Reference
5. **Case Number** - Official case number (CIV 123/2024)
6. **Case Type** - Type of case (Civil, Criminal, etc.)
7. **Parties** - Who is involved (Ram Kumar vs Shyam Singh)
8. **Advocate** - Lawyer name (Adv. Rajesh Sharma)
9. **Purpose** - Reason for hearing (Final Arguments)
10. **PDF Link** - Document download (if available)

---

## ✅ Verification Checklist

Your search is working correctly if you see:

- [ ] Green success message "✅ Case Found!"
- [ ] Date with calendar icon (📅)
- [ ] Serial number in green badge
- [ ] Court name displayed
- [ ] All case details in a table format
- [ ] Proper spacing between fields
- [ ] Buttons at the bottom (New Search, View Full Cause List)

---

## 🔧 If Display Looks Wrong

### Issue: Text is compressed or overlapping

**Solution:**
1. Refresh the browser (Ctrl + F5)
2. Clear browser cache
3. Try a different browser (Chrome, Firefox, Edge)
4. Check browser zoom level (should be 100%)

### Issue: No styling/colors

**Solution:**
1. Check if CSS is loading (view page source)
2. Restart the web server
3. Clear browser cache

### Issue: Data shows but formatting is off

**Solution:**
1. The data is correct! Just the display needs adjustment
2. Try viewing in full-screen mode
3. Check browser console for errors (F12)

---

## 📊 Sample Screenshots (Text Format)

### Good Output ✅
```
Clear spacing between fields
Readable font size
Proper alignment
Green success indicators
All information visible
```

### Bad Output ❌
```
Textallsquishedtogether
No spacing
Hard to read
Missing information
```

---

## 💡 Pro Tips

1. **Serial Number is Most Important** - This tells you your position in the court list
2. **Save the Results** - Take a screenshot or print the page
3. **Check Multiple Dates** - Use "Both Today & Tomorrow" option
4. **Verify Court ID** - Make sure you're checking the right court

---

## 📞 What to Do With Results

Once you see your case listed:

1. **Note the Serial Number** - You'll need this at court
2. **Check the Date** - Make sure you know when to appear
3. **Verify Court Name** - Confirm it's the right court
4. **Check Purpose** - Know why you're being called
5. **Contact Advocate** - Inform your lawyer if needed

---

## ✅ Your Current Output is CORRECT!

Based on your message, you're seeing:
```
CNR: ABCD1234567890123
Court ID: 101
When: Today
CIV 123/2024
Serial No: 15
Ram Kumar vs Shyam Singh
```

**This is exactly right!** ✅

All the information is displaying correctly:
- ✅ CNR Number shown
- ✅ Court ID shown
- ✅ Date shown (Today)
- ✅ Case Number shown (CIV 123/2024)
- ✅ Serial Number shown (15)
- ✅ Party names shown (Ram Kumar vs Shyam Singh)

The web interface adds nice formatting with colors, borders, and tables to make it easier to read, but the data itself is perfect!

---

**Need Help?** Check `TROUBLESHOOTING.md` for common issues.
