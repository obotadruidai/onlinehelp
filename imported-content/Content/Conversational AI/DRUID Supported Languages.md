<a id="DruidSupportedLanguages"></a>

# Druid Supported Languages

This section lists the supported languages across Druid NLP features.

| Language | Culture Code | Druid Language Code | NLP Support | Druid Default Stop Words | NER Deterministic | NER Non Deterministic | Spell Correction |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Afrikaans | AF | af | yes | yes | yes | yes | yes |
| Arabic | AR | ar | yes | yes | yes | yes | yes |
| Armenian | HY | hy | yes | yes | partial\* | yes | yes |
| Bangla | BN | bn-IN | yes | no | partial\* | yes | yes |
| Basque | EU | eu | yes | yes | partial\* | yes | yes |
| Belarusian | BE | be | yes | yes | partial\* | yes | yes |
| Bulgarian | BG | bg | yes | yes | yes | yes | yes |
| Bengali | BN | bn | yes | no | partial\* | yes | yes |
| Burmese | MY | my | partial\*\* | no | yes | partial | yes |
| Catalan | CA | ca | yes | yes | yes | yes | yes |
| Cantonese | YUE | yue | yes | no | partial\* | yes | yes |
| Chinese | ZH-CN | zh | yes | yes | yes | yes | no |
| Croatian | HR | hr | yes | yes | yes | yes | yes |
| Czech | CS | cs | yes | yes | yes | yes | yes |
| Danish | DA | da | yes | yes | yes | yes | yes |
| Dutch | NL | nl | yes | yes | yes | yes | yes |
| Dutch (Flemish) | nl-BE | nl-BE | yes | yes | yes | yes | yes |
| English UK | EN | en | yes | yes | yes | yes | yes |
| English United States | EN | en-US | yes | yes | yes | yes | yes |
| Estonian | ET | et | yes | yes | yes | yes | yes |
| Farsi | FA | fa | yes | no | partial\* | yes | yes |
| Filipino | FIL | fil | partial\*\* | no | partial\* | partial\*\* | yes |
| Finnish | FI | fi | yes | yes | yes | yes | yes |
| French | FR | fr | yes | yes | yes | yes | yes |
| Galician | GL | gl | yes | yes | partial\* | yes | yes |
| German | DE | de | yes | yes | yes | yes | yes |
| Greek | EL | el | yes | yes | yes | yes | yes |
| Gujarati | GU | gu-IN | yes | yes | no | no | yes |
| Hebrew | HE | he | yes | yes | yes | yes | yes |
| Hindi | HI | hi | yes | yes | yes | yes | yes |
| Hungarian | HU | hu | yes | yes | yes | yes | yes |
| Indonesian | ID | id | yes | yes | yes | yes | yes |
| Irish | GA | ga | yes | yes | yes | yes | yes |
| Italian | IT | it | yes | yes | yes | yes | yes |
| Japanese | JA | ja | yes | yes | yes | yes | no |
| Kannada | KN | kn | partial\*\* | no | partial\* | partial\*\* | yes |
| Khmer | KM | km | partial\*\* | no | partial\* | partial\*\* | yes |
| Korean | KO | ko | yes | yes | yes | yes | no |
| Northern Kurdish (Kurmanji) | KU-KMR | ku-Kmr | yes | no | partial\* | yes | yes |
| Central Kurdish (Sorani) | KU | ku | yes | no | partial\* | no | yes |
| Latvian | LV | lv | yes | yes | partial\* | yes | yes |
| Lithuanian | LT | lt | yes | yes | partial\* | yes | yes |
| Malagasy | MG | mg | partial\*\* | yes | partial\* | partial\*\* | yes |
| Malaysian | MS | ms | yes | yes | partial\* | yes | yes |
| Maltese | MT | mt | yes | yes | partial\* | yes | yes |
| Manipuri (Bengali) | MNI | mni | partial\*\* | no | partial\* | partial\*\* | yes |
| Marathi | MR | mr | partial\*\* | yes | partial\* | partial\*\* | yes |
| Mirpuri (a dialect of Punjabi) | PA | pa | no | no | no | no | yes |
| Nepali | NE | ne | yes | yes | no | no | yes |
| Norwegian | NB/NN | nb | yes | yes | yes | yes | yes |
| Pashto | PS | ps | no | no | no | no | yes |
| Persian | FA | fa | yes | no | partial\* | yes | yes |
| Polish | PL | pl | yes | yes | yes | yes | yes |
| Portuguese | PT | pt | yes | yes | yes | yes | yes |
| Punjabi | PA | pa | partial\*\* | no | yes | partial\*\* | yes |
| Romanian | RO | ro | yes | yes | yes | yes | yes |
| Russian | RU | ru | yes | yes | yes | yes | yes |
| Serbian | SR | sr | yes | yes | partial\* | yes | yes |
| Sinhala | SI | si | yes | no | partial\* | yes | yes |
| Slovak | SK | sk | yes | yes | yes | yes | yes |
| Slovenian | SL | sl | yes | yes | partial\* | yes | yes |
| Spanish | ES | es | yes | yes | yes | yes | yes |
| Somali | SO |  | partial\*\* | no | partial\* | partial\* | no |
| Swedish | SV | sv | yes | yes | yes | yes | yes |
| Tamil | TA | ta | yes | yes | yes | yes | yes |
| Telugu | TE | te | partial\*\* | no | yes | partial\*\* | yes |
| Thai | TH | th | yes | yes | yes | yes | yes |
| Traditional Chinese | ZH-HANT | zh-Hant | yes | yes | partial\* | yes | no |
| Turkish | TR | tr | yes | yes | yes | yes | yes |
| Ukrainian | UK | uk | yes | yes | yes | yes | yes |
| Urdu | UR | ur | partial\*\* | yes | yes | partial\*\* | yes |
| Vietnamese | VI | vi | yes | yes | yes | yes | yes |
| Welsh | CY | cy | yes | yes | yes | yes | yes |

\* NER always extracts Person, Location and Organization and extracts number, date, etc. only if written in English format.

\*\*Partial NLP support means that they support only the semantic-based classification (the parameter NLU.NER.Classification.UseSemantic = True)
