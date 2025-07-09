# YouTube Sentiment Analysis - Sinhala Language

A Python package for sentiment analysis on YouTube comments in Sinhala language. This project provides tools to analyze and classify the sentiment of Sinhala text comments from YouTube videos.

## 🎯 Project Overview

This project focuses on sentiment analysis specifically for Sinhala language text, addressing the unique challenges of processing and analyzing sentiment in this South Asian language. The system can classify YouTube comments into different sentiment categories.

## 🚀 Features

- **Sinhala Text Processing**: Specialized text preprocessing for Sinhala language
- **Emoji Handling**: Convert emojis to text for better sentiment analysis
- **Comment Cleaning**: Remove mentions, URLs, and unnecessary characters
- **Machine Learning Pipeline**: Complete workflow from data processing to model evaluation
- **YouTube Comment Analysis**: Specifically designed for YouTube comment sentiment analysis

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

The project includes three main datasets:

- `train.csv` - Training dataset with labeled Sinhala comments
- `test.csv` - Test dataset for model evaluation
- `youtube_comments.csv` - Raw YouTube comments for analysis

## 🔧 Usage

### Text Preprocessing

```python
from app.utils.text_utils import clean_comment, emoji_to_text

# Clean a Sinhala comment
comment = "මේක හරිම ලස්සනයි! 😍 @username https://example.com"
cleaned = clean_comment(emoji_to_text(comment))
print(cleaned)  # Output: "මේක හරිම ලස්සනයි smiling_face_with_heart_eyes"
```

### Running Experiments

The project includes Jupyter notebooks for the complete machine learning pipeline:

1. **Data Processing** (`01_text_data_processing.ipynb`)
   - Text cleaning and preprocessing
   - Emoji conversion
   - Data exploration

2. **Model Training** (`02_training_model.ipynb`)
   - Feature extraction
   - Model training and selection
   - Hyperparameter tuning

3. **Evaluation** (`03_evaluation.ipynb`)
   - Model performance evaluation
   - Results visualization
   - Error analysis

## 🧪 Text Processing Features

### Emoji Conversion
- Converts emojis to their text representations
- Maintains sentiment context through emoji meanings

### Comment Cleaning
- Removes user mentions (@username)
- Eliminates URLs and links
- Filters out punctuation while preserving Sinhala characters
- Removes numbers and extra whitespace
- Handles Sinhala Unicode range (U+0D80-U+0DFF)

## 📈 Model Performance

*Note: Add your model performance metrics here after training*

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
1. Check the [Issues](https://github.com/HasinthakaPiyumal/youtube-sentiment-analysis-lk/issues) page
2. Create a new issue if your problem isn't already addressed
3. Contact the author directly via email

## 🔮 Future Enhancements

- [ ] Real-time sentiment analysis
- [ ] Web interface for easy usage
- [ ] Support for other South Asian languages
- [ ] Integration with YouTube API
- [ ] Mobile app development
- [ ] Advanced deep learning models

---

**Made with ❤️ for the Sinhala NLP community**