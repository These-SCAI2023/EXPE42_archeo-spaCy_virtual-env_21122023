import spacy

test_text = "Bonjour, je suis un test de Marce u qui est à Serpente, rue Serpente Paris, Panaml"


def test_spacy_model(nlp):
    print(nlp)
    try:
        nlp = spacy.load(nlp)
        doc = nlp(test_text)
        print(doc.text)
        for ent in doc.ents:
            print(ent.text, ent.label_)
    except Exception as e:
        print(f"Erreur pour {nlp}")
        print(e)

    print("\n")


for model in ["fr_core_news_sm", "fr_core_news_md", "fr_core_news_lg"]:
    test_spacy_model(model)
