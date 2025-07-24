import argparse
import os
from metadata_handler import MetadataHandler
from image_processor import view_image_metadata, remove_image_metadata
from pdf_processor import view_pdf_metadata, remove_pdf_metadata

def print_banner():
    """Menampilkan banner menarik dengan tulisan Metadata Remover"""
    banner = """

███╗░░░███╗███████╗████████╗░█████╗░██████╗░░█████╗░████████╗░█████╗░  
████╗░████║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗  
██╔████╔██║█████╗░░░░░██║░░░███████║██║░░██║███████║░░░██║░░░███████║  
██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██║░░██║██╔══██║░░░██║░░░██╔══██║  
██║░╚═╝░██║███████╗░░░██║░░░██║░░██║██████╔╝██║░░██║░░░██║░░░██║░░██║  
╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝  

      ██████╗░███████╗███╗░░░███╗░█████╗░██╗░░░██╗███████╗██████╗░
      ██╔══██╗██╔════╝████╗░████║██╔══██╗██║░░░██║██╔════╝██╔══██╗
      ██████╔╝█████╗░░██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
      ██╔══██╗██╔══╝░░██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
      ██║░░██║███████╗██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
      ╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝ V.1.0
    """
    print(banner)
    print("=" * 80)
    print("🛡️  Metadata Remover - Lindungi Privasi Anda! 🛡️")
    print("=" * 80 + "\n")

def main():
    print_banner()
    
    parser = argparse.ArgumentParser(
        description='Metadata Remover Tool - Menghapus metadata sensitif dari file',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python main.py -f foto.jpg --view
  python main.py -f dokumen.pdf --remove
  python main.py -f gambar.png --remove -o bersih.png
        """
    )
    parser.add_argument('-f', '--file', required=True, help='Path file yang akan diproses')
    parser.add_argument('-v', '--view', action='store_true', help='Lihat metadata saja')
    parser.add_argument('-r', '--remove', action='store_true', help='Hapus metadata')
    parser.add_argument('-o', '--output', help='Nama file output (opsional)')
    parser.add_argument('-m', '--map', action='store_true', help='Tampilkan link Google Maps untuk lokasi GPS')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"❌ File tidak ditemukan: {args.file}")
        return
    
    # Cek apakah format file didukung
    handler = MetadataHandler()
    if not handler.is_supported_format(args.file):
        print(f"❌ Format file tidak didukung!")
        print("📝 Format yang didukung: JPG, JPEG, PNG, PDF")
        return
    
    file_extension = handler.get_file_type(args.file)
    
    print(f"📁 File: {args.file}")
    print(f"📊 Tipe: {file_extension.upper()}")
    print("-" * 50)
    
    # Simpan preference untuk Google Maps
    show_map = args.map
    
    if args.view:
        print("🔍 Menganalisis metadata...")
        # View metadata
        if file_extension in ['.jpg', '.jpeg', '.png']:
            view_image_metadata(args.file, show_map_link=show_map)
        elif file_extension in ['.pdf']:
            view_pdf_metadata(args.file)
            
    elif args.remove:
        print("⚙️  Memproses penghapusan metadata...")
        # Remove metadata
        if not args.output:
            name, ext = os.path.splitext(args.file)
            args.output = f"{name}_clean{ext}"
            
        if file_extension in ['.jpg', '.jpeg', '.png']:
            remove_image_metadata(args.file, args.output)
        elif file_extension in ['.pdf']:
            remove_pdf_metadata(args.file, args.output)
    else:
        print("⚠️  Silakan pilih --view atau --remove")
        print("💡 Gunakan -h untuk bantuan")

if __name__ == "__main__":
    main()