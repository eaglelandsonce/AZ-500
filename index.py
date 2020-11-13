import glob

with open('index.md', 'a') as out:
    for path in glob.glob('./Instructions/Labs/LAB_*.md'):
        with open(path, 'r', encoding="utf8") as file:
            file.readline()
            file.readline()
            lab = file.readline().split(':')[1].split('-')[1][1:-2]
            module = file.readline().split(':')[1].split('-')
            out.write("| " + module[0][2:] + " | ")
            out.write(module[1][1:-2] + " | ")
            out.write("[{}]({}) |\n".format(lab, path.replace('\\', '/').replace(' ', '\ ')))
