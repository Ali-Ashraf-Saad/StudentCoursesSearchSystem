files = ["txtData/CS.txt", "txtData/IT.txt", "txtData/IS.txt", "txtData/gen.txt"]

with open("txtData/All.txt", "w", encoding="utf-8") as outfile:
    for i, file in enumerate(files):
        with open(file, "r", encoding="utf-8") as infile:
            outfile.write(infile.read().rstrip())

        # سطر فارغ واحد فقط بين الملفات
        if i != len(files) - 1:
            outfile.write("\n\n")

print("تم إنشاء all.txt")