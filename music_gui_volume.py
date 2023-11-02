import pymem
import time
import subprocess

def check_process():
    while True:
        try:
            global pm
            global base
            global p
            p = subprocess.Popen("./Music_GUI.exe")
            pm = pymem.Pymem("Music_GUI.exe")
            base = pm.base_address
            break
        except:
            print("Waiting for process...")
            time.sleep(1)
            continue

# closing the console window hangs child process for a few seconds, attempt to kill it immediately
# TODO: actually kill it
# def terminate_process():
#     p.terminate() # Sends CTRL_BREAK_EVENT on Windows
#     if p.poll() is None: # Process hasn't exited
#         p.kill() # Sends CTRL_C_EVENT as last resort
#     p.wait()

# import atexit
# atexit.register(terminate_process)

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
