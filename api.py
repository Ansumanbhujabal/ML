{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8Eyu46M8Jx4mHn09LyhhU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ansumanbhujabal/ML/blob/main/API.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IePvU86FIJTd",
        "outputId": "016ee6d9-e568-49c2-e316-9a1402cf2e73"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: kaggle in /usr/local/lib/python3.10/dist-packages (1.5.16)\n",
            "Requirement already satisfied: six>=1.10 in /usr/local/lib/python3.10/dist-packages (from kaggle) (1.16.0)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.10/dist-packages (from kaggle) (2023.7.22)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from kaggle) (2.8.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from kaggle) (2.31.0)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.10/dist-packages (from kaggle) (4.66.1)\n",
            "Requirement already satisfied: python-slugify in /usr/local/lib/python3.10/dist-packages (from kaggle) (8.0.1)\n",
            "Requirement already satisfied: urllib3 in /usr/local/lib/python3.10/dist-packages (from kaggle) (2.0.4)\n",
            "Requirement already satisfied: bleach in /usr/local/lib/python3.10/dist-packages (from kaggle) (6.0.0)\n",
            "Requirement already satisfied: webencodings in /usr/local/lib/python3.10/dist-packages (from bleach->kaggle) (0.5.1)\n",
            "Requirement already satisfied: text-unidecode>=1.3 in /usr/local/lib/python3.10/dist-packages (from python-slugify->kaggle) (1.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->kaggle) (3.2.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->kaggle) (3.4)\n"
          ]
        }
      ],
      "source": [
        "#Installing Kaggle\n",
        "!pip install kaggle"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# configuring the path of Kaggle.json file\n",
        "!mkdir -p ~/.kaggle\n",
        "!cp kaggle.json ~/.kaggle/\n",
        "!chmod 600 ~/.kaggle/kaggle.json"
      ],
      "metadata": {
        "id": "hGxHEou7I4GB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Importing Kaggle Earthquake dataset**"
      ],
      "metadata": {
        "id": "fr5FY_CALIG0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#Api from kaggle dataset\n",
        "!kaggle competitions download -c LANL-Earthquake-Prediction"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qGibS6_rK-WO",
        "outputId": "e42f36ab-951a-4458-860b-e8631898a2da"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Downloading LANL-Earthquake-Prediction.zip to /content\n",
            "100% 2.27G/2.27G [00:57<00:00, 40.2MB/s]\n",
            "100% 2.27G/2.27G [00:57<00:00, 42.1MB/s]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# extracting the compessed Dataset\n",
        "from zipfile import ZipFile\n",
        "dataset = '/content/LANL-Earthquake-Prediction.zip'\n",
        "with ZipFile(dataset,'r') as zip:\n",
        "  zip.extractall()\n",
        "  print('The dataset is extracted')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "39nD6PUbLnp5",
        "outputId": "d8da2b3b-314c-4ea0-bd49-c089251c3093"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "The dataset is extracted\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "pd.read_csv('/content/train.csv')"
      ],
      "metadata": {
        "id": "MAKE4PmJOndd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "6UdfTYdHRnof"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
