from threading import Thread, Lock
import time

# Create a lock
print_lock = Lock()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)  # Wait for the delay before singing
    with print_lock:  # Ensure only one thread prints at a time
        for char in lyric:
            print(char, end='', flush=True)  # Print character by character
            time.sleep(speed)  # Delay for the next character
        print()  # Print a new line after the lyric

def sing_song():
    lyrics = [
        ("Aku ga mau jadi matahari mu", 0.08),
        ("Karena itu akan membuatku jauh", 0.09),
        ("Aku ga mau jadi bintang-bintangmu", 0.08),
        ("Walau indah itu juga 'kan jauh", 0.08),
        ("Yang aku mau menjadi udaramu", 0.09),
        ("Selalu aku setia tiap hela nafasmu\n", 0.1),
        ("Aku ga romantis", 0.08),
        ("Maaf, aku ga romantis", 0.08),
        ("Maaf, aku ga romantis", 0.08),
        ("Maaf, aku ga romantis\n", 0.08)
    ]
    
    delays = [0.3, 4.0, 7.8, 11.5, 14.9, 18.3, 22.0, 23.7, 25.3, 26.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()  # Start the thread

    for thread in threads:
        thread.join()  # Wait for all threads to finish

# Call the main function
sing_song()