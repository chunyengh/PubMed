
from .pubmed import esearch
from .pubmed import fetchoneid
import time
from datetime import datetime

#max 3 url requests/sec to server

if __name__ == '__main__':
     
    retstart = 0 #esearch retrievel start index
    retmax = 20 #max retrievels 
    rettotal = 0 #number of ids been retrieved
    total_id = [] #id list
    
    esdata = esearch(retstart= f'{retstart}', retmax = f'{retmax}')

    totalcount = esdata['esearchresult']['count']
    #count is the number of found ids from the queryterm   
    print(f'totalcount:{totalcount}')
    
    idlist = esdata['esearchresult']['idlist']
    #print(f"idlist:{','.join(idlist)}")
    [total_id.append(id) for id in idlist]

    #用 for 迴圈，可以確定有完成es.get的時候。用while，擔心會有無限迴路出現。
    quotient = (int(totalcount) - len(idlist))//retmax
    remainder = (int(totalcount) - len(idlist))%retmax
    loops = quotient if remainder == 0 else quotient + 1
 
    print(f"more loops:{loops}")

    if (loops == 0):
        pass
    else:
        for loop in range(1, loops + 1):
            print(f"loop:{loop}")
            time.sleep(1.0)
            retstart += retmax
            esdata = esearch(retstart=f'{retstart}', retmax = f'{retmax}')
            idlist = esdata['esearchresult']['idlist']
            [total_id.append(id) for id in idlist]

    if (len(total_id) != int(totalcount)):
        print(f"WARNING: total_id:{len(total_id)} != totalcount:{totalcount}")
    else:
        #不用擔心id是否重複，只是重複下載文件而已 
        for pmid in total_id:
            #pmid = '34987367'
            #pmid = '38764299' 
            #pmid = '37189446'
            time.sleep(1.0)
            fetchoneid(pmid)
       


#__main__.py