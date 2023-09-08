{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyMchtM3wlDzfM1boAt/bA7u"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["Install necessary libraries"],"metadata":{"id":"b7cArhrd4mNc"}},{"cell_type":"code","source":["!pip install langdetect"],"metadata":{"id":"mdf2U40R4GsC"},"execution_count":null,"outputs":[]},{"cell_type":"markdown","source":["import necessary libraries and modules"],"metadata":{"id":"z5W8Mvgf4NWY"}},{"cell_type":"code","source":["import argparse\n","import os\n","import vosk\n","import wave\n","from langdetect import detect\n","from pydub import AudioSegment"],"metadata":{"id":"LTC5DKu34sOY"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["def process_audio_file(audio_file):\n","    \"\"\"\n","    Process an audio file, perform automatic language detection, and transcribe it to text.\n","\n","    Args:\n","        audio_file (str): Path to the audio file.\n","\n","    Returns:\n","        None\n","    \"\"\"\n","    # Check if the provided audio file exists\n","    if not os.path.exists(audio_file):\n","        print(\"Audio file not found:\", audio_file)\n","        return\n","\n","    # Check and convert audio to WAV if not already in WAV format\n","    if not audio_file.lower().endswith(\".wav\"):\n","        try:\n","            audio = AudioSegment.from_file(audio_file)\n","            audio_file = \"audio.wav\"\n","            audio.export(audio_file, format=\"wav\")\n","        except Exception as e:\n","            print(\"Error converting audio to WAV:\", str(e))\n","            return\n","\n","    # Detect language of the audio\n","    detected_language = detect_language(audio_file)\n","\n","    # Initialize Vosk model based on the detected language\n","    vosk_model = vosk.Model(f\"vosk-model-{detected_language}\")\n","\n","    # Initialize Vosk Recognizer\n","    recognizer = vosk.KaldiRecognizer(vosk_model, 16000)\n","\n","    # Open and read audio file in chunks\n","    wf = wave.open(audio_file, \"rb\")\n","    while True:\n","        data = wf.readframes(4000)\n","        if len(data) == 0:\n","            break\n","        if recognizer.AcceptWaveform(data):\n","            result = recognizer.Result()\n","            print(f\"{detected_language.capitalize()} Text:\", result[\"text\"])\n","\n","    result = recognizer.FinalResult()\n","    print(f\"{detected_language.capitalize()} Text (Final):\", result[\"text\"])\n","\n","def detect_language(audio_file):\n","    \"\"\"\n","    Detect the language of an audio file using langdetect.\n","\n","    Args:\n","        audio_file (str): Path to the audio file.\n","\n","    Returns:\n","        str: Detected language code (e.g., \"en\" for English, \"ar\" for Arabic).\n","    \"\"\"\n","    try:\n","        audio_text = AudioSegment.from_file(audio_file).export(format=\"wav\").get_array_of_samples()\n","        detected_lang = detect(audio_text)\n","        return detected_lang\n","    except Exception as e:\n","        print(\"Error detecting language:\", str(e))\n","        return None\n","\n","if __name__ == \"__main__\":\n","    # Create a command-line argument parser\n","    parser = argparse.ArgumentParser(description=\"Perform ASR on an audio file.\")\n","    parser.add_argument(\"audio_file\", type=str, help=\"Path to the audio file\")\n","\n","    # Parse the command-line arguments\n","    args = parser.parse_args()\n","\n","    # Call the process_audio_file function with the provided audio file path\n","    process_audio_file(args.audio_file)"],"metadata":{"id":"WgvbBzrl5G48","colab":{"base_uri":"https://localhost:8080/","height":231},"executionInfo":{"status":"error","timestamp":1694146018763,"user_tz":-60,"elapsed":440,"user":{"displayName":"Janette Eni","userId":"13317147658978150616"}},"outputId":"5a8784a1-5aab-4dd4-fa4b-ce92ead731b7"},"execution_count":null,"outputs":[{"output_type":"stream","name":"stderr","text":["usage: ipykernel_launcher.py [-h] audio_file\n","ipykernel_launcher.py: error: unrecognized arguments: -f\n"]},{"output_type":"error","ename":"SystemExit","evalue":"ignored","traceback":["An exception has occurred, use %tb to see the full traceback.\n","\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 2\n"]},{"output_type":"stream","name":"stderr","text":["/usr/local/lib/python3.10/dist-packages/IPython/core/interactiveshell.py:3561: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n","  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"]}]},{"cell_type":"markdown","source":["    Check if provided audio_file exist"],"metadata":{"id":"m93zV7sI5dK_"}},{"cell_type":"code","source":[],"metadata":{"id":"19PJ43ln5lXK"},"execution_count":null,"outputs":[]}]}
