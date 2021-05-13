import os
from wxconv import WXC

paths= ["./datasets/Bhojpuri_Testset/",
        "./datasets/HDTB_pre_release_version-0.05/IntraChunk/CoNLL/utf/news_articles_and_heritage/Testing/",
        "./datasets/HDTB_pre_release_version-0.05/IntraChunk/CoNLL/utf/news_articles_and_heritage/Training/",
        "./datasets/HDTB_pre_release_version-0.05/IntraChunk/CoNLL/utf/news_articles_and_heritage/Development/"]

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    return lines

con = WXC(order='utf2wx')
for path in paths:
    if os.path.exists(path):
        for item in os.listdir(path):
            filepath = os.path.join(path, item)
            if os.path.isfile(filepath):
                lines = read_file(filepath)

                saveLines=[]
                for hin in lines:
                    try:
                        hin=hin.split()
                        line=str(hin[0])+'\t'+str(con.convert(hin[1]))+'\t'+str(con.convert(hin[2]))+'\t'+'\t'.join(hin[3:])
                        saveLines.append(line)
                    except:
                        saveLines.append("")

                savePath=os.path.join(path,"wx/")
                if not os.path.exists(savePath):
                    os.makedirs(savePath)
                
                savefile=os.path.join(savePath,item)
                with open(savefile, 'w', encoding='utf-8') as f:
                    f.writelines("\n".join(saveLines))
                assert(os.path.exists(savefile))
    else:
        print("Path doesn't exists", path)

print("Converted!")