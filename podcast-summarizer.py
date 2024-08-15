import os,sys, ollama
from markdown_pdf import MarkdownPdf, Section
from urllib.parse import urlparse

def main():
 url = sys.argv[1]
 path  = urlparse(url)
 prompt =f'''can you summarize the podcast at this link? {url} . 
 Please provide a detailed summary with noteable highlights and specific information from the podcast. 
 Please provide the specific start and end time in the podcast for each highlight. Do not add the times if you are not able to accurately determine them.
 Assume the listener is listening to the podcast at normal speed for getting the start and end times.
 The summary should be well formatted so that it can be read using a word processor like microsoft word. 
 After the title add the names of the people featured in the podcast along with the link to the podcast.
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