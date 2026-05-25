def reverse_string(s):
    return s[::-1]


def is_palindrome(s):
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


def count_words(text):
    if not text.strip():
        return 0
    return len(text.split())


def capitalize_words(text):
    return " ".join(word.capitalize() for word in text.split())


def truncate(text, max_length, suffix="..."):
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(is_palindrome("racecar"))
    print(count_words("hello world foo bar"))
    print(capitalize_words("the quick brown fox"))
    print(truncate("this is a very long string", 15))
