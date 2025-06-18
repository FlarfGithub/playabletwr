import os

# List of generic countries that should use the generic focus tree
# Format: (tag, name, capital_id, region_flag)
generic_countries = [
    ("GEO", "Georgia", 231, "EUROPE"),
    ("EGY", "Egypt", 1000, "AFRICA"),
    ("COL", "Colombia", 501, "AMERICAS"),
    ("VEN", "Venezuela", 502, "AMERICAS"),
    ("PER", "Peru", 503, "AMERICAS"),
    ("CHL", "Chile", 504, "AMERICAS"),
    ("ARG", "Argentina", 505, "AMERICAS"),
    ("URU", "Uruguay", 506, "AMERICAS"),
    ("PAR", "Paraguay", 507, "AMERICAS"),
    ("BOL", "Bolivia", 508, "AMERICAS"),
    ("ECU", "Ecuador", 509, "AMERICAS"),
    ("IRN", "Iran", 1001, "ASIA"),
    ("IRQ", "Iraq", 1002, "ASIA"),
    ("SAU", "Saudi Arabia", 1003, "ASIA"),
    ("YEM", "Yemen", 1004, "ASIA"),
    ("OMA", "Oman", 1005, "ASIA"),
    ("AFG", "Afghanistan", 1006, "ASIA"),
    ("PAK", "Pakistan", 1007, "ASIA"),
    ("BAN", "Bangladesh", 1008, "ASIA"),
    ("SRI", "Sri Lanka", 1009, "ASIA"),
    ("NEP", "Nepal", 1010, "ASIA"),
    ("BHU", "Bhutan", 1011, "ASIA"),
    ("MNG", "Mongolia", 1012, "ASIA"),
    ("LAO", "Laos", 1013, "ASIA"),
    ("KHM", "Cambodia", 1014, "ASIA"),
    ("MMR", "Myanmar", 1015, "ASIA"),
    ("THA", "Thailand", 1016, "ASIA"),
    ("MYS", "Malaysia", 1017, "ASIA"),
    ("IDN", "Indonesia", 1018, "ASIA"),
    ("PHL", "Philippines", 1019, "ASIA"),
    ("TWN", "Taiwan", 1020, "ASIA"),
    ("KOR", "Korea", 1021, "ASIA"),
    ("VNM", "Vietnam", 1022, "ASIA"),
    ("ETH", "Ethiopia", 2000, "AFRICA"),
    ("SOM", "Somalia", 2001, "AFRICA"),
    ("DJI", "Djibouti", 2002, "AFRICA"),
    ("ERI", "Eritrea", 2003, "AFRICA"),
    ("SDN", "Sudan", 2004, "AFRICA"),
    ("SSD", "South Sudan", 2005, "AFRICA"),
    ("CAF", "Central African Republic", 2006, "AFRICA"),
    ("TCD", "Chad", 2007, "AFRICA"),
    ("CMR", "Cameroon", 2008, "AFRICA"),
    ("GAB", "Gabon", 2009, "AFRICA"),
    ("COG", "Republic of the Congo", 2010, "AFRICA"),
    ("COD", "Democratic Republic of the Congo", 2011, "AFRICA"),
    ("RWA", "Rwanda", 2012, "AFRICA"),
    ("BDI", "Burundi", 2013, "AFRICA"),
    ("TZA", "Tanzania", 2014, "AFRICA"),
    ("UGA", "Uganda", 2015, "AFRICA"),
    ("KEN", "Kenya", 2016, "AFRICA"),
    ("MWI", "Malawi", 2017, "AFRICA"),
    ("ZMB", "Zambia", 2018, "AFRICA"),
    ("ZWE", "Zimbabwe", 2019, "AFRICA"),
    ("BWA", "Botswana", 2020, "AFRICA"),
    ("NAM", "Namibia", 2021, "AFRICA"),
    ("ZAF", "South Africa", 2022, "AFRICA"),
    ("LSO", "Lesotho", 2023, "AFRICA"),
    ("SWZ", "Eswatini", 2024, "AFRICA"),
    ("MOZ", "Mozambique", 2025, "AFRICA"),
    ("MDG", "Madagascar", 2026, "AFRICA"),
    ("COM", "Comoros", 2027, "AFRICA"),
    ("MUS", "Mauritius", 2028, "AFRICA"),
    ("SYC", "Seychelles", 2029, "AFRICA"),
    ("GMB", "Gambia", 2030, "AFRICA"),
    ("SEN", "Senegal", 2031, "AFRICA"),
    ("GIN", "Guinea", 2032, "AFRICA"),
    ("GNB", "Guinea-Bissau", 2033, "AFRICA"),
    ("SLE", "Sierra Leone", 2034, "AFRICA"),
    ("LBR", "Liberia", 2035, "AFRICA"),
    ("CIV", "Ivory Coast", 2036, "AFRICA"),
    ("BFA", "Burkina Faso", 2037, "AFRICA"),
    ("MLI", "Mali", 2038, "AFRICA"),
    ("NER", "Niger", 2039, "AFRICA"),
    ("NGA", "Nigeria", 2040, "AFRICA"),
    ("BEN", "Benin", 2041, "AFRICA"),
    ("TGO", "Togo", 2042, "AFRICA"),
    ("GHA", "Ghana", 2043, "AFRICA"),
    ("CPV", "Cape Verde", 2044, "AFRICA"),
    ("STP", "São Tomé and Príncipe", 2045, "AFRICA"),
    ("GNQ", "Equatorial Guinea", 2046, "AFRICA"),
    ("AGO", "Angola", 2047, "AFRICA"),
]

