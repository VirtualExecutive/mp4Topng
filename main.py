import os
from moviepy import VideoFileClip

def check_and_create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"{directory} klasörü oluşturuldu.")

def extract_frames(movie, imgdir, frames_per_second):
    # Klasör kontrolü
    check_and_create_directory(imgdir)
    
    clip = VideoFileClip(movie)
    duration = clip.duration  # Video süresi
    fps = clip.fps  # Orijinal framerate

    # Yeni framerate belirleniyor
    new_fps = frames_per_second

    # Her saniyede bir kare almak için gereken adım sayısı hesaplanıyor
    step = int(fps / new_fps)

    for t in range(int(duration * new_fps)):
        # Orijinal kareleri hesaplanan adımlarla al
        original_frame_index = t * step
        imgpath = os.path.join(imgdir, f'frame_{t}.png')
        clip.save_frame(imgpath, original_frame_index / fps)

        # Her saniyede bir çıktı al
        if t % new_fps == 0:
            print(f"\r{(t / new_fps):.1f}/{duration}s", end="")

    # VideoFileClip objesini kapat
    clip.close()

def ClearFrames():
    # Temizlik için frames klasörünü temizle    
    if os.path.exists(imgdir):
        files = os.listdir(imgdir)
        for file in files:
            if file.endswith('.png'):
                os.remove(os.path.join(imgdir, file))
        print(f"{imgdir} klasörü temizlendi.")
    else:
        print(f"{imgdir} klasörü bulunamadı.")


# Kullanım
movie = 'input.mp4'
imgdir = 'frames'
frames_per_second = 10  # Her saniyede bir kare almak için

ClearFrames()

# Frames çıkar
extract_frames(movie, imgdir, frames_per_second)
