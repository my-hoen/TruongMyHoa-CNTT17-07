import hashlib

def sha256_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def sha512_hash(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

def main():
    print("🔐 CHƯƠNG TRÌNH BĂM DỮ LIỆU BẰNG SHA-256 và SHA-512\n")

    original = input("Nhập dữ liệu gốc: ")
    modified = input("Nhập dữ liệu đã sửa đổi: ")

    print("\n🧾 KẾT QUẢ BĂM:")
    print("-" * 60)
    print("📦 SHA-256 (gốc):     ", sha256_hash(original))
    print("📦 SHA-256 (sửa):     ", sha256_hash(modified))
    print("-" * 60)
    print("📦 SHA-512 (gốc):     ", sha512_hash(original))
    print("📦 SHA-512 (sửa):     ", sha512_hash(modified))
    print("-" * 60)

    if sha256_hash(original) != sha256_hash(modified) or sha512_hash(original) != sha512_hash(modified):
        print("⚠️ Dữ liệu đã bị thay đổi (hash khác nhau).")
    else:
        print("✅ Dữ liệu KHÔNG bị thay đổi.")

if __name__ == "__main__":
    main()
