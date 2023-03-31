import translators as ts
import json
import asyncio
import time

async def translate2l(sourse_lang, target_lang, sourse_filepath, target_filepath, translator):
    with open(sourse_filepath, "r", encoding='utf8') as sf:
        print(f"[Translating {sourse_filepath} to {target_lang}...]")
        sf_dict = json.load(sf)
        tf_dict = {}
        for k, v in sf_dict.items():
            tf_dict[k] = {}
            for k1, v1 in v.items():
                tf_dict[k][k1] = ts.translate_text(query_text=v1, translator=translator, from_language=sourse_lang,
                                                   to_language=target_lang)
                time.sleep(2)
                with open(target_filepath, "w", encoding='utf8') as tf:
                    json.dump(tf_dict, tf, ensure_ascii=False, indent=4)

                print(f"[Translating {sourse_filepath} to {target_lang} number {k1}]")
        with open(target_filepath, "w", encoding='utf8') as tf:
            json.dump(tf_dict, tf, ensure_ascii=False, indent=4)
            print(f"[Translated {sourse_filepath} to {target_lang}...]")


async def main():
    await translate2l('ru', 'uk', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'uk', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'uk', './database/never.json', './database/uk/never.json', 'google')
    await translate2l('ru', 'uk', './database/never.json', './database/uk/themes_truth.json', 'google')

    await translate2l('ru', 'de', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'de', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'de', './database/never.json', './database/uk/never.json', 'google')
    await translate2l('ru', 'de', './database/never.json', './database/uk/themes_truth.json', 'google')

    await translate2l('ru', 'eng', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'eng', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'eng', './database/never.json', './database/uk/never.json', 'google')

    await translate2l('ru', 'fr', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'fr', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'fr', './database/never.json', './database/uk/never.json', 'google')
    await translate2l('ru', 'fr', './database/never.json', './database/uk/themes_truth.json', 'google')

    await translate2l('ru', 'es', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'es', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'es', './database/never.json', './database/uk/never.json', 'google')
    await translate2l('ru', 'es', './database/never.json', './database/uk/themes_truth.json', 'google')

    await translate2l('ru', 'sr', './database/dare.json', './database/uk/dare.json', 'google')
    await translate2l('ru', 'sr', './database/truth.json', './database/uk/truth.json', 'google')
    await translate2l('ru', 'sr', './database/never.json', './database/uk/never.json', 'google')
    await translate2l('ru', 'sr', './database/never.json', './database/uk/themes_truth.json', 'google')

async def run_translation():
    await main()

if __name__ == "__main__":
    asyncio.run(run_translation())