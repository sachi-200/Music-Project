from flask import Flask, render_template, send_from_directory, abort, jsonify, request
import mysql.connector
import os
import tempfile
import numpy as np
import mysql.connector, os, google.generativeai as genai
from gradio_client import Client, file as gradio_file
import re
from fuzzywuzzy import fuzz
from mysql.connector import connect

app = Flask(__name__)

genai.configure(api_key="")
model = genai.GenerativeModel("gemini-2.5-flash")

HOST = "localhost"
USER = "root"
PASSWORD = "Matilda+10"
DATABASE = "musicproject"

def get_db_connection():
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("""
            SELECT melakartha_number, raaga_name, arohanam, avarohanam 
            FROM melakartas 
            ORDER BY melakartha_number
        """)
        melakartas = cursor.fetchall()
        
        cursor.close()
        conn.close()
    except Exception as e:
        print("DB Error:", e)
        melakartas = []

    return render_template('index.html', melakartas=melakartas)

@app.route('/keyboard')
def keyboard():
    return render_template('keyboard.html')

@app.route('/audio-page')
def audio_page():
    return render_template('audio.html')

@app.route('/audio-mapping')
def audio_mapping():
    return render_template('audio_mapping.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    audio_dir = os.path.join(os.getcwd(), "audio")
    
    if not (filename.endswith('.m4a') or filename.endswith('.mp3')):
        if os.path.exists(os.path.join(audio_dir, filename + '.m4a')):
            filename = filename + '.m4a'
        elif os.path.exists(os.path.join(audio_dir, filename + '.mp3')):
            filename = filename + '.mp3'
    
    file_path = os.path.join(audio_dir, filename)
    
    if os.path.exists(file_path):
        if filename.endswith('.mp3'):
            print(f"▶️  Playing full melakarta: {filename}")
        return send_from_directory(audio_dir, filename)
    else:
        print(f"Audio file not found: {file_path}")
        abort(404)

@app.route('/keyboard-audio/<path:filename>')
def serve_keyboard_audio(filename):
    keyboard_dir = os.path.join(os.getcwd(), "keyboard")
    
    if not filename.endswith('.wav'):
        if os.path.exists(os.path.join(keyboard_dir, filename + '.wav')):
            filename = filename + '.wav'
    
    file_path = os.path.join(keyboard_dir, filename)
    
    if os.path.exists(file_path):
        print(f"▶️  Playing keyboard audio: {filename}")
        return send_from_directory(keyboard_dir, filename)
    else:
        print(f"Keyboard audio file not found: {file_path}")
        abort(404)

@app.route('/keyboard-audio-melakarta/<path:filename>')
def serve_keyboard_audio_melakarta(filename):
    keyboard_melakarta_dir = os.path.join(os.getcwd(), "keyboard_audio_melakarta")
    
    if not filename.endswith('.wav'):
        if os.path.exists(os.path.join(keyboard_melakarta_dir, filename + '.wav')):
            filename = filename + '.wav'
    
    file_path = os.path.join(keyboard_melakarta_dir, filename)
    
    if os.path.exists(file_path):
        print(f"▶️  Playing keyboard melakarta audio: {filename}")
        return send_from_directory(keyboard_melakarta_dir, filename)
    else:
        print(f"Keyboard melakarta audio file not found: {file_path}")
        abort(404)

@app.route('/keyboard-audio-janya/<path:filepath>')
def serve_keyboard_audio_janya(filepath):
    keyboard_janya_dir = os.path.join(os.getcwd(), "keyboard_audio_janya")
    file_path = os.path.join(keyboard_janya_dir, filepath)
    
    if os.path.exists(file_path):
        print(f"▶️  Playing keyboard janya audio: {filepath}")
        directory = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        return send_from_directory(directory, file_name)
    else:
        print(f"Keyboard janya audio file not found: {file_path}")
        abort(404)

@app.route('/janya-audio/<path:filepath>')
def serve_janya_audio(filepath):
    base_dir = os.getcwd()
    file_path = os.path.join(base_dir, filepath)
    
    if os.path.exists(file_path):
        print(f"▶️  Playing janya raga audio: {filepath}")
        directory = os.path.dirname(file_path)
        file_name = os.path.basename(file_path)
        return send_from_directory(directory, file_name)
    else:
        print(f"Janya raga audio file not found: {file_path}")
        abort(404)

@app.route('/api/check-audio/<swara>')
def check_audio(swara):
    audio_dir = os.path.join(os.getcwd(), "audio")
    filename = swara + '.m4a'
    file_path = os.path.join(audio_dir, filename)
    
    return jsonify({
        'exists': os.path.exists(file_path),
        'swara': swara,
        'filename': filename
    })

@app.route('/api/melakarta/<int:melakarta_number>')
def get_melakarta_details(melakarta_number):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        cursor.execute("""
            SELECT 
                m.melakartha_number,
                m.raaga_name,
                m.arohanam,
                m.avarohanam,
                ma.audio_path
            FROM melakartas m
            LEFT JOIN melakarta_audio ma ON m.melakartha_number = ma.melakartha_number
            WHERE m.melakartha_number = %s
        """, (melakarta_number,))
        
        melakarta = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if melakarta:
            keyboard_melakarta_dir = os.path.join(os.getcwd(), "keyboard_audio_melakarta")
            raaga_name = melakarta['raaga_name']
            raaga_name_cleaned = raaga_name.replace(' ', '').lower()
            
            keyboard_melakarta_audio_exists = False
            keyboard_melakarta_audio_path = None
            
            if os.path.exists(os.path.join(keyboard_melakarta_dir, f"{raaga_name_cleaned}.wav")):
                keyboard_melakarta_audio_exists = True
                keyboard_melakarta_audio_path = f"/keyboard-audio-melakarta/{raaga_name_cleaned}.wav"
            
            melakarta['keyboard_melakarta_audio_exists'] = keyboard_melakarta_audio_exists
            melakarta['keyboard_melakarta_audio_path'] = keyboard_melakarta_audio_path
            
            return jsonify(melakarta)
        else:
            return jsonify({'error': 'Melakarta not found'}), 404
            
    except Exception as e:
        print(f"Error fetching melakarta details: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/janya-ragas/<melakarta_name>')
def get_janya_ragas(melakarta_name):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = f"""
            SELECT 
                raga_number,
                janya_raga_name,
                arohanam,
                avarohanam,
                audio_path_arohanam,
                audio_path_avarohanam
            FROM `{melakarta_name}`
            ORDER BY raga_number
        """
        
        cursor.execute(query)
        janya_ragas = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        if janya_ragas:
            for janya in janya_ragas:
                if janya['audio_path_arohanam']:
                    janya['audio_path_arohanam'] = f"/janya-audio/{janya['audio_path_arohanam']}"
                    
                    arohanam_path = janya['audio_path_arohanam'].replace('/janya-audio/', '')
                    parts = arohanam_path.split('/')
                    if len(parts) >= 3:
                        folder_name = parts[1]
                        file_name_with_ext = parts[2]
                        janya_raga_name = file_name_with_ext.replace('_arohana.mp3', '')
                        
                        keyboard_arohanam_path = f"/keyboard-audio-janya/{folder_name}/{janya_raga_name}_arohana.mp3"
                        janya['keyboard_audio_path_arohanam'] = keyboard_arohanam_path
                    else:
                        janya['keyboard_audio_path_arohanam'] = None
                else:
                    janya['keyboard_audio_path_arohanam'] = None
                    
                if janya['audio_path_avarohanam']:
                    janya['audio_path_avarohanam'] = f"/janya-audio/{janya['audio_path_avarohanam']}"
                    
                    avarohanam_path = janya['audio_path_avarohanam'].replace('/janya-audio/', '')
                    parts = avarohanam_path.split('/')
                    if len(parts) >= 3:
                        folder_name = parts[1]
                        file_name_with_ext = parts[2]
                        janya_raga_name = file_name_with_ext.replace('_avarohana.mp3', '')
                        
                        keyboard_avarohanam_path = f"/keyboard-audio-janya/{folder_name}/{janya_raga_name}_avarohana.mp3"
                        janya['keyboard_audio_path_avarohanam'] = keyboard_avarohanam_path
                    else:
                        janya['keyboard_audio_path_avarohanam'] = None
                else:
                    janya['keyboard_audio_path_avarohanam'] = None
            
            return jsonify({
                'melakarta_name': melakarta_name,
                'janya_ragas': janya_ragas,
                'count': len(janya_ragas)
            })
        else:
            return jsonify({
                'melakarta_name': melakarta_name,
                'janya_ragas': [],
                'count': 0
            })
            
    except mysql.connector.Error as e:
        print(f"Error fetching janya ragas for {melakarta_name}: {e}")
        return jsonify({'error': f'Table {melakarta_name} not found or empty'}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/janya-raga-detail/<melakarta_name>/<int:raga_number>')
def get_janya_raga_detail(melakarta_name, raga_number):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = f"""
            SELECT 
                raga_number,
                janya_raga_name,
                arohanam,
                avarohanam,
                audio_path_arohanam,
                audio_path_avarohanam
            FROM `{melakarta_name}`
            WHERE raga_number = %s
        """
        
        cursor.execute(query, (raga_number,))
        janya_raga = cursor.fetchone()
        
        cursor.close()
        conn.close()
        
        if janya_raga:
            if janya_raga['audio_path_arohanam']:
                janya_raga['audio_path_arohanam'] = f"/janya-audio/{janya_raga['audio_path_arohanam']}"
            if janya_raga['audio_path_avarohanam']:
                janya_raga['audio_path_avarohanam'] = f"/janya-audio/{janya_raga['audio_path_avarohanam']}"
            
            return jsonify(janya_raga)
        else:
            return jsonify({'error': 'Janya raga not found'}), 404
            
    except mysql.connector.Error as e:
        print(f"Error fetching janya raga detail: {e}")
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/find-melakartas', methods=['POST'])
def find_melakartas():
    try:
        data = request.get_json()
        swara_sets = data.get('swarasets', [])

        if not swara_sets:
            return jsonify({'matches': []})

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        all_matches = []
        seen_names = set()

        for swara_list in swara_sets:
            swaras = set(swara_list)
            swara_columns = ['Sa', 'R1', 'R2', 'R3', 'G1', 'G2', 'G3',
                             'M1', 'M2', 'Pa', 'D1', 'D2', 'D3', 'N1', 'N2', 'N3']
            conditions = [f"{s}=1" for s in swaras if s in swara_columns]

            if not conditions:
                continue

            where_clause = " AND ".join(conditions)  # ✅ must contain all swaras

            # --- Search Melakarta ragas ---
            query_melakarta = f"""
                SELECT s.melakartha_number, m.raaga_name,
                       m.arohanam, m.avarohanam
                FROM swaras s
                JOIN melakartas m ON s.melakartha_number = m.melakartha_number
                WHERE {where_clause}
                ORDER BY s.melakartha_number
            """
            cursor.execute(query_melakarta)
            melakarta_results = cursor.fetchall()

            for raga in melakarta_results:
                name = raga['raaga_name']
                if name not in seen_names:
                    seen_names.add(name)

                    aro = raga['arohanam'].replace('Sa higher', 'Sā̇')
                    ava = raga['avarohanam'].replace('Sa higher', 'Sā̇')

                    raga['arohanam'] = ' '.join(
                        f'<span class="highlight">{s}</span>' if s in swaras else s
                        for s in aro.split()
                    )
                    raga['avarohanam'] = ' '.join(
                        f'<span class="highlight">{s}</span>' if s in swaras else s
                        for s in ava.split()
                    )
                    raga['type'] = 'Melakarta'
                    all_matches.append(raga)

            # --- Search Janya ragas ---
            cursor.execute("SHOW TABLES")
            all_tables = [t[f"Tables_in_musicproject"] for t in cursor.fetchall()]
            for table in all_tables:
                if table.lower() in ['melakartas', 'swaras', 'melakarta_audio']:
                    continue

                try:
                    query_janya = f"""
                        SELECT '{table}' AS parent_melakarta,
                               janya_raga_name,
                               arohanam, avarohanam
                        FROM `{table}`
                        WHERE {where_clause}
                    """
                    cursor.execute(query_janya)
                    janya_results = cursor.fetchall()

                    for j in janya_results:
                        name = j['janya_raga_name']
                        if name not in seen_names:
                            seen_names.add(name)

                            aro = j['arohanam'].replace('Sa higher', 'Sā̇')
                            ava = j['avarohanam'].replace('Sa higher', 'Sā̇')

                            j['arohanam'] = ' '.join(
                                f'<span class="highlight">{s}</span>' if s in swaras else s
                                for s in aro.split()
                            )
                            j['avarohanam'] = ' '.join(
                                f'<span class="highlight">{s}</span>' if s in swaras else s
                                for s in ava.split()
                            )
                            j['type'] = f"Janya of {table.title()}"
                            all_matches.append(j)
                except:
                    continue

        cursor.close()
        conn.close()

        # ✅ Normalize field names for frontend
        for m in all_matches:
            if "janya_raga_name" in m:
                m["raaga_name"] = m["janya_raga_name"]
                del m["janya_raga_name"]

        # ✅ Add sequential numbering (1, 2, 3, …)
        for i, r in enumerate(all_matches, start=1):
            r["display_number"] = i

        return jsonify({
            'matches': all_matches,
            'count': len(all_matches),
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'error': str(e)}), 500
    
# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     history = data.get("history", [])
#     convo = model.start_chat(history=history)

#     try:
#         user_msg = history[-1]["parts"][0]["text"].strip()

#         # 🩵 Friendly replies for short greetings
#         if len(user_msg) < 4 or re.match(r"^(hi|hello|hey|yo|hola|namaste)\b", user_msg.lower()):
#             return jsonify({"reply": "Hello 👋! I’m your Carnatic music assistant. Ask me about any rāga, its scale, or its Janya rāgas."})

#         # --- Connect to DB ---
#         conn = connect(
#             host="localhost",
#             user="root",              # ⚙️ adjust if needed
#             password="Matilda+10",    # ⚙️ your MySQL password
#             database="musicproject"

#             # HOST = "localhost"
#             # USER = "trishra"
#             # PASSWORD = "ASV@music2025"
#             # DATABASE = "music_project"
#         )
#         cursor = conn.cursor(dictionary=True)

#         # --- Fetch all Melakarta names ---
#         cursor.execute("SELECT raaga_name, melakartha_number FROM melakartas")
#         all_melakartas = cursor.fetchall()

#         detected_mela = None
#         mela_number = None
#         best_score = 0

#         # --- Fuzzy match user text to Melakarta name ---
#         for mela in all_melakartas:
#             mela_name = mela["raaga_name"]
#             score = fuzz.partial_ratio(user_msg.lower(), mela_name.lower())
#             if score > best_score and score >= 85:
#                 detected_mela = mela_name
#                 mela_number = mela["melakartha_number"]
#                 best_score = score

#         if detected_mela:
#             # --- Get Melakarta info ---
#             cursor.execute("""
#                 SELECT 
#                     m.melakartha_number,
#                     m.raaga_name,
#                     m.arohanam,
#                     m.avarohanam,
#                     ma.audio_path
#                 FROM melakartas m
#                 LEFT JOIN melakarta_audio ma 
#                 ON m.melakartha_number = ma.melakartha_number
#                 WHERE m.melakartha_number = %s
#             """, (mela_number,))
#             mela_data = cursor.fetchone()

#             # --- Try fetching Janya rāgas safely ---
#             try:
#                 cursor.execute(f"""
#                     SELECT 
#                         raga_number,
#                         janya_raga_name,
#                         arohanam,
#                         avarohanam,
#                         audio_path_arohanam,
#                         audio_path_avarohanam
#                     FROM `{detected_mela}`
#                 """)
#                 janyas = cursor.fetchall()
#             except Exception as e:
#                 print(f"⚠️ No Janya table found for {detected_mela}: {e}")
#                 janyas = []

#             # --- Build context ---
#             if not janyas:
#                 context = (
#                     f"You are a Carnatic music assistant.\n\n"
#                     f"The Melakarta rāga **{detected_mela}** exists in the database, "
#                     "but no Janya (derived) rāgas are currently listed for it.\n\n"
#                     f"• Aarohanam: {mela_data['arohanam']}\n"
#                     f"• Avarohanam: {mela_data['avarohanam']}\n"
#                     f"• Audio sample: {mela_data['audio_path'] or 'Not available'}\n\n"
#                     "Respond politely and informatively if the user asks about this rāga or its Janya rāgas."
#                 )
#             else:
#                 janya_names = [r["janya_raga_name"] for r in janyas]
#                 context = (
#                     f"You are a Carnatic music assistant.\n\n"
#                     f"Here’s detailed information about **{detected_mela}**:\n"
#                     f"• Aarohanam: {mela_data['arohanam']}\n"
#                     f"• Avarohanam: {mela_data['avarohanam']}\n"
#                     f"• Audio sample: {mela_data['audio_path'] or 'Not available'}\n\n"
#                     f"Janya Rāgas derived from this Melakarta include: {', '.join(janya_names)}.\n\n"
#                     "Answer the user’s query accurately based on this context."
#                 )

#         else:
#             # --- Generic fallback context ---
#             context = (
#                 "You are a Carnatic music assistant. The database includes all 72 Melakarta rāgas "
#                 "in the `melakartas` table, each with Aarohanam, Avarohanam, and audio paths, plus separate "
#                 "tables for their Janya rāgas. Answer questions about Carnatic rāgas and scales accurately."
#             )

#         cursor.close()
#         conn.close()

#         # --- Build prompt for Gemini ---
#         full_prompt = f"{context}\n\nUser: {user_msg}"
#         response = convo.send_message(full_prompt)

#         print("🎵 Gemini Response:", response.text)
#         return jsonify({"reply": response.text})

#     except Exception as e:
#         print("❌ Error:", e)
#         return jsonify({"reply": f"Error: {str(e)}"}), 500

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    history = data.get("history", [])
    convo = model.start_chat(history=history)

    try:
        user_msg = history[-1]["parts"][0]["text"].strip()

        # 🩵 Friendly replies for short greetings
        if len(user_msg) < 4 or re.match(r"^(hi|hello|hey|yo|hola|namaste)\b", user_msg.lower()):
            return jsonify({"reply": "Hello 👋! I’m your Carnatic music assistant. Ask me about any rāga, its scale, or its Janya rāgas."})

        # --- Connect to DB ---
        conn = connect(
            host="localhost",
            user="root",
            password="Matilda+10",
            database="musicproject"
        )
        cursor = conn.cursor(dictionary=True)

        # --- Fetch all Melakarta names ---
        cursor.execute("SELECT raaga_name, melakartha_number FROM melakartas")
        all_melakartas = cursor.fetchall()

        detected_mela = None
        mela_number = None
        best_score = 0
        janya_match = None

        # --- Fuzzy match user text to Melakarta name ---
        for mela in all_melakartas:
            mela_name = mela["raaga_name"]
            score = fuzz.partial_ratio(user_msg.lower(), mela_name.lower())
            if score > best_score and score >= 85:
                detected_mela = mela_name
                mela_number = mela["melakartha_number"]
                best_score = score

        # --- If not found, check Janya rāgas across all Melakartas ---
        if not detected_mela:
            for mela in all_melakartas:
                mela_name = mela["raaga_name"]
                try:
                    cursor.execute(f"SELECT * FROM `{mela_name}`")
                    janyas = cursor.fetchall()
                    for j in janyas:
                        score = fuzz.partial_ratio(user_msg.lower(), j["janya_raga_name"].lower())
                        if score > best_score and score >= 85:
                            detected_mela = mela_name
                            janya_match = j
                            best_score = score
                except:
                    continue

        # --- Build context ---
        if detected_mela and not janya_match:
            cursor.execute("""
                SELECT 
                    m.melakartha_number,
                    m.raaga_name,
                    m.arohanam,
                    m.avarohanam,
                    ma.audio_path
                FROM melakartas m
                LEFT JOIN melakarta_audio ma 
                ON m.melakartha_number = ma.melakartha_number
                WHERE m.melakartha_number = %s
            """, (mela_number,))
            mela_data = cursor.fetchone()

            try:
                cursor.execute(f"""
                    SELECT 
                        janya_raga_name,
                        arohanam,
                        avarohanam,
                        audio_path_arohanam,
                        audio_path_avarohanam
                    FROM `{detected_mela}`
                """)
                janyas = cursor.fetchall()
            except:
                janyas = []

            if not janyas:
                context = (
                    f"You are a Carnatic music assistant.\n\n"
                    f"The Melakarta rāga **{detected_mela}** exists in the database, "
                    "but no Janya (derived) rāgas are currently listed for it.\n\n"
                    f"• Aarohanam: {mela_data['arohanam']}\n"
                    f"• Avarohanam: {mela_data['avarohanam']}\n"
                    # f"• Audio sample: {mela_data['audio_path'] or 'Not available'}"
                )
            else:
                janya_names = [r["janya_raga_name"] for r in janyas]
                context = (
                    f"You are a Carnatic music assistant.\n\n"
                    f"Here’s detailed information about **{detected_mela}**:\n"
                    f"• Aarohanam: {mela_data['arohanam']}\n"
                    f"• Avarohanam: {mela_data['avarohanam']}\n"
                    # f"• Audio sample: {mela_data['audio_path'] or 'Not available'}\n\n"
                    f"Janya Rāgas derived from this Melakarta include: {', '.join(janya_names)}."
                )

        elif janya_match:
            context = (
                f"You are a Carnatic music assistant.\n\n"
                f"The rāga **{janya_match['janya_raga_name']}** is a *Janya* (derived) rāga of **{detected_mela}**.\n"
                f"• Aarohanam: {janya_match['arohanam']}\n"
                f"• Avarohanam: {janya_match['avarohanam']}\n"
                # f"• Audio (Aarohanam): {janya_match['audio_path_arohanam'] or 'Not available'}\n"
                # f"• Audio (Avarohanam): {janya_match['audio_path_avarohanam'] or 'Not available'}"
            )

        else:
            context = (
                "You are a Carnatic music assistant. The database includes all 72 Melakarta rāgas "
                "and their Janya rāgas. Answer questions about any rāga or its scale accurately."
            )

        cursor.close()
        conn.close()

        # --- Build prompt for Gemini ---
        full_prompt = f"{context}\n\nUser: {user_msg}"
        response = convo.send_message(full_prompt)

        print("🎵 Gemini Response:", response.text)
        return jsonify({"reply": response.text})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"reply": f"Error: {str(e)}"}), 500

@app.route("/api/analyze-audio", methods=["POST"])
def analyze_audio():
    try:
        if "audio" not in request.files:
            return jsonify({"error": "No audio file uploaded"}), 400

        audio_file = request.files["audio"]
        if audio_file.filename == "":
            return jsonify({"error": "Empty filename"}), 400

        # Save audio temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            audio_file.save(tmp.name)
            temp_path = tmp.name

        print(f"🎧 Received: {audio_file.filename}")
        client = Client("jeevster/carnatic-raga-classifier")
        result = client.predict(k=5, audio=gradio_file(temp_path), api_name="/predict")
        print("🎵 Raw model output:", result)

        confidences = result.get("confidences", []) if isinstance(result, dict) else result

        # Filter by confidence threshold (>20%)
        filtered_ragas = []
        for c in confidences:
            if c.get("confidence", 0) > 0.2:
                filtered_ragas.append({
                    "name": c["label"].strip(),
                    "confidence": round(c["confidence"] * 100, 2)
                })

        if not filtered_ragas:
            return jsonify({"ragas": [], "message": "No rāgas with >20% confidence"}), 200

        # 🔥 NEW: Query chatbot for each rāga's details
        raga_details_list = []
        for raga_info in filtered_ragas:
            raga_name = raga_info["name"]
            confidence = raga_info["confidence"]
            
            # --- Connect to DB ---
            conn = connect(
                host="localhost",
                user="root",              # ⚙️ adjust if needed
                password="Matilda+10",    # ⚙️ your MySQL password
                database="musicproject"

                # HOST = "localhost"
                # USER = "trishra"
                # PASSWORD = "ASV@music2025"
                # DATABASE = "music_project"
            )
            cursor = conn.cursor(dictionary=True)

            # --- Fetch all Melakarta names ---
            cursor.execute("SELECT raaga_name, melakartha_number FROM melakartas")
            all_melakartas = cursor.fetchall()

            detected_mela = None
            mela_number = None
            best_score = 0

            # --- Fuzzy match user text to Melakarta name ---
            for mela in all_melakartas:
                mela_name = mela["raaga_name"]
                score = fuzz.partial_ratio(raga_name.lower(), mela_name.lower())
                if score > best_score and score >= 85:
                    detected_mela = mela_name
                    mela_number = mela["melakartha_number"]
                    best_score = score

            if detected_mela:
                # --- Get Melakarta info ---
                cursor.execute("""
                    SELECT 
                        m.melakartha_number,
                        m.raaga_name,
                        m.arohanam,
                        m.avarohanam,
                        ma.audio_path
                    FROM melakartas m
                    LEFT JOIN melakarta_audio ma 
                    ON m.melakartha_number = ma.melakartha_number
                    WHERE m.melakartha_number = %s
                """, (mela_number,))
                mela_data = cursor.fetchone()

                # --- Try fetching Janya rāgas safely ---
                try:
                    cursor.execute(f"""
                        SELECT 
                            raga_number,
                            janya_raga_name,
                            arohanam,
                            avarohanam,
                            audio_path_arohanam,
                            audio_path_avarohanam
                        FROM `{detected_mela}`
                    """)
                    janyas = cursor.fetchall()
                except Exception as e:
                    print(f"⚠️ No Janya table found for {detected_mela}: {e}")
                    janyas = []

                # --- Build context ---
                if not janyas:
                    context = (
                        f"You are a Carnatic music assistant.\n\n"
                        f"The Melakarta rāga **{detected_mela}** exists in the database, "
                        "but no Janya (derived) rāgas are currently listed for it.\n\n"
                        f"• Aarohanam: {mela_data['arohanam']}\n"
                        f"• Avarohanam: {mela_data['avarohanam']}\n"
                        f"• Audio sample: {mela_data['audio_path'] or 'Not available'}\n\n"
                        "Respond politely and informatively if the user asks about this rāga or its Janya rāgas."
                    )
                else:
                    janya_names = [r["janya_raga_name"] for r in janyas]
                    context = (
                        f"You are a Carnatic music assistant.\n\n"
                        f"Here’s detailed information about **{detected_mela}**:\n"
                        f"• Aarohanam: {mela_data['arohanam']}\n"
                        f"• Avarohanam: {mela_data['avarohanam']}\n"
                        f"• Audio sample: {mela_data['audio_path'] or 'Not available'}\n\n"
                        f"Janya Rāgas derived from this Melakarta include: {', '.join(janya_names)}.\n\n"
                        "Answer the user’s query accurately based on this context."
                    )

            else:
                # --- Generic fallback context ---
                context = (
                    "You are a Carnatic music assistant. The database includes all 72 Melakarta rāgas "
                    "in the `melakartas` table, each with Aarohanam, Avarohanam, and audio paths, plus separate "
                    "tables for their Janya rāgas. Answer questions about Carnatic rāgas and scales accurately."
                )

            cursor.close()
            conn.close()

            # --- Build prompt for Gemini ---
            full_prompt = f"{context}\n\nUser: {raga_name}"
            
            try:
                # Start a fresh conversation for each query
                convo = model.start_chat(history=[])
                response = convo.send_message(full_prompt)
                chatbot_response_text = response.text.strip()
                
                print(f"🤖 Chatbot response for {raga_name}:")
                print(chatbot_response_text)
                
                # Store the raw chatbot response
                raga_details_list.append({
                    "raaga_name": raga_name,
                    "confidence": confidence,
                    "chatbot_details": chatbot_response_text  # Raw string from chatbot
                })
                
            except Exception as e:
                print(f"❌ Chatbot error for {raga_name}: {e}")
                # Fallback if chatbot fails
                raga_details_list.append({
                    "raaga_name": raga_name,
                    "confidence": confidence,
                    "chatbot_details": f"Could not retrieve details for {raga_name}. Error: {str(e)}"
                })

        return jsonify({
            "ragas": raga_details_list,
            "count": len(raga_details_list),
            "message": "Rāgas analyzed with chatbot-generated details"
        })

    except Exception as e:
        print("❌ Error analyzing audio:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
