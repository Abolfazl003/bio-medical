# (page index 0-based = pages/pNN.png, box@130dpi px, name)
CROPS = [
(11,(210,240,870,425),'fig_1400_q56.png'),
(11,(355,675,735,905),'fig_1400_q57.png'),
(11,(265,1120,800,1305),'fig_1400_q58.png'),
(12,(300,155,735,565),'fig_1400_q59.png'),
(12,(295,630,785,955),'fig_1400_q60.png'),
(12,(255,1165,790,1380),'fig_1400_q61.png'),
(13,(330,150,730,525),'fig_1400_q62.png'),
(13,(260,605,805,850),'fig_1400_q63.png'),
(13,(255,962,805,1225),'fig_1400_q64.png'),
(14,(340,185,730,590),'fig_1400_q65.png'),
(14,(300,860,790,1225),'fig_1400_q66.png'),
(15,(245,250,835,595),'fig_1400_q67.png'),
(15,(255,910,815,1305),'fig_1400_q68.png'),
(16,(295,185,740,645),'fig_1400_q69.png'),
(16,(215,880,1010,1270),'fig_1400_q70.png'),
]
if __name__=='__main__':
    import pymupdf as f, subprocess, sys
    from PIL import Image
    d=f.open('/home/user/konkur_bme_vezarat_behdasht/booklets/Arshad_BME_Bioelectric_VezaratBehdasht_1400.pdf')
    s=72/130; only=sys.argv[1:]
    for pg,b,n in CROPS:
        if only and n not in only: continue
        d[pg].get_pixmap(dpi=200,clip=f.Rect(*[v*s for v in b])).save('fig/'+n)
        subprocess.run(['python3','clean.py','fig/'+n])
        Image.open('fig/'+n).convert('L').quantize(16).save('fig/'+n,optimize=True)
