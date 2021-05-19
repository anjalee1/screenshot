import pyscreenshot

#for full screen
ss_full = pyscreenshot.grab()
ss_full.show()
ss_full.save("full_ss.png")

#for partial screen
ss_half = pyscreenshot.grab(bbox=(100, 200, 800, 800))
ss_half.show()
ss_half.save("ss_half.png")