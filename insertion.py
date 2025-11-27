################################## melakarta #1: Kanakangi Janya Ragas Insertion ###################################

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

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Melakarta name (for folder path)
MELAKARTA_NAME = "kanakangi"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Janya Ragas of Kanakangi (Melakarta #1)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Kanakāmbari", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G1 R1 Sa"),
    ("Kanakatodi", "Sa R1 G1 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 R1 Sa"),
    ("Mādhavapriyā", "Sa R1 G1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa G1 R1 Sa"),
    ("Karnataka Shuddha Sāveri", "Sa R1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R1 Sa"),
    ("Latantapriya", "Sa R1 G1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R1 Sa"),
    ("Lāvangi", "Sa R1 M1 D1 Sa higher", "Sa higher D1 M1 R1 Sa"),
    ("Megha", "Sa R1 M1 Pa D1 N1 D1 Pa Sa higher", "Sa higher N1 D1 Pa M1 R1 Sa"),
    ("Rishabhavilāsa", "Sa R1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R1 M1 R1 Sa"),
    ("Sarvashree", "Sa M1 Pa Sa higher", "Sa higher Pa M1 Sa"),
    ("Suddha Mukhāri", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G1 R1 Sa"),
    ("Tatillatika", "Sa R1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R1 Sa"),
    ("Vāgeeshwari", "Sa R1 G1 M1 Pa D1 Sa higher", "Sa higher D1 M1 Pa G1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Kanakangi table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kanakangi table
    cursor.execute(f"""
    INSERT INTO `Kanakangi` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Kanakangi table!")
print("🎵 Table: Kanakangi (Melakarta #1)")


################################## melakarta #2:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "ratnangi"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Ratnangi (Melakarta #2)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Phenadhyuti", "Sa R1 M1 Pa D1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G1 R1 Sa"),
    ("Ganamukhāri", "Sa R1 M1 D1 Sa higher", "Sa higher N2 D1 M1 R1 Sa"),
    ("Ratnavarāli", "Sa R1 M1 Pa N2 D1 Sa higher", "Sa higher N2 Pa M1 R1 G1 R1 Sa"),
    ("Revati", "Sa R1 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R1 Sa"),
    ("Shreemani", "Sa R1 G1 Pa D1 Sa higher", "Sa higher N2 D1 Pa G1 R1 Sa"),
    ("Shreemati", "Sa R1 G1 Pa D1 Sa higher", "Sa higher N2 D1 Pa G1 R1 Sa"),
    ("Svadhya", "Sa R1 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Ratnangi table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Ratnangi table
    cursor.execute(f"""
    INSERT INTO `Ratnangi` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Ratnangi table!")
print("🎵 Table: Ratnangi (Melakarta #2)")


################################## melakarta #3:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "ganamurti"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Ganamurti (Melakarta #3)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Gānasāmavarāli", "Sa R1 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G1 R1 Sa"),
    ("Bhinnapanchamam", "Sa R1 G1 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G1 R1 Sa"),
    ("Nādharanjani", "Sa R1 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G1 R1 Sa"),
    ("Poorvavarāli", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G1 R1 Sa"),
    ("Sāmavarāli", "Sa R1 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G1 R1 G1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Ganamurti table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Ganamurti table
    cursor.execute(f"""
    INSERT INTO `Ganamurti` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Ganamurti table!")
print("🎵 Table: Ganamurti (Melakarta #3)")

################################## melakarta #4:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "vanaspati"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Vanaspati (Melakarta #4)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Bhānumati", "N2 Sa M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    ("Rasāli", "Sa R1 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa M1 R1 Sa"),
    ("Vanāvali", "Sa R1 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa M1 R1 Sa"),
    ("Vittalapriya", "Sa R1 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Vanaspati table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Vanaspati table
    cursor.execute(f"""
    INSERT INTO `Vanaspati` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Vanaspati table!")
print("🎵 Table: Vanaspati (Melakarta #4)")

################################## melakarta #5:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "manavati"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Manavati (Melakarta #5)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Manoranjani", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G1 R1 Sa"),
    ("Ghanashyāmalā", "Sa G1 M1 Pa D2 Sa higher", "Sa higher D2 N3 Pa M1 G1 R1 Sa"),
    ("Kunjari", "Sa R1 M1 Pa D2 Pa Sa higher", "Sa higher N3 D2 Pa M1 G1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Manavati table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Manavati table
    cursor.execute(f"""
    INSERT INTO `Manavati` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Manavati table!")
print("🎵 Table: Manavati (Melakarta #5)")


################################## melakarta #6:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "tanarupi"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Tanarupi (Melakarta #6)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Tanukeerti", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 D3 N3 Pa M1 G1 M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Tanarupi table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Tanarupi table
    cursor.execute(f"""
    INSERT INTO `Tanarupi` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Tanarupi table!")
print("🎵 Table: Tanarupi (Melakarta #6)")

################################## melakarta #7:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "senavati"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Senavati (Melakarta #7)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Senāgrani", "Sa R1 G2 R1 M1 G2 M1 Pa N1 D1 Sa higher", "Sa higher N1 D1 Pa M1 G2 M1 G2 R1 Sa"),
    ("Bhogi", "Sa G2 M1 Pa D1 N1 D1 Sa higher", "Sa higher N1 D1 Pa M1 G2 Sa"),
    ("Chitthakarshani", "Sa R1 G2 M1 D1 Sa higher", "Sa higher D1 M1 G2 R1 Sa"),
    ("Navarasa Mālā", "Sa R1 G2 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 R1 Sa"),
    ("Sindhu Gowri", "Sa R1 G2 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 M1 G2 M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Senavati table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Senavati table
    cursor.execute(f"""
    INSERT INTO `Senavati` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Senavati table!")
print("🎵 Table: Senavati (Melakarta #7)")

################################## melakarta #8:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "hanumatodi"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Hanumatodi (Melakarta #8)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Janatodi", "Sa R1 G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Āhiri", "Sa R1 Sa G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
    ("Amrita Dhanyāsi", "Sa R1 G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 R1 Sa"),
    ("Asāveri", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N2 Sa Pa D1 M1 Pa R1 G2 R1 Sa"),
    ("Bhānuchandrika", "Sa M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G1 Sa"),
    ("Bhadratodi", "Sa R1 G2 M1 D1 Sa higher", "Sa higher N2 D1 Pa G2 Sa"),
    ("Bhoopālam", "Sa R1 G2 Pa D1 Sa higher", "Sa higher D1 Pa G2 R1 Sa"),
    ("Chandrikatodi", "Sa G2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G2 Sa"),
    ("Deshikatodi", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Dhanyāsi", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Divyamālati", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 Sa"),
    ("Ghanta", "Sa G2 R2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Kalāsāveri", "Sa R1 G2 Pa N2 Sa higher", "Sa higher N2 Pa G2 R1 Sa"),
    ("Kanakasāveri", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Nāgavarāli", "Sa R1 G2 M1 Pa M1 D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Prabhupriya", "Sa G2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G2 Sa"),
    ("Punnāgatodi", "N1 Sa R1 G2 M1 Pa", "Pa M1 G2 R1 Sa N2 D1"),
    ("Punnagavarali", "N2 Sa R1 G2 M1 Pa D1 N2", "N2 D1 Pa M1 G2 R1 Sa N2"),
    ("Shravanamallika", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    ("Sowjanya", "Sa R1 M1 D1 Sa higher", "Sa higher D1 M1 R1 Sa"),
    ("Shuddha Seemantini", "Sa R1 G2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G2 R1 Sa"),
    ("Shuddha Todi", "Sa R1 G2 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 R1 Sa"),
    ("Sindhubhairavi", "Sa R2 G2 M1 G2 Pa D1 N2 Sa higher", "N2 D1 Pa M1 G2 R1 Sa N2 Sa"),
    ("Srimati", "Sa G2 R1 G2 M1 Pa D1 Pa D2 N2 Sa higher", "Sa higher N2 D1 Pa M1 Pa M1 G2 R1 Sa"),
    ("Swarnamalli", "Sa G2 M1 Pa D1 N1 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Hanumatodi table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Hanumatodi table
    cursor.execute(f"""
    INSERT INTO `Hanumatodi` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Hanumatodi table!")
print("🎵 Table: Hanumatodi (Melakarta #8)")

################################## melakarta #9:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "dhenuka"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Dhenuka (Melakarta #9)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Dhunibhinnashadjam", "Sa R1 G2 R1 Pa M1 Pa N3 Sa higher", "Sa higher D1 Pa M1 G2 R1 Sa"),
    ("Bhinnashadjam", "Sa R1 G2 R1 Pa M1 Pa N3 Sa higher", "Sa higher D1 Pa M1 G2 R1 Sa"),
    ("Mohananāta", "Sa G2 M1 Pa D1 Pa M1 Pa N3 Sa higher", "Sa higher N3 Pa D1 Pa M1 G2 Sa"),
    ("Udayaravichandrika", "Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G2 Sa"),
    ("Vasanthatodi", "Sa R1 G2 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Dhenuka table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Dhenuka table
    cursor.execute(f"""
    INSERT INTO `Dhenuka` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Dhenuka table!")
print("🎵 Table: Dhenuka (Melakarta #9)")

################################## melakarta #10:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "natakapriya"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Natakapriya (Melakarta #10)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Natābharanam", "Sa R1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R1 Sa"),
    ("Alankārapriya", "Sa R1 G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R1 Sa"),
    ("Bhāgyashabari", "Sa R1 G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R1 Sa"),
    ("Deeparamu", "Sa R1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R1 Sa"),
    ("Gunāvati", "Sa R1 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 R1 Sa"),
    ("Hindoladeshikam", "Sa M1 R1 G2 M1 Pa D2 N2 Sa higher", "Sa higher Pa N2 D2 M1 G2 R1 Sa"),
    ("Kanakadri", "Sa R1 G2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R1 Sa"),
    ("Mātangakāmini", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 Sa"),
    ("Nātyadhārana", "Sa R1 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 R1 Sa"),
    ("Niranjana", "Sa R1 G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R1 Sa"),
    ("Shānthabhāshini", "Sa R1 G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 Sa"),
    ("Shivashakti", "Sa G2 M1 D2 Sa higher", "Sa higher N2 D2 M1 G2 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Natakapriya table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Natakapriya table
    cursor.execute(f"""
    INSERT INTO `Natakapriya` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Natakapriya table!")
print("🎵 Table: Natakapriya (Melakarta #10)")

################################## melakarta #11:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "kokilapriya"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kokilapriya (Melakarta #11)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Kokilāravam", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    ("Bhimsen", "Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
    ("Bhakthirasa", "Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G2 Sa"),
    ("Chitramani", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
    ("Jnānachintāmani", "Sa R1 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 R1 Sa"),
    ("Kowmāri", "Sa R1 G2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
    ("Shuddha Lalitha", "Sa Pa M1 D2 N3 Sa higher", "Sa higher N3 Sa D2 Pa M1 G2 R1 Sa"),
    ("Vardhani", "Sa G2 M1 Pa M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
    ("Vasantamalli", "Sa G2 M1 Pa N3 Sa higher", "Sa higher D2 Pa M1 G2 Sa"),
    ("Vasantanārāyani", "Sa R1 G2 M1 Pa Sa higher", "Sa higher N3 D2 Pa M1 G2 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Kokilapriya table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kokilapriya table
    cursor.execute(f"""
    INSERT INTO `Kokilapriya` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Kokilapriya table!")
print("🎵 Table: Kokilapriya (Melakarta #11)")

################################## melakarta #12:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "rupavati"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Rupavati (Melakarta #12)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Rowpyanaka", "Sa M1 Pa D3 N3 Sa higher", "Sa higher N3 Pa M1 G2 R1 Sa"),
    ("Shyāmakalyāni", "Sa M1 G2 M1 Pa D3 N3 Sa higher", "Sa higher N3 Pa D3 N3 Pa M1 G2 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Rupavati table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Rupavati table
    cursor.execute(f"""
    INSERT INTO `Rupavati` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Rupavati table!")
print("🎵 Table: Rupavati (Melakarta #12)")

################################## melakarta #13:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path)
MELAKARTA_NAME = "gayakapriya"

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_name):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_name}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Gayakapriya (Melakarta #13)
# Format: (Display Name, Arohanam, Avarohanam)
janya_ragas_data = [
    ("Geya Hejjajji", "Sa R1 M1 G3 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Hejjajji", "Sa R1 G3 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R1 Sa"),
    ("Kalākānti", "Sa R1 G3 M1 D1 N1 Sa higher", "Sa higher N1 D1 Pa G3 R1 Sa"),
    ("Kalkada", "Sa R1 G3 Pa D1 N1 Sa higher Sa R1 G3 Pa D1 Sa higher", "Sa higher N1 D1 Pa G3 R1 Sa"),
    ("Kalpanadhārini", "Sa G3 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_NAME)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into Gayakapriya table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Gayakapriya table
    cursor.execute(f"""
    INSERT INTO `Gayakapriya` 
    (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
     Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into Gayakapriya table!")
print("🎵 Table: Gayakapriya (Melakarta #13)")

################################## melakarta #14:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Vakulabharanam"
MELAKARTA_FOLDER = "vakulabharanam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Vakulabharanam (Melakarta #14)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: "Sa higher" represents upper octave Sa (Ṡ)
janya_ragas_data = [
    ("Ahiri", "Sa R1 Sa G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
    ("Vātee Vasantabhairavi", "Sa R1 G3 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G3 R1 Sa"),
    ("Amudhasurabhi", "Sa M1 G3 M1 Pa D1 Sa higher", "Sa higher N2 D1 Pa M1 R1 Sa"),
    ("Devipriya", "Sa G3 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
    ("Kalindaja", "Sa R1 G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 R1 Sa"),
    ("Kuvalayabharanam", "Sa R1 G3 M1 D1 N1 Sa higher", "Sa higher N2 D1 M1 G3 R1 Sa"),
    ("Mukthipradayini", "Sa R1 G3 Pa N2 Sa higher", "Sa higher N2 Pa D1 Pa G3 R1 Sa"),
    ("Sallapa", "Sa G3 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G3 Sa"),
    ("Soma", "Sa R1 Pa M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 Pa M1 G3 R1 Sa"),
    ("Suryā", "Sa G3 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G3 Sa"),
    ("Shuddha Kāmbhoji", "Sa G3 R1 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 R1 Sa"),
    ("Vasantabhairavi", "Sa R1 G3 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 Pa M1 G3 R1 Sa"),
    ("Vasanta Mukhāri", "Sa M1 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
    ("Vijayollāsini", "Sa R1 G3 M1 Pa M1 D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Vakulabharanam table
    cursor.execute(f"""
        INSERT INTO {MELAKARTA_NAME}
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #14)")
print("\n📝 Notes:")
print("   - 'Sa higher' represents upper octave Sa (Ṡ)")
print("   - 'Sa' represents normal octave Sa")

################################## melakarta #15:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Mayamalavagowla"
MELAKARTA_FOLDER = "mayamalavagowla"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("(", "").replace(")", "").replace("{", "").replace("}", "")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Mayamalavagowla (Melakarta #15)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: "Sa higher" represents upper octave Sa (Ṡ)
janya_ragas_data = [
    ("Ardhradesi", "Sa R1 G3 M1 Pa D1 N3 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Bhavini", "Sa G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 Sa"),
    ("Bibhas", "Sa R1 G3 Pa D1 Sa higher", "Sa higher D1 Pa M1 R1 Sa"),
    ("Bowli", "Sa R1 G3 Pa D1 Sa higher", "Sa higher N3 D1 Pa G3 R1 Sa"),
    ("Bowli Ramakriya", "Sa R1 G3 Pa D1 Sa higher", "Sa higher N3 Pa D1 Pa M1 G3 R1 Sa"),
    ("Charuvardhani", "Sa R1 M1 Pa D1 N3 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Chayagowla", "Sa R1 M1 G3 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Chandrachooda", "Sa M1 G3 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 Sa"),
    ("Deshyagowla", "Sa R1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa R1 Sa"),
    ("Devaranji", "Sa M1 Pa D1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 Sa"),
    ("Ekakshari", "Sa R1 G3 M1 Pa D1 N3 Sa higher", "Sa higher N1 Pa M1 R1 G3 M1 R1 Sa"),
    ("Ghanasindhu", "Sa M1 G3 M1 Pa D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Gowla", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 R1 G3 M1 R1 Sa"),
    ("Gowlipantu", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 D1 M1 G3 R1 Sa"),
    ("Gowri", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Gummakambhoji", "Sa R1 G3 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Gundakriya", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N1 Pa D1 Pa M1 G3 R1 Sa"),
    ("Gurjari", "Sa R1 G3 M1 Pa D1 N3 Sa higher", "Sa higher D1 N3 Pa M1 G3 R1 Sa"),
    ("Jaganmohini", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R1 Sa"),
    ("Kalyanakesari", "Sa R1 G3 Pa D1 Sa higher", "Sa higher D1 Pa G3 R1 Sa"),
    ("Kannadabangala", "Sa R1 M1 G3 M1 D1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Karnataka Saranga", "Sa R1 G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 R1 Sa"),
    ("Lalita", "Sa R1 G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G3 R1 Sa"),
    ("Lalitapanchamam", "Sa R1 G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 Pa M1 G3 R1 Sa"),
    ("Malavakurinji", "Sa G3 Pa D1 N3 Sa higher", "Sa higher N3 D1 M1 R1 Sa"),
    ("Malavapanchamam", "Sa R1 G3 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Margadesi", "Sa R1 G3 R1 G3 D1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Malahari", "Sa R1 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Mallikavasatam", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Mangalakaishiki", "Sa R1 M1 G3 D1 Pa Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Manolayam", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 R1 Sa"),
    ("Maruva", "Sa G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 Pa G3 M1 G3 R1 Sa R1 G3 R1 Sa"),
    ("Mechabowli", "Sa R1 G3 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Megharanjani", "Sa R1 G3 M1 Pa N3 Sa higher", "Sa higher N3 M1 G3 R1 Sa"),
    ("Nadanamakriya", "Sa R1 G3 M1 Pa D1 N3", "N3 D1 Pa M1 G3 R1 Sa N1"),
    ("Padi", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 Pa D1 Pa M1 R1 Sa"),
    ("Pharaju", "Sa G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Poornalalitha", "Sa R1 G3 M1 Pa Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R1 Sa"),
    ("Poorvi", "Sa R1 G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Poorvikavasanta", "Sa M1 G3 M1 D N3 Sa higher", "Sa higher N3 D1 M1 Pa M1 G3 R1 Sa"),
    ("Pratapadhanyasi", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Prataparanjani", "Sa R1 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Puranirmai", "Sa R1 G3 Pa D1 Sa higher", "Sa higher N3 D1 Pa G3 R1 Sa"),
    ("Ramakali", "Sa R1 G3 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Ramakriya", "Sa G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 Pa D1 Pa M1 G3 R1 Sa"),
    ("Revagupti", "Sa R1 G3 Pa D1 Sa higher", "Sa higher D1 Pa G3 R1 Sa"),
    ("Rukhmambari", "Sa R1 G3 Pa N3 Sa higher", "Sa higher N3 Pa G3 R1 Sa"),
    ("Samantadeepara", "Sa R1 G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R1 Sa"),
    ("Saranga Nata", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N3 Sa D1 Pa M1 G3 R1 Sa"),
    ("Saveri", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Salanganata", "Sa R1 M1 Pa D1 Sa higher", "Sa higher D1 Pa G3 R1 Sa"),
    ("Satyavati", "Sa G3 R1 G3 Pa D1 Sa higher", "Sa higher N3 D1 N3 Pa D1 Pa G3 R1 Sa"),
    ("Sindhu Ramakriya", "Sa G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 Pa M1 G3 R1 G3 Sa"),
    ("Surasindhu", "Sa M1 G3 M1 Pa N1 D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 G3 R1 Sa"),
    ("Tarakagowla", "Sa G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G3 Sa"),
    ("Takka", "Sa R1 Sa G3 M1 G3 Pa M1 D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    ("Ushavali", "Sa R1 M1 Pa D1 Sa higher", "Sa higher N3 D1 M1 Pa M1 R1 Sa"),
    ("Visharada", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 R1 Sa"),
]

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Mayamalavagowla table
    cursor.execute(f"""
        INSERT INTO {MELAKARTA_NAME}
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #15)")
print("\n📝 Notes:")
print("   - 'Sa higher' represents upper octave Sa (Ṡ)")
print("   - 'Sa' represents normal octave Sa")
print("   - Total ragas: 58")

################################## melakarta #16:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Chakravakam"
MELAKARTA_FOLDER = "chakravakam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Chakravakam (Melakarta #16)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: S = Sa (normal), Ṡ = Sa higher (upper octave), P = Pa
janya_ragas_data = [
    ("Toyavegavāhini", "Sa R1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R1 Sa"),
    ("Ahir Bhairavi", "Sa R1 G3 M1 Pa N2 D2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 Pa G3 R1 Sa"),
    ("Bhakthapriya", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R1 M1 G3 Sa"),
    ("Bhūjāngini", "Sa R1 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R1 Sa"),
    ("Bindhumālini", "Sa G3 R1 G3 M1 Pa N2 Sa higher", "Sa higher N2 Sa D2 Pa G3 M1 Pa G3 R1 Sa"),
    ("Chakranārāyani", "Sa R1 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R1 Sa"),
    ("Ghoshini", "Sa M1 G3 M1 Pa D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R1 Sa"),
    ("Guhapriya", "Sa R1 G3 M1 Pa Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa R1 Sa"),
    ("Kalavati", "Sa R1 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G3 Sa R1 Sa"),
    ("Kokilā", "Sa R1 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R1 Sa"),
    ("Malayamārutam", "Sa R1 G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 R1 Sa"),
    ("Mukthāngi", "Sa R1 G3 M1 Pa D2 N2 Sa higher", "Sa higher D2 N2 Pa M1 G3 R1 Sa"),
    ("Mukundamālini", "Sa R1 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R1 Sa"),
    ("Pūrṇapanchamam", "Pa M1 Sa R1 Sa M1 Pa D2", "D2 Pa M1 G3 R1 Sa N2"),
    ("Pravṛitti", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    ("Rāgamanjari", "Sa R1 M1 Pa D2 Sa higher", "Sa higher N2 D2 M1 R1 Sa"),
    ("Rasikaranjani", "Sa R1 G3 Pa Sa higher", "Sa higher D2 Pa G3 R1 Sa"),
    ("Rudra Panchami", "Sa G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R1 Sa"),
    ("Samya", "Sa R1 G3 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 R1 Sa"),
    ("Shree Nabhomārgini", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa M1 G3 R1 Sa"),
    ("Shyāmali", "Sa G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 R1 Sa"),
    ("Subhāshini", "Sa D2 N2 D2 R1 G3 M1 Pa", "M1 G3 R1 Sa N2 D2 N2 Sa"),
    ("Valaji", "Sa G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 Sa"),
    ("Veenadhāri", "Sa R1 G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R1 Sa"),
    ("Vegavāhini", "Sa R1 G3 M1 D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R1 Sa"),
]

# Note about selected scales:
print("=" * 70)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS:")
print("=" * 70)
for raga in janya_ragas_data:
    print(f"{raga[0]}: {raga[1]} / {raga[2]}")
print("=" * 70)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Chakravakam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #16)")

################################## melakarta #17:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Suryakantam"
MELAKARTA_FOLDER = "suryakantam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Suryakantam (Melakarta #17)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: S = Sa (normal), Ṡ = Sa higher (upper octave), P = Pa
janya_ragas_data = [
    ("Chāyāvathi", "Sa R1 G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R1 Sa"),
    ("Bhairavam", "Sa R1 G3 M1 Pa D2 N3 Sa higher", "Sa higher D2 Pa M1 G3 R1 Sa"),
    ("Haridarpa", "Sa R1 G3 M1 Pa D2 N3 Sa higher", "Sa higher D2 Pa M1 R1 Sa"),
    ("Jayasamvardhani", "Sa G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 Pa M1 G3 R1 Sa"),
    ("Jeevantikā", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 R1 Sa"),
    ("Kusumamāruta", "Sa M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R1 G3 M1 Sa"),
    ("Nāgachoodāmani", "Sa R1 G3 M1 Pa D2 Sa higher", "Sa higher D2 N2 D2 Pa M1 G3 M1 R2 Sa"),
    ("Rohini", "Sa R1 G3 M1 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 M1 G3 R1 Sa"),
    ("Sāmakannada", "Sa R2 M1 G2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 R1 Sa"),
    ("Sowrāshtram", "Sa R1 G3 M1 Pa M1 D2 N3 Sa higher", "Sa higher N3 D2 N2 D2 Pa M1 G3 R1 Sa"),
    ("Suddha Gowla", "Sa R1 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 R1 Sa"),
    ("Supradeepam", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 M1 R1 Sa"),
    ("Vasanthā", "Sa M1 G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 G3 R1 Sa"),
]

# Note about selected scales:
print("=" * 70)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS:")
print("=" * 70)
for raga in janya_ragas_data:
    print(f"{raga[0]}: {raga[1]} / {raga[2]}")
print("=" * 70)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Suryakantam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #17)")

################################## melakarta #18:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Hatakambari"
MELAKARTA_FOLDER = "hatakambari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Hatakambari (Melakarta #18)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: S = Sa (normal), Ṡ = Sa higher (upper octave), P = Pa
janya_ragas_data = [
    ("Jayashuddhamālavi", "Sa R1 G3 M1 Pa N3 Sa higher", "Sa higher N3 D3 Pa M1 G3 R1 Sa"),
    ("Hamsanantini", "Sa G3 M1 Pa Sa higher", "Sa higher Pa M1 G3 R1 Sa"),
    ("Kallola", "Sa Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 G3 R1 Sa"),
    ("Simhala", "Sa R1 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 N3 Pa M1 G3 R1 Sa"),
]

# Note about selected scales:
print("=" * 70)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS:")
print("=" * 70)
for raga in janya_ragas_data:
    print(f"{raga[0]}: {raga[1]} / {raga[2]}")
print("=" * 70)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Hatakambari table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #18)")

################################## melakarta #19:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Jhankaradhvani"
MELAKARTA_FOLDER = "jhankaradhvani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Jhankaradhvani (Melakarta #19)
# Format: (Display Name, Arohanam, Avarohanam)
# Note: S = Sa (normal), Ṡ = Sa higher (upper octave), P = Pa
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
     # Jhankārabhramari - Using the first variant (most commonly used)
     ("Jhankārabhramari", "Sa R2 G2 M1 Pa D1 N1 D1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G2 R2 Sa"),
   
     # Bhārati
     ("Bhārati", "Sa R2 G2 M1 Pa Sa higher", "Sa higher Pa M1 G2 R2 Sa"),
   
     # Chittaranjani - NO Sa higher at the end (as per image)
     ("Chittaranjani", "Sa R2 G2 M1 Pa D1 N1", "N1 D1 Pa M1 G2 R2 Sa"),
   
     # Jalmika
     ("Jalmika", "Sa R2 G1 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G1 Sa R2 Sa"),
   
     # Lalitabhairavi
     ("Lalitabhairavi", "Sa G2 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G2 R2 Sa"),
   
     # Poornalalita - Using the first variant (most commonly used)
     ("Poornalalita", "Sa G2 R2 M1 Pa Sa higher", "Sa higher N1 D1 Pa M1 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nJhankārabhramari - Selected: First variant (most commonly used)")
print("  Other 5 variants exist but first is standard")
print("\nBhārati - Single variant")
print("\nChittaranjani - Single variant (NOTE: No Sa higher at end of arohanam)")
print("\nJalmika - Single variant")
print("\nLalitabhairavi - Single variant")
print("\nPoornalalita - Selected: First variant (most commonly used)")
print("  Other 3 variants exist but first is standard")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Jhankaradhvani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #19)")

################################### melakarta #20:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Natabhairavi"
MELAKARTA_FOLDER = "natabhairavi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Natabhairavi (Melakarta #20)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the images - no modifications

janya_ragas_data = [
    # Nārēretigowla
    ("Nārēretigowla", "Sa G2 R2 G2 M1 N2 D1 M1 N2 N2 Sa higher", "Sa higher N2 D1 M1 G2 M1 Pa M1 G2 R2 Sa"),
    
    # Abheri (Dikshitar School)
    ("Abheri", "Sa M1 G2 M1 Pa Pa Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Anandabhairavi
    ("Anandabhairavi", "Sa G2 R2 G2 M1 Pa D2 Pa Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Amrithavāhini
    ("Amrithavāhini", "Sa R2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 R2 Sa"),
    
    # Bhairavi
    ("Bhairavi", "Sa G2 R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Bhuvanagāndhāri
    ("Bhuvanagāndhāri", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 Sa"),
    
    # Chapagantarva
    ("Chapagantarva", "Sa G2 M1 Pa N2", "D1 M1 G2 R2 Sa N2"),
    
    # Darbāri Kānada
    ("Darbāri Kānada", "N2 Sa R2 G2 R2 Sa M1 Pa D1 N2 Sa higher", "Sa higher D1 N2 Pa M1 Pa G2 M1 R2 Sa"),
    
    # Devakriya
    ("Devakriya", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D1 N2 Pa M1 G2 R2 Sa"),
    
    # Dhanashree
    ("Dhanashree", "N2 Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    
    # Dharmaprakāshini
    ("Dharmaprakāshini", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D1 M1 G2 R2 Sa"),
    
    # Dilipika Vasantha
    ("Dilipika Vasantha", "Sa G2 M1 Pa D1 Pa N2 Sa higher", "Sa higher D1 Pa M1 R2 Sa"),
    
    # Divyagāndhāri
    ("Divyagāndhāri", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 Pa M1 G2 Sa"),
    
    # Gopikāvasantam
    ("Gopikāvasantam", "Sa R2 G2 M1 Pa D1 Pa N2", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Hindolam
    ("Hindolam", "Sa G2 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 Sa"),
    
    # Hindolavasanta
    ("Hindolavasanta", "Sa G2 M1 Pa D1 N2 D1 Sa higher", "Sa higher N2 D1 Pa M1 D2 M1 G2 Sa"),
    
    # Indughantarava
    ("Indughantarava", "Sa G2 M1 Pa D1 Pa", "N2 D1 Pa M1 G2 R2 Sa N2"),
    
    # Jayanthashrī
    ("Jayanthashrī", "Sa G2 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 Pa M1 G2 Sa"),
    
    # Jingala
    ("Jingala", "Sa R2 G2 M1 Pa D1 N2 D1 Pa Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Jaunpuri
    ("Jaunpuri", "Sa R2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Kātyāyani
    ("Kātyāyani", "Sa R2 G2 Pa D1 Sa higher", "Sa higher D1 Pa G2 R2 Sa"),
    
    # Kanakavasantham
    ("Kanakavasantham", "Sa G2 M1 Pa N2 D1 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Kshanika
    ("Kshanika", "Sa G2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G2 Sa"),
    
    # Mānji
    ("Mānji", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D1 Pa M1 Pa M1 Pa G2 R2 Sa"),
    
    # Mahati
    ("Mahati", "Sa G2 Pa D1 N2 Sa higher", "Sa higher N2 Pa G2 R2 Sa"),
    
    # Malkosh
    ("Malkosh", "Sa G2 M1 D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 Sa"),
    
    # mArgahindOLaM
    ("mArgahindOLaM", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 Sa"),
    
    # Nāgagāndhāri
    ("Nāgagāndhāri", "Sa R2 M1 G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Navarathna Vilāsam
    ("Navarathna Vilāsam", "Sa R2 G2 M1 Pa D1 Pa Sa higher", "Sa higher D1 Pa M1 G2 M1 R2 Sa"),
    
    # Nīlamati
    ("Nīlamati", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 Sa"),
    
    # Nīlaveni
    ("Nīlaveni", "Sa R2 G2 M1 Pa D1 N2 D1 Sa higher", "Sa higher D1 Pa M1 G2 R2 Sa"),
    
    # Poornashadjam - Using first variant (most commonly used)
    ("Poornashadjam", "Sa R2 G2 M1 N2 N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Rājarājeshwari
    ("Rājarājeshwari", "Sa R2 M1 Pa D1 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Sāramati
    ("Sāramati", "Sa R2 G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 M1 G2 Sa"),
    
    # Sāranga Kāpi
    ("Sāranga Kāpi", "Sa R1 Pa M1 R1 Pa R1 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    
    # Sharadapriya
    ("Sharadapriya", "Sa R2 G2 Pa N2 Sa higher", "Sa higher N2 Pa G2 R2 Sa"),
    
    # Shree Navarasachandrika
    ("Shree Navarasachandrika", "Sa R2 G2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G2 R2 Sa"),
    
    # Sindhu Dhanyāsi
    ("Sindhu Dhanyāsi", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D1 M1 Pa M1 G2 R2 Sa"),
    
    # Shuddha Desi
    ("Shuddha Desi", "Sa R2 G2 R2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Shuddha Sālavi
    ("Shuddha Sālavi", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Sukumāri
    ("Sukumāri", "Sa G2 M1 Pa N2 D1 N2 Sa higher", "Sa higher N2 Pa M1 G2 M1 R2 Sa"),
    
    # Sushama
    ("Sushama", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R2 Sa"),
    
    # Sutradhāri
    ("Sutradhāri", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R2 Sa"),
    
    # Tarkshika
    ("Tarkshika", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 R2 G2 R2 Sa"),
    
    # Udayarāga
    ("Udayarāga", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 Sa"),
    
    # Vasantavarāli
    ("Vasantavarāli", "Sa R2 M1 Pa D1 Sa higher", "Sa higher N2 D1 Pa G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGES):")
print("=" * 80)
print("\nPoornashadjam - Selected: First variant (most commonly used)")
print("  Second variant exists but first is standard")
print("\nAll other ragas - Single variant as shown in images")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Natabhairavi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #20)")

################################## melakarta #21:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Keeravani"
MELAKARTA_FOLDER = "keeravani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kiravani (Melakarta #21)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Keeranāvali
    ("Keeranāvali", "Sa R2 G2 M1 Pa D1 N3 Sa higher", "Sa higher Pa M1 G2 R2 Sa"),
    
    # Aymmukhan
    ("Aymmukhan", "Sa G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G2 Sa"),
    
    # Bhānupriya
    ("Bhānupriya", "Sa R2 G2 D1 N3 Sa higher", "Sa higher N3 D1 G2 R2 Sa"),
    
    # Beethovanapriya
    ("Beethovanapriya", "G2 Pa N3 Sa R2 G2 M1 Pa D1", "Pa M2 Pa R2 M1 G2 Sa"),
    
    # Chandrika
    ("Chandrika", "Sa R2 G2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa G2 R2 Sa"),
    
    # Gaganabhoopālam
    ("Gaganabhoopālam", "Sa M1 G2 M1 Pa D1 N3", "Sa higher N3 D1 M1 G2 R2 Sa"),
    
    # Hamsapancama
    ("Hamsapancama", "Sa G2 M1 Pa N3 D1 N3 Pa Sa higher", "Sa higher N3 D1 M1 G2 R2 Sa"),
    
    # Hamsavāhini
    ("Hamsavāhini", "Sa R2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 R2 Sa"),
    
    # Jayashree
    ("Jayashree", "Sa R2 G2 M1 Pa D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M1 G2 R2 Sa"),
    
    # Kadaram
    ("Kadaram", "Sa G2 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G2 Sa"),
    
    # Kalyāna Vasantam
    ("Kalyāna Vasantam", "Sa G2 M1 D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G2 R2 Sa"),
    
    # Kusumāvali
    ("Kusumāvali", "Sa G2 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G2 M1 R2 Sa"),
    
    # Mādhavi
    ("Mādhavi", "Sa M1 G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 Sa M1 G2 R2 Sa"),
    
    # Mishramanolayam
    ("Mishramanolayam", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D2 D1 Pa M1 R2 Sa"),
    
    # Priyadarshani
    ("Priyadarshani", "Sa R2 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 R2 Sa"),
    
    # Rishipriya
    ("Rishipriya", "Sa R2 G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 Pa M1 G2 R2 Sa"),
    
    # Sāmapriya
    ("Sāmapriya", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R2 Sa"),
    
    # Shrothasvini
    ("Shrothasvini", "Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G2 Sa"),
    
    # Vasanthamanohari
    ("Vasanthamanohari", "Sa R2 G2 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kiravani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #21)")

################################### melakarta #22:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Kharaharapriya"
MELAKARTA_FOLDER = "kharaharapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ḻ", "l").replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kharaharapriya (Melakarta #22)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the images - no modifications

janya_ragas_data = [
    # Shree
    ("Shree", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa D2 N2 Pa M1 R2 G2 R2 Sa"),
    
    # Andolikā
    ("Andolikā", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 M1 R2 Sa"),
    
    # Abheri
    ("Abheri", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Abhogi
    ("Abhogi", "Sa R2 G2 M1 D2 Sa higher", "Sa higher D2 M1 G2 R2 Sa"),
    
    # Ādi Kāpi
    ("Ādi Kāpi", "Sa R2 M1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Āryamati
    ("Āryamati", "Sa R2 G2 Pa D2 Sa higher", "Sa higher N2 D2 Pa D2 M1 G2 R2 Sa"),
    
    # Agnikopa
    ("Agnikopa", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Bālachandrika
    ("Bālachandrika", "Sa G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Basant Bahār
    ("Basant Bahār", "Sa M2 Pa G3 M2 N3 D1 N3 Sa higher", "R2 Sa N2 D2 Pa M1 G2 M1 G2 R2 Sa"),
    
    # Bageshri
    ("Bageshri", "Sa G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 Pa D2 G2 M1 R2 Sa"),
    
    # Bhagavatapriya
    ("Bhagavatapriya", "Sa R2 G2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Bhagavathpriya
    ("Bhagavathpriya", "Sa R2 G2 M1 R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Bhimpalasi
    ("Bhimpalasi", "N2 Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Brindāvana Sāranga
    ("Brindāvana Sāranga", "Sa R2 M1 Pa N3 Sa higher", "Sa higher N2 Pa M1 R2 G2 R2 Sa"),
    
    # Brindāvani
    ("Brindāvani", "Sa R2 M1 Pa N3 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Chakrapradipta
    ("Chakrapradipta", "Sa R2 G2 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 Sa"),
    
    # Chittaranjani
    ("Chittaranjani", "Sa R2 G2 M1 Pa D2 N2", "N2 D2 Pa M1 G2 R2 Sa"),
    
    # Darbar
    ("Darbar", "Sa R2 M1 Pa D2 N2 Sa higher", "R2 Sa N2 Sa D2 Pa M1 R2 G2 G2 R2 Sa"),
    
    # Dayavati
    ("Dayavati", "Sa R2 G2 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 Sa"),
    
    # Devāmruthavarshani
    ("Devāmruthavarshani", "Sa R2 G2 M1 N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Deva Manohari
    ("Deva Manohari", "Sa R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 R2 Sa"),
    
    # Dhanakāpi
    ("Dhanakāpi", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R2 Sa"),
    
    # Dilipika
    ("Dilipika", "Sa R2 G2 M1 Pa N2 D2 N2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Gowla Kannada
    ("Gowla Kannada", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 Sa"),
    
    # Gāra
    ("Gāra", "Sa G2 M1 Pa D2 N3 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 G2 R2 Sa N3 Sa N2 D2 Sa"),
    
    # Hamsa ābheri
    ("Hamsa ābheri", "Sa G2 Pa M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 Sa"),
    
    # Haridasapriya
    ("Haridasapriya", "Sa Pa M1 G3 M1 Pa N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R2 Sa"),
    
    # Harinārāyani
    ("Harinārāyani", "Sa R2 G2 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Hindustāni Kāpi
    ("Hindustāni Kāpi", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 M1 D2 Pa G2 R2 Sa N2 Sa"),
    
    # Huseni - Using first variant (most commonly used)
    ("Huseni", "Sa R2 G2 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Jatādhāri
    ("Jatādhāri", "Sa R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Jayamanohari
    ("Jayamanohari", "Sa R2 G2 M1 D2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Jayanārāyani
    ("Jayanārāyani", "Sa R2 G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Jayanthasena
    ("Jayanthasena", "Sa G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 Sa"),
    
    # Jog
    ("Jog", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 M1 G2 Sa"),
    
    # Kanadā
    ("Kanadā", "Sa R2 G2 M1 D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 M1 R2 Sa"),
    
    # Kāpi
    ("Kāpi", "Sa R2 M1 Pa N3 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R2 Sa"),
    
    # Kāpijingala
    ("Kāpijingala", "Sa N2 Sa R2 G2 M1", "M1 G2 R2 Sa N2 D2 N2 Sa"),
    
    # Kalānidhi
    ("Kalānidhi", "Sa R2 G2 M1 Sa Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Kalika
    ("Kalika", "Sa R2 G2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G2 R2 Sa"),
    
    # Kannadagowla
    ("Kannadagowla", "Sa R2 G2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 Sa"),
    
    # Karnataka Hindolam
    ("Karnataka Hindolam", "Sa G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 Sa"),
    
    # Karnataka Kāpi
    ("Karnataka Kāpi", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Karnataka Devagāndhari
    ("Karnataka Devagāndhari", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Karnaranjani
    ("Karnaranjani", "Sa R2 G2 M1 G2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Kowmodaki
    ("Kowmodaki", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa G2 Sa"),
    
    # Kowshika
    ("Kowshika", "Sa G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 M1 R2 Sa"),
    
    # Lalitamanohari
    ("Lalitamanohari", "Sa G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Mādhavamanohari
    ("Mādhavamanohari", "Sa R2 G2 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Mālavashree
    ("Mālavashree", "Sa G2 M1 Pa N2 D2 N2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Māyapradeeptam
    ("Māyapradeeptam", "Sa M1 G2 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Madhyamarāvali
    ("Madhyamarāvali", "Sa R2 G2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G2 R2 Sa"),
    
    # Madhyamāvathi
    ("Madhyamāvathi", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Mahānandhi
    ("Mahānandhi", "Sa R2 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R2 Sa"),
    
    # Mandāmari
    ("Mandāmari", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 Sa D2 Pa M1 G2 R2 Sa"),
    
    # Mangalāvathi
    ("Mangalāvathi", "Sa R2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Manirangu
    ("Manirangu", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Manjari
    ("Manjari", "Sa G2 R2 G2 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Manohari
    ("Manohari", "Sa G2 R2 G2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Manorama
    ("Manorama", "Sa R2 G2 M1 Pa D1 Pa Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
    
    # Maruvadhanyāsi
    ("Maruvadhanyāsi", "Sa G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 D2 M1 G2 R2 Sa"),
    
    # Mishramanolayam
    ("Mishramanolayam", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D2 D1 Pa M1 R2 Sa"),
    
    # Mishra shivaranjani
    ("Mishra shivaranjani", "Sa R2 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R2 Sa"),
    
    # Malhar
    ("Malhar", "Sa R2 Pa M1 Pa N2 D2 N3 Sa higher", "Sa higher N2 Pa M1 Pa G2 M1 R2 Sa"),
    
    # Mukhāri
    ("Mukhāri", "Sa R2 M1 Pa N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Nādachintāmani
    ("Nādachintāmani", "Sa R2 G2 M1 N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Nādatārangini
    ("Nādatārangini", "Sa Pa M1 R2 G2 Sa higher", "Sa higher Pa N2 D2 Pa M1 G2 R2 G2 Sa"),
    
    # Nādavarangini
    ("Nādavarangini", "Sa Pa M1 N2 D2 N2 Sa higher", "Sa higher Pa N2 D2 Pa M1 G2 R2 G2 Sa"),
    
    # Nāgari
    ("Nāgari", "Sa R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 Sa"),
    
    # Nāgavalli
    ("Nāgavalli", "Sa R2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 R2 Sa"),
    
    # Nāyaki
    ("Nāyaki", "Sa R2 M1 Pa D2 N2 D2 Pa Sa higher", "Sa higher N2 D2 Pa M1 R2 G2 R2 Sa"),
    
    # Nigamagāmini
    ("Nigamagāmini", "M1 G2 Sa G2 M1 N2 Sa higher", "Sa higher N2 M1 G2 M1 G2 Sa"),
    
    # Nirmalāngi
    ("Nirmalāngi", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Omkāri
    ("Omkāri", "Sa R2 G2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Panchamam
    ("Panchamam", "Sa R2 D2 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Phalamanjari
    ("Phalamanjari", "Sa G2 M1 D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 M1 R2 Sa"),
    
    # Phalaranjani
    ("Phalaranjani", "Sa G2 M1 Pa M1 D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 M1 R2 Sa"),
    
    # Pilu
    ("Pilu", "N3 Sa G3 M1 Pa N3 Sa higher", "Sa higher N2 D2 Pa D1 Pa M1 G2 R2 Sa N3 Sa"),
    
    # Poornakalānidhi
    ("Poornakalānidhi", "Sa G2 M1 Pa D2 N2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Pushpalathika
    ("Pushpalathika", "Sa R2 G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Ratipatipriya
    ("Ratipatipriya", "Sa R2 G2 Pa N2 Sa higher", "Sa higher N2 Pa G2 R2 Sa"),
    
    # Reethigowla
    ("Reethigowla", "Sa G2 R2 G2 M1 N2 D2 M1 N2 N2 Sa higher", "Sa higher N2 D2 M1 G2 M1 Pa M1 G2 R2 Sa"),
    
    # Rudrapriyā
    ("Rudrapriyā", "Sa R2 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 R2 Sa"),
    
    # Sahāna
    ("Sahāna", "Sa R2 G2 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 G2 R2 G2 R2 Sa"),
    
    # Sālagabhairavi
    ("Sālagabhairavi", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Sārang
    ("Sārang", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Saindhavi
    ("Saindhavi", "N2 D2 N2 Sa R2 G2 M1 Pa D2 N2", "D2 Pa M1 G2 R2 Sa N2 D2 N2 Sa"),
    
    # Sangrama
    ("Sangrama", "Sa R2 M1 D2 N2 Pa Sa higher", "Sa higher N2 D2 G2 R2 Sa"),
    
    # Sankrāndanapriyā
    ("Sankrāndanapriyā", "Sa R2 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R2 Sa"),
    
    # Sarvachoodāmani
    ("Sarvachoodāmani", "Sa R2 M1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa D2 N2 D2 Pa M1 G2 R2 G2 R2 Sa"),
    
    # Shivapriyā
    ("Shivapriyā", "Sa R2 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R2 Sa"),
    
    # Shivaranjani
    ("Shivaranjani", "Sa R2 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 R2 Sa"),
    
    # Shree Manohari
    ("Shree Manohari", "Sa G2 R2 G2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G2 R2 Sa"),
    
    # Shree Manoranjani
    ("Shree Manoranjani", "Sa G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Shreeranjani
    ("Shreeranjani", "Sa R2 G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Siddhasena
    ("Siddhasena", "Sa G2 R2 G2 M1 Pa D2 Sa higher", "Sa higher N2 D2 M1 Pa M1 R2 G2 R2 Sa"),
    
    # Suddha Bangāla
    ("Suddha Bangāla", "Sa R2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 R2 G2 R2 Sa"),
    
    # Suddha Bhairavi
    ("Suddha Bhairavi", "Sa G2 M1 Pa N2 D2 Sa higher", "Sa higher N2 D2 M1 G2 R2 Sa"),
    
    # Suddha Dhanyāsi
    ("Suddha Dhanyāsi", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G2 Sa"),
    
    # Suddha Hindolam
    ("Suddha Hindolam", "Sa G2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G2 Sa"),
    
    # Suddha Manohari
    ("Suddha Manohari", "Sa R2 G2 M1 Pa D2 Sa higher", "Sa higher N2 Pa M1 R2 G2 Sa"),
    
    # Suddha Velāvali
    ("Suddha Velāvali", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R2 Sa"),
    
    # Sugunabhooshani
    ("Sugunabhooshani", "Sa G2 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 D2 M1 R2 Sa"),
    
    # Swarabhooshani
    ("Swarabhooshani", "Sa G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Swarakalānidhi
    ("Swarakalānidhi", "Sa M1 G2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G2 R2 Sa"),
    
    # Swararanjani
    ("Swararanjani", "Sa R2 G2 M1 D2 N2 Sa higher", "Sa higher N2 Pa M1 G2 M1 R2 Sa"),
    
    # Tavamukhāri
    ("Tavamukhāri", "Sa R2 G2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G2 R2 Sa"),
    
    # Vajrakānti
    ("Vajrakānti", "Sa G2 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGES):")
print("=" * 80)
print("\nHuseni - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa R2 G2 M2 Pa N2 D2 N2 Sa higher")
print("  Avarohanam: Sa higher N2 D1 Pa M1 G2 R2 Sa")
print("  (Second variant exists: Sa R2 G2 M1 Pa N2 D2 M1 Pa N2 Sa higher / Sa higher N2 Pa D2 M1 G2 R2 Sa)")
print("\nAll other ragas - Single variant as shown in images")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kharaharapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #22)")

################################### melakarta #23:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Gourimanohari"
MELAKARTA_FOLDER = "gourimanohari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Gourimanohari (Melakarta #23)
janya_ragas_data = [    
    # Gowrivelāvali - has two variants
    ("Gowrivelāvali", "Sa R2 G2 Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    # Second variant
    # ("Gowrivelāvali", "Sa R2 G1 G2 Sa R2 M1 M1 Pa D2 D2 Sa higher", "Sa higher N3 D2 Pa M1 G1 G2 R2 Sa"),
    
    # Gowrishankar
    ("Gowrishankar", "Sa R2 G2 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    
    # Hamsadeepika
    ("Hamsadeepika", "Sa R2 G2 M1 D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    
    # Hrudkamali
    ("Hrudkamali", "Sa R2 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 R2 Sa"),
    
    # Lavanthika
    ("Lavanthika", "Sa R2 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 R2 Sa"),
    
    # Sundaramanohari
    ("Sundaramanohari", "Sa R2 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    
    # Patdīp
    ("Patdīp", "N3 Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 Pa G2 M1 G2 R2 Sa"),
    
    # Thyagaraja Mangalam
    ("Thyagaraja Mangalam", "Sa G2 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    
    # Vasantashree (Amba Manohari)
    ("Vasantashree", "Sa R2 G2 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 G2 R2 Sa"),
    
    # Velāvali - has multiple variants, I'll include the most common ones
    ("Velāvali", "Sa G2 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    # Additional variants:
    # ("Velāvali", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    # ("Velāvali", "Sa R2 G2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 Sa"),
    # ("Velāvali", "Sa G2 R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    # ("Velāvali", "Sa R2 G2 Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
    # ("Velāvali", "Sa R2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G2 R2 Sa"),
]

print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    flags = get_swaras_flags(arohanam, avarohanam)
    
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #23)")

#################################### melakarta #24:  Janya Ragas Insertion ###################################


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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Varunapriya"
MELAKARTA_FOLDER = "varunapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Varunapriya (Melakarta #24)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Veeravasantham
    ("Veeravasantham", "Sa R2 G2 M1 Pa Sa higher", "Sa higher N3 D3 Pa M1 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Varunapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #24)")

#################################### melakarta #25:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Mararanjani"
MELAKARTA_FOLDER = "mararanjani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Mararanjani (Melakarta #25)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Sharāvathi
    ("Sharāvathi", "Sa R2 G3 M1 Pa D1 N1 D1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R2 Sa"),
    
    # Devasalaga
    ("Devasalaga", "Sa G3 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R2 Sa"),
    
    # Kesari
    ("Kesari", "Sa R2 G3 M1 Pa M1 D1 Pa D1 Sa higher", "Sa higher D1 N1 D1 Pa M1 G2 R2 Sa"),
    
    # Gayakamandini
    ("Gayakamandini", "Sa R2 G3 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R2 Sa"),
    
    # Rājathilaka
    ("Rājathilaka", "Sa R2 G3 M1 Pa Sa higher", "Sa higher Pa M1 G3 R2 Sa"),
]


# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Mararanjani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #25)")

#################################### melakarta #26:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Charukesi"
MELAKARTA_FOLDER = "charukesi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Charukesi (Melakarta #26)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Tarangini - Using first variant (most commonly used)
    ("Tarangini", "Sa R2 G3 Pa D1 N2 D1 Sa higher", "Sa higher D1 Pa M1 G3 R2 Sa"),
    
    # Chirswaroopi
    ("Chirswaroopi", "Sa R2 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 Sa"),
    
    # Māravi
    ("Māravi", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 Sa"),
    
    # Poorvadhanyāsi
    ("Poorvadhanyāsi", "Sa M1 G3 M1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 Sa"),
    
    # Shiva Manohari
    ("Shiva Manohari", "Sa M1 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 Sa"),
    
    # Shukrajyothi
    ("Shukrajyothi", "Sa R2 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 Pa D1 M1 G3 R2 Sa"),
    
    # Ushābharanam
    ("Ushābharanam", "Sa G3 M1 D1 Pa M1 D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R2 G3 M1 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nTarangini - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa R2 G3 Pa D1 N2 D1 Sa higher")
print("  Avarohanam: Sa higher D1 Pa M1 G3 R2 Sa")
print("  (Second variant exists: Sa R2 G3 Pa D1 N2 D1 Pa D1 Sa higher / Sa higher D1 Pa G2 R2 Sa G3 M1 R2 G3 Sa)")
print("\nAll other ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Charukesi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #26)")

#################################### melakarta #27:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Sarasangi"
MELAKARTA_FOLDER = "sarasangi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Sarasangi (Melakarta #27)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Sowrasenā
    ("Sowrasenā", "Sa R2 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R2 Sa"),
    
    # Haripriya
    ("Haripriya", "Sa R1 G3 M1 Pa Sa higher", "Sa higher N3 D1 Pa M1 G3 Sa"),
    
    # Srirangapriya
    ("Srirangapriya", "Sa R2 G3 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 G3 R2 Sa"),
    
    # Kamalā Manohari
    ("Kamalā Manohari", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 Sa"),
    
    # Madhulika
    ("Madhulika", "Sa R2 G3 M1 N3 Sa higher", "Sa higher N3 M1 G3 R2 Sa"),
    
    # Nalinakānthi
    ("Nalinakānthi", "Sa G3 R2 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R2 Sa"),
    
    # Neelamani
    ("Neelamani", "Sa R2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 R2 Sa"),
    
    # Salavi
    ("Salavi", "Sa G3 R2 G3 M1 Pa D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 R2 Sa"),
    
    # Sarasānana
    ("Sarasānana", "Sa R2 G3 M1 D1 N3 Sa higher", "Sa higher N3 D1 M1 G3 R2 Sa"),
    
    # Saraseeruha
    ("Saraseeruha", "Sa R2 G3 M1 D1 N1 D1 Sa higher", "Sa higher N1 D1 M1 G3 R2"),
    
    # Simhavāhini
    ("Simhavāhini", "Sa G2 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R2 Sa"),
    
    # Surasena
    ("Surasena", "Sa R2 M1 Pa D1 Sa higher", "Sa higher N3 D1 Pa M1 G3 Sa R2 Sa"),
    
    # Sutradhāri
    ("Sutradhāri", "Sa R2 M1 Pa D1 Sa higher", "Sa higher D1 Pa M1 R2 Sa"),
    
    # Vasanthi
    ("Vasanthi", "Sa R2 G3 Pa D1 Sa higher", "Sa higher D1 Pa G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Sutradhāri is marked as '(Also 20)' indicating it also appears in Melakarta #20")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Sarasangi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #27)")

#################################### melakarta #28:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Harikambhoji"
MELAKARTA_FOLDER = "harikambhoji"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Harikambhoji (Melakarta #28)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the images - no modifications

janya_ragas_data = [
    # Harikedāragowla
    ("Harikedāragowla", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Ambhojini
    ("Ambhojini", "Sa R2 G3 M1 D2 Sa higher", "Sa higher D2 M1 G3 R2 Sa"),
    
    # Andhali
    ("Andhali", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 G3 M1 R2 Sa"),
    
    # Aparoopam
    ("Aparoopam", "Sa R2 G3 M1 Pa N2 D2 N2 Sa higher", "Sa higher D2 M1 G3 R2 G3 Sa"),
    
    # Bālahamsa
    ("Bālahamsa", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 R2 M1 G3 Sa"),
    
    # Bahudāri
    ("Bahudāri", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa M1 G3 Sa"),
    
    # Chāyalagakhamās
    ("Chāyalagakhamās", "Sa M1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Chāyatārangini
    ("Chāyatārangini", "Sa R2 M1 G3 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Chandrahasitham
    ("Chandrahasitham", "Sa R2 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R2 Sa"),
    
    # Dasharatipriya
    ("Dasharatipriya", "Sa M1 G3 M1 Pa D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 M1 R2 Sa"),
    
    # Dayaranjani
    ("Dayaranjani", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 M1 G3 Sa"),
    
    # Desh
    ("Desh", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Deshākshi
    ("Deshākshi", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Deshkār
    ("Deshkār", "Sa R2 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Dwaithachintāmani - Using first variant (most commonly used)
    ("Dwaithachintāmani", "Sa G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 Pa G3 R2 Sa"),
    
    # Dwijāvanthi
    ("Dwijāvanthi", "Sa R2 M1 G3 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 M1 R2 G2 R2 Sa N2 D2 N2 Sa"),
    
    # Eēshamanohari
    ("Eēshamanohari", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R2 M1 G3 R2 Sa"),
    
    # Eēshaivaridhi
    ("Eēshaivaridhi", "Sa R2 M1 D2 N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Gāndhāralola
    ("Gāndhāralola", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 M1 G3 R2 Sa"),
    
    # Gāra
    ("Gāra", "Sa G3 M1 Pa D2 N3 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 G2 R2 Sa N3 Sa N2 D2 Sa"),
    
    # Gavati
    ("Gavati", "Sa M1 Pa N2 Sa higher", "Sa higher D2 M1 Pa G3 M1 R2 N2 Sa"),
    
    # Guhamanohari
    ("Guhamanohari", "Sa R2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 R2 Sa"),
    
    # Guharanjani
    ("Guharanjani", "Sa R2 Sa M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 Sa"),
    
    # Hamsaroopini
    ("Hamsaroopini", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Haridasapriya
    ("Haridasapriya", "Sa Pa M1 G3 M1 Pa N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 R2 Sa"),
    
    # Harikedāram
    ("Harikedāram", "Sa R2 G3 M1 Pa D2 N2 Sa N2 Sa higher", "Sa higher N2 Sa D2 N2 D2 Pa M1 G3 R2 Sa"),
    
    # Harini
    ("Harini", "Sa G3 M1 Pa D2 N2 D2 Sa higher", "Sa higher N2 Sa N2 D2 Pa M1 G3 M1 G2 R2 Sa"),
    
    # Harithapriya
    ("Harithapriya", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 G3 R2 Sa"),
    
    # Hemasāranga
    ("Hemasāranga", "Sa R2 G3 M1 Pa D2 N2 D2 Sa higher", "Sa higher Pa M1 G3 R2 Sa"),
    
    # Jaijaiwanti
    ("Jaijaiwanti", "Sa D2 N2 R2 Sa R2 G3 M1 Pa M1 G3 M1 G3 R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa D2 M1 G3 M1 R2 G2 R2 Sa N2 Sa"),
    
    # Jaithshree
    ("Jaithshree", "Sa R2 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Jana Sammodhini
    ("Jana Sammodhini", "Sa R2 G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 R2 Sa"),
    
    # Jayarāma
    ("Jayarāma", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    
    # Jhinjoti
    ("Jhinjoti", "D2 Sa R2 G3 M1 Pa D2 N2", "D2 Pa M1 G3 R2 Sa N2 D2 Pa D2 Sa"),
    
    # Jujahuli
    ("Jujahuli", "Sa M1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    
    # Kāmbhoji
    ("Kāmbhoji", "Sa R2 G3 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa N2 Pa D2 Sa"),
    
    # Kāpi Nārāyani
    ("Kāpi Nārāyani", "Sa R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Khamāj
    ("Khamāj", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Kamās
    ("Kamās", "Sa M1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Karnātaka Behāg
    ("Karnātaka Behāg", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa D2 M1 G3 R2 Sa"),
    
    # Karnātaka Devagāndhāri
    ("Karnātaka Devagāndhāri", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Karnātaka Khamās
    ("Karnātaka Khamās", "Sa G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    
    # Kedāragowla
    ("Kedāragowla", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Keshavapriyā
    ("Keshavapriyā", "Sa R2 Sa M1 Pa D2 N2 Sa higher", "Sa higher N2 Sa Pa M1 G3 R2 Sa"),
    
    # Kokiladhwani
    ("Kokiladhwani", "Sa R2 G3 M1 D2 N2 D2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 R2 Sa"),
    
    # Kokilavarāli
    ("Kokilavarāli", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 M1 Pa M1 G3 R2 G3 Sa"),
    
    # Kunthalavarāli
    ("Kunthalavarāli", "Sa M1 Pa D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 Sa"),
    
    # Mālavi
    ("Mālavi", "Sa R2 G3 M1 Pa N2 M1 D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 M1 R2 Sa"),
    
    # Madhurakokila
    ("Madhurakokila", "Sa R2 G3 D2 N2 Sa higher", "Sa higher N2 D2 G3 R2 Sa"),
    
    # Mahathi
    ("Mahathi", "Sa G3 Pa N2 Sa higher", "Sa higher N2 Pa G3 Sa"),
    
    # Mahuri
    ("Mahuri", "Sa R2 M1 G3 R2 G3 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa R2 G3 R2 Sa"),
    
    # Manjupriya
    ("Manjupriya", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa G3 R2 Sa"),
    
    # Manoharam
    ("Manoharam", "Sa R2 G3 M1 D2 N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Mattakokila
    ("Mattakokila", "Sa R2 Pa D2 N2 D2 Sa higher", "Sa higher D2 N2 D2 Pa R2 Sa"),
    
    # Meghana
    ("Meghana", "Sa M1 G3 M1 Pa D2 Sa higher", "Sa higher N2 D2 M1 G3 Sa"),
    
    # Mohanam
    ("Mohanam", "Sa R2 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Nādavalli
    ("Nādavalli", "Sa R2 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 R2 Sa"),
    
    # Nāgaswarāvali
    ("Nāgaswarāvali", "Sa G3 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G3 Sa"),
    
    # Nārāyanagowla
    ("Nārāyanagowla", "Sa R2 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 G3 Sa"),
    
    # Nārāyani
    ("Nārāyani", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Nāttai Kurinji - Using first variant (most commonly used)
    ("Nāttai Kurinji", "Sa R2 G3 M1 N2 D2 N2 Pa D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 M1 Pa G3 R2 Sa"),
    
    # Nāttai Nārāyani
    ("Nāttai Nārāyani", "Sa R2 G3 M1 D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 M1 R2 Sa"),
    
    # Nandhkowns
    ("Nandhkowns", "Sa G3 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa G3 Sa"),
    
    # Narani
    ("Narani", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Navarasa Kalānidhi
    ("Navarasa Kalānidhi", "Sa R2 M1 Pa Sa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Navarasa kannada
    ("Navarasa kannada", "Sa G3 M1 Pa Sa higher", "Sa higher N2 D2 M1 G3 R2 Sa"),
    
    # Neela
    ("Neela", "Sa G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 Sa"),
    
    # Pārsi
    ("Pārsi", "Sa R2 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Parameshwarapriyā
    ("Parameshwarapriyā", "Sa R2 G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R2 Sa"),
    
    # Pashupathipriyā
    ("Pashupathipriyā", "Sa R2 M1 Pa M1 D2 Sa higher", "Sa higher D2 M1 Pa R2 M1 Sa"),
    
    # Poornakāmbhoji
    ("Poornakāmbhoji", "Sa R2 G3 M1 Pa N2 Sa higher", "Sa higher D2 Pa M1 G3 R2 Sa"),
    
    # Pratāpa Nāttai
    ("Pratāpa Nāttai", "Sa R2 G3 M1 D2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 Sa"),
    
    # Pratāpavarāli
    ("Pratāpavarāli", "Sa R2 M1 Pa D2 Pa Sa higher", "Sa higher D2 Pa M1 G3 R2 Sa"),
    
    # Pravalajyoti
    ("Pravalajyoti", "Sa R2 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    
    # Rāgapanjaramu
    ("Rāgapanjaramu", "Sa R2 M1 Pa D2 N2 D2 Sa higher", "Sa higher N2 D2 M1 R2 Sa"),
    
    # Rāgavinodini
    ("Rāgavinodini", "Sa R2 G3 M1 D2 Sa higher", "Sa higher D2 M1 G3 R2 Sa"),
    
    # Rāgeshree - Using first variant (most commonly used)
    ("Rāgeshree", "Sa G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R2 Sa"),
    
    # Ravi Chandrikā
    ("Ravi Chandrikā", "Sa R2 G3 M1 D2 Sa higher", "Sa higher N2 D2 M1 G3 R2 Sa"),
    
    # Sāvithri
    ("Sāvithri", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 Sa"),
    
    # Sahāna
    ("Sahāna", "Sa R2 G3 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 Sa D2 N2 D2 Pa M1 G3 M1 R2 G3 R2 Sa"),
    
    # Saraswathi Manohari
    ("Saraswathi Manohari", "Sa R2 G3 M1 D2 Sa higher", "Sa higher D2 N2 Pa M1 G3 R2 Sa"),
    
    # Sathvamanjari
    ("Sathvamanjari", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 N2 D2 M1 R2 Sa"),
    
    # Shakunthala
    ("Shakunthala", "Sa R2 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 Sa"),
    
    # Shankaraharigowla
    ("Shankaraharigowla", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Shenchukāmbhoji
    ("Shenchukāmbhoji", "Sa Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Chenjurutti
    ("Chenjurutti", "D2 Sa R2 G3 M1 Pa D2 N2", "N2 D2 Pa M1 G3 R2 Sa N2 D2 Pa D2 Sa"),
    
    # Shiva Kāmbhoji
    ("Shiva Kāmbhoji", "Sa R2 G3 M1 N2 Sa higher", "Sa higher N2 Pa M1 G3 R2 Sa"),
    
    # Surutti
    ("Surutti", "Sa R2 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Pa M1 R2 Sa"),
    
    # Shyāmā - Using first variant (most commonly used)
    ("Shyāmā", "Sa R2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G3 R2 Sa"),
    
    # Simhavikrama
    ("Simhavikrama", "Sa R2 G3 R2 M1 Pa D2 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Sindhu Kannada
    ("Sindhu Kannada", "Sa M1 G3 M1 R2 G3 M1 Pa D2 Pa Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Sindhu Surutti
    ("Sindhu Surutti", "Sa R2 M1 Pa N2 Sa Sa N2 Sa higher", "Sa higher N2 D2 Pa M1 R2 M1 G3 R2 Sa"),
    
    # Suddha Khamās
    ("Suddha Khamās", "Sa M1 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Suddha Varāli
    ("Suddha Varāli", "Sa R2 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 Sa"),
    
    # Suddha
    ("Suddha", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 R2 Sa"),
    
    # Suddhatārangini
    ("Suddhatārangini", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Sumanapriyā
    ("Sumanapriyā", "Sa R2 G3 M1 Pa D2 Pa Sa higher", "Sa higher D2 Sa Pa M1 G3 R2 Sa"),
    
    # Suposhini
    ("Suposhini", "Sa R2 Sa M1 Pa N2 D2 Sa higher", "Sa higher D2 Pa M1 R2 M1 Sa"),
    
    # Suvarnakriyā
    ("Suvarnakriyā", "Sa R2 G3 Pa N2 D2 Sa higher", "Sa higher N2 Pa G3 R2 Sa"),
    
    # Swarāvali
    ("Swarāvali", "Sa M1 G3 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Swaravedi
    ("Swaravedi", "Sa M1 G3 M1 Pa N2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 G3 Sa"),
    
    # Tilakavathi
    ("Tilakavathi", "Sa R2 G3 M1 Pa D2 Pa Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Tilang
    ("Tilang", "Sa G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 G3 Sa"),
    
    # Umābharanam
    ("Umābharanam", "Sa R2 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 Pa M1 R2 G3 M1 R2 Sa"),
    
    # Vaishnavi
    ("Vaishnavi", "Sa R2 G3 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 G3 R2 Sa"),
    
    # Veenavadini
    ("Veenavadini", "Sa R2 G3 Pa N2 Sa higher", "Sa higher N2 Pa G3 R2 Sa"),
    
    # Vivardhani
    ("Vivardhani", "Sa R2 M1 Pa Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Yadukula Kāmbhoji
    ("Yadukula Kāmbhoji", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGES):")
print("=" * 80)
print("\nDwaithachintāmani - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa G3 M1 D2 N2 Sa higher")
print("  Avarohanam: Sa higher N2 D2 M1 Pa G3 R2 Sa")
print("  (Second variant exists: Sa G3 M1 D2 N2 Sa higher / Sa higher N2 D2 M1 G3 R2 Sa)")
print("\nNāttai Kurinji - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa R2 G3 M1 N2 D2 N2 Pa D2 N2 Sa higher")
print("  Avarohanam: Sa higher N2 D2 M1 G3 M1 Pa G3 R2 Sa")
print("  (Second and third variants exist)")
print("\nRāgeshree - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa G3 M1 D2 N2 Sa higher")
print("  Avarohanam: Sa higher N2 D2 M1 G3 R2 Sa")
print("  (Three other variants exist)")
print("\nShyāmā - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa R2 M1 Pa D2 Sa higher")
print("  Avarohanam: Sa higher D2 Pa M1 G3 R2 Sa")
print("  (Second variant exists: Sa R2 G3 Sa R2 Pa M1 D2 D2 Sa higher / Sa higher D2 Pa M1 G3 R2 Sa)")
print("\nAll other ragas - Single variant as shown in images")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Harikambhoji table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #28)")

#################################### melakarta #29:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Dheerasankarabharanam"
MELAKARTA_FOLDER = "dheerasankarabharanam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Dhirasankarabharanam (Melakarta #29)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the images - no modifications

janya_ragas_data = [
    # Ānandharoopa
    ("Ānandharoopa", "Sa R2 G3 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa G3 R2 Sa"),
    
    # Ārābhi - Using first variant (most commonly used)
    ("Ārābhi", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Atāna
    ("Atāna", "Sa R2 M1 Pa N2 Sa higher", "Sa higher N2 D2 Pa M1 G2 M1 R2 Sa"),
    
    # Bangāla
    ("Bangāla", "Sa R2 G3 M1 Pa M1 R2 Pa Sa higher", "Sa higher N3 Pa M1 R2 G3 M1 R2 Sa"),
    
    # Begada
    ("Begada", "Sa G3 R2 G3 M1 Pa D2 Pa Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Behāg
    ("Behāg", "Sa G3 M1 Pa N3 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Behāg Deshikam
    ("Behāg Deshikam", "Sa R2 G3 M1 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 M1 G3 R2 Sa"),
    
    # Bihag
    ("Bihag", "N3 Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 Pa G3 M1 G3 R2 Sa"),
    
    # Bilahari
    ("Bilahari", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Buddhamanohari
    ("Buddhamanohari", "Sa R2 G3 M1 Sa Pa Sa higher", "Sa higher Pa M1 G3 R2 Sa"),
    
    # Buddharanjani
    ("Buddharanjani", "Sa R2 G3 M1 Pa Sa higher", "Sa higher N3 Pa M1 G3 M1 R2 Sa"),
    
    # Chāyā
    ("Chāyā", "Sa Pa M1 Pa D2 Pa N3 R2 Sa higher", "Sa higher D2 Pa M1 Pa D2 Pa G3 M1 R2 Sa"),
    
    # Chāyashankarābharanam
    ("Chāyashankarābharanam", "Sa R1 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R1 Sa"),
    
    # Devagāndhāri
    ("Devagāndhāri", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Dharmalakhi
    ("Dharmalakhi", "Sa M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 Sa"),
    
    # Dhurvanki
    ("Dhurvanki", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Durga
    ("Durga", "Sa R2 M1 D2 Pa D2 Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Gajagowri
    ("Gajagowri", "Sa R2 M1 G3 M1 N3 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 Pa M1 G3 R2 Sa"),
    
    # Garudadhvani
    ("Garudadhvani", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Gowdamalhār
    ("Gowdamalhār", "Sa R2 M1 Pa D2 Sa higher", "Sa higher N3 M1 G3 R2 Sa"),
    
    # Hamsadhwani
    ("Hamsadhwani", "Sa R2 G3 Pa N3 Sa higher", "Sa higher N3 Pa G3 R2 Sa"),
    
    # Hamsavinodhini
    ("Hamsavinodhini", "Sa R2 G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 G3 R2 Sa"),
    
    # Hemant
    ("Hemant", "N3 Sa D2 N3 Sa G3 G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Jana Ranjani
    ("Jana Ranjani", "Sa R2 G3 M1 Pa D2 Pa N3 Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Julavu
    ("Julavu", "Pa D2 N3 Sa R2 G3 M1 Pa", "M1 G3 R2 Sa N3 D2 Pa M1"),
    
    # Kamaripriyā
    ("Kamaripriyā", "Sa G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 M1 G3 M1 R2 Sa"),
    
    # Kannada
    ("Kannada", "Sa R2 G3 M1 Pa M1 D2 N3 Sa higher", "Sa higher N3 Sa D2 Pa M1 G3 M1 G3 M1 R2 Sa"),
    
    # Kathanakuthuhalam
    ("Kathanakuthuhalam", "Sa R2 M1 D2 N3 G3 Pa Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Kaushikadhwani
    ("Kaushikadhwani", "Sa G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 G3 Sa"),
    
    # Kedaram
    ("Kedaram", "Sa M1 G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R2 Sa"),
    
    # Kokilabhāshani
    ("Kokilabhāshani", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 Pa M1 G3 M1 R2 Sa"),
    
    # Kolahalam
    ("Kolahalam", "Sa Pa M1 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Kurinji
    ("Kurinji", "Sa N3 Sa R2 G3 M1 Pa D2", "D2 Pa M1 G3 R2 Sa N3 Sa"),
    
    # Kusumavichithra
    ("Kusumavichithra", "Sa G3 R2 G3 M1 Pa N3 Pa D2 N3 Sa higher", "Sa higher D2 N3 D2 M1 G3 Pa M1 G3 R2 Sa"),
    
    # Kutuhala
    ("Kutuhala", "Sa R2 M1 N3 D2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Lahari
    ("Lahari", "Sa R2 G3 Pa D2 Sa higher", "Sa higher D2 Pa M1 G3 R2 Sa"),
    
    # Mānd
    ("Mānd", "Sa G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Māyadravila
    ("Māyadravila", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N2 Pa M1 Pa G3 M1 R2 Sa"),
    
    # Mohanadhwani
    ("Mohanadhwani", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N3 Pa D2 Pa G3 R2 Sa"),
    
    # Nāgabhooshani
    ("Nāgabhooshani", "Sa R2 M1 Pa D2 N3 Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Nāgadhwani
    ("Nāgadhwani", "Sa R2 Sa M1 G3 M1 Pa N3 D2 N3 Sa higher", "Sa higher N3 D2 N3 Pa M1 G3 Sa"),
    
    # Nārāyanadeshākshi
    ("Nārāyanadeshākshi", "Sa R2 M1 G3 R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Navaroj
    ("Navaroj", "Pa D2 N3 Sa R2 G3 M1 Pa", "M1 G1 R3 Sa N2 D2 Pa"),
    
    # Neelāmbari
    ("Neelāmbari", "Sa R2 G3 M1 Pa D2 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R2 G3 Sa"),
    
    # Niroshta
    ("Niroshta", "Sa R2 G3 D2 N3 Sa higher", "Sa higher N3 D2 G3 R2 Sa"),
    
    # Pahādi
    ("Pahādi", "Sa R2 G3 Pa D2 Pa D2 Sa higher", "N3 D2 Pa G3 M1 G3 R2 Sa N3 D2 Pa D2 Sa"),
    
    # Poornachandrika
    ("Poornachandrika", "Sa R2 G3 M1 Pa D2 Pa Sa higher", "Sa higher N3 Pa M1 R2 G3 M1 R2 Sa"),
    
    # Poornagowla
    ("Poornagowla", "Sa R2 G3 M1 Pa N3 D2 N3 Pa D2 N3 Sa higher", "Sa higher N3 D2 N3 Pa M1 G3 R2 Sa"),
    
    # Poorvagowla
    ("Poorvagowla", "Sa G3 R2 G3 Sa R2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Rathnabhooshani
    ("Rathnabhooshani", "Sa R2 G3 M1 Pa Sa higher", "Sa higher Pa M1 G3 R2 Sa"),
    
    # Reetuviḻāsa
    ("Reetuviḻāsa", "Sa G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 Sa"),
    
    # Sāranga Mallār
    ("Sāranga Mallār", "Sa R2 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 R2 Sa N3 Sa"),
    
    # Shankara
    ("Shankara", "Sa G3 Pa Sa higher", "Sa higher N3 D2 Pa G3 Pa R2 G3 Sa"),
    
    # Shankara
    ("Shankara(hindustani)", "Sa G3 Pa N3 D2 Sa N3 Sa higher", "Sa higher N3 D2 Pa G3 Pa G3 R2 Sa"),
    
    # Shankaraharigowla
    ("Shankaraharigowla", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N2 D2 Pa M1 G3 R2 Sa"),
    
    # Shankaramohana
    ("Shankaramohana", "Sa R2 G3 Pa N3 D2 Sa N3", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Shankari
    ("Shankari", "Sa G3 Pa N3 Sa higher", "Sa higher N3 Pa G3 Sa"),
    
    # Sindhu
    ("Sindhu", "Sa M1 Pa D2 Sa higher", "Sa higher N3 D2 M1 Pa M1 G3 R2 Sa"),
    
    # Sindhu Mandāri
    ("Sindhu Mandāri", "Sa R2 G3 M1 Pa Sa higher", "Sa higher N3 D2 Pa G3 M1 Pa M1 R2 Sa"),
    
    # Suddha Mālavi
    ("Suddha Mālavi", "Sa R2 G3 M1 Pa N3 Sa higher", "Sa higher D2 N3 Pa M1 G3 R2 Sa"),
    
    # Suddha Sārang
    ("Suddha Sārang", "Sa R2 G3 M1 Pa D2 N3 D2 Sa higher", "Sa higher D2 Pa M1 R2 G3 R2 Sa"),
    
    # Suddha Sāveri
    ("Suddha Sāveri", "Sa R2 M1 Pa D2 Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Suddha Vasantha
    ("Suddha Vasantha", "Sa R2 G3 M1 Pa N3 Sa higher", "Sa higher N3 D2 N3 Pa M1 G3 Sa"),
    
    # Suranandini
    ("Suranandini", "Sa R2 G3 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa G3 R2 Sa"),
    
    # Suraranjani
    ("Suraranjani", "Sa G3 Pa R2 M1 D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Tāndavam
    ("Tāndavam", "Sa G3 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa G3 Sa"),
    
    # Vallabhi
    ("Vallabhi", "Sa R2 G3 M1 Pa D2 N3 Sa higher", "Sa higher N3 D2 N3 D2 Pa M1 Pa G3 M1 R2 Sa"),
    
    # Vasanthamalai
    ("Vasanthamalai", "Sa R2 M1 Pa N3 Sa higher", "Sa higher D2 Pa M1 R2 Sa"),
    
    # Vedhāndhagamana
    ("Vedhāndhagamana", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 Sa"),
    
    # Veerapratāpa
    ("Veerapratāpa", "Sa G3 M1 Pa D2 Sa higher", "Sa higher N3 D2 Pa M1 G3 R2 Sa"),
    
    # Vilāsini
    ("Vilāsini", "Sa R2 G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGES):")
print("=" * 80)
print("\nĀrābhi - Selected: First variant (most commonly used)")
print("  Arohanam:   Sa R2 M1 Pa D2 Sa higher")
print("  Avarohanam: Sa higher N3 D2 Pa M1 G3 R2 Sa")
print("  (Second variant exists: Sa R2 M1 Pa D2 Sa higher / Sa higher D2 Pa M1 G3 R2 Sa)")
print("\nAll other ragas - Single variant as shown in images")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Dhirasankarabharanam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #29)")

#################################### melakarta #30:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Naganandini"
MELAKARTA_FOLDER = "naganandini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Naganandini (Melakarta #30)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Nāgabharanam
    ("Nāgabharanam", "Sa R2 G2 M1 Pa D3 N3 Sa higher", "Sa higher N3 D Pa M1 G2 R2 Sa"),
    
    # Gambheeravani
    ("Gambheeravani", "Sa G3 Pa M1 D3 N3 Sa higher", "Sa higher N3 Pa M1 G3 R2 G3 R2 Sa"),
    
    # Lalithāṅdharya
    ("Lalithāṅdharva", "Sa R2 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 Pa G3 R2 Sa"),
    
    # Sāmanta
    ("Sāmanta", "Sa R2 G3 M1 Pa D3 N3 Sa higher", "Sa higher N3 D3 N3 D3 Pa M1 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Naganandini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #30)")


############################################## melakarta #31:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Yagapriya"
MELAKARTA_FOLDER = "yagapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Yagapriya (Melakarta #31)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Kalāvathi
    ("Kalāvathi", "Sa R3 G3 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R3 Sa"),
    
    # Damarugapriya
    ("Damarugapriya", "Sa R3 G3 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa G3 R3 Sa"),
    
    # Desharanjani
    ("Desharanjani", "Sa R3 M1 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 R3 Sa"),
    
    # Deshyathodi
    ("Deshyathodi", "Sa G2 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 R1 Sa"),
    
    # Kalāhamsa
    ("Kalāhamsa", "Sa R3 G3 M1 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G3 R3 Sa"),
    
    # Niranjani
    ("Niranjani", "Sa R3 M1 D1 N1 Sa higher", "Sa higher N1 D1 M1 R3 Sa"),
    
    # Prathāpahamsi
    ("Prathāpahamsi", "Sa G3 M1 Pa N1 D1 N1 Sa higher", "Sa higher N1 D1 Pa M1 G3 M1 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Yagapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #31)")

############################################## melakarta #32:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Ragavardhini"
MELAKARTA_FOLDER = "ragavardhini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Ragavardhini (Melakarta #32)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Rāgachoodāmani
    ("Rāgachoodāmani", "Sa R3 G3 M1 Pa N2 Sa higher", "Sa higher N2 D1 M1 R3 G3 Sa"),
    
    # Amudagāndhāri
    ("Amudagāndhāri", "Sa G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M1 G3 R3 Sa"),
    
    # Dhowmya
    ("Dhowmya", "Sa R3 G3 M1 Pa D1 N2 Pa Sa higher", "Sa higher N2 D1 Pa M1 G3 R3 Sa"),
    
    # Hindoladarbār
    ("Hindoladarbār", "Sa G3 M1 Pa Sa higher", "Sa higher N2 D1 Pa M1 R3 Sa"),
    
    # Ramyā
    ("Ramyā", "Sa R3 G3 M1 Pa D1 N2 Pa Sa higher", "Sa higher N2 D1 Pa M1 G3 R3 Sa"),
    
    # Sāmantajingala
    ("Sāmantajingala", "Sa R3 G3 M1 Pa D1 N2 Sa higher", "Sa higher N2 Pa D1 N2 Pa M1 G3 M1 R3 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Ragavardhini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #32)")

################################################ melakarta #33:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Gangeyabhushani"
MELAKARTA_FOLDER = "gangeyabhushani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Gangeyabhushani (Melakarta #33)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Gangātarangini
    ("Gangātarangini", "Sa R3 G3 M1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 M1 G3 M1 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Gangeyabhushani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #33)")

############################################## melakarta #34:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Vagadheeswari"
MELAKARTA_FOLDER = "vagadheeswari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Vagadhisvari (Melakarta #34)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Amarasindhu
    ("Amarasindhu", "Sa R3 G3 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 R3 Sa"),
    
    # Bhogachāyā Nāttal
    ("Bhogachāyā Nāttai", "Sa R3 G3 R3 G3 M1 Pa N2 N2 Sa higher", "Sa higher N2 D2 N2 Pa Sa N2 Pa M1 M1 R3 Sa"),
    
    # Bhānumanjari
    ("Bhānumanjari", "Sa R3 G3 M1 Pa N2 Sa higher", "Sa higher N2 Pa M1 R3 G3 R3 Sa"),
    
    # Chāyanāttai
    ("Chāyanāttai", "Sa R3 G3 M1 Pa M1 Pa Sa higher", "Sa higher N2 D2 N2 Pa M1 R3 Sa"),
    
    # Maghathi
    ("Maghathi", "Sa R3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M1 R3 Sa"),
    
    # Drāvida Kalāvati
    ("Drāvida Kalāvati", "Sa R3 G3 Pa D2 Sa higher", "Sa higher N2 D2 Pa G3 R3 Sa"),
    
    # Mohanāngi
    ("Mohanāngi", "Sa R3 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 Pa D2 Pa G3 R3 Sa"),
    
    # Murali
    ("Murali", "Sa R3 G3 M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 G3 R3 Sa"),
    
    # Sharadabharana
    ("Sharadabharana", "Sa M1 G3 M1 Pa M1 D2 N2 Sa higher", "Sa higher N2 D2 M1 Pa M1 R3 Sa"),
    
    # Vikhavathi
    ("Vikhavathi", "Sa R3 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Vagadhisvari table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #34)")

############################################## melakarta #35:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Shoolini"
MELAKARTA_FOLDER = "shoolini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Sulini (Melakarta #35)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Shalladeshākshshi
    ("Shailadeshākshhi", "Sa M1 G3 Pa D2 Sa higher", "Sa higher N3 D2 Sa N3 Pa M1 G3 Sa"),
    
    # Suryavasantham
    ("Suryavasantham", "Sa M1 G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 M1 G3 R3 Sa"),
    
    # Dheerahindolam
    ("Dheerahindolam", "Sa G3 M1 D2 N3 Sa higher", "Sa higher N3 D2 Pa M1 G3 R3 Sa"),
    
    # Ganavaridhi (variant 1)
    ("Ganavaridhi", "Sa M1 R3 G3 M1 Pa D2 N2 Sa higher", "Sa higher D2 N2 Pa M1 R3 Sa"),
    
    # Shokavarāli
    ("Shokavarāli", "Sa G3 D2 N3", "D2 Pa M1 G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nGanavaridhi - Using first variant (S M1 R3 G3 M1 P D2 N2 Ṡ)")
print("\nNote: Ganavaridhi has 2 variants in the image. Selected the first one.")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Sulini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #35)")

############################################## melakarta #36:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Chalanata"
MELAKARTA_FOLDER = "chalanata"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Chalanattai (Melakarta #36)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Devanāttai
    ("Devanāttai", "Sa G3 M1 Pa Sa higher", "Sa higher N3 D3 Pa M1 G3 R3 Sa"),
    
    # Gambheeranāttai
    ("Gambheeranāttai", "Sa G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 Sa"),
    
    # Ganaranjani
    ("Ganaranjani", "Sa R3 G3 M1 Pa M1 D3 N3 Sa higher", "Sa higher N3 D3 Pa M1 Pa M1 R3 Sa"),
    
    # Nāttai
    ("Nāttai", "Sa R3 G3 M1 Pa N3 Sa higher", "Sa higher N3 Pa M1 G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Chalanattai table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #36)")

############################################## melakarta #37:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Salagam"
MELAKARTA_FOLDER = "salagam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Salagam (Melakarta #37)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Sowgandhini
    ("Sowgandhini", "Sa R1 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M2 G1 R1 Sa"),
    
    # Bhogasāveri
    ("Bhogasāveri", "Sa R1 M2 D1 N1", "D1 Pa M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Salagam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #37)")

############################################## melakarta #38:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Jalarnavam"
MELAKARTA_FOLDER = "jalarnavam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Jalarnavam (Melakarta #38)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Jaganmohinam
    ("Jaganmohinam", "Sa R1 G1 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G1 R1 Sa"),
    
    # Jaganmohana
    ("Jaganmohana", "Sa R1 G1 M2 Pa D2 Sa higher", "Sa higher N2 D1 Pa M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Jalarnavam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #38)")

############################################## melakarta #39:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Jhalavarali"
MELAKARTA_FOLDER = "jhalavarali"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Jhalavarali (Melakarta #39)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Dhālivarāli
    ("Dhālivarāli", "Sa R1 G1 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G1 R1 Sa"),
    
    # Bhoopālapanchamam
    ("Bhoopālapanchamam", "Sa G1 R1 G1 Pa M2 D1 Sa higher", "Sa higher Pa D1 M2 G1 R1 Sa"),
    
    # Godari
    ("Godari", "Sa R1 G1 R1 M2 G1 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 R1 Sa"),
    
    # Jālasugandhi
    ("Jālasugandhi", "Sa R1 G1 M2 Pa D1 Sa higher", "Sa higher D1 Pa M2 G1 R1 Sa"),
    
    # Janāvali
    ("Janāvali", "Sa G2 R1 G2 M2 Pa D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    
    # Karunāmritavarshini
    ("Karunāmritavarshini", "Sa R1 G1 M2 Pa D1 N3 Pa Sa higher", "Sa higher N3 D1 M2 G1 R1 Sa"),
    
    # Kokilapanchamam
    ("Kokilapanchamam", "Sa G1 R1 G1 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G1 R1 Sa"),
    
    # Varāli
    ("Varāli", "Sa G1 R1 G1 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Jhalavarali table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #39)")

############################################## melakarta #40:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Navaneetam"
MELAKARTA_FOLDER = "navaneetam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Navanitam (Melakarta #40)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Nabhomani
    ("Nabhomani", "Sa G1 R1 G1 M2 Pa Sa higher", "Sa higher N2 D2 Pa M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Navanitam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #40)")

############################################### melakarta #41:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Pavani"
MELAKARTA_FOLDER = "pavani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Pavani (Melakarta #41)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Kumbhini
    ("Kumbhini", "Sa G1 R1 G1 M2 Pa N3 D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G1 R1 Sa"),
    
    # Chandrajyothi
    ("Chandrajyothi", "Sa R1 G1 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 G1 R1 Sa"),
    
    # Prabhāvali
    ("Prabhāvali", "Sa R1 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 M2 Pa M2 R1 G1 R1 Sa"),
    
    # Poornalalitha
    ("Poornalalitha", "Sa R1 M2 G1 R1 M2 Pa N3 D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G1 R1 Sa"),
    
    # Poornapanchamam
    ("Poornapanchamam", "Sa R1 G1 M2 Pa D2", "D2 Pa M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nPoornapanchamam - Note: Image shows '(See 15, 16)' indicating it also appears in Melakartas 15 and 16")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Pavani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #41)")

############################################## melakarta #42:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Raghupriya"
MELAKARTA_FOLDER = "raghupriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Raghupriya (Melakarta #42)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Ravi Kriyā
    ("Ravi Kriyā", "Sa G1 R1 G1 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G1 R1 Sa"),
    
    # Gāndharva
    ("Gāndharva", "M2 Pa D3 N3 Sa R1 G1", "R1 Sa N3 Pa M2 Pa"),
    
    # Gomathi
    ("Gomathi", "Sa R1 G1 M2 Pa D3 N3", "Pa M2 G1 R1 Sa"),
    
    # Raghuleela
    ("Raghuleela", "Sa M2 R1 Pa M2 G1 M2 Pa M2 R1 M2 Pa N3 Sa higher", "Sa higher N3 D3 N3 Pa M2 G1 M2 R1 M2 G1 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Raghupriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #42)")

############################################## melakarta #43:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Gavambodhi"
MELAKARTA_FOLDER = "gavambodhi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Gavambhodi (Melakarta #43)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Geervāni
    ("Geervāni", "Sa R1 G2 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 R1 Sa"),
    
    # Kanchanabowli
    ("Kanchanabowli", "Sa G2 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M1 G2 R1 Sa"),
    
    # Mahathi
    ("Mahathi", "Sa G2 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 Sa"),
    
    # Mechagāndhāri
    ("Mechagāndhāri", "Sa R3 G3 M1 Pa D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M1 G3 M1 R3 Sa"),
    
    # Sūvarnadeepakam
    ("Sūvarnadeepakam", "Sa R1 G2 M2 Pa D1 Sa higher", "Sa higher D1 Pa M2 G2 R1 Sa"),
    
    # Vijayabhooshāvali
    ("Vijayabhooshāvali", "Sa R1 G3 M2 Pa Sa higher", "Sa higher N3 D3 Pa M2 G3 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Gavambhodi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #43)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Ghavāmbhodi - Used the standard arohanam/avarohanam shown")
print("2. Geervāni - Used the standard arohanam/avarohanam shown")
print("3. Kanchanabowli - Used the standard arohanam/avarohanam shown")
print("4. Mahathi - Used the standard arohanam/avarohanam shown")
print("5. Mechagāndhāri - Used the standard arohanam/avarohanam shown")
print("6. Sūvarnadeepakam - Used the standard arohanam/avarohanam shown")
print("7. Vijayabhooshāvali - Used the standard arohanam/avarohanam shown")
print("=" * 80)

############################################### melakarta #44:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Bhavapriya"
MELAKARTA_FOLDER = "bhavapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Bhavapriya (Melakarta #44)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Bhavāni (variant 1)
    ("Bhavāni", "Sa R1 G2 M2 D1 N2 Sa higher", "Sa higher N2 D1 M2 G2 R1 Sa"),
    
    # Kanchanāvathi
    ("Kanchanāvathi", "Sa R1 G2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G2 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nNote: There are TWO ragas named 'Bhavāni' with different scales in the image.")
print("Only the first variant is included (Sa R1 G2 M2 D1 N2 Sa higher)")
print("The second variant with 'Pa D1 P N2' arohanam is listed separately in the image.")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Bhavapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #44)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Bhavapriyā - Used: Sa R1 G2 M2 Pa D1 N2 Sa higher")
print("2. Bhavāni - Used: Sa R1 G2 M2 D1 N2 Sa higher (first variant)")
print("   Note: Second variant 'Sa R1 G2 M2 Pa D1 P N2 Sa higher' not included")
print("3. Kanchanāvathi - Used: Sa R1 G2 M2 Pa N2 Sa higher")
print("=" * 80)
print("\n⚠️  IMPORTANT: There are TWO different 'Bhavāni' entries in the image.")
print("    Only the first one (without Pa in arohanam) was included.")
print("    If you need both variants, they should be named differently")
print("    (e.g., 'Bhavāni 1' and 'Bhavāni 2') to avoid duplicate names.")
print("=" * 80)

############################################### melakarta #45:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Shubhapantuvarali"
MELAKARTA_FOLDER = "shubhapantuvarali"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Subhapantuvarali (Melakarta #45)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Shivapanthuvarāli
    ("Shivapanthuvarāli", "Sa R1 G2 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    
    # Arunāngi
    ("Arunāngi", "Sa R1 M2 Pa N3 D1 Sa higher", "Sa higher N3 D1 M2 R1 G2 R1 Sa"),
    
    # Bandhuvarāli
    ("Bandhuvarāli", "Sa M2 Sa N3 D1 Pa M2", "D1 M2 G2 R1 Sa"),
    
    # Bhānudhanyāsi
    ("Bhānudhanyāsi", "Sa R1 G2 M2 N3 D1 N3", "D1 Pa M2 G2 R1 Sa N3 Sa"),
    
    # Bhānukeeravāni
    ("Bhānukeeravāni", "Sa R1 G2 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 M2 G2 R1 Sa"),
    
    # Chāyaranjani
    ("Chāyaranjani", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 Sa"),
    
    # Dhowreyani
    ("Dhowreyani", "Sa R1 G2 M2 N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    
    # Hindusthāni Todi
    ("Hindusthāni Todi", "N3 R1 G2 M2 D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    
    # Jālakesari
    ("Jālakesari", "Sa R1 M2 Pa D1 N3 Sa higher", "Sa higher D1 Pa M2 R1 Sa"),
    
    # Kumudhachandrikā
    ("Kumudhachandrikā", "Sa G2 M2 D1 Sa higher", "Sa higher N3 D1 M2 G2 R1 Sa"),
    
    # Mahānandhini
    ("Mahānandhini", "Sa M2 G2 M2 Pa D1 N3 Sa higher", "Sa higher D1 N3 D1 Pa M2 G2 R1 Sa"),
    
    # Multani
    ("Multani", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G2 R1 Sa"),
    
    # Parpathi
    ("Parpathi", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 Sa"),
    
    # Shekharachandrikā
    ("Shekharachandrikā", "Sa R1 G2 M2 D1 N3 Sa higher", "Sa higher N3 D1 M2 G2 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Multani is marked as '{Hindustani}' indicating its Hindustani origin")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Subhapantuvarali table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #45)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Subhapantuvarāli - Standard arohanam/avarohanam")
print("2. Shivapanthuvarāli - Standard arohanam/avarohanam")
print("3. Arunāngi - Standard arohanam/avarohanam")
print("4. Bandhuvarāli - Standard arohanam/avarohanam")
print("5. Bhānudhanyāsi - Standard arohanam/avarohanam")
print("6. Bhānukeeravāni - Standard arohanam/avarohanam")
print("7. Chāyaranjani - Standard arohanam/avarohanam")
print("8. Dhowreyani - Standard arohanam/avarohanam")
print("9. Hindusthāni Todi - Standard arohanam/avarohanam")
print("10. Jālakesari - Standard arohanam/avarohanam")
print("11. Kumudhachandrikā - Standard arohanam/avarohanam")
print("12. Mahānandhini - Standard arohanam/avarohanam")
print("13. Multani - Standard arohanam/avarohanam (Hindustani origin)")
print("14. Parpathi - Standard arohanam/avarohanam")
print("15. Shekharachandrikā - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################## melakarta #46:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Shadvidamargini"
MELAKARTA_FOLDER = "shadvidamargini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Sadvidamargini (Melakarta #46)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Sthavarājam
    ("Sthavarājam", "Sa R1 M2 Pa D2 Sa higher", "Sa higher N2 D2 M2 G2 Sa"),
    
    # Ganahemāvati
    ("Ganahemāvati", "Sa G2 M2 Pa N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 Sa"),
    
    # Indhudhanyāsi
    ("Indhudhanyāsi", "Sa G2 M2 D2 N2 Sa higher", "Sa higher N2 D2 Pa D2 M2 G2 R1 Sa"),
    
    # Shreekānti
    ("Shreekānti", "Sa G2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 Sa"),
    
    # Teevravāhini
    ("Teevravāhini", "Sa R1 G2 M2 Pa D2 Pa N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R1 G2 M2 R1 Sa"),
    
    # Vaishalini
    ("Vaishalini", "R1 G2 M2 D2 N2", "N2 D2 M2 G2 R1"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Sadvidamargini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #46)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Sadvidamārgini - Standard arohanam/avarohanam")
print("2. Sthavarājam - Standard arohanam/avarohanam")
print("3. Ganahemāvati - Standard arohanam/avarohanam")
print("4. Indhudhanyāsi - Standard arohanam/avarohanam")
print("5. Shreekānti - Standard arohanam/avarohanam")
print("6. Teevravāhini - Standard arohanam/avarohanam")
print("7. Vaishalini - Standard arohanam/avarohanam (no Sa in either scale)")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("\nNote: Vaishalini uniquely has no 'Sa' in either arohanam or avarohanam.")
print("=" * 80)

############################################### melakarta #47:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Suvarnangi"
MELAKARTA_FOLDER = "suvarnangi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Suvarnangi (Melakarta #47)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Sowveeram
    ("Sowveeram", "Sa R1 G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R1 Sa"),
    
    # Abhiru
    ("Abhiru", "Sa R1 G2 R1 M2 Pa N3 Sa higher", "Sa higher D2 Pa M2 G2 R1 G2 Sa"),
    
    # Rathikā
    ("Rathikā", "Sa M2 G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R1 Sa"),
    
    # Vijayashree
    ("Vijayashree", "Sa R1 G2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G2 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Suvarnangi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #47)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Suvarnāngi - Standard arohanam/avarohanam")
print("2. Sowveeram - Standard arohanam/avarohanam (same as parent melakarta)")
print("3. Abhiru - Standard arohanam/avarohanam")
print("4. Rathikā - Standard arohanam/avarohanam")
print("5. Vijayashree - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################### melakarta #48:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Divyamani"
MELAKARTA_FOLDER = "divyamani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Divyamani (Melakarta #48)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Jeevanthikā
    ("Jeevanthikā", "Sa M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G2 Sa"),
    
    # Deshamukhāri
    ("Deshamukhāri", "Sa R1 G2 M2 Pa D3 N3 D3 Sa higher", "Sa higher D3 N3 D3 Pa M2 G2 R1 Sa"),
    
    # Dundubi
    ("Dundubi", "Sa R1 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G2 R1 Sa"),
    
    # Jeevanthini
    ("Jeevanthini", "Sa M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G2 Sa"),
    
    # Suddha Gāndhāri
    ("Suddha Gāndhāri", "Sa R1 G2 M2 N3 Sa higher", "Sa higher N3 D3 N3 Sa N3 Pa M2 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Divyamani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #48)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Divyamani - Standard arohanam/avarohanam")
print("2. Jeevanthikā - Standard arohanam/avarohanam")
print("3. Deshamukhāri - Standard arohanam/avarohanam")
print("4. Dundubi - Standard arohanam/avarohanam")
print("5. Jeevanthini - Standard arohanam/avarohanam")
print("6. Suddha Gāndhāri - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################## melakarta #49:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Dhavalambari"
MELAKARTA_FOLDER = "dhavalambari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Dhavalambari (Melakarta #49)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Dhavalāngam
    ("Dhavalāngam", "Sa R1 G3 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M2 G3 R1 Sa"),
    
    # Abhirāmam
    ("Abhirāmam", "Sa R1 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 R1 Sa"),
    
    # Bhinnapauarali
    ("Bhinnapauarali", "Sa M2 Pa D1 N1 D1 Sa higher", "Sa higher N1 D1 Pa M2 G3 Sa"),
    
    # Dharmini
    ("Dharmini", "Sa R1 G3 M2 D1 N1 Sa higher", "Sa higher N1 D1 M2 G3 R1 Sa"),
    
    # Sudharmini
    ("Sudharmini", "Sa R1 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 M2 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Dhavalambari table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #49)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Dhavalāmbari - Standard arohanam/avarohanam")
print("2. Dhavalāngam - Standard arohanam/avarohanam")
print("3. Abhirāmam - Standard arohanam/avarohanam")
print("4. Bhinnapauarali - Standard arohanam/avarohanam")
print("5. Dharmini - Standard arohanam/avarohanam")
print("6. Sudharmini - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################## melakarta #50:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Namanarayani"
MELAKARTA_FOLDER = "namanarayani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Namananarayani (Melakarta #50)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Nāmadeshi
    ("Nāmadeshi", "Sa R1 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R1 Sa"),
    
    # Narmada
    ("Narmada", "Sa R1 G3 M2 D1 N2 Sa higher", "Sa higher N2 D1 M2 Pa M2 G3 R1 Sa"),
    
    # Swaramanjari
    ("Swaramanjari", "Sa G3 M2 Pa D1 Sa higher", "Sa higher N2 D1 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Namananarayani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #50)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Nāmanārāyani - Standard arohanam/avarohanam")
print("2. Nāmadeshi - Standard arohanam/avarohanam (same as parent melakarta)")
print("3. Narmada - Standard arohanam/avarohanam")
print("4. Swaramanjari - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################### melakarta #51:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Kamavardhini"
MELAKARTA_FOLDER = "kamavardhini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kamavardhini (Melakarta #51)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Kāshirāmakriyā
    ("Kāshirāmakriyā", "Sa G3 R1 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M1 G3 R1 Sa"),
    
    # Mandāri
    ("Mandāri", "Sa R1 G3 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G3 R1 Sa"),
    
    # ādhi Panchama
    ("ādhi Panchama", "Sa R1 Pa D1 N3 Sa higher", "Sa higher N3 D1 N3 Pa M2 G3 R1 Sa"),
    
    # Basant
    ("Basant", "Sa G3 M2 D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 M2 N3 D1 M2 G3 R1 Sa"),
    
    # Basant Bahār
    ("Basant Bahār", "Sa M2 Pa G3 M2 N3 D1 N3 Sa higher", "R2 Sa N2 D2 Pa M1 G2 M1 G2 R2 Sa"),
    
    # Bhogavasantha
    ("Bhogavasantha", "Sa R1 G3 M2 D1 N3 Sa higher", "Sa higher N3 D1 M2 G3 R1 Sa"),
    
    # Deepakam
    ("Deepakam", "Sa R2 M2 Pa D1 Pa Sa higher", "Sa higher N3 D1 N3 Pa M2 G3 R1 Sa"),
    
    # Gamakapriyā
    ("Gamakapriyā", "Sa R1 G3 M2 Pa N3 D1 Sa higher", "Sa higher D1 Pa M2 G3 R1 Sa"),
    
    # Gamanapriyā
    ("Gamanapriyā", "Sa R1 G3 M2 Pa N3 D1 Sa higher", "Sa higher D1 Pa M2 G3 R1 Sa"),
    
    # Hamsanārāyani
    ("Hamsanārāyani", "Sa R1 G3 M2 Pa Sa higher", "Sa higher N3 Pa M2 G3 R1 Sa"),
    
    # Indumathi
    ("Indumathi", "Sa G3 M2 D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 Sa"),
    
    # Kamalāptapriyā
    ("Kamalāptapriyā", "Sa R1 G3 M2 Pa D1 Sa higher", "Sa higher D1 Pa M2 G3 R1 Sa"),
    
    # Kumudhākriyā
    ("Kumudhākriyā", "Sa R1 G3 M2 D1 Sa higher", "Sa higher N3 D1 M2 G3 R1 Sa"),
    
    # Māruthi
    ("Māruthi", "Sa R1 M2 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R1 Sa"),
    
    # Ponni
    ("Ponni", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G3 R1 Sa"),
    
    # Prathāpa
    ("Prathāpa", "Sa G3 M2 D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R1 Sa"),
    
    # Puriya Dhanashree
    ("Puriya Dhanashree", "N3 R1 G3 M2 Pa D1 Pa N3 Sa higher", "R1 N3 D1 Pa M2 G3 M2 R1 G3 R1 Sa"),
    
    # Tāndavapriyā
    ("Tāndavapriyā", "Sa R1 G3 M2 Pa Sa higher", "Sa higher Pa M2 G3 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Basant is marked as '/Vasant {Hindustani}' indicating Hindustani origin")
print("Note: Basant Bahār is marked as '{Hindustani}' indicating Hindustani origin")
print("Note: Puriya Dhanashree is marked as '{Hindustani}' indicating Hindustani origin")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kamavardhini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #51)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Panthuvarāli - Standard arohanam/avarohanam")
print("2. Kāshirāmakriyā - Standard arohanam/avarohanam")
print("3. Mandāri - Standard arohanam/avarohanam")
print("4. ādhi Panchama - Standard arohanam/avarohanam")
print("5. Basant - Standard arohanam/avarohanam (Hindustani origin)")
print("6. Basant Bahār - Standard arohanam/avarohanam (Hindustani origin)")
print("7. Bhogavasantha - Standard arohanam/avarohanam")
print("8. Deepakam - Standard arohanam/avarohanam")
print("9. Gamakapriyā - Standard arohanam/avarohanam")
print("10. Gamanapriyā - Standard arohanam/avarohanam")
print("11. Hamsanārāyani - Standard arohanam/avarohanam")
print("12. Indumathi - Standard arohanam/avarohanam")
print("13. Kamalāptapriyā - Standard arohanam/avarohanam")
print("14. Kumudhākriyā - Standard arohanam/avarohanam")
print("15. Māruthi - Standard arohanam/avarohanam")
print("16. Ponni - Standard arohanam/avarohanam")
print("17. Prathāpa - Standard arohanam/avarohanam")
print("18. Puriya Dhanashree - Standard arohanam/avarohanam (Hindustani origin)")
print("19. Tāndavapriyā - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("\nNote: Three ragas have Hindustani origin - Basant, Basant Bahār, and Puriya Dhanashree")
print("=" * 80)

############################################### melakarta #52:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Ramapriya"
MELAKARTA_FOLDER = "ramapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Ramapriya (Melakarta #52)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Ramāmanohari
    ("Ramāmanohari", "Sa R1 G3 M2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R1 Sa"),
    
    # Chintaramani
    ("Chintaramani", "Sa G3 M2 Pa D2 N2 Sa higher", "Sa higher D2 Pa M2 G3 R1 Sa"),
    
    # Hamsagamini
    ("Hamsagamini", "Sa G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 D2 Pa M2 G3 R1 Sa"),
    
    # Lokaranjani
    ("Lokaranjani", "Sa G3 M2 Pa M2 D2 N2 Sa higher", "Sa higher N2 D2 N2 Pa M2 G3 R1 Sa"),
    
    # Meghashyāmala
    ("Meghashyāmala", "Sa G3 M2 Pa D2 N2 D2 Pa Sa higher", "Sa higher N2 D2 Pa M2 G3 R1 Sa"),
    
    # Namoveenapaani
    ("Namoveenapaani", "Sa G3 M2 D2 N2 Sa higher", "Sa higher N2 D2 M2 G3 R1 Sa"),
    
    # Patalāmbari
    ("Patalāmbari", "Sa R1 G3 M2 D2 Sa higher", "Sa higher D2 M2 G3 R1 Sa"),
    
    # Raktimārgini
    ("Raktimārgini", "Sa Pa M2 D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 Pa G3 R1 Sa"),
    
    # Rasavinodini
    ("Rasavinodini", "Sa G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 Sa"),
    
    # Reethi Chandrikā
    ("Reethi Chandrikā", "Sa R1 G3 M2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R1 Sa"),
    
    # Seemantinipriyā
    ("Seemantinipriyā", "Sa R1 G3 M2 D2 N2 Sa higher", "Sa higher N2 D2 M2 G3 R1 Sa"),
    
    # Sukhakari
    ("Sukhakari", "Sa R1 Sa Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 Sa R1 Sa"),
    
    # Vedhaswaroopi
    ("Vedhaswaroopi", "Sa R1 G3 M2 Pa D2 N3 Pa Sa higher", "Sa higher N3 D2 Pa N3 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Namoveenapaani is noted as 'creation by Siri Girish'")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Ramapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #52)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Rāmapriyā - Standard arohanam/avarohanam")
print("2. Ramāmanohari - Standard arohanam/avarohanam")
print("3. Chintaramani - Standard arohanam/avarohanam")
print("4. Hamsagamini - Standard arohanam/avarohanam")
print("5. Lokaranjani - Standard arohanam/avarohanam")
print("6. Meghashyāmala - Standard arohanam/avarohanam")
print("7. Namoveenapaani - Standard arohanam/avarohanam (creation by Siri Girish)")
print("8. Patalāmbari - Standard arohanam/avarohanam")
print("9. Raktimārgini - Standard arohanam/avarohanam")
print("10. Rasavinodini - Standard arohanam/avarohanam")
print("11. Reethi Chandrikā - Standard arohanam/avarohanam")
print("12. Seemantinipriyā - Standard arohanam/avarohanam")
print("13. Sukhakari - Standard arohanam/avarohanam")
print("14. Vedhaswaroopi - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("\nNote: Namoveenapaani is a modern creation by Siri Girish")
print("=" * 80)

############################################### melakarta #53:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Gamanashrama"
MELAKARTA_FOLDER = "gamanashrama"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Gamanasrama (Melakarta #53)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Gamakakriyā
    ("Gamakakriyā", "Sa R1 G3 M2 Pa D2 Sa higher", "Sa higher N3 D2 Pa M2 G3 R1 Sa"),
    
    # Alankāri
    ("Alankāri", "Sa G3 M2 D2 N3 D2 Sa higher", "Sa higher N3 D2 M2 G3 Sa"),
    
    # Bhatiyār
    ("Bhatiyār", "Sa D2 Pa D2 M2 Pa G3 M2 D2 Sa higher", "R1 N3 D2 Pa M2 Pa G3 R1 Sa"),
    
    # Dvigāndhārabhooshani
    ("Dvigāndhārabhooshani", "Sa R1 G2 G3 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 G3 G2 R1 Sa D2 Sa"),
    
    # Hamsānandi
    ("Hamsānandi", "Sa R1 G3 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G3 R1 Sa"),
    
    # Mechakāngi
    ("Mechakāngi", "Sa R1 G3 M2 Pa D2 Pa N3 Sa higher", "Sa higher N3 Pa D2 Pa M2 G3 R1 Sa"),
    
    # Padmakalyāni
    ("Padmakalyāni", "Sa G3 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 Sa"),
    
    # Poorvi Kalyāni
    ("Poorvi Kalyāni", "Sa R1 G3 M2 Pa D2 Pa Sa higher", "Sa higher N3 D2 Pa M2 G3 R1 Sa"),
    
    # Sharabadhvāja
    ("Sharabadhvāja", "Sa R1 G3 M2 Pa D2 Sa higher", "Sa higher D2 Pa G3 R1 Sa"),
    
    # Sohini
    ("Sohini", "Sa G3 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G3 R1 Sa"),
    
    # Vaishaka
    ("Vaishaka", "Sa R1 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 N3 Pa M2 G3 M2 R1 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Bhatiyār is marked as '{Hindustani}' indicating Hindustani origin")
print("Note: Hamsānandi is marked in blue indicating special significance")
print("Note: Sohini is marked as '{Hindustani}' indicating Hindustani origin")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Gamanasrama table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #53)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Gamanāśrama - Standard arohanam/avarohanam")
print("2. Gamakakriyā - Standard arohanam/avarohanam")
print("3. Alankāri - Standard arohanam/avarohanam")
print("4. Bhatiyār - Standard arohanam/avarohanam (Hindustani origin)")
print("5. Dvigāndhārabhooshani - Standard arohanam/avarohanam")
print("6. Hamsānandi - Standard arohanam/avarohanam")
print("7. Mechakāngi - Standard arohanam/avarohanam")
print("8. Padmakalyāni - Standard arohanam/avarohanam")
print("9. Poorvi Kalyāni - Standard arohanam/avarohanam")
print("10. Sharabadhvāja - Standard arohanam/avarohanam")
print("11. Sohini - Standard arohanam/avarohanam (Hindustani origin)")
print("12. Vaishaka - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("\nNote: Two ragas have Hindustani origin - Bhatiyār and Sohini")
print("Note: Ignored 'Anya swara* : M₁' note for Bhatiyār as instructed")
print("=" * 80)

############################################### melakarta #54:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Vishwambari"
MELAKARTA_FOLDER = "vishwambari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Visvambari (Melakarta #54)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Vamshavathi
    ("Vamshavathi", "Sa R1 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G3 R1 Sa"),
    
    # Hemāngi
    ("Hemāngi", "Sa R1 G3 M2 D3 Sa higher", "Sa higher D3 M2 G3 R1 Sa"),
    
    # Pooshakalyāni
    ("Pooshakalyāni", "Sa R1 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G3 R1 Sa"),
    
    # Sharadhyuthi
    ("Sharadhyuthi", "Sa R1 G3 M2 Pa D3 N3 D3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R1 Sa"),
    
    # Suddhakriyā
    ("Suddhakriyā", "Sa R1 M2 M2 Pa D3 Sa higher", "Sa higher D3 Pa M2 G3 R1 Sa"),
    
    # Sundarāngi
    ("Sundarāngi", "Sa R1 G3 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa G3 R1 Sa"),
    
    # Vijayavasantham
    ("Vijayavasantham", "Sa M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Visvambari table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #54)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Viśvambari - Standard arohanam/avarohanam")
print("2. Vamshavathi - Standard arohanam/avarohanam")
print("3. Hemāngi - Standard arohanam/avarohanam")
print("4. Pooshakalyāni - Standard arohanam/avarohanam")
print("5. Sharadhyuthi - Standard arohanam/avarohanam")
print("6. Suddhakriyā - Standard arohanam/avarohanam")
print("7. Sundarāngi - Standard arohanam/avarohanam")
print("8. Vijayavasantham - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################### melakarta #55:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Shamalangi"
MELAKARTA_FOLDER = "shamalangi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Samalangi (Melakarta #55)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Shyāmalam
    ("Shyāmalam", "Sa R2 G2 M2 Pa D1 N1 Sa higher", "Sa higher N1 D1 Pa M2 G2 R2 Sa"),
    
    # Deshāvali
    ("Deshāvali", "Sa R2 G2 M2 D1 N1 D1 Sa higher", "Sa higher N1 D1 M2 G2 R2 Sa"),
    
    # Vijayamālavi
    ("Vijayamālavi", "Sa R2 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Samalangi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #55)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Sāmalāngi - Standard arohanam/avarohanam")
print("2. Shyāmalam - Standard arohanam/avarohanam (same as parent melakarta)")
print("3. Deshāvali - Standard arohanam/avarohanam")
print("4. Vijayamālavi - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("=" * 80)

############################################### melakarta #56:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Shanmukhapriya"
MELAKARTA_FOLDER = "shanmukhapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Sanmukhapriya (Melakarta #56)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Chāmaram
    ("Chāmaram", "Sa R2 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G2 R2 Sa"),
    
    # Bhāshini
    ("Bhāshini", "Sa G2 R2 G2 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G2 R1 Sa"),
    
    # Chintāmani
    ("Chintāmani", "Sa G2 R2 G2 M2 G2 R2 G2 Pa M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R2 Sa"),
    
    # Dhanakari
    ("Dhanakari", "Sa G2 Pa D1 N2 Sa higher", "Sa higher N2 D1 M2 G2 Sa"),
    
    # Garigadya
    ("Garigadya", "N2 Sa G2 M2 Pa D1 N2", "D1 Pa M2 G2 R2 Sa"),
    
    # Gopikathilakam
    ("Gopikathilakam", "Sa R2 G2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G2 R2 Sa"),
    
    # Kokilanandhi
    ("Kokilanandhi", "Sa G2 M2 D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G2 Sa"),
    
    # Rājeshwari
    ("Rājeshwari", "Sa R2 G2 Pa N2 Sa higher", "Sa higher N2 D1 Pa M1 G2 Sa"),
    
    # Samudrapriyā
    ("Samudrapriyā", "Sa G2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G2 Sa"),
    
    # Shanmukhi
    ("Shanmukhi", "Sa R1 G2 M2 D1 N2 Sa higher", "Sa higher N2 D1 M2 G2 R1 Sa"),
    
    # Sumanasaranjani
    ("Sumanasaranjani", "Sa G2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G2 Sa"),
    
    # Vasukari
    ("Vasukari", "Sa G2 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 M2 G2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("\nNote: Shanmukhi is marked as '(Trimoorti)' in the image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Sanmukhapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #56)")
print("\n" + "=" * 80)
print("SCALES USED (FROM IMAGE):")
print("=" * 80)
print("1. Sanmukhapriyā - Standard arohanam/avarohanam")
print("2. Chāmaram - Standard arohanam/avarohanam")
print("3. Bhāshini - Standard arohanam/avarohanam")
print("4. Chintāmani - Standard arohanam/avarohanam")
print("5. Dhanakari - Standard arohanam/avarohanam")
print("6. Garigadya - Standard arohanam/avarohanam")
print("7. Gopikathilakam - Standard arohanam/avarohanam")
print("8. Kokilanandhi - Standard arohanam/avarohanam")
print("9. Rājeshwari - Standard arohanam/avarohanam")
print("10. Samudrapriyā - Standard arohanam/avarohanam")
print("11. Shanmukhi - Standard arohanam/avarohanam (Trimoorti)")
print("12. Sumanasaranjani - Standard arohanam/avarohanam")
print("13. Vasukari - Standard arohanam/avarohanam")
print("=" * 80)
print("\nAll ragas use the scales exactly as shown in the image.")
print("No multiple variants were present for any raga.")
print("\nNote: Shanmukhi is marked as '(Trimoorti)' indicating it may be a composition")
print("      or special classification within this raga family.")
print("=" * 80)

############################################### melakarta #57:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Simhendramadhyamam"
MELAKARTA_FOLDER = "simhendramadhyamam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Simhendramadhyamam (Melakarta #57)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Anandavalli
    ("Anandavalli", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 Sa"),
    
    # Ghantana
    ("Ghantana", "Sa R2 G2 M2 D1 N3 Sa higher", "Sa higher N3 D1 M2 G2 R2 Sa"),
    
    # Jayachoodāmani
    ("Jayachoodāmani", "Sa G2 M2 Pa D1 Sa higher", "Sa higher N3 D1 Pa M2 G2 R2 Sa"),
    
    # Pranavapriyā
    ("Pranavapriyā", "Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Sarvāngi
    ("Sarvāngi", "Sa R2 M2 D1 N3 Sa higher", "Sa higher N3 D1 M2 G2 Sa R3 Sa"),
    
    # Seshanādam
    ("Seshanādam", "Sa R2 G2 M2 Pa D1 Sa higher", "Sa higher N3 D1 Pa M2 G2 R2 Sa"),
    
    # Suddha
    ("Suddha", "Sa R2 G2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Sunādapriyā
    ("Sunādapriyā", "Sa R2 G2 M2 Pa Sa higher", "Sa higher N3 D1 Pa M2 G2 R2 Sa"),
    
    # Urmikā
    ("Urmikā", "Sa R2 G2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Vijayasaraswathi
    ("Vijayasaraswathi", "Sa G2 M2 Pa D1 N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #57: {MELAKARTA_NAME} (Sumadhyuti)")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Simhendramadhyamam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #57)")

############################################### melakarta #58:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Hemavati"
MELAKARTA_FOLDER = "hemavati"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Hemavati (Melakarta #58)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Deshisimhāravam
    ("Deshisimhāravam", "Sa R2 G2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R2 Sa"),
    
    # Chandrarekhā
    ("Chandrarekhā", "Sa R2 G2 M2 Pa D2 Sa higher", "Sa higher N2 D2 M2 G2 R2 Sa"),
    
    # Hamsabhramari
    ("Hamsabhramari", "Sa R2 G2 M2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M2 G2 R2 Sa"),
    
    # Hemāmbari
    ("Hemāmbari", "Sa R2 G2 M2 Pa D2 N2 Sa higher", "Sa higher Pa M2 G2 R2 Sa"),
    
    # Hemapriya
    ("Hemapriya", "Sa R2 G2 M2 D2 Sa higher", "Sa higher D2 M2 G2 R2 Sa"),
    
    # Kshemakari
    ("Kshemakari", "Sa R2 M2 D2 N2 Sa higher", "Sa higher N2 D2 M2 R2 Sa"),
    
    # Madhukowns
    ("Madhukowns", "Sa G2 M2 Pa N2 Pa Sa higher", "Sa higher N2 Pa M2 G2 Sa"),
    
    # Shakthiroopini
    ("Shakthiroopini", "Sa G2 M2 D2 Sa higher", "Sa higher N2 D2 M2 G2 Sa"),
    
    # Simhārava
    ("Simhārava", "Sa R2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 R2 G2 R2 Sa"),
    
    # Vijayasāranga
    ("Vijayasāranga", "Sa R2 G2 M2 Pa D2 Sa higher", "Sa higher N2 D2 M2 G2 R2 Sa"),
    
    # Vijayashrāngi
    ("Vijayashrāngi", "Sa R2 G2 M2 Pa D2 Sa higher", "Sa higher N2 D2 M2 G2 R2 Sa"),
    
    # Yāgini
    ("Yāgini", "Sa R2 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #58: {MELAKARTA_NAME}")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Hemavati table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #58)")

############################################### melakarta #59:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Dharmavati"
MELAKARTA_FOLDER = "dharmavati"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Dharmavati (Melakarta #59)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Dhāmavathi
    ("Dhāmavathi", "Sa R2 G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R2 Sa"),
    
    # Sri Tyagaraja
    ("Sri Tyagaraja", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Gowrikriya
    ("Gowrikriya", "Sa G2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 N3 Pa M2 G2 Sa"),
    
    # Karmukhāvati
    ("Karmukhāvati", "Sa R2 G2 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G2 R2 Sa"),
    
    # Karpoora Bharani
    ("Karpoora Bharani", "Sa R2 G2 Pa M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 Pa G2 R2 Sa"),
    
    # Lalitasimhāravam
    ("Lalitasimhāravam", "Sa R2 G2 M2 Pa Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Madhumālti
    ("Madhumālti", "N3 Sa G2 M2 Pa Sa higher", "Sa higher N3 D2 Pa M2 G2 R2 Sa"),
    
    # Madhuvanthi
    ("Madhuvanthi", "Sa G2 M2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 G2 R2 Sa"),
    
    # Moharanjani
    ("Moharanjani", "Sa R2 G2 Pa D2 Sa higher", "Sa higher N3 D2 M2 G2 Sa"),
    
    # Ranjani
    ("Ranjani", "Sa R2 G2 M2 D2 Sa higher", "Sa higher N3 D2 M2 G2 Sa"),
    
    # Varada
    ("Varada", "Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 R2 Sa"),
    
    # Vijayanāgari
    ("Vijayanāgari", "Sa R2 G2 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 G2 R2 Sa"),
    
    # Vishveshwarapriyā
    ("Vishveshwarapriyā", "Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #59: {MELAKARTA_NAME}")
print("\nNotes:")
print("- Sri Tyagaraja: Raga created by Mahesh Mahadev")
print("- Madhumālti: Hindustani raga")
print("- Madhuvanthi: Hindustani raga")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Dharmavati table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #59)")

############################################### melakarta #60:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Neetimati"
MELAKARTA_FOLDER = "neetimati"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Nitimati (Melakarta #60)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Nisshadham
    ("Nisshadham", "Sa R2 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Amarasenapriyā
    ("Amarasenapriyā", "Sa R2 M2 Pa N2 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Deshyagānavaridhi
    ("Deshyagānavaridhi", "Sa R2 G2 M2 Pa D3 N3 Pa Sa higher", "Sa higher N3 Sa Pa M2 G2 R2 Sa"),
    
    # Hamsanādam (first variant)
    ("Hamsanādam", "Sa R2 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 R2 Sa"),
    
    # Kaikavashi
    ("Kaikavashi", "Sa R2 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa M2 G2 R2 Sa"),
    
    # Nuthanachandrikā
    ("Nuthanachandrikā", "Sa R2 G2 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa D3 N3 Pa M2 G2 Sa"),
    
    # Rathnasāranga
    ("Rathnasāranga", "Sa R2 G2 M2 Pa N3 Sa higher", "Sa higher N3 D3 Pa M2 G2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #60: {MELAKARTA_NAME}")
print("\nNote: Hamsanādam has 2 variants shown in the image.")
print("Selected: First variant (Sa R2 M2 Pa D3 N3 Sa higher / Sa higher N3 D3 Pa M2 R2 Sa)")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Nitimati table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #60)")

############################################### melakarta #61:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Kantamani"
MELAKARTA_FOLDER = "kantamani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kantamani (Melakarta #61)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Kunthalam
    ("Kunthalam", "Sa R2 G3 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M2 G3 R2 Sa"),
    
    # Kanakakusumāvali
    ("Kanakakusumāvali", "Sa R2 G3 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 G3 R2 Sa"),
    
    # Shruthiranjani
    ("Shruthiranjani", "Sa R2 G3 M2 Pa D1 N1", "N1 D1 Pa M2 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #61: {MELAKARTA_NAME}")
print("\nNote: Image appears to be cut off - only 3 janya ragas visible")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kantamani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #61)")

############################################### melakarta #62:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Rishabhapriya"
MELAKARTA_FOLDER = "rishabhapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Risabhapriya (Melakarta #62)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Rathipriyā
    ("Rathipriyā", "Sa R2 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R2 Sa"),
    
    # Gopriya
    ("Gopriya", "Sa R2 G3 M2 D1 N2 Sa higher", "Sa higher N2 D1 M2 G3 R2 Sa"),
    
    # Poornasāveri
    ("Poornasāveri", "Sa R2 M2 Pa D1 Sa higher", "Sa higher N2 D1 Pa M2 G3 R2 Sa"),
    
    # Rathnabhānu
    ("Rathnabhānu", "Sa R2 M2 Pa N2 D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 R2 Sa"),
    
    # Suddha Sāranga
    ("Suddha Sāranga", "Sa G3 M2 Pa N2 Sa higher", "Sa higher D1 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #62: {MELAKARTA_NAME}")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Risabhapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #62)")

############################################### melakarta #63:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Latangi"
MELAKARTA_FOLDER = "latangi"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Latangi (Melakarta #63)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Geethapriyā
    ("Geethapriyā", "Sa R2 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R2 Sa"),
    
    # Chitrachandrika
    ("Chitrachandrika", "Sa G3 R2 G3 M2 Pa N3 D1 Sa higher", "Sa higher N3 D1 M2 G3 R2 Sa"),
    
    # Hamsalatha
    ("Hamsalatha", "Sa R2 G3 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R2 Sa"),
    
    # Kananapriyā
    ("Kananapriyā", "Sa R2 G3 M2 Pa M2 D1 N3 Sa higher", "Sa higher D1 N3 Pa M2 G3 R2 Sa"),
    
    # Karunākari
    ("Karunākari", "Sa M2 Pa D1 N3 D1 Sa higher", "Sa higher N3 D1 Pa M2 Sa"),
    
    # Lalithāngi
    ("Lalithāngi", "Sa R2 G3 M2 D1 N3 Sa higher", "Sa higher N3 D1 M2 G3 R2 Sa"),
    
    # Ramani
    ("Ramani", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 Sa"),
    
    # Rathnakānthi
    ("Rathnakānthi", "Sa R2 G3 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G3 R2 Sa"),
    
    # Raviswaroopini
    ("Raviswaroopini", "Sa G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 Sa"),
    
    # Sajjananandhi
    ("Sajjananandhi", "Sa R2 G3 M2 Pa D1 N3 Sa higher", "Sa higher N3 D1 M2 G3 R2 Sa"),
    
    # Skandamanorama
    ("Skandamanorama", "Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #63: {MELAKARTA_NAME}")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Latangi table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #63)")

############################################### melakarta #64:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Vachaspati"
MELAKARTA_FOLDER = "vachaspati"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Vachaspati (Melakarta #64)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Bhooshāvathi
    ("Bhooshāvathi", "Sa R2 G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R2 Sa"),
    
    # Bhagavataranjana
    ("Bhagavataranjana", "Sa R2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R2 Sa"),
    
    # Bhogeeshwari
    ("Bhogeeshwari", "Sa R2 G3 Pa D2 N2 D2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R2 Sa"),
    
    # Bhooshāvali
    ("Bhooshāvali", "Sa R2 G3 M2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R2 Sa"),
    
    # Dwigāndhārabhooshani
    ("Dwigāndhārabhooshani", "Sa R2 G2 G3 G2 Pa D2 Sa higher", "Sa higher D2 Pa G2 G3 G2 R2 Sa D2 Sa"),
    
    # Gaganamohini
    ("Gaganamohini", "Sa G3 Pa D2 N2 Sa higher", "Sa higher N2 Pa M2 G3 Sa"),
    
    # Gurupriya
    ("Gurupriya", "Sa R2 G3 M2 D2 N2 Sa higher", "Sa higher N2 D2 M2 G3 R2 Sa"),
    
    # Hrdhini
    ("Hrdhini", "Sa G3 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G3 Sa"),
    
    # Mangalakari
    ("Mangalakari", "Sa R2 Pa M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa G3 R2 Sa"),
    
    # Mukthidāyini
    ("Mukthidāyini", "Sa G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 Sa"),
    
    # Nādhabrahma
    ("Nādhabrahma", "Sa Pa M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 Sa"),
    
    # Pranavākāri
    ("Pranavākāri", "Pa N2 D2 N2 Sa R2 G3 M2", "Pa M2 G3 R2 Sa N2 D2 N2 Pa"),
    
    # Saraswathi
    ("Saraswathi", "Sa R2 M2 Pa D2 Sa higher", "Sa higher N2 D2 Pa M2 R2 Sa"),
    
    # Shivaranjani
    ("Shivaranjani", "Sa R2 G3 M2 D2 Pa N2 Sa higher", "Sa higher N2 D2 Pa D2 M2 G3 R2 Sa"),
    
    # Triveni
    ("Triveni", "Sa R2 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 R2 Sa"),
    
    # Utthari
    ("Utthari", "Sa G3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #64: {MELAKARTA_NAME}")
print("\nNote: Shivaranjani is marked as '(Original)' in the image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Vachaspati table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #64)")

############################################### melakarta #65:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Mechakalyani"
MELAKARTA_FOLDER = "mechakalyani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Mechakalyani (Melakarta #65)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Shānthakalyāni
    ("Shānthakalyāni", "Sa R2 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    
    # Amritha Kalyani
    ("Amritha Kalyani", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    
    # Amritha Behāg
    ("Amritha Behāg", "Sa M2 G3 Pa N3 Sa higher", "D2 N3 D2 M2 G3 Sa"),
    
    # Aprameya
    ("Aprameya", "Sa R2 M2 Pa D2 Sa higher", "Sa higher N3 D2 M2 G3 M2 R2 Sa"),
    
    # Bhoopkalyāni
    ("Bhoopkalyāni", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    
    # Bhoopāli
    ("Bhoopāli", "Sa R2 G3 Pa D2 Sa higher", "Sa higher D2 Pa G3 R2 Sa"),
    
    # Chandrakāntha
    ("Chandrakāntha", "Sa R2 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 N3 Pa M2 G3 R2 Sa"),
    
    # Hameer
    ("Hameer", "Sa R2 Sa G3 M1 D2 N3 D2 Sa higher", "Sa higher N3 D2 N3 Pa G3 M1 D2 M2 Pa D2 Pa G3 M1 R2 Sa"),
    
    # Hameer Kalyāni (first variant)
    ("Hameer Kalyāni", "Sa Pa M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 M1 G3 Pa M2 R2 Sa"),
    
    # Hamsakalyāni
    ("Hamsakalyāni", "Sa R2 G3 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    
    # Kalyānadāyini
    ("Kalyānadāyini", "Sa R2 G3 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G3 R2 Sa"),
    
    # Kannadamaruva
    ("Kannadamaruva", "Sa G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 Sa"),
    
    # Kedār
    ("Kedār", "Sa M1 G3 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 Pa M1 Sa R2 Sa"),
    
    # Kowmoda
    ("Kowmoda", "Sa R2 G3 M2 N3 Sa higher", "Sa higher N3 Pa M2 G3 Sa"),
    
    # Kunthalashreekānti
    ("Kunthalashreekānti", "Sa G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 Pa M2 G3 R2 Sa"),
    
    # Mohana Kalyāni
    ("Mohana Kalyāni", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N3 D2 Pa M2 G3 R2 Sa"),
    
    # Mrgānandhanā
    ("Mrgānandhanā", "Sa R2 G3 D2 N3 Sa higher", "Sa higher N3 D2 M2 D2 G3 R2 Sa"),
    
    # Nada Kalyani
    ("Nada Kalyani", "Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 D2 M2 G3 R2 Sa"),
    
    # Nāndhakalyāni
    ("Nāndhakalyāni", "Sa G3 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G3 M2 R2 Sa"),
    
    # Pramodhini
    ("Pramodhini", "Sa G3 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 G3 Sa"),
    
    # Rajasadhaka
    ("Rajasadhaka", "Sa R2 G3 Pa D2 Sa higher", "Sa higher N3 Pa M2 R2 Sa"),
    
    # Sāranga (first variant)
    ("Sāranga", "Sa R2 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 R2 G3 M1 R2 Sa"),
    
    # Sāranga Tārangini
    ("Sāranga Tārangini", "Sa R2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 R2 Sa"),
    
    # Shilangi
    ("Shilangi", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G3 Sa"),
    
    # Shuddha Sārang
    ("Shuddha Sārang", "N3 Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 Pa M1 R2 Sa N3 Sa"),
    
    # Suddha Koshala
    ("Suddha Koshala", "Sa G3 M2 Pa Sa higher", "Sa higher N3 D2 M2 G3 R2 Sa"),
    
    # Shyām Kalyān
    ("Shyām Kalyān", "N3 Sa R2 M2 Pa N3 Sa higher", "Sa higher N3 D2 Pa M2 Pa D2 Pa G3 M1 Pa G3 M1 R2 Sa N3 Sa"),
    
    # Sunādavinodini / Hindol
    ("Sunādavinodini", "Sa G3 M2 D2 N3 Sa higher", "Sa higher N3 D2 M2 G3 Sa"),
    
    # Swayambhooshwara Rāga
    ("Swayambhooshwara Rāga", "Sa G3 Pa Sa higher", "Sa higher Pa G3 Sa"),
    
    # Vandanadhārini
    ("Vandanadhārini", "Sa R2 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 R2 Sa"),
    
    # Vivāhapriyā
    ("Vivāhapriyā", "Sa R2 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 R2 Sa"),
    
    # Yamuna Kalyāni / Yaman Kalyan
    ("Yamuna Kalyāni", "Sa R2 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 M1 G3 R2 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #65: {MELAKARTA_NAME}")
print("\nNotes:")
print("- Amritha Kalyani: Raga created by Mahesh Mahadev")
print("- Bhoopāli: Hindustani")
print("- Hameer: Hindustani")
print("- Hameer Kalyāni: Carnatic interpretation of Kedar - First variant selected")
print("- Kedār: Hindustani")
print("- Nada Kalyani: Raga created by Mahesh Mahadev")
print("- Rajasadhaka: Raga created by Mahesh Mahadev")
print("- Sāranga: First variant selected (has 3 variants)")
print("- Shuddha Sārang: Hindustani")
print("- Shyām Kalyān: Hindustani")
print("- Sunādavinodini / Hindol: Hindustani")
print("- Yamuna Kalyāni / Yaman Kalyan: Hindustani")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Mechakalyani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #65)")

############################################### melakarta #66:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Chitrambari"
MELAKARTA_FOLDER = "chitrambari"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Chitrambari (Melakarta #66)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Chaturāngini
    ("Chaturāngini", "Sa R2 G3 M2 Pa N3 Sa higher", "Sa higher N3 D3 N3 Pa G3 M2 G3 R2 Sa"),
    
    # Amritavarshini
    ("Amritavarshini", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 Pa M2 G3 Sa"),
    
    # Chitrasindhu
    ("Chitrasindhu", "Sa G3 M2 Pa N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R2 Sa"),
    
    # Churnikavinodhini
    ("Churnikavinodhini", "Sa R2 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 N3 Pa M2 G3 R2 Sa"),
    
    # Vijayakoshalam
    ("Vijayakoshalam", "Sa R2 G3 M2 Pa Sa higher", "Sa higher N3 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print(f"\nMelakarta #66: {MELAKARTA_NAME}")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Chitrambari table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #66)")

############################################### melakarta #67:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Sucharitra"
MELAKARTA_FOLDER = "sucharitra"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# === Janya Ragas of Sucharitra (Melakarta #67) ===

janya_ragas_data = [

    # Santhāna Manjari
    ("Santhāna Manjari", "Sa R3 G3 M2 Pa D1 Sa higher", "Sa higher N1 D1 Pa M2 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Sucharitra table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #67)")

############################################### melakarta #68:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Jyotiswarupini"
MELAKARTA_FOLDER = "jyotiswarupini"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# === Janya Ragas of Jyothisvarūpini (Melakarta #68) ===

janya_ragas_data = [
    # Jyothi
    ("Jyothi", "Sa R3 G3 M2 Pa D1 N2 Sa higher", "Sa higher N2 D1 Pa M2 G3 Sa"),
    
    # Deepavaraali
    ("Deepavarali", "Sa R3 M2 Pa N2 Sa higher", "Sa higher N2 Pa M2 G3 R3 Sa"),
    
    # Jyothishmathi
    ("Jyothishmathi", "Sa R3 G3 M2 Pa Sa higher", "Sa higher N2 D1 M2 Pa M2 G3 R3 Sa"),
    
    # Ramagiri
    ("Ramagiri", "Sa R3 M2 G3 M2 Pa D1 N2 Sa higher", "Sa higher D1 N2 D1 Pa M2 G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Jyothisvarupini table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #68)")

# === Arohanam–Avarohanam Used ===
print("\nArohanam–Avarohanam used:")
print("- Jyothi: S R3 G3 M2 P D1 N2 S / S N2 D1 P M2 G3 S")
print("- Deepavaraali: S R3 M2 P N2 S / S N2 P M2 G3 R3 S")
print("- Jyothishmathi: S R3 G3 M2 P S / S N2 D1 M2 P M2 G3 R3 S")
print("- Ramagiri: S R3 M2 G3 M2 P D1 N2 S / S D1 N2 D1 P M2 G3 R3 S")

############################################### melakarta #69:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Dhatuvardhani"
MELAKARTA_FOLDER = "dhatuvardhani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Dhatuvardhani (Melakarta #69)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Dhowtha Panchamam
    ("Dhowtha Panchamam", "Sa R3 G3 M2 Pa N3 Pa Sa higher", "Sa higher N3 D1 Pa M2 R3 G3 M2 R3 Sa"),
    
    # Dhwthiyapanchamam
    ("Dhwithiyapanchamam", "Sa R3 G3 M2 Pa N3 Pa Sa higher", "Sa higher N3 D1 Pa M2 R3 M2 G3 R3 Sa"),
    
    # Sumukham
    ("Sumukham", "Sa R3 M2 N3 Sa higher", "Sa higher N3 M2 R3 Sa"),
    
    # Tavapriyā
    ("Tavapriyā", "Sa R3 M2 Pa N3 Sa higher", "Sa higher N3 D1 Pa M2 G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Dhatuvardhani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #69)")

############################################## melakarta #70:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Nasikabhushani"
MELAKARTA_FOLDER = "nasikabhushani"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Nasikabhusani (Melakarta #70)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Nāsāmani
    ("Nāsāmani", "Sa R3 Sa M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R3 Sa"),
    
    # Marakathagowla
    ("Marakathagowla", "Sa R3 M2 Pa D2 N2 Sa higher", "Sa higher N2 D2 Pa M2 G3 R3 Sa"),
    
    # Thilakamandāri
    ("Thilakamandāri", "Sa R3 M2 Pa D2 Sa higher", "Sa higher D2 Pa M2 G3 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Nasikabhusani table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #70)")

############################################## melakarta #71:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Kosalam"
MELAKARTA_FOLDER = "kosalam"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Kosalam (Melakarta #71)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Kusumākaram
    ("Kusumākaram", "Sa R3 G3 M2 Pa D2 N3 Sa higher", "Sa higher N3 D2 Pa M2 G3 R3 Sa"),
    
    # Ayodhya
    ("Ayodhya", "Sa G3 M2 Pa N3 Sa higher", "Sa higher D2 Pa M2 G3 M2 R3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Kosalam table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #71)")

############################################## melakarta #72:  Janya Ragas Insertion ###################################

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

# Melakarta name (for folder path and table name)
MELAKARTA_NAME = "Rasikapriya"
MELAKARTA_FOLDER = "rasikapriya"  # lowercase for file paths

# Function to generate audio paths
def get_audio_paths(janya_raga_name, melakarta_folder):
    # Remove spaces, special characters, convert to lowercase
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    clean_name = clean_name.replace("ṭ", "t").replace("ḍ", "d").replace("ñ", "n")
    clean_name = clean_name.replace("ṛ", "r").replace("ḻ", "l")
    
    arohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_arohana.mp3"
    avarohanam_path = f"janya ragas/{melakarta_folder}/{clean_name}_avarohana.mp3"
    
    return arohanam_path, avarohanam_path

# Function to extract swara flags from arohanam and avarohanam
def get_swaras_flags(arohanam, avarohanam):
    # Combine both to get all swaras used in the raga
    combined = arohanam + " " + avarohanam
    
    flags = {
        "Sa": 0, "R1": 0, "R2": 0, "R3": 0,
        "G1": 0, "G2": 0, "G3": 0,
        "M1": 0, "M2": 0,
        "Pa": 0,
        "D1": 0, "D2": 0, "D3": 0,
        "N1": 0, "N2": 0, "N3": 0
    }
    
    for key in flags.keys():
        if key in combined:
            flags[key] = 1
    
    return flags

# Janya Ragas of Rasikapriya (Melakarta #72)
# Format: (Display Name, Arohanam, Avarohanam)
# EXACTLY as shown in the image - no modifications

janya_ragas_data = [
    # Rasamanjari
    ("Rasamanjari", "Sa R3 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R3 Sa"),
    
    # Hamsagiri
    ("Hamsagiri", "Sa R3 G3 M2 Pa D3 N3 Sa higher", "Sa higher N3 Pa D3 N3 Pa M2 G3 Sa"),
    
    # Ishtārangini
    ("Ishtārangini", "Sa R3 M2 Pa N3 Sa higher", "Sa higher N3 D3 Pa M2 G3 R3 Sa"),
    
    # Nāgagiri
    ("Nāgagiri", "Sa G3 M2 Pa D2 Pa Sa higher", "Sa higher D2 Pa M2 G3 Sa"),
]

# Note about selected scales:
print("=" * 80)
print("SELECTED AROHANAM/AVAROHANAM FOR RAGAS (EXACTLY AS IN IMAGE):")
print("=" * 80)
print("\nAll ragas - Single variant as shown in image")
print("=" * 80)
print("\nDetailed scales:")
print("-" * 80)
for raga in janya_ragas_data:
    print(f"{raga[0]}:")
    print(f"  Arohanam:   {raga[1]}")
    print(f"  Avarohanam: {raga[2]}")
print("=" * 80)
print()

# Prepare data with audio paths
janya_ragas = []
for raga_info in janya_ragas_data:
    janya_name = raga_info[0]
    arohanam = raga_info[1]
    avarohanam = raga_info[2]
    
    audio_aro, audio_ava = get_audio_paths(janya_name, MELAKARTA_FOLDER)
    janya_ragas.append((janya_name, arohanam, avarohanam, audio_aro, audio_ava))

print(f"🎵 Inserting {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table...\n")

# Insert each janya raga
for raga_data in janya_ragas:
    janya_name = raga_data[0]
    arohanam = raga_data[1]
    avarohanam = raga_data[2]
    audio_aro = raga_data[3]
    audio_ava = raga_data[4]
    
    # Get swara flags
    flags = get_swaras_flags(arohanam, avarohanam)
    
    # Insert into Rasikapriya table
    cursor.execute(f"""
        INSERT INTO `{MELAKARTA_NAME}`
        (janya_raga_name, arohanam, avarohanam, audio_path_arohanam, audio_path_avarohanam,
         Sa, R1, R2, R3, G1, G2, G3, M1, M2, Pa, D1, D2, D3, N1, N2, N3)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        janya_name, arohanam, avarohanam, audio_aro, audio_ava,
        flags["Sa"], flags["R1"], flags["R2"], flags["R3"],
        flags["G1"], flags["G2"], flags["G3"],
        flags["M1"], flags["M2"],
        flags["Pa"],
        flags["D1"], flags["D2"], flags["D3"],
        flags["N1"], flags["N2"], flags["N3"]
    ))
    
    print(f"✅ Inserted: {janya_name}")

conn.commit()
cursor.close()
conn.close()

print(f"\n✅ Successfully inserted all {len(janya_ragas)} Janya Ragas into {MELAKARTA_NAME} table!")
print(f"🎵 Table: {MELAKARTA_NAME} (Melakarta #72)")