import tkinter as tk
from tkinter import messagebox
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

class SocialMediaPostGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Social Media Post Generator")

        self.label_text = tk.Label(master, text="Enter your post text:")
        self.label_text.pack()

        self.post_text = tk.Text(master, height=4, width=50)
        self.post_text.pack()

        self.label_output = tk.Label(master, text="Generated Post:")
        self.label_output.pack()

        self.output_text = tk.Text(master, height=4, width=50)
        self.output_text.pack()

        self.generate_button = tk.Button(master, text="Generate Post", command=self.generate_post)
        self.generate_button.pack()

        self.copy_button = tk.Button(master, text="Copy Output", command=self.copy_output)
        self.copy_button.pack()

        self.paste_button = tk.Button(master, text="Paste Input", command=self.paste_input)
        self.paste_button.pack()

    def generate_hashtags(self, post_text):
        tokens = word_tokenize(post_text)
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word.lower() for word in tokens if word.isalnum() and word.lower() not in stop_words]
        word_freq = nltk.FreqDist(filtered_tokens)
        hashtags = [word for word, _ in word_freq.most_common(3)]
        return hashtags

    def generate_post(self):
        post_text = self.post_text.get("1.0", "end-1c")

        if not post_text:
            messagebox.showwarning("Error", "Please enter post text.")
            return

        hashtags = self.generate_hashtags(post_text)
        post = f"{post_text}\n\n"
        if hashtags:
            post += "Hashtags: " + " ".join(['#' + tag for tag in hashtags]) + "\n"

        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", post)

    def copy_output(self):
        output_text = self.output_text.get("1.0", "end-1c")
        self.master.clipboard_clear()
        self.master.clipboard_append(output_text)

    def paste_input(self):
        input_text = self.master.clipboard_get()
        self.post_text.delete("1.0", "end")
        self.post_text.insert("1.0", input_text)


def main():
    root = tk.Tk()
    app = SocialMediaPostGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
