# -*- coding: utf-8 -*-
#------------------------------------------------------------
# Stream On Demand PureITA
# Server per zinwa
# http://www.mimediacenter.info/foro/viewforum.php?f=36
#------------------------------------------------------------

import urlparse,urllib2,urllib,re
import os

from core import scrapertools
from core import logger
from core import config

def test_video_exists( page_url ):
    return True,""

def get_video_url( page_url , premium = False , user="" , password="", video_password="" ):
    logger.info("[zinwa.py] get_video_url(page_url='%s')" % page_url)
    video_urls = []

    data = scrapertools.cache_page(page_url)
    mediaurl = scrapertools.get_match(data,'file\: "([^"]+)"')
    extension = scrapertools.get_filename_from_url(mediaurl)[-4:]
    
    video_urls.append( [ extension + " [zinwa]",mediaurl ] )

    return video_urls

# Encuentra vídeos del servidor en el texto pasado
def find_videos(data):
    encontrados = set()
    devuelve = []

    #http://zinwa.com/frap5b3uhesl
    patronvideos  = '(zinwa.com/[a-z0-9]+)'
    logger.info("[zinwa.py] find_videos #"+patronvideos+"#")
    matches = re.compile(patronvideos,re.DOTALL).findall(data)

    for match in matches:
        titulo = "[zinwa]"
        url = "http://"+match
        if url not in encontrados:
            logger.info("  url="+url)
            devuelve.append( [ titulo , url , 'zinwa' ] )
            encontrados.add(url)
        else:
            logger.info("  url duplicada="+url)

    return devuelve

def test():
    video_urls = get_video_url("http://zinwa.com/frap5b3uhesl")
    return len(video_urls)>0