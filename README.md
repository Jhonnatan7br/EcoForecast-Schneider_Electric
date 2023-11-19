# EcoForecast Schneider_Electric
 
# SE-Europe-Data_Challenge
NUWE - Schneider Electric European Data Science Challenge in November 2023.

Create a model capable of predicting the country (from a list of nine) that will have the most surplus of green energy in the next hour. It is needed to consider both the energy generation from renewable sources (wind, solar, geothermic, etc.), and the load (energy consumption). The surplus of green energy is considered to be the difference between the generated green energy and the consumed energy.

The countries to focus on are: Spain, UK, Germany, Denmark, Sweden, Hungary, Italy, Poland, and the Netherlands.

The solution must not only align with Schneider Electric's ethos but also go beyond its current offerings, presenting an unprecedented approach.

# Types of energy on the ingested

It was selected only renewables sources of energy with the following codes ["B01", "B09", "B11", "B10", "B12", "B13", "B15", "B16", "B18", "B19"]

"""
#Interpolate any missing data
df.interpolate(method='linear', limit_direction='both', inplace=True)

a) There's a specific hour (e.g. 01/02/22 15:30h) but there's no more time rows in that same hour (no 15:00h or 15:15h or 15:45). In this case these fields should be populated with the interpolate() function
b) There's a specific hour (e.g. 22/03/22 18h) that doesn't have a single time interval in the dataset (no 18:00, 18:15, 18:30, or 18:45, nothing). In this case simply ignore the whole hour and move to the next one
"""

ENTSO-E documentation B17 is no longer considered green. for this reason are not included, Reference: Gather Worlds
URL: https://eepublicdownloads.blob.core.windows.net/public-cdn-container/clean-documents/Publications/Statistics/Factsheet/entsoe_sfs2022_web.pdf

- B01 Biomass 
- B02 Fossil Brown coal/Lignite
- B03 Fossil Coal-derived gas
- B04 Fossil Gas
- B05 Fossil Hard coal
- B06 Fossil Oil
- B07 Fossil Oil shale
- B08 Fossil Peat
- B09 Geothermal
- B10 Hydro Pumped Storage
- B11 Hydro Run-of-river and poundage
- B12 Hydro Water Reservoir
- B13 Marine
- B14 Nuclear
- B15 Other renewable
- B16 Solar
- B17 Waste
- B18 Wind Offshore
- B19 Wind Onshore
- B20 Other

# Tokens:
- b5b8c21b-a637-4e17-a8fe-0d39a16aa849
- fb81432a-3853-4c30-a105-117c86a433ca
- 2334f370-0c85-405e-bb90-c022445bd273
- 1d9cd4bd-f8aa-476c-8cc1-3442dc91506d