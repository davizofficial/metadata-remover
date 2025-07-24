import webbrowser

class MetadataHandler:
    """Handler utama untuk mengelola tipe file"""
    
    @staticmethod
    def get_file_type(file_path):
        """Menentukan tipe file berdasarkan ekstensi"""
        import os
        extension = os.path.splitext(file_path)[1].lower()
        return extension
    
    @staticmethod
    def is_supported_format(file_path):
        """Mengecek apakah format file didukung"""
        supported_formats = ['.jpg', '.jpeg', '.png', '.pdf']
        file_type = MetadataHandler.get_file_type(file_path)
        return file_type in supported_formats
    
    @staticmethod
    def generate_google_maps_link(latitude, longitude):
        """Menghasilkan link Google Maps dari koordinat"""
        return f"https://www.google.com/maps?q={latitude},{longitude}"
    
    @staticmethod
    def open_google_maps(latitude, longitude):
        """Membuka lokasi di Google Maps"""
        try:
            maps_url = MetadataHandler.generate_google_maps_link(latitude, longitude)
            webbrowser.open(maps_url)
            return maps_url
        except Exception as e:
            print(f"❌ Error membuka Google Maps: {str(e)}")
            return None
    
    @staticmethod
    def format_coordinates_for_maps(lat_decimal, lon_decimal):
        """Memformat koordinat untuk Google Maps"""
        return f"{lat_decimal:.6f}, {lon_decimal:.6f}"