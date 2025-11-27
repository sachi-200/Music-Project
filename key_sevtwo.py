import numpy as np
from scipy.io.wavfile import write
import os

# -----------------------------
# 1. Swara frequency ratios relative to Sa
# -----------------------------
swara_ratios = {
    'Sa': 1.0,
    'R1': 16/15, 'R2': 9/8, 'R3': 6/5,
    'G1': 10/9, 'G2': 5/4, 'G3': 81/64,
    'M1': 4/3, 'M2': 45/32,
    'Pa': 3/2,
    'D1': 8/5, 'D2': 5/3, 'D3': 9/5,
    'N1': 16/9, 'N2': 15/8, 'N3': 9/5,
    'Sa_high': 2.0
}

# -----------------------------
# 2. Triangle waveform generator
# -----------------------------
def generate_note(frequency, duration=1.0, sample_rate=44100):
    n_samples = int(sample_rate * duration)
    t = np.linspace(0, duration, n_samples, endpoint=False)
    waveform = 2*np.abs(2*((t*frequency) % 1) - 1) - 1
    fade_len = int(sample_rate*0.01)
    waveform[:fade_len] *= np.linspace(0,1,fade_len)
    waveform[-fade_len:] *= np.linspace(1,0,fade_len)
    return waveform

# -----------------------------
# 3. Merge raaga
# -----------------------------
def merge_raaga(raaga_notes, sa_frequency=415.3, duration_per_note=1.0, speed=0.5, sample_rate=44100):
    audio = np.array([], dtype=np.float32)
    note_freqs = [sa_frequency * swara_ratios[n] for n in raaga_notes]
    adjusted_duration = duration_per_note / speed
    n_samples_per_note = int(sample_rate * adjusted_duration)

    for f in note_freqs:
        t = np.linspace(0, adjusted_duration, n_samples_per_note, endpoint=False)
        waveform = 2*np.abs(2*((t*f) % 1) - 1) - 1
        fade_len = int(sample_rate*0.01)
        waveform[:fade_len] *= np.linspace(0,1,fade_len)
        waveform[-fade_len:] *= np.linspace(1,0,fade_len)
        audio = np.concatenate([audio, waveform])

    audio *= 0.9
    return (audio * 32767).astype(np.int16), sample_rate

# -----------------------------
# 4. Define 72 Melakarta raga names
# -----------------------------
melakarta_names = [
    "kanakangi","ratnangi","ganamurti","vanaspati","manavati","tanarupi","senavati","hanumatodi",
    "dhenuka","natakapriya","kokilapriya","rupavati","gayakapriya","vakulabharanam","mayamalavagowla",
    "chakravakam","suryakantam","hatakambari","jhankaradhwani","natabhairavi","kiravani","kharaharapriya",
    "gaurimanohari","varunapriya","mararanjani","charukesi","sarasangi","harikambhoji","dheerasankarabharanam",
    "naganandini","yagapriya","ragavardhini","gangeyabhushani","vagadhishvari","sulini","chalanata",
    "salagam","jalarnavam","jhalavarali","navaneetam","pavani","raghupriya","gavambodhi","bhavapriya",
    "subhapantuvarali","shadvidamargini","suvarnangi","divyamani","dhavalambari","namanarayani","kamavardhini",
    "ramapriya","gamanashrama","vishwambari","shamalangi","shanmukhapriya","simhendramadhyamam","hemavati",
    "dharmavati","nitimati","kantamani","rishabhapriya","latangi","vachaspati","mechakalyani","chitrambari",
    "sucharitra","jyotiswarupini","dhatuvardhani","nasikabhushani","kosalam","rasikapriya"
]

# -----------------------------
# 5. Generate all 72 Melakarta ragas
# -----------------------------
r_g_options = [
    ('R1','G1'), ('R1','G2'), ('R1','G3'),
    ('R2','G2'), ('R2','G3'),
    ('R3','G3')
]

d_n_options = [
    ('D1','N1'), ('D1','N2'), ('D1','N3'),
    ('D2','N2'), ('D2','N3'),
    ('D3','N3')
]

def melakarta_raagas():
    ragas = []
    # First 36 with M1
    for r,g in r_g_options:
        for d,n in d_n_options:
            ragas.append(['Sa', r, g, 'M1', 'Pa', d, n, 'Sa_high'])
    # Next 36 with M2
    for r,g in r_g_options:
        for d,n in d_n_options:
            ragas.append(['Sa', r, g, 'M2', 'Pa', d, n, 'Sa_high'])
    return ragas

# -----------------------------
# 6. Generate and save
# -----------------------------
output_folder = "melakarta_ragas"
os.makedirs(output_folder, exist_ok=True)

sa_frequency = 415.3
duration_per_note = 0.8
speed = 0.5

all_ragas = melakarta_raagas()
for notes, name in zip(all_ragas, melakarta_names):
    audio_data, sr = merge_raaga(notes, sa_frequency, duration_per_note, speed)
    filename = f"{output_folder}/{name.lower().replace(' ','')}.wav"
    write(filename, sr, audio_data)
    print(f"✅ Saved {filename}")

print("🎵 All 72 Melakarta ragas generated at speed 0.5!")
