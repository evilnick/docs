import re
p = re.compile(ur'<---TEST(?:\n|\r\n?)(.+?)(?:\n|\r\n?)--->(?:\n|\r\n?)```bash(?:\n|\r\n?)(.+?)(?:\n|\r\n?)```', re.DOTALL)
test_str = u"some random text, more text. And some more text\nThere is a lot of text\n\n# Heading\n\nStill more text\n\n<---TEST\na command\nanother command\nsomething else\n--->\n```bash\nvisible one-line command\n```\n\nmore text goes here, and yet more.\nWe should really do something about all this text\n\n<---TEST\nsetup stuff here\n--->\n```bash\nnew command\nadditional command\n```\n"
 
x= re.findall(p, test_str)
print(x)

src="https://regex101.com/r/tX5qU8/1#python"
