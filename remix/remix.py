from pydub import AudioSegment
import librosa
import soundfile as sf
import os

# Melakarta raga name
melakarta = "kanakangi"

# Janya ragas data

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

def clean_raga_name(janya_raga_name):
    """Clean and normalize raga name"""
    clean_name = janya_raga_name.lower()
    clean_name = clean_name.replace(" ", "").replace("ā", "a").replace("ī", "i").replace("ū", "u")
    clean_name = clean_name.replace("ē", "e").replace("ō", "o").replace("ṁ", "m").replace("ṅ", "n")
    clean_name = clean_name.replace("ś", "s").replace("ṣ", "s").replace("ll", "l")
    return clean_name

def parse_swaras(swara_string):
    """Parse swara string and convert to list of audio file names"""
    # First, handle "Sa higher" pattern by converting to "Sa_higher"
    temp_string = swara_string.replace("Sa higher", "Sa_higher")
    
    # Split by spaces
    swaras = temp_string.split()
    
    # Convert back "Sa_higher" to "Sa higher"
    swaras = [s.replace("Sa_higher", "Sa higher") for s in swaras]
    
    # Add .mp3 extension to each swara
    audio_files = [f"{swara}.mp3" for swara in swaras]
    
    return audio_files

def combine_with_background(note_files, background_file, output_file):
    """Combine note files with background tanpura"""
    combined_notes = AudioSegment.empty()
    for file in note_files:
        audio = AudioSegment.from_file(file)
        audio = audio.set_frame_rate(44100).set_channels(2)
        # If this is M1.mp3, add 1s silence after it
        if "M1.mp3" in file:
            combined_notes += audio
            combined_notes += AudioSegment.silent(duration=1000)  # 1000 ms = 1 sec
        else:
            combined_notes += audio  
    
    background = AudioSegment.from_file(background_file).set_frame_rate(44100).set_channels(2)
    if len(background) < len(combined_notes):
        repeats = (len(combined_notes) // len(background)) + 1
        background *= repeats
    background = background[:len(combined_notes)]
    
    final_mix = combined_notes.overlay(background - 10)
    final_mix.export(output_file, format="mp3")
    print(f"Saved sequential mix: {output_file}")

def change_audio_speed(input_file, output_file, speed=1.0):
    """Change speed (tempo) of audio without changing pitch."""
    y, sr = librosa.load(input_file, sr=None)  # keep original sample rate
    y_stretched = librosa.effects.time_stretch(y, rate=speed)
    sf.write(output_file, y_stretched, sr)
    print(f"Exported: {output_file}")

def process_janya_raga(raga_name, arohanam, avarohanam, background_file, output_folder, speed=1.5):
    """Process a single janya raga and create separate arohanam and avarohanam audio files"""
    # Clean the raga name
    clean_name = clean_raga_name(raga_name)
    
    # Parse arohanam and avarohanam
    arohanam_files = parse_swaras(arohanam)
    avarohanam_files = parse_swaras(avarohanam)
    
    print(f"\nProcessing: {raga_name} (cleaned: {clean_name})")
    print(f"Arohanam: {arohanam_files}")
    print(f"Avarohanam: {avarohanam_files}")
    
    # Create arohanam file
    arohanam_temp = os.path.join(output_folder, f"{clean_name}_arohanam_temp.mp3")
    arohanam_final = os.path.join(output_folder, f"{clean_name}_arohana.mp3")
    combine_with_background(arohanam_files, background_file, arohanam_temp)
    change_audio_speed(arohanam_temp, arohanam_final, speed=speed)
    
    # Create avarohanam file
    avarohanam_temp = os.path.join(output_folder, f"{clean_name}_avarohanam_temp.mp3")
    avarohanam_final = os.path.join(output_folder, f"{clean_name}_avarohana.mp3")
    combine_with_background(avarohanam_files, background_file, avarohanam_temp)
    change_audio_speed(avarohanam_temp, avarohanam_final, speed=speed)
    
    # Clean up temp files
    if os.path.exists(arohanam_temp):
        os.remove(arohanam_temp)
    if os.path.exists(avarohanam_temp):
        os.remove(avarohanam_temp)
    
    return arohanam_final, avarohanam_final

# Example usage
if __name__ == "__main__":
    background = "tanpura.mp4"
    
    # Clean the melakarta name and create folder
    clean_melakarta = clean_raga_name(melakarta)
    output_folder = clean_melakarta
    
    # Create the folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created folder: {output_folder}")
    else:
        print(f"Folder already exists: {output_folder}")
    
    # Process each janya raga in the array
    for raga_name, arohanam, avarohanam in janya_ragas_data:
        try:
            arohanam_file, avarohanam_file = process_janya_raga(
                raga_name, arohanam, avarohanam, background, output_folder, speed=1.5
            )
            print(f"✓ Successfully created: {arohanam_file}")
            print(f"✓ Successfully created: {avarohanam_file}\n")
        except Exception as e:
            print(f"✗ Error processing {raga_name}: {e}\n")
    
    print(f"\nAll files saved in folder: {output_folder}")