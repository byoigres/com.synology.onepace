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
        # print('{"success":true,"result":[{"title":"One Pace","original_available":"2013-01-01","original_title":"","summary":"One Pace is a fan project that recuts the One Piece anime in an endeavor to bring it more in line with the pacing of the original manga by Eiichiro Oda. The team accomplishes this by removing filler scenes not present in the source material. This process requires meticulous editing and quality control to ensure seamless music and transitions.","extra":{"com.synology.onepace":{"poster":["https://raw.githubusercontent.com/byoigres/com.synology.onepace/main/images/one-pace-poster.png"],"backdrop":["https://image.tmdb.org/t/p/original/4Mt7WHox67uJ1yErwTBFcV8KWgG.jpg"]}}}]}')
        print(_tvshow())

    if argv_type == 'tvshow_episode':
        # print('{"success":true,"result":[{"title":"The Big Bang Theory","tagline":"The Loobenfeld Decay","original_available":"2008-03-24","summary":"Leonard and Sheldon each lie to avoid seeing Penny\'s concert, but Sheldon\'s is a bit too complicated for his own good.","certificate":"TV-14","genre":["Comedy"],"actor":["Johnny Galecki","Jim Parsons","Kaley Cuoco","Simon Helberg","Kunal Nayyar","DJ Qualls"],"director":["Mark Cendrowski","Bill Ghaffary"],"writer":["Chuck Lorre","Bill Prady","Lee Aronsohn"],"season":1,"episode":10,"extra":{"com.synology.onepace":{"tvshow":{"title":"The Big Bang Theory","original_available":"2007-09-24","original_title":"","summary":"Physicists Leonard and Sheldon find their nerd-centric social circle with pals Howard and Raj expanding when aspiring actress Penny moves in next door.","extra":{"com.synology.onepace":{"poster":["https://image.tmdb.org/t/p/w500/ooBGRQBdbGzBxAVfExiO8r7kloA.jpg"],"backdrop":["https://image.tmdb.org/t/p/original/7RySzFeK3LPVMXcPtqfZnl6u4p1.jpg"]}}},"poster":["https://image.tmdb.org/t/p/w500/6dssfbhNv1g3FFqKWKJhNqaqSQH.jpg"],"reference":{"themoviedb_tv":1418,"imdb":"tt0898266"},"rating":{"themoviedb_tv":7.891}}}}]}')
        print(__tvshow_episode())

def _tvshow():
    raw = """
{
    "success": true,
    "result": [
        {
            "title": "One Pace",
            "original_available": "2013-01-01",
            "original_title": "",
            "summary": "One Pace is a fan project that recuts the One Piece anime in an endeavor to bring it more in line with the pacing of the original manga by Eiichiro Oda. The team accomplishes this by removing filler scenes not present in the source material. This process requires meticulous editing and quality control to ensure seamless music and transitions.",
            "extra": {
                "com.synology.onepace": {
                    "poster": [
                        "https://raw.githubusercontent.com/byoigres/com.synology.onepace/main/images/one-pace-poster.png"
                    ],
                    "backdrop": [
                        "https://image.tmdb.org/t/p/original/4Mt7WHox67uJ1yErwTBFcV8KWgG.jpg"
                    ]
                }
            }
        }
    ]
}
    """

    parsed = json.loads(raw)
    return json.dumps(parsed)

def __tvshow_episode():
    raw = """
{
    "success": true,
    "result": [
        {
            "title": "One Pace",
            "tagline": "Romance Dawn, the Dawn of an Adventure",
            "original_available": "2020-12-02",
            "summary":"Influenced by the straw-hat-wearing pirate Red-Haired Shanks, an enthusiastic young boy named Monkey D. Luffy dreams of one day becoming king of the pirates.",
            "certificate": "TV-14",
            "genre": [
                "Animation"
            ],
            "actor": [
                "https://onepace.net/about"
            ],
            "director": [
                "https://onepace.net/about"
            ],
            "writer": [
                "https://onepace.net/about"
            ],
            "season": 1,
            "episode": 1,
            "extra": {
                "com.synology.onepace": {
                    "tvshow": {
                        "title": "The Big Bang Theory",
                        "original_available": "2007-09-24",
                        "original_title": "",
                        "summary": "Physicists Leonard and Sheldon find their nerd-centric social circle with pals Howard and Raj expanding when aspiring actress Penny moves in next door.",
                        "extra": {
                            "com.synology.onepace": {
                                "poster": [
                                    "https://image.tmdb.org/t/p/w500/ooBGRQBdbGzBxAVfExiO8r7kloA.jpg"
                                ],
                                "backdrop": [
                                    "https://image.tmdb.org/t/p/original/7RySzFeK3LPVMXcPtqfZnl6u4p1.jpg"
                                ]
                            }
                        }
                    },
                    "poster": [
                        "https://image.tmdb.org/t/p/w500/6dssfbhNv1g3FFqKWKJhNqaqSQH.jpg"
                    ]
                }
            }
        }
    ]
}
    """

    parsed = json.loads(raw)
    return json.dumps(parsed)

def _process_output(success, error_code, datas):
    result_obj = {}
    if success:
        result_obj = {'success': True, 'result': datas}
    else:
        result_obj = {'success': False, 'error_code': error_code}

    json_string = json.dumps(result_obj, ensure_ascii=False, separators=(',', ':'))
    json_string = html.unescape(json_string)
    print(json_string)


if __name__ == "__main__":
    _plugin_run()
