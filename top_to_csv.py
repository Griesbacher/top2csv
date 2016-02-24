import re
import sys

# top -p 123456 -b -d 5 > top_dump

if __name__ == '__main__':
    filename = sys.argv[1]
    replace_dot_to = ","
    lines = [line.rstrip('\n') for line in open(filename)]
    f = open(filename + '.csv', 'w')
    sep = ";"
    i = 2
    f.write(
            'time abs' + sep + 'time' + sep + 'load1' + sep + 'load5' + sep + 'load15' + sep +
            'name' + sep + 'virt' + sep + 'res' + sep + 'shr' + sep + '%cpu' + sep + '%mem\n'
    )
    for line in lines:
        header = re.search(b'^top - (.*?) up.*? load average: (\d+.\d+), (\d+.\d+), (\d+.\d+)$', line)
        if header:
            f.write(
                    "=B" + str(i) + "-$B$2" + sep +
                    header.group(1) + sep +
                    header.group(2).replace(".", replace_dot_to) + sep +
                    header.group(3).replace(".", replace_dot_to) + sep +
                    header.group(4).replace(".", replace_dot_to) + sep
            )
        else:
            process = re.search(
                    b'^\s*\d+\s(\w+).?\s+-?\d+\s+\d+\s+(\d+)\s+(\d+)\s+(\d+)\s+\w\s+(\d+\.\d+)\s+(\d+\.\d+)',
                    line
            )
            if process:
                f.write(
                        process.group(1) + sep +
                        process.group(2) + sep +
                        process.group(3) + sep +
                        process.group(4) + sep +
                        process.group(5).replace(".", replace_dot_to) + sep +
                        process.group(6).replace(".", replace_dot_to) + '\n'
                )
                i += 1
    f.close()
