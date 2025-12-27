# Puerto Morelos Property Search

A simple tool to help find affordable properties in Puerto Morelos, Mexico - perfect for budget-conscious buyers looking to move to this beautiful Caribbean town.

## 🎯 Purpose

This project helps budget-conscious Americans (and others) find affordable real estate in Puerto Morelos, with a focus on:
- Properties under $100,000 USD
- Non-renovated or older properties (better value)
- Land lots for self-building
- Investment opportunities

## 📁 Files

- **`puerto-morelos-property-search.md`** - Comprehensive search results and findings
- **`property_searcher.py`** - Python tool for organizing and filtering properties
- **`puerto_morelos_results.md`** - Auto-generated search results (example output)

## 🚀 Quick Start

### View Current Results
```bash
cat puerto-morelos-property-search.md
```

### Run the Python Tool
```bash
python3 property_searcher.py
```

## 💰 What We Found

### Best Deal
**$27,000 USD** - Land lot on Ruta de los Cenotes
- 1,250 m² (50m x 25m)
- Titled and free of liens
- Raw land requiring construction

### Budget Breakdown
- **Under $50k:** Land only (starting at $27k)
- **$50k-$100k:** Land with services, possible older structures
- **$100k-$200k:** Condos, small houses

## 🔍 Search Sources

We searched across multiple real estate platforms:
- Properstar (1,050+ cheap properties listed)
- ForSalePuertoMorelos.com
- MyCasa.mx
- RivieraMayaCozy.com
- RunAwayRealty.com
- BlueCaribbeanProperties.com
- TopMexicoRealEstate.com

## 📊 Market Overview

- **Total cheap properties:** 1,050+ listings
- **Cheap houses:** 147 listings
- **Land lots:** 278 listings
- **Apartments/houses:** 1,280+ combined

## 💡 Tips for Budget Buyers

1. **Ruta de los Cenotes** has the cheapest land ($27k+)
2. Most properties under $200k are land only
3. Beachfront starts at $200k+
4. Building costs add $50-100k+ to land purchases
5. Contact local agents for unlisted deals

## 🌐 Useful Links

- [Properstar - Cheap Properties](https://www.properstar.com/mexico/puerto-morelos/buy/price-low-to-high)
- [For Sale Puerto Morelos](https://www.forsalepuertomorelos.com/)
- [MyCasa.mx Puerto Morelos](https://mycasa.mx/all-properties-for-sale-in-puerto-morelos/)
- [Riviera Maya Cozy](https://rivieramayacozy.com/puerto-morelos-properties/)

## 🛠️ Using the Python Tool

The `property_searcher.py` script helps organize and filter properties:

```python
from property_searcher import PropertySearcher

searcher = PropertySearcher()

# Add properties
searcher.add_property({
    "title": "My Property",
    "price": 50000,
    "type": "land",
    "location": "Puerto Morelos"
})

# Filter by price
cheap = searcher.filter_by_price(50000)

# Export to markdown
searcher.export_to_markdown("results.md")

# Get recommendations
print(searcher.get_budget_recommendations(50000))
```

## 📝 Next Steps

1. Review `puerto-morelos-property-search.md` for detailed findings
2. Visit the real estate websites listed
3. Contact local agents for current listings
4. Consider visiting Puerto Morelos in person
5. Join expat Facebook groups for insider deals

## ⚠️ Important Notes

- All prices in USD (as of December 2025)
- Mexican real estate is often negotiable
- Cash buyers may get better deals
- Consider long-term rentals before buying
- Always verify titles and legal status

---

*Made for poor dudes dreaming of Caribbean living* 🌴
