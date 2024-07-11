## :bookmark_tabs: GalMisoCorpus 2023

[![GitHub issues](https://img.shields.io/github/issues/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/issues) [![GitHub license](https://img.shields.io/github/license/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/downloads/release/python-310/)
[![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)](https://scikit-learn.org/)

[![GitHub forks](https://img.shields.io/github/forks/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/network)
[![GitHub stars](https://img.shields.io/github/stars/luciamariaalvarezcrespo/GalMisoCorpus2023)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/stargazers) [![GitHub watching](https://img.shields.io/github/watchers/luciamariaalvarezcrespo/GalMisoCorpus2023?style=social)](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/watchers)

###### :octopus: _O primeiro corpus galego para a detección de misoxinia_ :octopus:
###### :gb: _The First Galician corpus for misogyny detection_ 🇬🇧

### Corpus :books:

:octopus: Este repositorio contén un corpus de chíos e toots procedentes de Twitter e Mastodon para a detección de misoxinia en lingua galega. Asemade, engádense os modelos adestrados co corpus proposto e os scripts desenvolvidos tanto para a creación do corpus como para o adestramento dos modelos. Este traballo foi aceptado no 16th International Conference on Computational Processing of Portuguese (PROPOR 2024). O artigo está dispoñíbel [aquí](https://aclanthology.org/2024.propor-1.3/). 

:gb: This repository contains a corpus of tweets and toots from Twitter and Mastodon for the detection of misogyny in the Galician language. Additionally, it includes the trained models with the proposed corpus and the scripts developed both for creating the corpus and training the models. This work was accepted at the 16th International Conference on Computational Processing of Portuguese (PROPOR 2024). The paper is available [here](https://aclanthology.org/2024.propor-1.3/).

### Cítao como / Cite as :sparkling_heart:

:octopus: Se consideras ao GalMisoCorpus2023 útil para o teu traballo de investigación, podes darlle unha :star: a este repo e citar o noso traballo facendo uso do seguinte BibTeX:

:gb: If you find GalMisoCorpus2023 useful for your research, welcome to :star: this repo and cite our work using the following BibTeX:

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

### Responsabilidade / Disclaimer :warning:
> [!WARNING] 
> :octopus: Este conxunto de datos pode conter discurso de odio, linguaxe ofensiva ou outro material semellante. O contido foi recollido de diversas fontes e non foi creado nin avaliado polas autoras do proxecto, así como non reflicte as súas opinións ou puntos de vista. O conxunto de datos está destinado exclusivamente a fins de investigación, análise ou educativos. As autoras non avalan ningún comportamento prexudicial ou discriminatorio atopado nel. Debido ás políticas de privacidade, non se pode publicar o texto procedente de X/Twitter. As persoas usuarias deben actuar con precaución e sensibilidade ao usar o conxunto de datos e cumprir coas directrices éticas e as leis aplicábeis. As responsables do proxecto non asumen ningunha responsabilidade polo contido nin polo seu uso ou interpretación por terceiros.

> [!WARNING]
> :gb: This dataset may contain hate speech, offensive language, or other objectionable material. The content was collected from various sources and is not created or endorsed by the project authors. It does not reflect their views or opinions. The dataset is intended solely for research, analysis, or educational purposes. The authors do not endorse any harmful or discriminatory behavior found within it. Due to privacy policies, text from X/Twitter cannot be published. Users should exercise caution and sensitivity when using the dataset and adhere to ethical guidelines and applicable laws. The project maintainers disclaim any responsibility for the content and its use or interpretation by others.

### Estrutura do repositorio / Repository structure :file_folder:

#### :octopus: Galego

> - `/corpus`: aquí atópase o corpus utilizado para os adestramentos, así como o non preprocesado para interese dos grupos de investigación.
> - `/scripts`: aquí atópanse os scripts usados durante a recompilación do corpus e durante o adestramento dos modelos. Engadíronse, tamén, scripts que axudaron no proceso de colleita de datos e de procesamento dos textos.
> - `/models`: aquí atópanse os modelos xa adestrados.

#### :gb: English

> - `/corpus`: Here you will find the corpus used for training, as well as the non-preprocessed corpus for the interest of research groups.
> - `/scripts`: Here are the scripts used during the creation of the corpus and during the training of the models. Scripts were also added to assist in the data collection and text processing processes.
> - `/models`: Here are the already trained models.

### Instalación / Installation :wrench:
:octopus: Utiliza a ferramenta [requirements.txt](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/requirements.txt) para instalar todas as dependencias.  
:gb: Use the [requirements.txt](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/requirements.txt) tool to install all the requirements.   

```bash
pip3 install -r requirements.txt
```

### Contribucións / Contributing :open_hands:
:octopus: As pull requests son benvidas. Para cambios maiores, abride primeiro unha issue para debater o que queirades cambiar, por favor.  

> [!TIP]
> Así é como lle suxerimos que propoña un cambio neste proxecto:
>
> 1. [Fai un fork deste proxecto][fork] na túa conta.
> 2. [Crea unha nova póla][branch] para o cambio que pretende facer.
> 3. Fai os cambios no teu fork.
> 4. [Envía unha pull request][pr] dende a póla do teu fork á nosa póla `main`.

:gb: Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.  

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

### Licenza / Licensing :scroll:

:octopus: Este proxecto atópase baixo a licenza de Mozilla. Véxase [LICENSE](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE) para o texto completo.  
:gb: This project is licensed under the Mozilla License. See [LICENSE](https://github.com/luciamariaalvarezcrespo/GalMisoCorpus2023/blob/main/LICENSE) for the full license text.

### Manteñamos o contacto! / Get in touch! :telephone_receiver:
[@luciamac_](https://www.twitter.com/luciamac_)
