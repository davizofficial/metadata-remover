import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread
from metadata_handler import MetadataHandler

def get_readable_tag_name(tag):
    """Mendapatkan nama tag yang mudah dibaca"""
    tag_names = {
        'Image Make': '📱 Perangkat',
        'Image Model': '📷 Model Kamera',
        'EXIF DateTimeOriginal': '📅 Tanggal Pengambilan',
        'EXIF DateTimeDigitized': '⏱️ Tanggal Digitalisasi',
        'EXIF ExposureTime': '⏱️ Waktu Eksposur',
        'EXIF FNumber': '🔢 Aperture',
        'EXIF ISOSpeedRatings': '🎛️ ISO',
        'EXIF FocalLength': '🔍 Focal Length',
        'GPS GPSLatitude': '📍 Latitude',
        'GPS GPSLongitude': '📍 Longitude',
        'GPS GPSAltitude': '🏔️ Ketinggian',
        'Image Software': '💻 Software',
        'Image Artist': '👤 Pembuat',
        'Image Copyright': '© Hak Cipta',
    }
    return tag_names.get(tag, tag)

def extract_gps_info(tags):
    """Mengekstrak informasi GPS"""
    gps_info = {}
    for tag in tags.keys():
        if tag.startswith('GPS'):
            gps_info[tag] = tags[tag]
    return gps_info

def convert_to_degrees(value):
    """Konversi koordinat GPS ke derajat desimal"""
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def get_gps_coordinates(tags):
    """Mendapatkan koordinat GPS dalam format desimal"""
    try:
        gps_info = extract_gps_info(tags)
        
        if 'GPS GPSLatitude' in gps_info and 'GPS GPSLongitude' in gps_info:
            lat = gps_info['GPS GPSLatitude'].values
            lon = gps_info['GPS GPSLongitude'].values
            lat_ref = gps_info.get('GPS GPSLatitudeRef', 'N').values
            lon_ref = gps_info.get('GPS GPSLongitudeRef', 'E').values
            
            lat_decimal = convert_to_degrees(lat)
            lon_decimal = convert_to_degrees(lon)
            
            if lat_ref == 'S':
                lat_decimal = -lat_decimal
            if lon_ref == 'W':
                lon_decimal = -lon_decimal
                
            return lat_decimal, lon_decimal
    except Exception as e:
        print(f"⚠️  Error parsing GPS coordinates: {str(e)}")
        pass
    return None, None

def format_gps_display(gps_info):
    """Memformat tampilan GPS"""
    try:
        if 'GPS GPSLatitude' in gps_info and 'GPS GPSLongitude' in gps_info:
            lat = gps_info['GPS GPSLatitude'].values
            lon = gps_info['GPS GPSLongitude'].values
            lat_ref = gps_info.get('GPS GPSLatitudeRef', 'N').values
            lon_ref = gps_info.get('GPS GPSLongitudeRef', 'E').values
            
            lat_decimal = convert_to_degrees(lat)
            lon_decimal = convert_to_degrees(lon)
            
            if lat_ref == 'S':
                lat_decimal = -lat_decimal
            if lon_ref == 'W':
                lon_decimal = -lon_decimal
                
            return f"📍 Koordinat: {lat_decimal:.6f}, {lon_decimal:.6f}"
    except:
        pass
    return "📍 Koordinat: Tidak tersedia"

def view_image_metadata(image_path, show_map_link=False):
    """Menampilkan metadata gambar dengan tampilan menarik"""
    print("🔍 HASIL ANALISIS METADATA")
    print("=" * 50)
    
    try:
        # Menggunakan PIL untuk metadata dasar
        image = Image.open(image_path)
        exifdata = image.getexif()
        
        # Menggunakan exifread untuk metadata lebih lengkap
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
        
        if not tags and not exifdata:
            print("✅ Tidak ada metadata ditemukan")
            return True
        
        # Informasi umum
        print(f"📄 Nama File: {os.path.basename(image_path)}")
        print(f"📊 Dimensi: {image.width} x {image.height} pixels")
        print(f"🎨 Mode: {image.mode}")
        print()
        
        # Informasi penting
        important_info = [
            'Image Make',
            'Image Model', 
            'EXIF DateTimeOriginal',
            'EXIF DateTimeDigitized',
            'Image Software',
            'Image Artist',
            'Image Copyright'
        ]
        
        found_info = False
        for info in important_info:
            if info in tags:
                print(f"🔹 {get_readable_tag_name(info)}: {tags[info]}")
                found_info = True
        
        if found_info:
            print()
        
        # Informasi GPS dengan integrasi Google Maps
        gps_info = extract_gps_info(tags)
        if gps_info:
            gps_display = format_gps_display(gps_info)
            print(f"🗺️  {gps_display}")
            
            # Dapatkan koordinat untuk Google Maps
            lat, lon = get_gps_coordinates(tags)
            if lat is not None and lon is not None:
                maps_link = MetadataHandler.generate_google_maps_link(lat, lon)
                print(f"🔗 Google Maps: {maps_link}")
                
                # Opsi untuk membuka di browser
                if show_map_link:
                    open_map = input("\n🌍 Buka lokasi di Google Maps? (y/N): ").lower().strip()
                    if open_map == 'y':
                        MetadataHandler.open_google_maps(lat, lon)
                        print("🌐 Membuka Google Maps...")
            found_info = True
            print()
        
        # Informasi teknis
        technical_info = [
            'EXIF ExposureTime',
            'EXIF FNumber',
            'EXIF ISOSpeedRatings',
            'EXIF FocalLength'
        ]
        
        tech_found = False
        for info in technical_info:
            if info in tags:
                if not tech_found:
                    print("⚙️  Informasi Teknis:")
                    tech_found = True
                print(f"   • {get_readable_tag_name(info)}: {tags[info]}")
        
        if tech_found:
            print()
        
        # Tampilkan semua metadata jika diminta
        show_all = input("👀 Tampilkan semua metadata? (y/N): ").lower().strip()
        if show_all == 'y':
            print("\n📋 SEMUA METADATA:")
            print("-" * 30)
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode()
                print(f"{tag:25}: {data}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error membaca metadata gambar: {str(e)}")
        return False

def remove_image_metadata(image_path, output_path):
    """Menghapus metadata dari gambar"""
    try:
        print("🧹 Menghapus metadata...")
        image = Image.open(image_path)
        
        # Hapus metadata
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        
        # Simpan tanpa metadata
        image_without_exif.save(output_path, quality=95)
        print("✅ Metadata berhasil dihapus!")
        print(f"💾 File disimpan sebagai: {output_path}")
        
        # Verifikasi
        print("\n🔍 Verifikasi hasil...")
        with open(output_path, 'rb') as f:
            tags = exifread.process_file(f)
        
        if not tags:
            print("✅ Verifikasi berhasil - tidak ada metadata yang tersisa")
        else:
            print("⚠️  Masih ada beberapa metadata yang tersisa")
        
        return True
        
    except Exception as e:
        print(f"❌ Error menghapus metadata gambar: {str(e)}")
        return False