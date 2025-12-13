def trans(text_dict, lang_code):
    return text_dict.get(lang_code, text_dict.get('en', ''))


def seconds_to_minutes(seconds, return_string=True, lang_code='en'):
    minutes = seconds // 60
    reste = seconds % 60

    if return_string:
        if minutes == 0:
            txt = trans(dict(en=f"{reste} seconds", fr=f"{reste} secondes", vi=f"{reste} giây"), lang_code=lang_code)
        else:
            txt = trans(dict(en=f"{minutes} minutes", fr=f"{minutes} minutes", vi=f"{minutes} phút"),
                        lang_code=lang_code)
            if reste:
                txt += trans(dict(en=f" and {reste} seconds", fr=f" et {reste} secondes", vi=f" và {reste} giây"),
                             lang_code=lang_code)
        return txt
    else:
        return minutes, reste
