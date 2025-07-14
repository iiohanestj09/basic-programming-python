import pygame as pyg

#* 1. init
pyg.init()
# Variabel running game
isRun = True

# Membuat Display Surface Object
windowLebar = 500
windowPanjang = 500
window = pyg.display.set_mode((windowLebar, windowPanjang))

# Object Game
    # Posisi
x = 250                             # Posisi Kotak di Tengah, karena windownya 500x500
y = 250
    
    # Ukuran
panjang = 20
lebar = 20

    # Kecepatan Gerak
kecepatan = 5

while isRun:
    pyg.time.delay(10)
    
    #* 2. User Input, Database Input
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            isRun = False
    
    # Ambil Semua Keyboard Press
    kunci = pyg.key.get_pressed()
    
    # ambil ke kiri
    if kunci[pyg.K_LEFT] and x > 0:
        x -= kecepatan
    elif kunci[pyg.K_RIGHT] and x < windowLebar - lebar:
        x += kecepatan
    elif kunci[pyg.K_UP] and y > 0:
        y -= kecepatan
    elif kunci[pyg.K_DOWN] and y < windowPanjang - panjang:
        y += kecepatan
    
    #* 3. Update Asset
    window.fill((255,255,255))                              #rgb(255,255,255)
    pyg.draw.rect(window,(255,122,0), (x,y,lebar,panjang))  #rgb(255,122,0)
    
    #* 4. Render ke Display
    pyg.display.update()

pyg.quit()