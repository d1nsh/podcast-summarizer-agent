import os,sys, ollama
from markdown_pdf import MarkdownPdf, Section
from urllib.parse import urlparse

def main():
 url = sys.argv[1]
 path  = urlparse(url)
 prompt =f'''Generate a detailed summary of the podcast linked here {url}. Include the following elements in clear, well-organized formatting:

Podcast Title: Provide the title of the podcast and any relevant details about its content or context.

Interviewees: List all notable guests or interviewees featured in the podcast, along with their bios if available (or indicate where you can find more information).

Specific Highlights: For each significant point covered in the podcast:

Summarize the key takeaway.
Include relevant details about what was discussed.
Note any interesting facts, quotes, or insights.
Mention when each highlight occurred within the podcast (using start and end times, assuming normal listening speed).
Links: Provide a direct link to the podcast so listeners can access it easily.

Format: Ensure that the summary is well-organized and easy to read, such as using bullet points or subheadings for clarity.'''

 if path.netloc != 'podcasts.apple.com':
  print("I currently only support apple podcasts. Please provide a valid apple podcast url")
  exit()

 response = ollama.generate(model='deepseek-r1', prompt=prompt)

 filename = path.path.replace("/", "-").lstrip('-') + "-summary.pdf"                    

 summary = response["response"]


 pdf = MarkdownPdf()
 pdf.meta["title"] = 'Podcast Summary'
 pdf.add_section(Section(summary, toc=False))
 pdf.save(filename)


if __name__ == '__main__':
    main()