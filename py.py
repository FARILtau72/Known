import os
import sys
from datetime import datetime
import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

BANNER = r"""
============================================================                                                                                            
                                                                                            
     ██╗  ██╗███╗   ██╗ ██████╗ ██╗    ██╗███╗   ██╗
'    ██║ ██╔╝████╗  ██║██╔═══██╗██║    ██║████╗  ██║
'    █████╔╝ ██╔██╗ ██║██║   ██║██║ █╗ ██║██╔██╗ ██║
'    ██╔═██╗ ██║╚██╗██║██║   ██║██║███╗██║██║╚██╗██║
'    ██║  ██╗██║ ╚████║╚██████╔╝╚███╔███╔╝██║ ╚████║ 1.0
'    ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝
'                                                                                                                                      
                                                                                              
        By @fr.project.id — Inspired by Sherlock
       Powered by OpenCage Geocoder API
============================================================
"""
print(BANNER)

# Ambil API Key dari environment variable, kalau gak ada minta input
API_KEY = os.getenv("OPENCAGE_API_KEY")
if not API_KEY:
    API_KEY = input("Masukkan OpenCage API Key: ").strip()
    if not API_KEY:
        print("⚠️  ERROR: API Key kosong.")
        sys.exit(1)

# Input nomor telepon
phonenumber = input("📞 Masukkan nomor telepon (contoh 628123456789): ").strip()
if not phonenumber:
    print("❌ Input kosong.")
    sys.exit(1)

# Normalisasi nomor
if not phonenumber.startswith('+'):
    if phonenumber.startswith('00'):
        phonenumber = '+' + phonenumber[2:]
    else:
        phonenumber = '+' + phonenumber

# Parse & validasi
try:
    number_obj = phonenumbers.parse(phonenumber, None)
except phonenumbers.NumberParseException as npe:
    print(f"⚠️ Nomor tidak valid: {npe}")
    sys.exit(1)

if not phonenumbers.is_valid_number(number_obj):
    print("❌ Nomor telepon tidak valid.")
    sys.exit(1)

# Ambil lokasi dasar dari phonenumbers
location = geocoder.description_for_number(number_obj, "en")
operator_name = carrier.name_for_number(number_obj, "en") or "Unknown"

# OpenCage Geocoder
geocoder_api = OpenCageGeocode(API_KEY)
try:
    results = geocoder_api.geocode(location, no_annotations=1, limit=5)
except Exception as e:
    print(f"⚠️ Gagal memanggil OpenCage API: {e}")
    sys.exit(1)

if not results:
    print("❌ Koordinat tidak ditemukan oleh OpenCage.")
    sys.exit(1)

entry = results[0]
geometry = entry.get('geometry')
if not geometry or 'lat' not in geometry or 'lng' not in geometry:
    print("❌ Hasil OpenCage tidak ada koordinat.")
    sys.exit(1)

lat = geometry['lat']
lng = geometry['lng']

formatted_number = phonenumbers.format_number(number_obj, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
components = entry.get('components', {})
country = components.get('country', "Unknown")
city = components.get('city') or components.get('town') or components.get('village') or "Unknown"

# Print info lengkap
print("\n✅ Data ditemukan:")
print(f"   • Nomor    : {formatted_number}")
print(f"   • Operator : {operator_name}")
print(f"   • Domisili : {city}, {country}")
print(f"   • Latitude : {lat}")
print(f"   • Longitude: {lng}")

# Buat map
timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
map_filename = f"farsec_map_{timestamp}.html"

try:
    my_map = folium.Map(location=[lat, lng], zoom_start=10)
    folium.CircleMarker(
        location=[lat, lng],
        radius=8,
        popup=f"{city}, {country} ({formatted_number})",
        tooltip=f"{city} — {formatted_number} — {operator_name}",
        fill=True,
        fill_opacity=0.9
    ).add_to(my_map)
    my_map.save(map_filename)
    print(f"\n🗺️ Map berhasil disimpan sebagai '{map_filename}'")
    print("👉 Buka file tersebut di browser untuk melihat lokasi.")
except Exception as e:
    print(f"⚠️ Gagal membuat/menyimpan map: {e}")
    sys.exit(1)

print("\n🚀 selesai yah jangan di buat macem-macem, .")

