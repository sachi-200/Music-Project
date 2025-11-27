import mysql.connector

# === DB Config ===
HOST = "localhost"
USER = "root"
PASSWORD = "Matilda+10"
DATABASE = "musicproject"

# Connect to MySQL
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()

# List of all 72 Melakarta names (EXACT names from your code)
melakarta_names = [
    "Kanakangi", "Ratnangi", "Ganamurti", "Vanaspati", "Manavati", "Tanarupi",
    "Senavati", "Hanumatodi", "Dhenuka", "Natakapriya", "Kokilapriya", "Rupavati",
    "Gayakapriya", "Vakulabharanam", "Mayamalavagowla", "Chakravakam", "Suryakantam", "Hatakambari",
    "Jhankaradhvani", "Natabhairavi", "Keeravani", "Kharaharapriya", "Gourimanohari", "Varunapriya",
    "Mararanjani", "Charukesi", "Sarasangi", "Harikambhoji", "Dheerasankarabharanam", "Naganandini",
    "Yagapriya", "Ragavardhini", "Gangeyabhushani", "Vagadheeswari", "Shoolini", "Chalanata",
    "Salagam", "Jalarnavam", "Jhalavarali", "Navaneetam", "Pavani", "Raghupriya",
    "Gavambodhi", "Bhavapriya", "Shubhapantuvarali", "Shadvidamargini", "Suvarnangi", "Divyamani",
    "Dhavalambari", "Namanarayani", "Kamavardhini", "Ramapriya", "Gamanashrama", "Vishwambari",
    "Shamalangi", "Shanmukhapriya", "Simhendramadhyamam", "Hemavati", "Dharmavati", "Neetimati",
    "Kantamani", "Rishabhapriya", "Latangi", "Vachaspati", "Mechakalyani", "Chitrambari",
    "Sucharitra", "Jyotiswarupini", "Dhatuvardhani", "Nasikabhushani", "Kosalam", "Rasikapriya"
]

print("🎵 Creating 72 Melakarta Janya Raga tables...\n")

print("🗑️  Dropping existing tables if they exist...")
# First, drop all existing tables
for idx, melakarta_name in enumerate(melakarta_names, start=1):
    table_name = melakarta_name
    drop_query = f"DROP TABLE IF EXISTS `{table_name}`"
    cursor.execute(drop_query)
    print(f"   Dropped table (if existed): {table_name}")

print("\n✅ All existing tables dropped successfully!\n")
print("📝 Creating new tables...\n")

# Create table for each Melakarta
for idx, melakarta_name in enumerate(melakarta_names, start=1):
    table_name = melakarta_name
    
    # Create table with all required columns
    create_query = f"""
    CREATE TABLE `{table_name}` (
        raga_number INT AUTO_INCREMENT PRIMARY KEY,
        janya_raga_name VARCHAR(100) NOT NULL,
        arohanam VARCHAR(255) NOT NULL,
        avarohanam VARCHAR(255) NOT NULL,
        audio_path_arohanam VARCHAR(255),
        audio_path_avarohanam VARCHAR(255),
        Sa INT DEFAULT 0,
        R1 INT DEFAULT 0,
        R2 INT DEFAULT 0,
        R3 INT DEFAULT 0,
        G1 INT DEFAULT 0,
        G2 INT DEFAULT 0,
        G3 INT DEFAULT 0,
        M1 INT DEFAULT 0,
        M2 INT DEFAULT 0,
        Pa INT DEFAULT 0,
        D1 INT DEFAULT 0,
        D2 INT DEFAULT 0,
        D3 INT DEFAULT 0,
        N1 INT DEFAULT 0,
        N2 INT DEFAULT 0,
        N3 INT DEFAULT 0
    )
    """
    
    cursor.execute(create_query)
    print(f"✅ Created table: {table_name} (Melakarta #{idx})")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully created all 72 Melakarta Janya Raga tables!")
print(f"📊 Each table has 23 columns:")
print(f"   - raga_number (Primary Key, Auto Increment)")
print(f"   - janya_raga_name")
print(f"   - arohanam")
print(f"   - avarohanam")
print(f"   - audio_path_arohanam")
print(f"   - audio_path_avarohanam")
print(f"   - 17 swara columns (Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)")
print(f"\n💡 You can now access each table using the exact melakarta name from your existing code!")