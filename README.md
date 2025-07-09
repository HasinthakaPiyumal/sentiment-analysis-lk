# YouTube Sentiment Analysis – Sinhala Language (Fine-Tuning Edition)

This is a Python project for fine-tuning sentiment analysis models on YouTube comments written in Sinhala, Singlish, and English. It includes scripts and resources to train and adapt sentiment classification models using your own YouTube comment datasets.

The goal is to build a robust multilingual sentiment classifier that works effectively in real-world Sri Lankan social media contexts.

## 🎯 Project Overview

This project is focused on **finetuning** sentiment analysis models for Sinhala language YouTube comments. It enables users to preprocess data, train, and evaluate custom models, addressing the unique challenges of sentiment detection in Sinhala text.

## 🚀 Features

- **Sinhala Text Preprocessing**: Tailored cleaning and normalization for Sinhala comments
- **Emoji Handling**: Converts emojis to text to preserve sentiment cues
- **Data Cleaning**: Removes mentions, URLs, and extraneous characters
- **Finetuning Pipeline**: End-to-end workflow for adapting sentiment models
- **YouTube Comment Support**: Designed for real-world YouTube comment data

## 📁 Project Structure

```
sentiment-analysis-lk/
├── README.md
├── requirements.txt
├── setup.py
├── data/
│   ├── test.csv
│   ├── train.csv
│   └── youtube_comments.csv
├── experiment/
│   ├── 01_text_data_processing.ipynb
│   ├── 02_training_model.ipynb
│   └── 03_evaluation.ipynb
└── src/
    └── app/
        └── utils/
            └── text_utils.py
```

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/HasinthakaPiyumal/youtube-sentiment-analysis-lk.git
   cd sentiment-analysis-lk
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install the package in development mode**
   ```bash
   pip install -e .
   ```

## 📊 Data

The project expects your own datasets for finetuning:

- `train.csv` - Labeled Sinhala comments for training
- `test.csv` - Labeled Sinhala comments for evaluation
- `youtube_comments.csv` - Raw YouTube comments for preprocessing and annotation

## 🔧 Usage

### Text Preprocessing

```python
from app.utils.text_utils import clean_comment, emoji_to_text

# Clean a Sinhala comment
comment = "මේක හරිම ලස්සනයි! 😍 @username https://example.com"
cleaned = clean_comment(emoji_to_text(comment))
print(cleaned)  # Output: "මේක හරිම ලස්සනයි smiling_face_with_heart_eyes"
```

### Finetuning Workflow

Use the provided Jupyter notebooks to:

1. **Data Processing** (`01_text_data_processing.ipynb`)

   - Clean and preprocess your data
   - Convert emojis
   - Explore and annotate data

2. **Model Finetuning** (`02_training_model.ipynb`)

   - Extract features
   - Finetune sentiment models on your dataset
   - Tune hyperparameters

3. **Evaluation** (`03_evaluation.ipynb`)
   - Evaluate model performance
   - Analyze errors

## 🧪 Text Processing Features

### Emoji Conversion

- Converts emojis to text to retain sentiment information

### Comment Cleaning

- Removes user mentions, URLs, punctuation, numbers, and extra whitespace
- Preserves Sinhala Unicode characters

## 📈 Model Performance

_Note: Add your finetuned model's performance metrics here after training._

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Hasinthaka Piyumal**

- Email: hasinthakapiyumal@gmail.com
- GitHub: [@HasinthakaPiyumal](https://github.com/HasinthakaPiyumal)

## 🙏 Acknowledgments

- Thanks to the Sinhala NLP community for their contributions
- YouTube API for comment data access
- Open source libraries that made this project possible

## 📞 Support

If you have any questions or issues, please:

1. Check the [Issues](https://github.com/HasinthakaPiyumal/sentiment-analysis-lk/issues) page
2. Create a new issue if your problem isn't already addressed
3. Contact the author directly via email

---

**Made with ❤️ for the Sinhala NLP community**
