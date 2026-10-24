import sys, cv2, numpy as np
PHOTO={'fig_1402_q20.png'}
for p in sys.argv[1:]:
    a=cv2.imread(p)
    b,g,r=[a[...,i].astype(int) for i in range(3)]
    red=(r-g>35)&(r-b>25)
    if p.split('/')[-1] in PHOTO:
        m=cv2.dilate(red.astype('uint8')*255,np.ones((3,3),np.uint8))
        out=cv2.cvtColor(cv2.inpaint(a,m,3,cv2.INPAINT_TELEA),cv2.COLOR_BGR2GRAY)
    else:
        gray=cv2.cvtColor(a,cv2.COLOR_BGR2GRAY).astype(int)
        # under watermark: darkness of ink shows as low G; light watermark -> white
        ink=np.clip((g-40)*255//(115-40),0,255)   # g<=40 -> black, g>=150 -> white
        gray[red]=ink[red]
        out=gray.astype('uint8')
    cv2.imwrite(p,out,[cv2.IMWRITE_PNG_COMPRESSION,9])
