from pydub import AudioSegment
import os

def combine_audio_files(file_list, output_file="combined.wav"):
    """
    Combine multiple audio files into a single audio file.
    Supports .wav, .mp3, .m4a, .flac, etc.
    """
    if not file_list:
        print("❌ No input files provided!")
        return

    combined = AudioSegment.empty()

    for file in file_list:
        try:
            print(f"🎵 Adding: {file}")
            audio = AudioSegment.from_file(file)
            combined += audio
        except Exception as e:
            print(f"⚠️ Skipping {file}: {e}")

    if len(combined) == 0:
        print("❌ No valid audio files found to combine!")
        return

    # Export as WAV
    combined.export(output_file, format="wav")
    print(f"\n✅ Combined audio saved as: {output_file}")


if __name__ == "__main__":
    print("🎧 Enter paths of audio files you want to combine (comma-separated):")
    user_input = input("> ").strip()

    if not user_input:
        print("❌ No input given. Exiting.")
        exit()

    file_paths = [path.strip() for path in user_input.split(",") if path.strip()]
    output_name = input("Enter output file name (default: combined.wav): ").strip() or "combined.wav"

    combine_audio_files(file_paths, output_name)
