from PIL import Image, ImageEnhance, ImageDraw, ImageFont
import PIL
#1. buka file gambar
img = Image.open("jisoo.jpg")

#tampilkan gambar
# img.show()
#ubah ke bmp
img.save('jisoo.bmp', format='BMP')
#2. lihat beberapa atribut gambar
print(img.filename)
print(img.format)
print(img.mode)
print(img.size)
print(img.width)
print(img.height)
print(img.info)
#3. mengubah ukuran gambar
resized_img = img.resize((750, 750), resample=Image.BICUBIC)
resized_img.save('resized.bmp')


#5
crop_img = img.crop((0, 500, 1000, 1500))
crop_img.save('cropped.jpg')

#4. thumbnail
img.thumbnail((450, 450))
img.save('thumb.gif')


#6 border
border_im = PIL.Image.new('RGB', (img.width+20, img.height+20), 'red')
border_im.paste(img, (10, 10))
border_im.save('jisoo-border.jpg')

#7
rotated = img.transpose(Image.ROTATE_90)
# rotated.show()

rotated.save('rotate90.jpg')

#8# Flip kiri-kanan (axis vertikal)
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)

# flipped.show()

flipped.save('flipped.jpg')

#9
# buat instansi enhancer untuk brightness
enhancer = ImageEnhance.Brightness(img)

factor = 1
# panggil metode enhance untuk memanipulasi
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # darkens
im_output = enhancer.enhance(factor)
im_output.save('darkened.png')

factor = 1.5 # brightens
im_output = enhancer.enhance(factor)
im_output.save('brightened.png')

# contrast
enhancer = ImageEnhance.Contrast(img)

factor = 1
im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')

factor = 0.5 # kurangi kontras
im_output = enhancer.enhance(factor)
im_output.save('less-contrast.png')

factor = 1.5 # tambah kontras
im_output = enhancer.enhance(factor)
im_output.save('more-contrast.png')

#sharpen

enhancer = ImageEnhance.Sharpness(img)

factor = 1
im_s_1 = enhancer.enhance(factor)
#im_s_1.save('original-image.png')

factor = 0.05
im_s_1 = enhancer.enhance(factor)
im_s_1.save('blurred.png')

factor = 2
im_s_1 = enhancer.enhance(factor)
im_s_1.save('sharpened.png')

#watermark
img = Image.open('jisoo.jpg')
width, height = img.size  # lebar dan tinggi untuk kalkulasi koordinat teks

# menambahkan elemen 2d ke gambar yang sudah ada
draw = ImageDraw.Draw(img)

text = '52417159' # ganti dengan npm mu...

# mendefinisikan font baru, lengkap dengan ukurannya
font = ImageFont.truetype('arial.ttf', 50)
# hitung lebar dan tinggi font relatif terhadap gambar utama
textwidth, textheight = draw.textsize(text, font)

# hitung koordinat x, y teks
margin = 15
x = width - textwidth - margin
y = height - textheight - margin

# terapkan watermark
draw.text((x, y), text, font=font)
img.show()

# Simpan gambar
img.save('watermark.jpg')