def create_country_file(tag, name, capital_id, region):
    """Create a country history file for a generic country."""
    
    # Determine the region flag based on the region
    region_flag_map = {
        "EUROPE": "NEWS_EVENTS_EUROPE_FLAG",
        "ASIA": "NEWS_EVENTS_ASIA_FLAG", 
        "AFRICA": "NEWS_EVENTS_AFRICA_FLAG",
        "AMERICAS": "NEWS_EVENTS_AMERICAS_FLAG"
    }
    
    region_flag = region_flag_map.get(region, "NEWS_EVENTS_ASIA_FLAG")
    
    content = f"""#########################################################################
# {name}
#########################################################################
capital = {capital_id}
oob = "{tag}_1952"
set_research_slots = 2
set_country_flag = {region_flag}
set_country_flag = NEWS_EVENTS_PERMANENT_{region}_FLAG

#######################
# Research
#######################
set_technology = {{
	infantry_weapons_1 = 1
	tech_mountaineers = 1
	motorised_infantry = 1

	basic_infantry_equipment = 1
	infantry_at = 1

	artillery4 = 1

	base_armor = 1
	medium_tank_basic = 1
	light_tank_basic = 1
	gw_artillery = 1
}}

#######################
# Politics
#######################
set_politics = {{
	ruling_party = paternal_autocrat
	last_election = "1932.11.8"
	election_frequency = 48
	elections_allowed = no	
}}

set_popularities = {{
    national_socialist = 0
    fascist = 10
    paternal_autocrat = 34
    conservative = 3
    liberal = 1
    social_democrat = 6
    socialist = 36
    bolshevik_leninist = 0
    marxist_leninist = 10
}}

add_ideas = {{
	authoritarian_system
	agrarian_nation
}}

#######################
# Focus Tree
#######################
focus_tree = generic

autocomplete_starting_projects = yes
"""
    
    return content

def main():
    """Create country files for all generic countries."""
    
    # Create the history/countries directory if it doesn't exist
    countries_dir = "history/countries"
    if not os.path.exists(countries_dir):
        os.makedirs(countries_dir)
    
    created_count = 0
    
    for tag, name, capital_id, region in generic_countries:
        filename = f"{tag} - {name}.txt"
        filepath = os.path.join(countries_dir, filename)
        
        # Skip if file already exists
        if os.path.exists(filepath):
            print(f"Skipping {filename} (already exists)")
            continue
        
        content = create_country_file(tag, name, capital_id, region)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Created {filename}")
        created_count += 1
    
    print(f"\nCreated {created_count} country files for generic countries.")
    print("These countries will now use the generic focus tree and advisors.")

if __name__ == "__main__":
    main() 