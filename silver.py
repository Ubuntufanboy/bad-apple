import logging
class Silver:
    rec = []
    def verbose():
        import logging
        logging.basicConfig(level=logging.DEBUG)
    
    def np_play(file):
        import playsound
        playsound.playsound(file)

    def video(file):
        import playsound
        import time
        def player(file):
            while 1:
                playsound.playsound(file)
        from multiprocessing import Process
        playing = Process(target = player, args=(file,))
        playing.start()
    def play(file):
        import playsound
        Silver.rec.append(file)
        def player(file):
            playsound.playsound(file)
        global playing
        from multiprocessing import Process
        playing = Process(target = player, args=(file,))
        playing.start()
    
    def stop():
        import logging
        from multiprocessing import Process
        try:
            if playing:
                pass
            exists = True
        
        except:
            exists = False
        
        
        if exists:
            
            if playing.is_alive():
                playing.terminate()
                logging.info("Audio stopped!")
            
            else:
                logging.warning("No audio is playing...")
        
        
        else:
            logging.warning("No audio is playing")
    
    def restart():
        logging.debug("Restart function called!")
        Silver.stop()
        Silver.play(Silver.rec[-1])
    
    def layer(file, times):
        import time
        logging.info(f"Function is layering {times} times.")
        for i in range(times):
            Silver.play(file)
            time.sleep(0.1)        
    
    def layer_kill(times):
        import time
        for i in range(times):
            time.sleep(1)
            Silver.stop()
