# (page, box@130dpi, name)
CROPS = [
 (5,(200,860,820,1045),'fig_1402_q20.png'),
 (6,(290,150,600,490),'fig_1402_q22.png'),
 (6,(290,1060,740,1240),'fig_1402_q24.png'),
 (7,(190,615,925,1235),'fig_1402_q27.png'),
 (8,(255,155,835,600),'fig_1402_q28.png'),
 (10,(130,250,965,560),'fig_1402_q35.png'),
 (10,(60,910,800,1015),'fig_1402_q36.png'),
 (11,(60,262,700,485),'fig_1402_q37.png'),
 (11,(55,1160,500,1340),'fig_1402_q39.png'),
 (14,(130,160,770,300),'fig_1402_q47.png'),
 (15,(120,145,540,245),'fig_1402_q52.png'),
 (15,(120,1160,560,1362),'fig_1402_q56.png'),
 (16,(130,150,540,338),'fig_1402_q57.png'),
 (16,(98,628,515,808),'fig_1402_q58.png'),
 (16,(85,1142,520,1325),'fig_1402_q59.png'),
 (17,(140,160,430,385),'fig_1402_q60.png'),
 (17,(155,620,590,820),'fig_1402_q61.png'),
 (17,(140,1035,580,1235),'fig_1402_q62.png'),
 (18,(100,150,420,295),'fig_1402_q63.png'),
 (18,(110,575,360,805),'fig_1402_q64.png'),
 (18,(130,1075,500,1370),'fig_1402_q65.png'),
 (19,(95,120,275,395),'fig_1402_q66.png'),
 (19,(70,490,320,760),'fig_1402_q67.png'),
 (19,(80,865,390,1175),'fig_1402_q68.png'),
 (19,(80,1220,530,1425),'fig_1402_q69.png'),
 (20,(100,205,640,395),'fig_1402_q70.png'),
]
if __name__=='__main__':
    import pymupdf as f, subprocess, sys
    d=f.open('/home/user/konkur_bme_vezarat_behdasht/booklets/Arshad_BME_Bioelectric_VezaratBehdasht_1402.pdf')
    s=72/130; only=sys.argv[1:]
    for pg,b,n in CROPS:
        if only and n not in only: continue
        d[pg-1].get_pixmap(dpi=200,clip=f.Rect(*[v*s for v in b])).save('fig/'+n)
        subprocess.run(['python3','clean.py','fig/'+n])
