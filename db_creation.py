import os
import mysql.connector

# === DB Config ===
HOST = "localhost"
USER = "root"
PASSWORD = "Matilda+10"
DATABASE = "musicproject"

# === Directory where your audio files are ===
AUDIO_DIR = "audio/"

# Connect to MySQL
conn = mysql.connector.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    database=DATABASE
)
cursor = conn.cursor()

# -----------------------------------------------------------------
# Drop tables if they exist
# -----------------------------------------------------------------
cursor.execute("DROP TABLE IF EXISTS melakarta_audio")
cursor.execute("DROP TABLE IF EXISTS raagas_audio")
cursor.execute("DROP TABLE IF EXISTS swaras")
cursor.execute("DROP TABLE IF EXISTS melakartas")

# -----------------------------------------------------------------
# 1. Create melakartas table
# -----------------------------------------------------------------
cursor.execute("""
CREATE TABLE melakartas (
    melakartha_number INT PRIMARY KEY,
    raaga_name VARCHAR(100) NOT NULL,
    arohanam VARCHAR(255) NOT NULL,
    avarohanam VARCHAR(255) NOT NULL
)
""")

# 72 Melakarta Ragas
melakartha_data = [
    (1, "Kanakangi", "Sa R1 G1 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G1 R1 Sa"),
    (2, "Ratnangi", "Sa R1 G1 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G1 R1 Sa"),
    (3, "Ganamurti", "Sa R1 G1 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G1 R1 Sa"),
    (4, "Vanaspati", "Sa R1 G1 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G1 R1 Sa"),
    (5, "Manavati", "Sa R1 G1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G1 R1 Sa"),
    (6, "Tanarupi", "Sa R1 G1 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G1 R1 Sa"),
    (7, "Senavati", "Sa R1 G2 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G2 R1 Sa"),
    (8, "Hanumatodi", "Sa R1 G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    (9, "Dhenuka", "Sa R1 G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G2 R1 Sa"),
    (10, "Natakapriya", "Sa R1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R1 Sa"),
    (11, "Kokilapriya", "Sa R1 G2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
    (12, "Rupavati", "Sa R1 G2 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G2 R1 Sa"),
    (13, "Gayakapriya", "Sa R1 G3 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R1 Sa"),
    (14, "Vakulabharanam", "Sa R1 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
    (15, "Mayamalavagowla", "Sa R1 G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    (16, "Chakravakam", "Sa R1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R1 Sa"),
    (17, "Suryakantam", "Sa R1 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R1 Sa"),
    (18, "Hatakambari", "Sa R1 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G3 R1 Sa"),
    (19, "Jhankaradhvani", "Sa R2 G2 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G2 R2 Sa"),
    (20, "Natabhairavi", "Sa R2 G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    (21, "Keeravani", "Sa R2 G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G2 R2 Sa"),
    (22, "Kharaharapriya", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    (23, "Gourimanohari", "Sa R2 G2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    (24, "Varunapriya", "Sa R2 G2 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G2 R2 Sa"),
    (25, "Mararanjani", "Sa R2 G3 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R2 Sa"),
    (26, "Charukesi", "Sa R2 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 Sa"),
    (27, "Sarasangi", "Sa R2 G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R2 Sa"),
    (28, "Harikambhoji", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    (29, "Dheerasankarabharanam", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    (30, "Naganandini", "Sa R2 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G3 R2 Sa"),
    (31, "Yagapriya", "Sa R3 G3 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R3 Sa"),
    (32, "Ragavardhini", "Sa R3 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R3 Sa"),
    (33, "Gangeyabhushani", "Sa R3 G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R3 Sa"),
    (34, "Vagadheeswari", "Sa R3 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R3 Sa"),
    (35, "Shoolini", "Sa R3 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R3 Sa"),
    (36, "Chalanata", "Sa R3 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G3 R3 Sa"),
    (37, "Salagam", "Sa R1 G1 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G1 R1 Sa"),
    (38, "Jalarnavam", "Sa R1 G1 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G1 R1 Sa"),
    (39, "Jhalavarali", "Sa R1 G1 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G1 R1 Sa"),
    (40, "Navaneetam", "Sa R1 G1 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G1 R1 Sa"),
    (41, "Pavani", "Sa R1 G1 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G1 R1 Sa"),
    (42, "Raghupriya", "Sa R1 G1 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G1 R1 Sa"),
    (43, "Gavambodhi", "Sa R1 G2 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 R1 Sa"),
    (44, "Bhavapriya", "Sa R1 G2 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G2 R1 Sa"),
    (45, "Shubhapantuvarali", "Sa R1 G2 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    (46, "Shadvidamargini", "Sa R1 G2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R1 Sa"),
    (47, "Suvarnangi", "Sa R1 G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R1 Sa"),
    (48, "Divyamani", "Sa R1 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G2 R1 Sa"),
    (49, "Dhavalambari", "Sa R1 G3 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G3 R1 Sa"),
    (50, "Namanarayani", "Sa R1 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R1 Sa"),
    (51, "Kamavardhini", "Sa R1 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R1 Sa"),
    (52, "Ramapriya", "Sa R1 G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R1 Sa"),
    (53, "Gamanashrama", "Sa R1 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R1 Sa"),
    (54, "Vishwambari", "Sa R1 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R1 Sa"),
    (55, "Shamalangi", "Sa R2 G2 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 R2 Sa"),
    (56, "Shanmukhapriya", "Sa R2 G2 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G2 R2 Sa"),
    (57, "Simhendramadhyamam", "Sa R2 G2 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R2 Sa"),
    (58, "Hemavati", "Sa R2 G2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R2 Sa"),
    (59, "Dharmavati", "Sa R2 G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R2 Sa"),
    (60, "Neetimati", "Sa R2 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G2 R2 Sa"),
    (61, "Kantamani", "Sa R2 G3 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G3 R2 Sa"),
    (62, "Rishabhapriya", "Sa R2 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R2 Sa"),
    (63, "Latangi", "Sa R2 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R2 Sa"),
    (64, "Vachaspati", "Sa R2 G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R2 Sa"),
    (65, "Mechakalyani", "Sa R2 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    (66, "Chitrambari", "Sa R2 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R2 Sa"),
    (67, "Sucharitra", "Sa R3 G3 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G3 R3 Sa"),
    (68, "Jyotiswarupini", "Sa R3 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R3 Sa"),
    (69, "Dhatuvardhani", "Sa R3 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R3 Sa"),
    (70, "Nasikabhushani", "Sa R3 G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R3 Sa"),
    (71, "Kosalam", "Sa R3 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R3 Sa"),
    (72, "Rasikapriya", "Sa R3 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R3 Sa"),
]

# Insert melakarthas
cursor.executemany("""
INSERT INTO melakartas (melakartha_number, raaga_name, arohanam, avarohanam)
VALUES (%s, %s, %s, %s)
""", melakartha_data)
conn.commit()

# -----------------------------------------------------------------
# 2. Create raagas_audio table
# -----------------------------------------------------------------
cursor.execute("""
CREATE TABLE raagas_audio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    audio_file VARCHAR(255) NOT NULL
)
""")

# Insert audio files
audio_files_inserted = 0
if os.path.exists(AUDIO_DIR):
    for file in os.listdir(AUDIO_DIR):
        if file.endswith(".m4a"):
            name = os.path.splitext(file)[0]
            filepath = os.path.join(AUDIO_DIR, file)
            cursor.execute("""
                INSERT INTO raagas_audio (name, audio_file)
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE
                    audio_file = VALUES(audio_file)
            """, (name, filepath))
            audio_files_inserted += 1
    print(f"✅ Inserted {audio_files_inserted} audio files into raagas_audio table")
else:
    print(f"⚠️  Warning: Audio directory '{AUDIO_DIR}' not found")

# -----------------------------------------------------------------
# 3. Create swaras table
# -----------------------------------------------------------------
cursor.execute("""
CREATE TABLE swaras (
    melakartha_number INT PRIMARY KEY,
    raaga_name VARCHAR(100),
    Sa INT, R1 INT, R2 INT, R3 INT,
    G1 INT, G2 INT, G3 INT,
    M1 INT, M2 INT,
    Pa INT,
    D1 INT, D2 INT, D3 INT,
    N1 INT, N2 INT, N3 INT
)
""")

# Function to map swaras flags from arohanam
def get_swaras_flags(arohanam):
    flags = {
        "Sa":0, "R1":0, "R2":0, "R3":0,
        "G1":0, "G2":0, "G3":0,
        "M1":0, "M2":0,
        "Pa":0,
        "D1":0, "D2":0, "D3":0,
        "N1":0, "N2":0, "N3":0
    }
    for key in flags.keys():
        if key in arohanam:
            flags[key] = 1
    return flags

# Insert swaras
for mel in melakartha_data:
    mel_number = mel[0]
    raaga_name = mel[1]
    arohanam = mel[2]
    flags = get_swaras_flags(arohanam)
    cursor.execute("""
    INSERT INTO swaras (melakartha_number, raaga_name, Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        mel_number, raaga_name,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))

# -----------------------------------------------------------------
# 4. Create melakarta_audio table - Maps each melakarta to its audio file PATH
# -----------------------------------------------------------------
cursor.execute("""
CREATE TABLE melakarta_audio (
    melakartha_number INT PRIMARY KEY,
    raaga_name VARCHAR(100) NOT NULL,
    audio_path VARCHAR(255) NOT NULL,
    FOREIGN KEY (melakartha_number) REFERENCES melakartas(melakartha_number)
)
""")

# Mapping with full path relative to Flask app (audio/filename.mp3)
# This path will work with your Flask route: /audio/<filename>
audio_mapping = [
    (1, "Kanakangi", "audio/kanakangi.mp3"),
    (2, "Ratnangi", "audio/ratnangi.mp3"),
    (3, "Ganamurti", "audio/ganamurti.mp3"),
    (4, "Vanaspati", "audio/vanaspati.mp3"),
    (5, "Manavati", "audio/manavati.mp3"),
    (6, "Tanarupi", "audio/tanarupi.mp3"),
    (7, "Senavati", "audio/senavati.mp3"),
    (8, "Hanumatodi", "audio/hanumatodi.mp3"),
    (9, "Dhenuka", "audio/dhenuka.mp3"),
    (10, "Natakapriya", "audio/natakapriya.mp3"),
    (11, "Kokilapriya", "audio/kokilapriya.mp3"),
    (12, "Rupavati", "audio/rupavati.mp3"),
    (13, "Gayakapriya", "audio/gayakapriya.mp3"),
    (14, "Vakulabharanam", "audio/vakulabharanam.mp3"),
    (15, "Mayamalavagowla", "audio/mayamalavagowla.mp3"),
    (16, "Chakravakam", "audio/chakravakam.mp3"),
    (17, "Suryakantam", "audio/suryakantam.mp3"),
    (18, "Hatakambari", "audio/hatakambari.mp3"),
    (19, "Jhankaradhvani", "audio/jhankaradhwani.mp3"),
    (20, "Natabhairavi", "audio/natabhairavi.mp3"),
    (21, "Keeravani", "audio/keeravani.mp3"),
    (22, "Kharaharapriya", "audio/kharaharapriya.mp3"),
    (23, "Gourimanohari", "audio/gourimanohari.mp3"),
    (24, "Varunapriya", "audio/varunapriya.mp3"),
    (25, "Mararanjani", "audio/mararanjani.mp3"),
    (26, "Charukesi", "audio/charukesi.mp3"),
    (27, "Sarasangi", "audio/sarasangi.mp3"),
    (28, "Harikambhoji", "audio/harikambhoji.mp3"),
    (29, "Dheerasankarabharanam", "audio/dheerasankarabharanam.mp3"),
    (30, "Naganandini", "audio/naganandini.mp3"),
    (31, "Yagapriya", "audio/yagapriya.mp3"),
    (32, "Ragavardhini", "audio/ragavardhini.mp3"),
    (33, "Gangeyabhushani", "audio/gangeyabhushani.mp3"),
    (34, "Vagadheeswari", "audio/vagadheeswari.mp3"),
    (35, "Shoolini", "audio/shulini.mp3"),
    (36, "Chalanata", "audio/chalanata.mp3"),
    (37, "Salagam", "audio/salagam.mp3"),
    (38, "Jalarnavam", "audio/jalarnavam.mp3"),
    (39, "Jhalavarali", "audio/jhalavarali.mp3"),
    (40, "Navaneetam", "audio/navaneetam.mp3"),
    (41, "Pavani", "audio/pavani.mp3"),
    (42, "Raghupriya", "audio/raghupriya.mp3"),
    (43, "Gavambodhi", "audio/gavambodhi.mp3"),
    (44, "Bhavapriya", "audio/bhavapriya.mp3"),
    (45, "Shubhapantuvarali", "audio/shubhapantuvarali.mp3"),
    (46, "Shadvidamargini", "audio/shadvidamargini.mp3"),
    (47, "Suvarnangi", "audio/suvarnangi.mp3"),
    (48, "Divyamani", "audio/divyamani.mp3"),
    (49, "Dhavalambari", "audio/dhavalambari.mp3"),
    (50, "Namanarayani", "audio/namanarayani.mp3"),
    (51, "Kamavardhini", "audio/kamavardhini.mp3"),
    (52, "Ramapriya", "audio/ramapriya.mp3"),
    (53, "Gamanashrama", "audio/gamanashrama.mp3"),
    (54, "Vishwambari", "audio/vishwambari.mp3"),
    (55, "Shamalangi", "audio/shamalangi.mp3"),
    (56, "Shanmukhapriya", "audio/shanmukhapriya.mp3"),
    (57, "Simhendramadhyamam", "audio/simhendramadhyamam.mp3"),
    (58, "Hemavati", "audio/hemavati.mp3"),
    (59, "Dharmavati", "audio/dharmavati.mp3"),
    (60, "Neetimati", "audio/neetimati.mp3"),
    (61, "Kantamani", "audio/kantamani.mp3"),
    (62, "Rishabhapriya", "audio/rishabhapriya.mp3"),
    (63, "Latangi", "audio/latangi.mp3"),
    (64, "Vachaspati", "audio/vachaspati.mp3"),
    (65, "Mechakalyani", "audio/mechakalyani.mp3"),
    (66, "Chitrambari", "audio/chitrambari.mp3"),
    (67, "Sucharitra", "audio/sucharitra.mp3"),
    (68, "Jyotiswarupini", "audio/jyotiswarupini.mp3"),
    (69, "Dhatuvardhani", "audio/dhatuvardhani.mp3"),
    (70, "Nasikabhushani", "audio/nasikabhushani.mp3"),
    (71, "Kosalam", "audio/kosalam.mp3"),
    (72, "Rasikapriya", "audio/rasikapriya.mp3"),
]

# Insert melakarta audio mappings
cursor.executemany("""
    INSERT INTO melakarta_audio (melakartha_number, raaga_name, audio_path)
    VALUES (%s, %s, %s)
""", audio_mapping)

conn.commit()
cursor.close()
conn.close()

print("✅ Tables dropped, recreated, and data inserted successfully.")
print(f"✅ Total melakartas: {len(melakartha_data)}")
print(f"✅ Total audio files in raagas_audio: {audio_files_inserted}")
print(f"✅ Total melakarta audio mappings: {len(audio_mapping)}")
print("\n📁 Audio paths stored as: audio/filename.mp3")
print("🎵 HTML can access via Flask route: /audio/filename or use stored path directly")