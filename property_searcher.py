#!/usr/bin/env python3
"""
Puerto Morelos Property Search Tool
Helps find affordable properties in Puerto Morelos, Mexico
"""

import json
from datetime import datetime
from typing import List, Dict

class PropertySearcher:
    """Search and filter properties in Puerto Morelos"""

    def __init__(self):
        self.properties = []
        self.search_sources = {
            "properstar": "https://www.properstar.com/mexico/puerto-morelos/buy/price-low-to-high",
            "forsale_pm": "https://www.forsalepuertomorelos.com/",
            "mycasa": "https://mycasa.mx/all-properties-for-sale-in-puerto-morelos/",
            "riviera_cozy": "https://rivieramayacozy.com/puerto-morelos-properties/",
            "runaway": "https://runawayrealty.com/home-search/",
            "blue_caribbean": "https://bluecaribbeanproperties.com/mexico-real-estate/puerto-morelos/",
            "topmexicorealestate": "https://www.topmexicorealestate.com/puertomorelos-real-estate/b-listado-puertomorelos.php"
        }

    def add_property(self, property_data: Dict):
        """Add a property to the search results"""
        self.properties.append({
            **property_data,
            "added_date": datetime.now().isoformat()
        })

    def filter_by_price(self, max_price: int) -> List[Dict]:
        """Filter properties by maximum price"""
        return [p for p in self.properties if p.get('price', float('inf')) <= max_price]

    def filter_by_type(self, property_type: str) -> List[Dict]:
        """Filter properties by type (land, house, condo, apartment)"""
        return [p for p in self.properties if p.get('type', '').lower() == property_type.lower()]

    def exclude_new_construction(self) -> List[Dict]:
        """Exclude new construction and recently renovated properties"""
        keywords = ['new', 'renovated', 'remodeled', 'modern', 'luxury', 'pre-construction', 'presale']
        filtered = []
        for prop in self.properties:
            desc = prop.get('description', '').lower()
            if not any(keyword in desc for keyword in keywords):
                filtered.append(prop)
        return filtered

    def get_search_sources(self) -> Dict[str, str]:
        """Return all property search sources"""
        return self.search_sources

    def export_to_markdown(self, filename: str = "search_results.md"):
        """Export search results to markdown file"""
        with open(filename, 'w') as f:
            f.write("# Puerto Morelos Property Search Results\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write(f"**Total Properties:** {len(self.properties)}\n\n")

            for idx, prop in enumerate(sorted(self.properties, key=lambda x: x.get('price', 0)), 1):
                f.write(f"## {idx}. {prop.get('title', 'Property Listing')}\n\n")
                f.write(f"- **Price:** ${prop.get('price', 'N/A'):,} USD\n")
                f.write(f"- **Type:** {prop.get('type', 'N/A')}\n")
                f.write(f"- **Location:** {prop.get('location', 'Puerto Morelos')}\n")
                if prop.get('size'):
                    f.write(f"- **Size:** {prop.get('size')}\n")
                if prop.get('bedrooms'):
                    f.write(f"- **Bedrooms:** {prop.get('bedrooms')}\n")
                if prop.get('bathrooms'):
                    f.write(f"- **Bathrooms:** {prop.get('bathrooms')}\n")
                if prop.get('description'):
                    f.write(f"- **Description:** {prop.get('description')}\n")
                if prop.get('url'):
                    f.write(f"- **Link:** {prop.get('url')}\n")
                f.write("\n")

    def get_budget_recommendations(self, budget: int) -> str:
        """Get recommendations based on budget"""
        if budget < 50000:
            return """
Budget Under $50,000:
- Focus on LAND ONLY purchases (Ruta de los Cenotes area)
- Expect to build from scratch
- Land lots starting at $27,000
- Will need additional funds for construction
"""
        elif budget < 100000:
            return """
Budget $50,000-$100,000:
- Land with some services/infrastructure
- Possibly older structures needing work
- Some equipped lots available
- Good for DIY investors
"""
        elif budget < 200000:
            return """
Budget $100,000-$200,000:
- Small condos/apartments available
- Older houses that may need updates
- Better selection of livable properties
- Some investment properties with rental income
"""
        else:
            return """
Budget $200,000+:
- Modern condos and houses
- Beachfront options become available
- Turnkey properties
- Luxury and new construction options
"""


def main():
    """Main function to demonstrate usage"""
    searcher = PropertySearcher()

    # Example: Add the properties we found
    searcher.add_property({
        "title": "Land Lot - Ruta de los Cenotes",
        "price": 27000,
        "type": "land",
        "size": "1,250 m² (50m x 25m)",
        "location": "Ruta de los Cenotes, Central Vallarta",
        "description": "Titled land, free of liens, raw land requiring construction",
        "url": "https://www.forsalepuertomorelos.com/Puerto_Morelos/Quintana_Roo/Lots_and_Land/Ruta_de_los_Cenotes/Agent/Listing_259944340.html"
    })

    searcher.add_property({
        "title": "Equipped Land",
        "price": 73189,
        "type": "land",
        "size": "2,799 sq ft",
        "location": "Puerto Morelos",
        "description": "Land with some infrastructure/utilities"
    })

    print("=" * 60)
    print("PUERTO MORELOS PROPERTY SEARCH TOOL")
    print("=" * 60)
    print()

    # Show all sources
    print("📍 Search Sources:")
    for name, url in searcher.get_search_sources().items():
        print(f"   - {name}: {url}")
    print()

    # Filter examples
    print(f"💰 Properties under $50,000: {len(searcher.filter_by_price(50000))} found")
    print(f"🏞️  Land properties: {len(searcher.filter_by_type('land'))} found")
    print()

    # Budget recommendation
    budget = 50000
    print(f"💡 Recommendations for ${budget:,} budget:")
    print(searcher.get_budget_recommendations(budget))

    # Export results
    searcher.export_to_markdown("puerto_morelos_results.md")
    print("✅ Results exported to: puerto_morelos_results.md")


if __name__ == "__main__":
    main()
