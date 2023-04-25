from plot import normalize


def stop_words():
    file='stopwords.txt'
    f=open(file,encoding='utf-8')
    lines=f.readlines()
    sw={}
    for l in lines:
        l = l.strip(' \n\r').lower()
        sw[l]=True
    return sw

def read_lyric(file,sw):

    f=open(file,encoding='UTF-8')
    wc={}
    while True:
        line=f.readline()
        if not line:
            break
        words=line.split()
        for w in words:
            w=w.strip(",?()").lower()
            
            if w in sw:
                continue

            if not w in wc:
                wc[w]=0
            wc[w]=wc[w]+1
    return wc

def store_results(out_filename,wc):
    fo = open(out_filename, "w" , encoding="UTF-8")
    for w,c in sorted(wc.items(),key=lambda item:item[1], reverse=True):
        fo.write(f'{w},{c}\n')

sw=stop_words()
wc_l1=read_lyric("mtr.txt",sw)
wc_l2=read_lyric("hbt.txt",sw)

store_results("mtr.result.csv",wc_l1)
store_results("hbt.result.csv",wc_l2)

