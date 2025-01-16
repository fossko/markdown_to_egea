import argparse
import os
import re


parser = argparse.ArgumentParser()

parser.add_argument('md',
                     help='file name markdown'
                     )

args = parser.parse_args()
print(args)
print(args.md)

file_markdown = args.md

print(file_markdown, os.path.isfile(file_markdown),os.path.exists(file_markdown))


def convert_to_egea(markdown_text):
    # Convert headers
    egea_text = re.sub(r'^### (.*)$', r'### \1', markdown_text, flags=re.MULTILINE)
    egea_text = re.sub(r'^## (.*)$', r'## \1', egea_text, flags=re.MULTILINE)
    egea_text = re.sub(r'^# (.*)$', r'# \1', egea_text, flags=re.MULTILINE)
    
    # Convert bold (leave as is)
    # Make sure to selectively replace *italic* with //italic// by considering ___not both_bold and italic___
    egea_text = re.sub(r'\*\*(.*?)\*\*', r'**\1**', egea_text)
    
    # Convert italic
    egea_text = re.sub(r'(?<!\*)\*(?!\*)(.*?)\*(?!\*)(?<!\*)', r'//\1//', egea_text)
    
    # Convert strikethrough (leave as is)
    egea_text = re.sub(r'~~(.*?)~~', r'--\1--', egea_text)
    
    # Convert links
    egea_text = re.sub(r'\[(.*?)\]\((.*?)\)', r'((\2 \1))', egea_text)
    
    # Convert blockquotes
    egea_text = re.sub(r'^> (.*)$', r'> \1', egea_text, flags=re.MULTILINE)
    
    # Convert unordered lists
    egea_text = re.sub(r'^\* (.*)$', r'- \1', egea_text, flags=re.MULTILINE)
    
    # Convert ordered lists
    egea_text = re.sub(r'^\d+\. (.*)$', r'1. \1', egea_text, flags=re.MULTILINE)
    
    # Convert images
    egea_text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'\2 \1', egea_text)

    # Convert tables
    egea_text = re.sub(
        r'((?:\|.*\|\n)+)', 
        lambda match: f"-----\n{match.group(1)}-----\n", 
        egea_text
    )
  
    return egea_text





if os.path.isfile(file_markdown) and os.path.exists(file_markdown):
    print("файл существует")
    # f = open(file_markdown,'r')
    # f.close
    with open(file_markdown,'r',encoding='utf-8') as f:
        markdown_text = f.read()
    # print(markdown_text)
    egea_text = convert_to_egea(markdown_text)
    print("Тест для эгеи")
    print(egea_text)
    file_egea=f"{file_markdown}_egea.txt"
    with open(file_egea,'w',encoding='utf-8') as f:
        f.write(egea_text)

else:
    print("файл не найден")


