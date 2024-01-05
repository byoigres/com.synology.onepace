import argparse
import html
import os
import json
import copy
import re
import util_themoviedb
import searchinc
import constant


def _plugin_run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=str, required=True, help='json string')
    parser.add_argument("--lang", type=str, required=True, default=None, help='enu|cht|...')
    parser.add_argument("--type", type=str, required=True, default=None, help='movie|tvshow|...')
    parser.add_argument("--limit", type=int, default=1, help='result count')
    parser.add_argument("--allowguess", type=bool, default=True)

    # unknownPrm is useless, just for prevent error when unknow param inside
    args, unknownPrm = parser.parse_known_args()

    argv_input = json.loads(args.input)
    argv_lang = args.lang
    argv_type = args.type
    argv_limit = args.limit
    argv_allowguess = args.allowguess

    if argv_type == 'tvshow':
        print('{"success":true,"result":[{"title":"The Big Bang Theory","original_available":"2007-09-24","original_title":"","summary":"Physicists Leonard and Sheldon find their nerd-centric social circle with pals Howard and Raj expanding when aspiring actress Penny moves in next door.","extra":{"com.synology.onepace":{"poster":["https://raw.githubusercontent.com/byoigres/com.synology.onepace/main/images//ooBGRQBdbGzBxAVfExiO8r7kloA.jpg"],"backdrop":["https://raw.githubusercontent.com/byoigres/com.synology.onepace/main/images//7RySzFeK3LPVMXcPtqfZnl6u4p1.jpg"]}}}]}')

    if argv_type == 'tvshow_episode':
        print('{"success":true,"result":[{"title":"The Big Bang Theory","tagline":"The Loobenfeld Decay","original_available":"2008-03-24","summary":"Leonard and Sheldon each lie to avoid seeing Penny\'s concert, but Sheldon\'s is a bit too complicated for his own good.","certificate":"TV-14","genre":["Comedy"],"actor":["Johnny Galecki","Jim Parsons","Kaley Cuoco","Simon Helberg","Kunal Nayyar","DJ Qualls"],"director":["Mark Cendrowski","Bill Ghaffary"],"writer":["Chuck Lorre","Bill Prady","Lee Aronsohn"],"season":1,"episode":10,"extra":{"com.synology.onepace":{"tvshow":{"title":"The Big Bang Theory","original_available":"2007-09-24","original_title":"","summary":"Physicists Leonard and Sheldon find their nerd-centric social circle with pals Howard and Raj expanding when aspiring actress Penny moves in next door.","extra":{"com.synology.onepace":{"poster":["https://image.tmdb.org/t/p/w500/ooBGRQBdbGzBxAVfExiO8r7kloA.jpg"],"backdrop":["https://image.tmdb.org/t/p/original/7RySzFeK3LPVMXcPtqfZnl6u4p1.jpg"]}}},"poster":["https://image.tmdb.org/t/p/w500/6dssfbhNv1g3FFqKWKJhNqaqSQH.jpg"],"reference":{"themoviedb_tv":1418,"imdb":"tt0898266"},"rating":{"themoviedb_tv":7.891}}}}]}')


if __name__ == "__main__":
    _plugin_run()
