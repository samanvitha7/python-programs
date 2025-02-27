"""Create a tokenizer for your own language (mother tongue you speak). The tokenizer should tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
“3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
this. [Hint: Use unicode blocks for your language, check wikipedia pages]"""


import re

def tokenize_telugu(text):
    telugu_pattern = r'[\u0C00-\u0C7F]+'
    punctuation_pattern = r"[.,!?;:\"'()\[\]{}]"
    date_pattern = r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2})\b'
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    number_pattern = r'\b\d{1,3}(,\d{2})*(,\d{3})*\b|\b\d+\.\d+\b|\b\d+/\d+\b'
    handle_pattern = r'@[A-Za-z0-9_]+'
    combined_pattern = f'({telugu_pattern}|{punctuation_pattern}|{date_pattern}|{url_pattern}|{email_pattern}|{number_pattern}|{handle_pattern})'
    tokens = re.findall(combined_pattern, text)
    return tokens

telugu_text = "నమస్తే! ఇది 15-01-2025 తేదీన జరిగింది. నా ఇమెయిల్ abc@gmail.com మరియు వెబ్‌సైట్ https://example.com. నా ఫోన్ నంబర్ 3,22,243, అలాగే నా ట్విట్టర్ హ్యాండిల్ @username."

tokens = tokenize_telugu(telugu_text)
print(tokens)
