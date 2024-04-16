# Progetto Multimedia (LM-18)

## Requisiti:
1. Python > 3.10
2. Node.js > 12.20
3. Cmake > 3.8
4. OpenCV con supporto a FFMPEG:
[Tutorial](https://medium.com/@vladakuc/compile-opencv-4-7-0-with-ffmpeg-5-compiled-from-the-source-in-ubuntu-434a0bde0ab6).
5. Libreria Pystab:
```
pip install vidstab[cv2]
```
## Istruzioni:
in /node_script/video:
```
cmake .
make
```
In /node_script/:
```
node index.js
```
## Esempi e Documentazione
+ Esempi: examples
- Documentazione: /node_script/public/doc.pdf 

