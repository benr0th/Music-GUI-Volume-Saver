import pymem
import time

def check_process():
    while True:
        try:
            global pm
            global base
            pm = pymem.Pymem("Music_GUI.exe")
            base = pm.base_address
            break
        except:
            print("Waiting for process...")
            time.sleep(1)
            continue

def main():
    check_process()
    volume = pm.read_int(base + 0x251010)
    try:
        with open("volume.ini", "r") as f:
            volume = int(f.read())
    except:
        pass # file doesn't exist yet
    pm.write_int(base + 0x251010, volume)
    print("Volume: " + str(volume))
    
    # if volume changed, write it to the file
    while True:
        time.sleep(0.1)
        try:
            new_volume = pm.read_int(base + 0x251010)
        except:
            print("Process closed, exiting.")
            exit()
            
        if new_volume != volume:
            volume = new_volume
            print("Volume: " + str(volume))
            with open("volume.ini", "w") as f:
                        f.write(str(volume))

if __name__ == '__main__':
    main()
