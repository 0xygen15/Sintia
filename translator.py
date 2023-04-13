import json
import time
import os

import translators as ts


def translate_one_file(sourse_lang, target_lang, sourse_filepath: str, translator, sleep_time):

    file_name = sourse_filepath.split(sep="/")[-1]
    target_file_path = f"./local/{target_lang}/{file_name}"

    with open(sourse_filepath, "r", encoding="utf8") as source_file:
        source_dict = json.load(source_file)
        print(f"[ >>> Starting {file_name} of {target_lang} >>> ]")

        target_dict = {}
        exception_dict = {}

        for key, value in source_dict.items():
            try:
                translated_value = ts.translate_text(value, translator, sourse_lang, target_lang)
                target_dict[key] = translated_value
            except Exception as Ex:
                target_dict[key] = "*" * 50
                print(f"\n[ *** ATTENTION! Exception {Ex} with {key} of {file_name} of {target_lang}! *** ]\n")
                exception_dict[key] = value
            else:
                print(f"[ >>> Translated {key} >>> ]")
            finally:
                time.sleep(sleep_time)


    with open(target_file_path, "w", encoding="utf8") as target_file:
        json.dump(target_dict, target_file, indent=4, ensure_ascii=False)
    print(f"[ >>> {file_name} of {target_lang} successfully written! >>>]\n")

    with open(f'./local/{target_lang}/exceptions_{file_name}', "w", encoding="utf8") as ex_file:
        json.dump(exception_dict, ex_file, indent=4, ensure_ascii=False)
    print(f"[ >>> Exceptions of {file_name} of {target_lang} successfully written! >>>]\n")


filenames = ["info.json", "keyboards.json", "never_i_ever.json", "themes.json", "three_of_five.json", "truth_or_dare.json"]
lang_codes = ["en", "de", "es", "fr", "uk", "sr"]



def main():
    for lang_code in lang_codes:
        for filename in filenames:
            translate_one_file('ru', lang_code, f'./local/ru/{filename}', 'google', 0.3)



if __name__ == "__main__":
    main()