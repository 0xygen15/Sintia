import translators as ts
import json
import asyncio
import time



def translate2l(sourse_lang, target_lang, sourse_filepath, target_filepath, translator):
    with open(sourse_filepath, "r", encoding='utf8') as sf:
        print(f"[Translating {sourse_filepath} to {target_lang}...]")
        errors = {}
        sf_dict = json.load(sf)
        tf_dict = {}
        for k, v in sf_dict.items():
            tf_dict[k] = {}
            for k1, v1 in v.items():
                try:
                    v2 = ts.translate_text(query_text=v1, translator=translator, from_language=sourse_lang,
                                                       to_language=target_lang)
                    while type(v2) != str:
                        v2 = ts.translate_text(query_text=v1, translator=translator, from_language=sourse_lang,
                                               to_language=target_lang)
                    tf_dict[k][k1] = v2
                    time.sleep(0.6)
                    with open(target_filepath, "w", encoding='utf8') as tf:
                        json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
                    print(f"[Translating {sourse_filepath} to {target_lang} {k} number {k1}]")
                except Exception as e:
                    print(f"\n***PROBLEM WITH {sourse_filepath} {k} {k1} {e}***\n")
                    print(v1)
                    time.sleep(3)
                    errors[f"{str(sourse_filepath)} {k} {k1} {target_lang}"] = v1
        with open("./database/errors.json", "w", encoding="utf8") as f:
            json.dump(errors, f, indent=4, ensure_ascii=False)

        with open(target_filepath, "w", encoding='utf8') as tf:
            json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
            print(f"[Translated {sourse_filepath} to {target_lang}...]")

# def translate2l(sourse_lang, target_lang, sourse_filepath, target_filepath, translator):
#     with open(sourse_filepath, "r", encoding='utf8') as sf:
#         print(f"[Translating {sourse_filepath} to {target_lang}...]")
#         errors = {}
#         sf_dict = json.load(sf)
#         tf_dict = {}
#         for k, v in sf_dict.items():
#             tf_dict[k] = {}
#             for k1, v1 in v.items():
#                 v2 = ts.translate_text(query_text=v1, translator=translator, from_language=sourse_lang,
#                                                    to_language=target_lang)
#                 if v2 is None:
#                     while type(v2) != str:
#                         v2 = ts.translate_text(query_text=v1, translator=translator, from_language=sourse_lang,
#                                                to_language=target_lang)
#                     tf_dict[k][k1] = v2
#                     time.sleep(0.6)
#                     with open(target_filepath, "w", encoding='utf8') as tf:
#                         json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
#                     print(f"[Translating {sourse_filepath} to {target_lang} {k} number {k1}]")
#                 else:
#                     tf_dict[k][k1] = v2
#                     time.sleep(0.6)
#                     with open(target_filepath, "w", encoding='utf8') as tf:
#                         json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
#                     print(f"[Translating {sourse_filepath} to {target_lang} {k} number {k1}]")
#
#         with open(target_filepath, "w", encoding='utf8') as tf:
#             json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
#             print(f"[Translated {sourse_filepath} to {target_lang}...]")


def main():
    # translate2l('ru', 'uk', './database/dare.json', './database/uk/dare.json', 'google')
    # translate2l('ru', 'uk', './database/truth.json', './database/uk/truth.json', 'google')
    # translate2l('ru', 'uk', './database/never.json', './database/uk/never.json', 'google')
    # translate2l('ru', 'uk', './database/themes_truth.json', './database/uk/themes_truth.json', 'google')

    # translate2l('ru', 'de', './database/dare.json', './database/de/dare.json', 'google')
    # translate2l('ru', 'de', './database/truth.json', './database/de/truth.json', 'google')
    # translate2l('ru', 'de', './database/never.json', './database/de/never.json', 'google')
    # translate2l('ru', 'de', './database/themes_truth.json', './database/de/themes_truth.json', 'google')
    #
    # translate2l('ru', 'en', './database/dare.json', './database/en/dare.json', 'google')
    # translate2l('ru', 'en', './database/truth.json', './database/en/truth.json', 'google')
    # translate2l('ru', 'en', './database/never.json', './database/en/never.json', 'google')
    #
    # translate2l('ru', 'fr', './database/dare.json', './database/fr/dare.json', 'google')
    # translate2l('ru', 'fr', './database/truth.json', './database/fr/truth.json', 'google')
    # translate2l('ru', 'fr', './database/never.json', './database/fr/never.json', 'google')
    # translate2l('ru', 'fr', './database/themes_truth.json', './database/fr/themes_truth.json', 'google')
    # #
    # translate2l('ru', 'es', './database/dare.json', './database/es/dare.json', 'google')
    # translate2l('ru', 'es', './database/truth.json', './database/es/truth.json', 'google')
    # translate2l('ru', 'es', './database/never.json', './database/es/never.json', 'google')
    # translate2l('ru', 'es', './database/themes_truth.json', './database/es/themes_truth.json', 'google')
    #
    # translate2l('ru', 'sr', './database/dare.json', './database/sr/dare.json', 'google')
    # translate2l('ru', 'sr', './database/truth.json', './database/sr/truth.json', 'google')
    # translate2l('ru', 'sr', './database/never.json', './database/sr/never.json', 'google')
    translate2l('ru', 'sr', './database/themes_truth.json', './database/sr/themes_truth.json', 'google')

if __name__ == "__main__":
    main()