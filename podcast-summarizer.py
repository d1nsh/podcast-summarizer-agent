import os,sys, ollama
from markdown_pdf import MarkdownPdf, Section
from urllib.parse import urlparse

def main():
 url = sys.argv[1]
 path  = urlparse(url)
 prompt =f'''can you summarize the podcast at this link? {url} . 
 Please provide a detailed summary with noteable highlights and specific information from the podcast. 
 The summary should be well formatted so that it can read using a word processor like microsoft word. 
 Do not ask for any feedback after the summary.'''


 if path.netloc != 'podcasts.apple.com':
  print("I currently only support apple podcasts. Please provide a valid apple podcast url")
  exit()

 response = ollama.generate(model='llama3', prompt=prompt)

 filename = path.path.replace("/", "-").lstrip('-') + "-summary.pdf"                    

 summary = response["response"]

 pdf = MarkdownPdf()
 pdf.meta["title"] = 'Podcast Summary'
 pdf.add_section(Section(summary, toc=False))
 pdf.save(filename)


if __name__ == '__main__':
    main()