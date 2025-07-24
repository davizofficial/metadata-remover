import os
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime

def view_pdf_metadata(pdf_path):
    """Menampilkan metadata PDF dengan tampilan menarik"""
    print("🔍 HASIL ANALISIS METADATA PDF")
    print("=" * 50)
    
    try:
        reader = PdfReader(pdf_path)
        metadata = reader.metadata
        
        print(f"📄 Nama File: {os.path.basename(pdf_path)}")
        print(f"📊 Jumlah Halaman: {len(reader.pages)}")
        print()
        
        if metadata:
            print("📋 Informasi Dokumen:")
            metadata_mapping = {
                '/Title': '📌 Judul',
                '/Author': '👤 Penulis',
                '/Subject': '📝 Subjek',
                '/Creator': '🏗️  Pembuat',
                '/Producer': '🖨️  Software',
                '/CreationDate': '📅 Tanggal Pembuatan',
                '/ModDate': '✏️  Tanggal Modifikasi',
                '/Keywords': '🔑 Kata Kunci',
                '/Trapped': '🎯 Trapped'
            }
            
            for key, readable_name in metadata_mapping.items():
                if key in metadata:
                    value = metadata[key]
                    # Format tanggal jika perlu
                    if key in ['/CreationDate', '/ModDate'] and isinstance(value, str):
                        try:
                            # Parsing tanggal PDF
                            date_str = value.replace("D:", "")
                            if len(date_str) >= 14:
                                year = date_str[:4]
                                month = date_str[4:6]
                                day = date_str[6:8]
                                hour = date_str[8:10]
                                minute = date_str[10:12]
                                second = date_str[12:14]
                                value = f"{day}/{month}/{year} {hour}:{minute}:{second}"
                        except:
                            pass
                    print(f"🔹 {readable_name}: {value}")
        else:
            print("✅ Tidak ada metadata ditemukan")
        
        # Informasi tambahan
        print(f"\n📊 Informasi Tambahan:")
        print(f"   • Jumlah Halaman: {len(reader.pages)}")
        if reader.is_encrypted:
            print(f"   • Status: 🔒 Terenkripsi")
        else:
            print(f"   • Status: 🔓 Tidak Terenkripsi")
            
        return True
        
    except Exception as e:
        print(f"❌ Error membaca metadata PDF: {str(e)}")
        return False

def remove_pdf_metadata(pdf_path, output_path):
    """Menghapus metadata dari PDF"""
    try:
        print("🧹 Menghapus metadata PDF...")
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        
        # Salin semua halaman
        for page in reader.pages:
            writer.add_page(page)
        
        # Tambahkan metadata minimal
        writer.add_metadata({
            "/Producer": "Metadata Remover Tool",
            "/Creator": "Privacy Protection Tool"
        })
        
        # Simpan file
        with open(output_path, "wb") as out_file:
            writer.write(out_file)
            
        print("✅ Metadata berhasil dihapus!")
        print(f"💾 File disimpan sebagai: {output_path}")
        
        # Verifikasi
        print("\n🔍 Verifikasi hasil...")
        verification_reader = PdfReader(output_path)
        verification_metadata = verification_reader.metadata
        
        if verification_metadata and len(verification_metadata) <= 2:
            print("✅ Verifikasi berhasil - metadata telah dikurangi")
        else:
            print("⚠️  Masih ada metadata yang tersisa")
        
        return True
        
    except Exception as e:
        print(f"❌ Error menghapus metadata PDF: {str(e)}")
        return False