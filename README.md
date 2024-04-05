# :bookmark_tabs: GalMisoCorpus 2023

[![GitHub issues](https://img.shields.io/github/issues/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/issues) [![GitHub license](https://img.shields.io/github/license/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/release/python-310/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)](https://scikit-learn.org/)

[![GitHub forks](https://img.shields.io/github/forks/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/network)
[![GitHub stars](https://img.shields.io/github/stars/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/stargazers) [![GitHub watching](https://img.shields.io/github/watchers/luciamariaalvarezcrespo/GalMisoCorpus2023?style=social)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/watchers)

##### 🐙 _O primeiro corpus galego para a detección de misoxinia_ 🐙 // 🇬🇧 _The First Galician corpus for misogyny detection_ 🇬🇧

# Corpus

🐙 Este repositorio contén un corpus de chíos e toots procedentes de Twitter e Mastodon para a detección de misoxinia en lingua galega. Asemade, engádense os modelos adestrados co corpus proposto e os scripts desenvolvidos tanto para a creación do corpus como para o adestramento dos modelos.  

🇬🇧 This repository contains a corpus of tweets and toots from Twitter and Mastodon for the detection of misogyny in the Galician language. Additionally, it includes the trained models with the proposed corpus and the scripts developed both for creating the corpus and training the models.

## Estrutura do repositorio / Repository structure

### 🐙 Galego

> - `/corpus`: aquí atópase o corpus utilizado para os adestramentos, así como o non preprocesado para interese dos grupos de investigación.
> - `/scripts`: aquí atópanse os scripts usados durante a recompilación do corpus e durante o adestramento dos modelos. Engadíronse, tamén, scripts que axudaron no proceso de colleita de datos e de procesamento dos textos.
> - `/models`: aquí atópanse os modelos xa adestrados.

### 🇬🇧 English

> - `/corpus`: Here you will find the corpus used for training, as well as the non-preprocessed corpus for the interest of research groups.
> - `/scripts`: Here are the scripts used during the creation of the corpus and during the training of the models. Scripts were also added to assist in the data collection and text processing processes.
> - `/models`: Here are the already trained models.

## Instalación / Installation
🐙 Utiliza a ferramenta [requirements.txt](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/requirements.txt) para instalar todas as dependencias.  
🇬🇧 Use the [requirements.txt](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/requirements.txt) tool to install all the requirements.   

```bash
pip3 install -r requirements.txt
```

## Contribucións / Contributing
🐙 As pull requests son benvidas. Para cambios maiores, abride primeiro unha issue para debater o que queirades cambiar, por favor.  

> [!TIP]
> Así é como lle suxerimos que propoña un cambio neste proxecto:
>
> 1. [Fai un fork deste proxecto][fork] na túa conta.
> 2. [Crea unha nova póla][branch] para o cambio que pretende facer.
> 3. Fai os cambios no teu fork.
> 4. [Envía unha pull request][pr] dende a póla do teu fork á nosa póla `main`.

🇬🇧 Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

> [!TIP]
> Here’s how we suggest you go about proposing a change to this project:  
>
> 1. [Fork this project][fork] to your account.
> 2. [Create a branch][branch] for the change you intend to make.
> 3. Make your changes to your fork.
> 4. [Send a pull request][pr] from your fork's branch to our `main` branch.

[fork]: https://help.github.com/articles/fork-a-repo/
[branch]: https://help.github.com/articles/creating-and-deleting-branches-within-your-repository
[pr]: https://help.github.com/articles/using-pull-requests/

## Licenza / Licensing

🐙 Este proxecto atópase baixo a licenza de Mozilla. Véxase [LICENSE](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE) para o texto completo.  
🇬🇧 This project is licensed under the Mozilla License. See [LICENSE](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE) for the full license text.

## Cítao como / Cite as
```bib
@inproceedings{alvarez-crespo-castro-2024-galician,
  title     = "A {G}alician Corpus for Misogyny Detection Online",
  author    = "{\'A}lvarez-Crespo, Luc{\'\i}a M. and Castro, Laura M.",
  editor    = "Gamallo, Pablo  and Claro, Daniela and Teixeira, Ant{\'o}nio and Real, Livy  and Garcia, Marcos  and Oliveira, Hugo Gon{\c{c}}alo  and Amaro, Raquel",
  booktitle = "Proceedings of the 16th International Conference on Computational Processing of Portuguese",
  month     = mar,
  year      = "2024",
  address   = "Santiago de Compostela, Galicia/Spain",
  publisher = "Association for Computational Lingustics",
  url       = "https://aclanthology.org/2024.propor-1.3",
  pages     = "22--31",
}
```

## Manteñamos o contacto! / Get in touch! 
[@luciamac_](https://www.twitter.com/luciamac_)
