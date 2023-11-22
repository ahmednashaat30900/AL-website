{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ahmednashaat30900/AL-website/blob/master/yolo.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ibJhouhisXsz"
      },
      "outputs": [],
      "source": [
        "from google.colab import drive\n",
        "drive.mount(\"/content/drive\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "WS49h4Mauaq9"
      },
      "outputs": [],
      "source": [
        "%cd ../content/drive/MyDrive/yolov8"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "gxoPCtaVRIwI"
      },
      "outputs": [],
      "source": [
        "%pip install ultralytics\n",
        "import ultralytics\n",
        "ultralytics.checks()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "yH5__9Ruol96"
      },
      "outputs": [],
      "source": [
        "!yolo predict model=\"yolov8n.pt\""
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from ultralytics import YOLO\n",
        "\n",
        "# Load the YOLOv8 model\n",
        "model = YOLO('yolov8m.pt')\n",
        "\n",
        "# Detect objects from classes\n",
        "# 2-> Car  3->Motorcycle  5->Bus   7->Truck\n",
        "classes = [2, 3, 5, 7]\n",
        "\n",
        "# Set the confidence threshold\n",
        "conf_thresh = 0.5\n",
        "\n",
        "# Set the source of the input data\n",
        "source = \"66.mp4\"\n",
        "\n",
        "# Perform prediction on the video\n",
        "results = model.track(source= source , save=True, classes= classes, conf = conf_thresh)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "xBPxNp5ZXnbE"
      },
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "accelerator": "GPU",
    "colab": {
      "provenance": [],
      "mount_file_id": "1055KdrifFZtXhZchXGYFiP4_a4lTA3a4",
      "authorship_tag": "ABX9TyNgIWJ13eDv4FbDqRGxYbbh",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}