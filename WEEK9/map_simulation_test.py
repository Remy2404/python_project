import folium

# Create a map centered around Cambodia
m = folium.Map(location=[12.5657, 104.991], zoom_start=7)

# Add markers with correct coordinates and popups
folium.Marker([11.56245, 104.91601], popup='Phnom Penh').add_to(m)
folium.Marker([13.58588, 102.97369], popup='Banteay Meanchey').add_to(m)
folium.Marker([13.10271, 103.19822], popup='Battambang').add_to(m)
folium.Marker([11.99339, 105.4635], popup='Kampong Cham').add_to(m)
folium.Marker([12.25, 104.66667], popup='Kampong Chhnang').add_to(m)
folium.Marker([11.4600, 104.5247], popup='Kampong Speu').add_to(m)
folium.Marker([12.71121, 104.89108], popup='Kampong Thom').add_to(m)
folium.Marker([10.61041, 104.18145], popup='Kampot').add_to(m)
folium.Marker([11.2016, 105.2096], popup='Kandal').add_to(m)
folium.Marker([11.6089, 103.0787], popup='Koh Kong').add_to(m)
folium.Marker([12.4880, 106.0190], popup='Kratie').add_to(m)
folium.Marker([12.8000, 107.2000], popup='Mondul Kiri').add_to(m)
folium.Marker([14.18175, 103.51761], popup='Oddar Meanchey').add_to(m)
folium.Marker([12.84895, 102.60928], popup='Pailin').add_to(m)
folium.Marker([13.7911, 104.9830], popup='Preah Vihear').add_to(m)
folium.Marker([11.48682, 105.32533], popup='Prey Veng').add_to(m)
folium.Marker([12.53878, 103.9192], popup='Pursat').add_to(m)
folium.Marker([13.73939, 106.98727], popup='Ratanakiri').add_to(m)
folium.Marker([13.36179, 103.86056], popup='Siem Reap').add_to(m)
folium.Marker([13.52586, 105.9683], popup='Stung Treng').add_to(m)
folium.Marker([11.08785, 105.79935], popup='Svay Rieng').add_to(m)
folium.Marker([10.99081, 104.78498], popup='Takeo').add_to(m)
folium.Marker([10.4833, 104.3167], popup='Kep').add_to(m)
folium.Marker([10.60932, 103.52958], popup='Sihanoukville').add_to(m)

# Save the map as an HTML file
m.save('./cambodia_map2.html')
